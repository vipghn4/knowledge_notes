<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Kubernetes](#kubernetes)
  - [Kubernetes](#kubernetes-1)
    - [Historical deployment strategies](#historical-deployment-strategies)
    - [Needs for Kubernetes](#needs-for-kubernetes)
  - [Kubernetes components](#kubernetes-components)
    - [Node components](#node-components)
    - [Add-ons](#add-ons)
- [Appendix](#appendix)
  - [Concepts](#concepts)
<!-- /TOC -->

# Kubernetes
## Kubernetes
**Kubernetes (K8s)**. A portable, extensible, open source platform for managing containerized workloads and services

$\to$ Kubernetes facilitates both declarative configuration and automation
* *"Kubernetes"*. Originate from Greek, meaning helmsman or pilot
    * *"K8s"*. An abbreviation results from counting the eight letters between the "K" and the "s"
    * *Author*. Google

### Historical deployment strategies

<div style="text-align:center">
    <img src="https://d33wubrfki0l68.cloudfront.net/26a177ede4d7b032362289c6fccd448fc4a91174/eb693/images/docs/container_evolution.svg">
    <figcaption>Common deployment strategies through time</figcaption>
</div>

**Traditional deployment area**. Early on, organizations ran applications on physical servers

$\to$ There was no way to define resource boundaries for applications in a physical server
* *Consequence*. This causes resource allocation issues
    * *Example*. If multiple applications run on a physical server
        
        $\to$ There can be instances where one application would take up most of the resources, and as a result, the other applications would underperform
* *Solution*. Run each application on a different physical server
    * *Drawback*. 
        * This did not scale as resources were underutilized
        * This was expensive for organizations to maintain many physical servers

**Virtualized deployment era**. Allow us to run multiple VMs on a single physical server's CPU
* *Benefits*. 
    * Allow applications to be isolated between VMs
    * Provide a level of security, i.e. the information of one application cannot be freely accessed by another application
    * Allow better utilization of resources in a physical server and allows better scalability
        * *Explain*. An application can be added or updated easily, reduces hardware costs, etc.
* *Consequence*. We can present a set of physical resources as a cluster of disposable virtual machines

    $\to$ Each VM is a full machine running all the components, including its own operating system, on top of the virtualized hardware

**Container deployment era**. Similar to VMs, but containers have relaxed isolation properties to share the OS among the applications

$\to$ Containers are considered lightweight
* *Similarity to a VM*. A container has its own filesystem, share of CPU, memory, process space, etc. 
    * *Consequence*. Containers are portable across clouds and OS distributions
* *Benefits*.
    * *Agile application creation and deployment*. Increased ease and efficiency of container image creation compared to VM image use
    * *Continuous development, integration, and deployment*. Provide for reliable and frequent container image build and deployment with quick and efficient rollbacks, i.e. due to image immutability
    * *Dev and Ops separation of concerns*. Create application container images at build/release time rather than deployment time
        
        $\to$ This decouples applications from infrastructure
    * *Observability*. Not only surfaces OS-level information and metrics, but also application health and other signals
    * *Environmental consistency across development, testing, and production*. Run the same on a laptop as it does in the cloud
    * *Cloud and OS distribution portability*. Run on Ubuntu, RHEL, CoreOS, on-premises, on major public clouds, and anywhere else
    * *Application-centric management*. Raise the level of abstraction from running an OS on virtual hardware to running an application on an OS using logical resources
    * *Loosely coupled, distributed, elastic, liberated micro-services*. Applications are broken into smaller, independent pieces and can be deployed and managed dynamically
    * *Resource isolation*. Predictable application performance
    * *Resource utilization*. High efficiency and density

### Needs for Kubernetes
**Brief**. In a production environment, we need to manage the containers running the applications and ensure that there is no downtime
* *Kubernetes*. A framework to run distributed systems resiliently

    $\to$ It takes care of scaling and failover for your application, provides deployment patterns, etc. 

**Provided features of Kubernetes**.
* *Service discovery and load balancing*. Kubernetes can expose a container using the DNS name or using their own IP address
    
    $\to$ If traffic to a container is high, Kubernetes is able to load balance and distribute the network traffic, leading to stable deployment
* *Storage orchestration of Kubernetes*. Allow us to automatically mount a storage system of our choice, e.g. local storages, public cloud providers, etc.
* *Automated rollouts and rollbacks*. We can describe the desired state for our deployed containers using Kubernetes
    
    $\to$ Kubernetes can change the actual state to the desired state at a controlled rate
    * *Example*. We can automate Kubernetes to 
        * Create new containers for our deployment
        * Remove existing containers and adopt all their resources to the new container
* *Automatic bin packing*. We provide Kubernetes with a cluster of nodes that it can use to run containerized tasks
    * *Idea*. By telling Kubernetes how much CPU and memory (RAM) each container needs
        
        $\to$ Kubernetes can fit containers onto the nodes to make the best use of our resources
* *Self-healing*. Kubernetes 
    * Restart containers that fail
    * Replace containers
    * Kill containers that do not respond to our user-defined health check
    * Do not advertise the failed containers to clients until they are ready to serve
* *Secret and configuration management*. 
    * We can store and manage sensitive information, e.g. passwords, OAuth tokens, and SSH keys, with Kubernetes
    * We can deploy and update secrets and application configuration without rebuilding our container images, and without exposing secrets in our stack configuration

## Kubernetes components
**Kubernetes cluster**. Consist of a set of worker machines, i.e. nodes, running containerized applications

<div style="text-align:center">
    <img src="https://d33wubrfki0l68.cloudfront.net/2475489eaf20163ec0f54ddc1d92aa8d4c87c96b/e7c81/images/docs/components-of-kubernetes.svg">
    <figcaption>Components of a Kubernetes cluster</figcaption>
</div>

>**NOTE**. Every cluster has at least one worker node

* *Worker node(s)*. Host the Pods, i.e. the components of the application workload
* *Control plane*. Manage the worker nodes and the Pods in the cluster
* *Kubernetes in production environments*. 
    * Control plane usually runs across multiple computers
    * A cluster usually runs multiple nodes, providing fault-tolerance and high availability

**The control plane's components**. 
* *Functionality*.
    * Make global decisions about the cluster, e.g. scheduling
    * Detect and respond to cluster events, e.g. starting up a new pod when a deployment's replicas field is unsatisfied
* *Setup*. Control plane components can be run on any machine in the cluster
    * *Convention*. For simplicity, set up scripts typically start all control plane components on the same machine
        
        $\to$ User containers are not on this machine

**API server**. A component of the Kubernetes control plane, which exposes the Kubernetes API

$\to$ This is the front end for the Kubernetes control plane
* *Main implementation*. `kube-apiserver`, which is designed to scale horizontally
    * *Scale horizontally*. Scaling by deploying more instances
    
        $\to$ We can run several instances of `kube-apiserver` and balance traffic between those instances

**Persistence store `etcd`**. Consistent and highly-available key value store used as Kubernetes' backing store for all cluster data

>**NOTE**. If the Kubernetes cluster uses etcd as its backing store
>
>$\to$ Have a back up plan for those data

* *Backing store*. A computer storage device, e.g. disk, providing additional storage space for information
    
    $\to$ It can be accessed and referred to when required and may be copied into the processor if needed
* *`etcd`*. An open source, distributed, consistent key-value store for shared configuration, service discovery, and scheduler coordination of distributed systems or clusters of machines

**Scheduler `kube-scheduler`**. Control plane component watching for newly created Pods with no assigned node, and selects a node for them to run on
* *Scheduling factors*. 
    * Individual and collective resource requirements
    * Hardware/software/policy constraints
    * Affinity and anti-affinity specifications
    * Data locality
    * Inter-workload interference
    * Deadlines

**Controller manager `kube-controller-manager`**. Control plane component running controller processes
* *Idea*. Each controller is logically a separate process
    
    $\to$ To reduce complexity, they are compiled into a single binary and run in a single process
* *Controller manager*. A daemon embedding the core control loops shipped with Kubernetes
    * *Control loop*. A non-terminating loop regulating the state of the system
    * *Controller in Kubernetes*. A control loop watching the shared state of the cluster through the API server

        $\to$ It then makes changes attempting to move the current state towards the desired state 
* *Controller types*.
    * *Node controller*. Responsible for noticing and responding when nodes go down
    * *Job controller*. Watches for Job objects that represent one-off tasks, then creates Pods to run those tasks to completion
        * *One-off tasks*. Tasks which can be independent of any process, or can be added to any active processes
    * *Endpoints controller*. Populates the Endpoints object, i.e. joins Services and Pods
    * *Service account and token controllers*. Create default accounts and API access tokens for new namespaces

**Cloud controller manager `cloud-controller-manager`**. A Kubernetes control plane component embeding cloud-specific control logic
* *Main functionality*. 
    * Let us link our cluster into our cloud provider's API
    * Separate the components interacting with the cloud platform from components only interacting with our cluster
* *Controllers running in cloud controller manager*. The cloud-controller-manager only runs controllers specific to our cloud provider
    
    >**NOTE**. When running Kubernetes on our own premises, or in a learning environment inside our own PC
    >
    >$\to$ The cluster does not have a cloud controller manager

* *Types of controllers*.
    * *Node controller*. For checking the cloud provider to determine if a node has been deleted in the cloud after it stops responding
    * *Route controller*. For setting up routes in the underlying cloud infrastructure
    * *Service controller*. For creating, updating and deleting cloud provider load balancers

### Node components
**Node components**. Run on every node, maintaining running pods and providing the Kubernetes runtime environment

**kubelet**. An agent running on each node in the cluster to make sure that containers are running in a Pod
* *Idea*. The kubelet takes a set of PodSpecs that are provided through various mechanisms
    
    $\to$ It then ensures that the containers described in those PodSpecs are running and healthy
    
    >**NOTE**. The kubelet does not manage containers which were not created by Kubernetes

**kube-proxy**. A network proxy running on each node in the cluster, implementing part of the Kubernetes Service concept
* *Idea*. kube-proxy maintains network rules on nodes, which allow network communication to the Pods from network sessions inside or outside of the cluster
* *Implementation*. Use the OS packet filtering layer if there is one and it is available

    $\to$ Otherwise, kube-proxy forwards the traffic itself.

**Container runtime**. The software responsible for running containers
* *Supported container runtime*. `containerd`, CRI-O, and any other implementation of the Kubernetes CRI (Container Runtime Interface)

### Add-ons
**Add-ons**. Use Kubernetes resources (DaemonSet, Deployment, etc) to implement cluster features
* *Add-on namespaces*. Since these are providing cluster-level features
    
    $\to$ Namespaced resources for addons belong within the kube-system namespace

**DNS**. While the other addons are not strictly required, all Kubernetes clusters should have cluster DNS, as many examples rely on it
* *Cluster DNS*. A DNS server, in addition to the other DNS server(s) in our environment, which serves DNS records for Kubernetes services

>**NOTE**. Containers started by Kubernetes automatically include this DNS server in their DNS searches

**Web UI (Dashboard)**. A general purpose, web-based UI for Kubernetes clusters
* *Purposes*. Allow users to manage and troubleshoot applications running in the cluster, as well as the cluster itself

**Container resource monitoring**. Record generic time-series metrics about containers in a central database, and provides a UI for browsing that data

**Cluster-level logging**. Responsible for saving container logs to a central log store with search/browsing interface

# Appendix
## Concepts
**Key-value database (or key–value store)**. Store data as a collection of key-value pairs in which a key serves as a unique identifier

<div style="text-align:center">
    <img src="https://d1.awsstatic.com/product-marketing/DynamoDB/PartitionKey.8dd0530a7f6d66d101f31de30db515564f4cf28a.png">
    <figcaption>Example of data stored as key-value pairs in DynamoDB</figcaption>
</div>

* *Key-value database*. Consist of
    * A data storage paradigm designed for storing, retrieving, and managing associative arrays, and
    * A dictionary or hash table
* *Dictionaries and keys*. 
    * *Dictionaries*. Contain a collection of objects, or records, which in turn have many different fields within them, each containing data
    * *Keys*. The records are stored and retrieved using a key that uniquely identifies the record, and is used to find the data within the database
* *Key-value database versus relational database*. Key–value databases in very different from relational databases
    * *Relational database*. Predefine the data structure in the database as a series of tables containing fields with well defined data types
        * *Pros*. Exposing the data types to the database program allows it to apply a number of optimizations
    * *Key–value database*. Treat the data as a single opaque collection, which may have different fields for every record
        * *Pros*. 
            * This offers considerable flexibility and more closely follows modern concepts like OOP
            * Since optional values are not represented by placeholders or input parameters, as in most RDBs
                
                $\to$ Key–value databases often use far less memory to store the same database
        * *Cons*. Performance, a lack of standardization and other issues 
* *Historial development*. 
    * Key-value database' drawbacks limited them to niche uses for many years
    * The rapid move to cloud computing after 2010 has led to a renaissance as part of the broader NoSQL movement