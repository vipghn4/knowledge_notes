<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Docker overview](#docker-overview)
  - [Linux namespace](#linux-namespace)
    - [Process namespace](#process-namespace)
    - [Network namespace](#network-namespace)
    - [Mount namespace](#mount-namespace)
    - [Other namespaces](#other-namespaces)
    - [Cross-namespace commuication](#cross-namespace-commuication)
  - [Docker platform](#docker-platform)
  - [Docker architecture](#docker-architecture)
  - [The underlying technology](#the-underlying-technology)
- [Appendix](#appendix)
  - [Concepts](#concepts)
  - [References](#references)
<!-- /TOC -->

# Docker overview
**Docker**. An open platform for developing, shipping, and running applications
* *Purposes*.
    * Docker enables us to separate applications from infrastructure for fast software delivery
    * Docker allows us to manage infrastructure in the same ways as managing applications
* *Conclusion*. By taking advantage of Docker’s methodologies for shipping, testing, and deploying code quickly
    
    $\to$ We can significantly reduce the delay between writing code and running it in production

## Linux namespace
**Namespace**. A feature of the Linux kernel that partitions kernel resources

$\to$ One set of processes sees one set of resources while another set of processes sees a different set of resources
* *Idea*. 
    1. A Linux system starts out with a single namespace of each type, used by all processes
    2. Processes can create additional namespaces and join different namespaces
* *Terminology*. The term "namespace" is often used for a type of namespace, e.g. process ID, as well as for a particular space of names
* *Analogy*. Just as `chroot` allows processes to see any arbitrary directory as the root of the system, independent of the rest of the processes
    
    $\to$ Linux namespaces allow other aspects of the OS to be independently modified as well, including the process tree, networking interfaces, mount points, inter-process communication resources, etc.

>**NOTE**. Namespaces are a fundamental aspect of containers on Linux

**Implementation details**.
* *Idea*. The kernel assigns each process a symbolic link per namespace kind in `/proc/<pid>/ns/`
    * *Example*.

        ```bash
        sudo ls -la /proc/<some_pid>/ns/
        # Outputs:
        total 0
        dr-x--x--x 2 root root 0 Thg 5   4 10:45 .
        dr-xr-xr-x 9 root root 0 Thg 4  29 09:34 ..
        lrwxrwxrwx 1 root root 0 Thg 5   4 10:45 cgroup -> 'cgroup:[4026531835]'
        lrwxrwxrwx 1 root root 0 Thg 5   4 10:45 ipc -> 'ipc:[4026531839]'
        lrwxrwxrwx 1 root root 0 Thg 5   4 10:45 mnt -> 'mnt:[4026531840]'
        lrwxrwxrwx 1 root root 0 Thg 5   4 10:45 net -> 'net:[4026531992]'
        lrwxrwxrwx 1 root root 0 Thg 5   4 10:45 pid -> 'pid:[4026531836]'
        lrwxrwxrwx 1 root root 0 Thg 5   4 10:45 pid_for_children -> 'pid:[4026531836]'
        lrwxrwxrwx 1 root root 0 Thg 5   4 10:45 time -> 'time:[4026531834]'
        lrwxrwxrwx 1 root root 0 Thg 5   4 10:45 time_for_children -> 'time:[4026531834]'
        lrwxrwxrwx 1 root root 0 Thg 5   4 10:45 user -> 'user:[4026531837]'
        lrwxrwxrwx 1 root root 0 Thg 5   4 10:45 uts -> 'uts:[4026531838]'
        ```
    
    * *Explain*. The inode number pointed to by this symlink is the same for each process in this namespace
        
        $\to$ This uniquely identifies each namespace by the inode number pointed to by one of its symlinks
    * *Consequence*. Reading the symlink via `readlink` returns a string containing the namespace kind name, and the inode number of the namespace
* *Syscalls to manipulate namespaces*
    * `clone`. Flag to specify which new namespace the new process should be migrated to
    * `unshare`. Allow a process, or thread, to disassociate parts of its execution context, which are currently being shared with other processes, or threads
    * `setns`. Enter the namespace specified by a file descriptor
* *Destruction*. If a namespace is no longer referenced, it will be deleted
    
    $\to$ The handling of the contained resource depends on the namespace kind
* *Namespace reference*. Can be accomplished in three ways
    * By a process belonging to the namespace
    * By an open filedescriptor to the namespace's file `/proc/<pid>/ns/<ns-kind>`
    * A bind mount of the namespace's file `/proc/<pid>/ns/<ns-kind>`

### Process namespace
**Process tree**. Historically, the Linux kernel has maintained a single process tree

<div style="text-align:center">
    <img src="https://uploads.toptal.io/blog/image/674/toptal-blog-image-1416487554032.png">
    <figcaption>Process tree</figcaption>
</div>

* *Process tree*. Contain a reference to every process currently running in a parent-child hierarchy
    * *Process privileges*. Given sufficient privileges and satisfies certain conditions
        
        $\to$ A process can inspect another process by attaching a tracer to it or may even be able to kill it
* *Process namespace*. With the introduction of Linux namespaces, it became possible to have multiple nested process trees
    * *Nested process tree*. Each process tree can have an entirely isolated set of processes
        * *Consequece*. This can ensure that processes belonging to one process tree cannot inspect or kill, in fact cannot even know of the existence of, processes in other sibling or parent process trees

**Process tree initiation**.
* *Root tree initiation*. Every time a computer with Linux boots up
    1. It starts with just one process, with process identifier `(PID)1`
        
        $\to$ This process is the root of the process tree
    2. The root process initiates the rest of the system by performing the appropriate maintenance work and starting the correct daemons/services
        
        $\to$ All the other processes start below this process in the tree
* *PID namespace*. Allow one to spin off a new tree, with its own `(PID)1` process
    * *Idea*. The process doing this remains in the parent namespace, in the original tree, but makes the child the root of its own process tree
    * *Scope of processes in a namespace*. 
        * With PID namespace isolation, processes in the child namespace have no way of knowing of the parent process’s existence
        * Processes in the parent namespace have a complete view of processes in the child namespace, as if they were any other process in the parent namespace
* *Nested child namespaces*. One process starts a child process in a new PID namespace
    
    $\to$ That child process spawns yet another process in a new PID namespace

**Multiple PIDs associated with a process**. With the introduction of PID namespaces

$\to$ A single process can now have multiple PIDs associated with it, one for each namespace it falls under
* *Linux source code reference*. 
    * *`pid` struct*. Used to keep track of multiple PIDs through the use of a struct `upid`

        ```cpp
        struct upid {
        int nr;                     // the PID value
        struct pid_namespace *ns;   // namespace where this PID is relevant
        // ...
        };

        struct pid {
        // ...
        int level;                  // number of upids
        struct upid numbers[0];     // array of upids
        };
        ```

**System calls**.
* *`clone()` system call*. To create a new PID namespace
    
    $\to$ One must call the `clone()` system call with a special flag `CLONE_NEWPID`
    * *Procedure*. The new process immediately starts in a new PID namespace, under a new process tree
        
        $\to$ This can be demonstrated with a simple `C` program

        ```cpp
        #define _GNU_SOURCE
        #include <sched.h>
        #include <stdio.h>
        #include <stdlib.h>
        #include <sys/wait.h>
        #include <unistd.h>

        static char child_stack[1048576];

        static int child_fn() {
            printf("PID: %ld\n", (long)getpid());
            return 0;
        }

        int main() {
            pid_t child_pid = clone(
                child_fn, child_stack+1048576, 
                CLONE_NEWPID | SIGCHLD, NULL
            );
            printf("clone() = %ld\n", (long)child_pid);

            waitpid(child_pid, NULL, 0);
                return 0;
        }
        ```
        
      * *Explain*. Compile and run this program with root privileges and we will notice an output that resembles this
  
          ```bash
          clone() = 5304
          PID: 1
          ```
                  
* *`unshare()` system call*. Other namespaces can also be created using the `unshare()` system call
    
    >**NOTE**. A PID namespace can only be created at the time a new process is spawned using `clone()`
    
### Network namespace
**Network namespace**. Allow each of processes in a namespace to see an entirely different set of networking interfaces

>**NOTE**. Even the loopback interface is different for each network namespace

**System call**. Introducing flag `CLONE_NEWNET` to the `clone()` function call
* *Example code*.

    ```cpp
    #define _GNU_SOURCE
    #include <sched.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <sys/wait.h>
    #include <unistd.h>


    static char child_stack[1048576];

    static int child_fn() {
        printf("New `net` Namespace:\n");
        system("ip link");
        printf("\n\n");
        return 0;
    }

    int main() {
        printf("Original `net` Namespace:\n");
        system("ip link");
        printf("\n\n");

        pid_t child_pid = clone(
            child_fn, child_stack+1048576, 
            CLONE_NEWPID | CLONE_NEWNET | SIGCHLD, NULL
        );

        waitpid(child_pid, NULL, 0);
        return 0;
    }
    ```

* *Output*.

    ```bash
    Original `net` Namespace:
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    2: enp4s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
        link/ether 00:24:8c:a1:ac:e7 brd ff:ff:ff:ff:ff:ff


    New `net` Namespace:
    1: lo: <LOOPBACK> mtu 65536 qdisc noop state DOWN mode DEFAULT group default
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    ```

* *Problem*. The network interface in the child namespace is not usable
    * The physical ethernet device `enp4s0` belongs to the global network namespace
        
        $\to$ However, the physical interface is not available in the new network namespace
    * The loopback device is active in the original network namespace, but is `DOWN` in the child network namespace
* *Solution*. 

    <div style="text-align:center">
        <img src="https://uploads.toptal.io/blog/image/675/toptal-blog-image-1416487605202.png">
        <figcaption>Network interface with routing process</figcaption>
    </div>

    * Set up additional virtual network interfaces spanning multiple namespaces
        
        $\to$ Once that is done, we can create Ethernet bridges, and even route packets between the namespaces
    * To make the whole thing work, a routing process must be running in the global network namespace
        * *Routing process*. Receive traffic from the physical interface, and route it through the appropriate virtual interfaces to the correct child network namespaces

**Creating a routing process**.
* *Option 1 - Linux network namespace*. Linux network namespace is comprised of a routing process to multiple child net namespaces
* *Option 2 - Manual setup*. Create a pair of virtual Ethernet connections between a parent and a child namespace by running a single command from the parent namespace

    ```bash
    ip link add name veth0 type veth peer name veth1 netns <pid>
    ```

    where `<pid>` is the process ID of the process in the child namespace as observed by the parent
    * *Explain*. Running this command establishes a pipe-like connection between these two namespaces, i.e.
        * The parent namespace retains the `veth0` device
        * The `veth1` device is passed to the child namespace
    * *Consequence*. Anything entering one of the ends, comes out through the other end
        
        $\to$ Just as you would expect from a real Ethernet connection between two real nodes
        
        >**NOTE**. Accordingly, both sides of this virtual Ethernet connection must be assigned IP addresses

### Mount namespace
**Linux mountpoints**. Linux also maintains a data structure for all the mountpoints of the system
* *Mountpoint data structure*. Include information like what disk partitions are mounted, where they are mounted, whether they are readonly, etc. 
* *Linux namespaces*. One can have this data structure cloned
    
    $\to$ Processes under different namespaces can change the mountpoints without affecting each other

**Mount namespace creation**. Creating separate mount namespace has an effect similar to doing a `chroot()`
* *`chroot()`*. Do not provide complete isolation, and its effects are restricted to the root mountpoint only
* *Creating a separate mount namespace*. Allow each of these isolated processes to have a completely different view of the entire system’s mountpoint structure from the original one
    
    $\to$ This allows you to have a different root for each isolated process, as well as other mountpoints specific to those processes

**System call**. The `clone()` flag required to achieve this is `CLONE_NEWNS`, i.e.

```cpp
clone(child_fn, child_stack+1048576, CLONE_NEWPID | CLONE_NEWNET | CLONE_NEWNS | SIGCHLD, NULL)
```

* *Mountpoint without namespace*. The child process sees the exact same mountpoints as its parent process would
* *Mountpoint under a new namespace*. The child process can mount or unmount whatever endpoints it wants to, and the change will affect neither its parent’s namespace, nor any other mount namespace in the entire system
    * *Example*. If the parent process has a particular disk partition mounted at root
        * The isolated process will see the exact same disk partition mounted at the root in the beginning
        * Under mountpoint namespace, when the isolated process tries to change the root partition to something else
            
            $\to$ The change will only affect the isolated mount namespace

**Abusement of mountpoint namespaces**. It is a bad idea to spawn the target child process directly with the `CLONE_NEWNS` flag
* *A better approach*. 
    1. Start a special `init` process with the `CLONE_NEWNS` flag
    2. Have the `init` process change the `/`, `/proc`, `/dev` or other mountpoints as desired
    3. Start the target process

### Other namespaces
**Other namespaces**. There are other namespaces that these processes can be isolated into, namely user, IPC, and UTS
* *User namespace*. Allow a process to have root privileges within the namespace, without giving it that access to processes outside of the namespace
* *IPC namespace*. Isolating a process by the IPC namespace gives it its own interprocess communication resources, e.g. System V IPC and POSIX messages
* *UNIX time sharing (UTS) namespace*. Isolate two specific identifiers of the system, i.e. nodename and domainname

### Cross-namespace commuication
**Brief**. Often it is necessary to establish communication between the parent and the child namespace
* *Example*. 
    * For doing configuration work within an isolated environment
    * To retain the ability to peek into the condition of that environment from outside
* *Naive solution*. Keep an SSH daemon running within the isolated environment
    
    $\to$ We can have a separate SSH daemon inside each network namespace
    * *Drawback*. Having multiple SSH daemons running uses a lot of valuable resources, e.g. memory
        
        $\to$ This is where having a special “init” process proves to be a good idea

**`init` process**. Can establish a communication channel between the parent namespace and the child namespace
* *Communication channel*. Can be based on UNIX sockets or can even use TCP
* *UNIX socket spanning two namespaces*. To create a UNIX socket that spans two different mount namespaces, we need to
    1. Create the child process
    2. Create the UNIX socket
    3. Isolate the child into a separate mount namespace
* *Implementation*. How can we create the process first, and isolate it later? 
    
    $\to$ Linux provides `unshare()`
    * *`unshare()` system call*. Allow a process to isolate itself from the original namespace, instead of having the parent isolate the child in the first place
* *Example*. 

    ```cpp
    #define _GNU_SOURCE
    #include <sched.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <sys/wait.h>
    #include <unistd.h>


    static char child_stack[1048576];

    static int child_fn() {
        // calling unshare() from inside the init process lets you create a new namespace after a new process has been spawned
        unshare(CLONE_NEWNET);

        printf("New `net` Namespace:\n");
        system("ip link");
        printf("\n\n");
        return 0;
    }

    int main() {
        printf("Original `net` Namespace:\n");
        system("ip link");
        printf("\n\n");

        pid_t child_pid = clone(
            child_fn, child_stack+1048576, CLONE_NEWPID | SIGCHLD, NULL
        );

        waitpid(child_pid, NULL, 0);
        return 0;
    }
    ```

**Play around with `init` process**. Since the `init` process is something we have devised

$\to$ We can make it do all the necessary work first, and then isolate itself from the rest of the system before executing the target child

## Docker platform
**Container**. Docker provides the ability to package and run an application in a loosely isolated environment called a container
* *Concurrently running containers*. The isolation and security allows running many containers simultaneously on a given host
* *Isolation*. Containers are lightweight and contain everything needed to run the application
    
    $\to$ We do not need to rely on what is currently installed on the host
* *Sharing containers*. We can easily share containers, and be sure that everyone gets the same container working in the same way

**Provided tooling and platform by Docker**. Docker provides tooling and a platform to manage the lifecycle of your containers
* Develop application and its supporting components using containers
* The container becomes the unit for distributing and testing the application
* Deploy the application into production environment, as a container or an orchestrated service
    
    $\to$ This works the same whether your production environment is a local data center, a cloud provider, or a hybrid of the two

**Usage of Docker**.
* *Fast and consistent delivery of applications*.
    * *Key points*.
        * Docker streamlines the development lifecycle by allowing developers to work in standardized environments
            * *Explain*. Using local containers, which provide applications and services
        * Containers are great for continuous integration and continuous delivery (CI/CD) workflows
    * *Workflow with Docker*.
        * Developers write code locally and share their work with their colleagues using Docker containers
        * Developers use Docker to push their applications into a test environment and execute automated and manual tests
        * When bugs are found, developers can fix them in the development environment
            
            $\to$ Developers then redeploy them to the test environment for testing and validation
        * When testing is complete, getting the fix to the customer is as simple as pushing the updated image to the production environment
* *Responsive deployment and scaling*.
    * *Responsive deployment*. Docker’s container-based platform allows for highly portable workloads
        * *Explain*. Docker containers can run on a developer’s local laptop, on physical or virtual machines in a data center, on cloud providers, or in a mixture of environments
    * *Scaling*. Docker’s portability and lightweight nature makes it easy to carry out the followings in near real time
        * Dynamically manage workloads
        * Scale up or tear down applications and services as business needs dictate
* *Running more workloads on the same hardware*. Docker is lightweight and fast
    
    $\to$ It provides a viable, cost-effective alternative to hypervisor-based virtual machines
    * *Consequence*. 
        * We can use more of our compute capacity to achieve business goals
        * Docker is perfect for high density environments and for small and medium deployments, where we need to do more with fewer resources

## Docker architecture
**Docker architecture**. Docker uses a client-server architecture

<div style="text-align:center">
    <img src="https://docs.docker.com/engine/images/architecture.svg">
    <figcaption>Docker architecture</figcaption>
</div>

* *Idea*. Docker clients talks to the Docker daemon, which does the heavy lifting of building, running, and distributing Docker containers 
    * *Physical implementation*. 
        * The Docker client and daemon can run on the same system, or
        * The Docker client connects to a remote Docker daemon
    * *Client-daemon communication*. Use a REST API, over UNIX sockets or a network interface
* *Docker compose*. Another Docker client, which allows working with applications consisting of a set of containers

**Docker daemon (`dockerd`)**. 
* Listen for Docker API requests
* Manage Docker objects, e.g. images, containers, networks, and volumes
* Communicate with other daemons to manage Docker services

**Docker client (`docker`)**. The primary way many Docker users interact with Docker
* *Command execution*. When you use commands, e.g. `docker run`, the client sends these commands to `dockerd`, which carries them out
* *Docker API*. The `docker` command uses the Docker API
* *Client-daemon communication*. A Docker client can communicate with more than one daemon
* *Docker Desktop*. An easy-to-install application for Mac or Windows environment, which enables building and sharing containerized applications and microservices
    * *Components*. Docker Desktop includes 
        * Docker daemon (`dockerd`)
        * Docker client (`docker`)
        * Docker Compose
        * Docker Content Trust
        * Kubernetes
        * Credential Helper
* *Docker registry*. Store Docker images
    * *Docker Hub*. A public registry that anyone can use
        
        $\to$ Docker is configured to look for images on Docker Hub by default
    * *Private registry*. We can even run our own private registry
    * *Commands to interact with Docker registry*. 
        * *Pulling Docker images*. When using the `docker pull` or `docker run` commands
            
            $\to$ The required images are pulled from your configured registry
        * *Pushing DOcker images*. When using the `docker push` command
            
            $\to$ Our image is pushed to our configured registry

**Docker objects**. When using Docker, you are creating and using images, containers, networks, volumes, plugins, and other objects
* *Docker image*. A read-only template with instructions for creating a Docker container
    * *Image inheritance*. An image is often based on another image, with some additional customization
    * *Creating images*. We can create our own images or only use those created by others and published in a registry
    * *Building a an image*. Create a Dockerfile with a simple syntax for defining the steps needed to create the image and run it
        * *Dockerfile*. Each instruction in a Dockerfile creates a layer in the image
        * *Layer caching*. When changing the Dockerfile and rebuilding the image
            
            $\to$ Only changed layers are rebuilt
            * *Consequence*. Images are so lightweight, small, and fast, when compared to other virtualization technologies
* *Docker container*. A runnable instance of an image
    * *Operations on containers*. 
        * We can create, start, stop, move, or delete a container using the Docker API or CLI
        * We can connect a container to one or more networks, attach storage to it
        * We can create a new image based on its current state
    * *Container isolation*.
        * *Default mode*. A container is relatively well isolated from other containers and its host machine
        * *Custom mode*. We can control how isolated a container’s network, storage, or other underlying subsystems are from other containers or from the host machine
    * *Container definition*.  A container is defined by its image and any configuration options provided to it during creation or initialization
    * *Persistency of containers*. When a container is removed, any changes to its state that are not stored in persistent storage disappear

## The underlying technology
**Programming framework**. Docker is written in the Go programming language and takes advantage of several features of the Linux kernel to deliver its functionality

**Namespace**. Docker uses namespaces to provide the isolated workspace called the container
* *Idea*. When you run a container, Docker creates a set of namespaces for that container
      
    $\to$ These namespaces provide a layer of isolation
    * *Explain*. Each aspect of a container runs in a separate namespace and its access is limited to that namespace

# Appendix
## Concepts
**Namespace versus `cgroups`**. Namespaces provide isolation of system resources, and `cgroup`s allow for fine‑grained control and enforcement of limits for those resources
* *`cgroups`*. Limit how much a process can use
* *Namespaces*. Limit what a process can see, and therefore use

## References
* https://www.toptal.com/linux/separation-anxiety-isolating-your-system-with-linux-namespaces