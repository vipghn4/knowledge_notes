<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Kubernetes Pods and Services](#kubernetes-pods-and-services)
  - [Pods](#pods)
    - [Pod lifecycle](#pod-lifecycle)
    - [Creating pods](#creating-pods)
    - [Pod requests](#pod-requests)
    - [Pod limits](#pod-limits)
      - [Pod templates](#pod-templates)
    - [Pod usage patterns](#pod-usage-patterns)
  - [Deployment object](#deployment-object)
    - [Usage patterns](#usage-patterns)
    - [Updating Deployments](#updating-deployments)
    - [Status and lifecycle](#status-and-lifecycle)
  - [Service](#service)
    - [Needs for Kubernetes Service](#needs-for-kubernetes-service)
    - [Types of Kubernetes services](#types-of-kubernetes-services)
- [References](#references)
<!-- /TOC -->

# Kubernetes Pods and Services
## Pods
**Pods**. The smallest, most basic deployable objects in Kubernetes

$\to$ A Pod represents a single instance of a running process in your cluster
* *Pods and containers*. Pods contain one or more containers, e.g. Docker containers
    * *Sharing resources between containers within a pod*. When a Pod runs multiple containers
        
        $\to$ the containers are managed as a single entity and share the Pod's resources
    * *Sharing networking and storage resources between containers within a pod*. Pods also contain shared networking and storage resources for their containers
        * *Network*. Pods are automatically assigned unique IP addresses
            
            $\to$ Pod containers share the same network namespace, i.e. IP address and network ports
            * *Communication between containers within a pod*. Containers in a Pod communicate with each other inside the Pod on `localhost`
        * *Storage*. Pods can specify a set of shared storage volumes to be shared among the containers
* *Interpretation*. A Pod can be considered as a self-contained, isolated "logical host" that contains the systemic needs of the application it serves
* *Intended usage*. Run a single instance of our application on our cluster
    * *Pod creation*. It is not recommended to create individual Pods directly
        
        $\to$ We generally create a set of identical Pods, i.e. replicas, to run our application
    * *Management of replicated Pods*. Pod replicas are created and managed by a controller, e.g. a Deployment
        * *Controllers*. 
            * Manage the lifecycle of their constituent Pods
            * Perform horizontal scaling, i.e. changing the number of Pods as necessary

    >**NOTE**. Although we may occasionally interact with Pods directly to debug, troubleshoot, or inspect them
    >
    >$\to$ It is highly recommended that you use a controller to manage the Pods

**Pods and Nodes**. Pods run on nodes in our cluster
* *Pod termination*. Once created, a Pod remains on its node until 
    * Its process is complete, or
    * It is deleted, or
    * It is evicted from the node due to lack of resources, or
    * The node fails, i.e. if a node fails
        
        $\to$ Pods on the node are automatically scheduled for deletion

### Pod lifecycle
**Pod lifecycle**. They are not designed to run forever, and when a Pod is terminated it cannot be brought back
* *Pod deletion*. Pods do not disappear until they are deleted by a user or by a controller
* *Pod recovery*. Pods do not heal or repair themselves
    * *Example*. 
        * If a Pod is scheduled on a node which later fails, the Pod is deleted
        * If a Pod is evicted from a node for any reason, the Pod does not replace itself

**Pod status**. Each Pod has a `PodStatus` API object represented by a Pod's status field

$\to$ Pods publish their phase to the `status: phase` field
* *Pod phase*. A high-level summary of the Pod in its current state
* *Possible pod phases*.
    * *Pending*. Pod has been created and accepted by the cluster, but one or more of its containers are not running
        * *Explain*. This phase includes time spent being scheduled on a node and downloading images
    * *Running*. Pod has been bound to a node, and all of the containers have been created
        
        $\to$ At least one container is running, is in the process of starting, or is restarting
    * *Succeeded*. All containers in the Pod have terminated successfully
        
        >**NOTE**. Terminated Pods do not restart

    * *Failed*. All containers in the Pod have terminated, and at least one container has terminated in failure
        * *Container failure*. A container fails if it exits with a non-zero status
    * *Unknown*. The state of the Pod cannot be determined
* *Pod condition*. `PodStatus` contains an array called `PodConditions`, which is represented in the Pod manifest as `conditions`
    * *`PodConditions`*. The field has a `type` and `status` field. 
        * *`conditions`*. Indicates more specifically the conditions within the Pod that are causing its current status
            * *`type` field*. Contain `PodScheduled`, `Ready`, `Initialized`, and `Unschedulable`
            * *`status` field*. Correspond with the `type` field, and can contain `True`, `False`, or `Unknown`

### Creating pods
**Creating pods using controller**. It is not recommended to create Pods directly

$\to$ We can use a controller, e.g. a Deployment, to create and manage Pods
* *Other usages of controllers*. Rolling out updates, e.g. changing the version of an application running in a container
    * *Explain*. The controller manages the whole update process for us

### Pod requests
**Pod requests**. When a Pod starts running, it requests an amount of CPU and memory
* *Purposes*. Help Kubernetes schedule the Pod onto an appropriate node to run the workload
    * *Explain*. A Pod will not be scheduled onto a node that does not have the resources to honor the Pod's request
* *Pod's request*. The minimum amount of CPU or memory that Kubernetes guarantees to a Pod
* *Request specification for pods*
    * We can configure the CPU and memory requests for a Pod, based on the resources our applications need
    * We can also specify requests for individual containers running in the Pod

>**NOTE**. It is strongly recommended that we configure requests for our Pods

### Pod limits
**Pod limits**. By default, a Pod has no upper bound on the maximum amount of CPU or memory it can use on a node

$\to$ We can set limits to control the amount of CPU or memory our Pod can use on a node
* *Limit*. The maximum amount of CPU or memory that Kubernetes guarantees to a Pod
* *Setting limits for individual containers*. We can specify limits for each container running in the Pod
    * *Pod limits from container limits*. If specifying only limits for the containers
        
        $\to$ The Pod's limits are the sum of the limits specified for the containers
    * *Requirements*. Each container can only access resources up to its limit
        
        $\to$ If choosing to specify the limits on containers only, we must specify limits for each container
    
    >**NOTE**. If we specify both, the sum of limits for all containers must not exceed the Pod limit

**Pod limits and pod scheduling**. Limits are not taken into consideration when scheduling Pods, i.e.
* Limits can prevent resource contention among Pods on the same node
* Limits can prevent a Pod from causing system instability on the node by starving the underlying OS of resources

>**NOTE**. It is strongly recommended that we configure limits for our Pods

#### Pod templates
**Pod templates**. Controller objects, e.g. Deployments and StatefulSets, contain a Pod template field
* *Pod template structure*. Contain a Pod specification which determines how each Pod should run, i.e.
    * Which containers should be run within the Pods
    * Which volumes the Pods should mount
* *Usage*. Controller objects use Pod templates to create Pods and to manage their desired state within the cluster
* *Changing pod templates*. When a Pod template is changed
    
    $\to$ All future Pods reflect the new template, but all existing Pods do not

### Pod usage patterns
**Ways of using a pod**.
* *Pods running a single container*. The simplest and most common Pod pattern
    * *Explain*. A single container represents an entire application, i.e. the Pod as a wrapper
* *Pods running multiple containers*. Pods with multiple containers are primarily used to support colocated, co-managed programs required to share resources
    
    $\to$ These colocated containers might form a single cohesive unit of service
    * *Consequence*. The Pod wraps these containers and storage resources together as a single manageable entity

**Replication**. Each Pod is meant to run a single instance of a given application

$\to$ For running multiple instances, we should use one Pod for each instance of the application
* *Managing replicated pods*. Replicated Pods are created and managed as a group by a controller, e.g. a Deployment

## Deployment object
**Deployments**. A set of multiple, identical Pods with no unique identities
* *Explain*. A Deployment runs multiple replicas of our application and automatically replaces any instances that fail or become unresponsive
    * *Consequence*. Deployments ensure that one or more instances of our application are available to serve user requests
* *Managing Deployments*. Deployments are managed by the Kubernetes Deployment controller

**Pod template of Deployments**. Contain a specification for the Deployment's Pods
* *Pod specification*. Determine how each Pod should look like, i.e.
    * What applications should run inside its containers
    * Which volumes the Pods should mount, its labels, etc.
* *Changing pod template*. When a Deployment's Pod template is changed
    
    $\to$ New Pods are automatically created one at a time

### Usage patterns
**Usage patterns**. Deployments are well-suited for stateless applications using `ReadOnlyMany` or `ReadWriteMany` volumes mounted on multiple replicas
* *Stateless applications*. Applications which do not store data or application state to the cluster or to persistent storage

**Cases not to use Deployment**. For workloads using `ReadWriteOnce` volumes

$\to$ For stateful applications using `ReadWriteOnce` volumes, use `StatefulSets`
* *Explain*. `StatefulSets` are designed to deploy stateful applications and clustered applications saving data to persistent storage
    
    $\to$ StatefulSets are suitable for deploying Kafka, MySQL, Redis, ZooKeeper, and other applications needing unique, persistent identities and stable hostnames

### Updating Deployments
**Updating Deployments**. We can update a Deployment by making changes to the Deployment's Pod template specification
  
$\to$ This automatically triggers an update rollout
* *Work flow*. By default, when a Deployment triggers an update
    1. The Deployment stops the Pods
    2. The Deployment gradually scales down the number of Pods to zero
    3. The Deployment drains and terminates the Pods
    4. The Deployment uses the updated Pod template to bring up new Pods
    5. Old Pods are not removed until a sufficient number of new Pods are Running
    6. New Pods are not created until a sufficient number of old Pods have been removed

### Status and lifecycle
**Status**. Deployments can be in one of three states during its lifecycle
* *Progressing*. The Deployment is in process of performing its tasks, e.g. bringing up or scaling its Pods
* *Completed*. The Deployment has successfully completed its tasks, i.e.
    * All of its Pods are running with the latest specification and are available
    * No old Pods are running
* *Failed*. The Deployment has encountered one or more issues preventing it from completing its tasks

## Service
**Service**. Group a set of Pod endpoints into a single resource

$\to$ We can configure various ways to access the grouping
* *Pod access methods*. There is a stable cluster IP address that clients inside the cluster can use to contact Pods in the Service
    
    $\to$ A client sends a request to the stable IP address, and the request is routed to one of the Pods in the Service
* *Member Pod identification in Service*. Use a selector
    * *Idea*. For a Pod to be a member of the Service
        
        $\to$ The Pod must have all of the labels specified in the selector
    * *Pod label*. An arbitrary key/value pair that is attached to an object
* *Example*. A selector specifies two labels, i.e. any Pod having both the `app: metrics` label and the `department:engineering` label is a member of this Service

    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
    name: my-service
    spec:
    selector:
        app: metrics
        department: engineering
    ports:
    ...
    ```

**Service endpoints**. When creating a Service, Kubernetes creates an Endpoints object with the same name as our Service

$\to$ This is used to keep track of which Pods are members of the Service

### Needs for Kubernetes Service
**Needs for Kubernetes Service**. 
* In a Kubernetes cluster, each Pod has an internal IP address

    $\to$ The Pods in a Deployment come and go, and their IP addresses change
    * *Consequence*. It does not make sense to use Pod IP addresses directly
    * *Solution with a Service*. We get a stable IP address lasting for the life of the Service
* A Service also provides load balancing
    * *Explain*. Clients call a single, stable IP address
        
        $\to$ Their requests are balanced across the member Pods of the Service

### Types of Kubernetes services
**Types of Kubernetes services**.
* *ClusterIP (default)*. Internal clients send requests to a stable internal IP address
* *NodePort*. Clients send requests to the IP address of a node on one or more `nodePort` values specified by the Service

    $\to$ This is an extension of ClusterIP
    * *Consequence*. A NodePort Service has a cluster IP address
* *LoadBalancer*. Clients send requests to the IP address of a network load balancer

    $\to$ This is an extension of NodePort
    * *Consequence*. A LoadBalancer Service has a cluster IP address and one or more `nodePort` values
* *ExternalName*. Internal clients use the DNS name of a Service as an alias for an external DNS name
* *Headless*. We can use a headless service when we want a Pod grouping, but do not need a stable IP address

# References
* https://cloud.google.com/kubernetes-engine/docs/concepts/pod#:~:text=Pods%20are%20the%20smallest%2C%20most,and%20share%20the%20Pod's%20resources.