 <!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Kubernetes objects](#kubernetes-objects)
  - [Understanding Kubernetes objects](#understanding-kubernetes-objects)
    - [Understanding Kubernetes objects](#understanding-kubernetes-objects-1)
    - [Object spec and status](#object-spec-and-status)
    - [Describing a Kubernetes object](#describing-a-kubernetes-object)
      - [Required Fields](#required-fields)
  - [Kubernetes object management](#kubernetes-object-management)
    - [Imperative commands](#imperative-commands)
    - [Imperative object configuration](#imperative-object-configuration)
    - [Declarative object configuration](#declarative-object-configuration)
  - [Object names and IDs](#object-names-and-ids)
    - [Names](#names)
    - [UIDs](#uids)
  - [Namespaces](#namespaces)
    - [When to use multiple namespaces](#when-to-use-multiple-namespaces)
    - [Working with namespaces](#working-with-namespaces)
    - [Namespaces and DNS](#namespaces-and-dns)
    - [Not all objects are in a Namespace](#not-all-objects-are-in-a-namespace)
  - [Labels and selectors](#labels-and-selectors)
    - [Motivation](#motivation)
    - [Syntax and character set](#syntax-and-character-set)
    - [Label selectors](#label-selectors)
      - [Equality-based requirement](#equality-based-requirement)
      - [Set-based requirement](#set-based-requirement)
    - [API](#api)
      - [LIST and WATCH filtering](#list-and-watch-filtering)
      - [Set references in API objects](#set-references-in-api-objects)
  - [Annotations](#annotations)
    - [Attaching metadata to objects](#attaching-metadata-to-objects)
    - [Syntax and character set](#syntax-and-character-set-1)
  - [Field selector](#field-selector)
    - [Supported fields](#supported-fields)
    - [Supported operators](#supported-operators)
    - [Chained selectors](#chained-selectors)
    - [Multiple resource types](#multiple-resource-types)
  - [Finalizers](#finalizers)
    - [How finalizers work](#how-finalizers-work)
    - [Owner references, labels, and finalizers](#owner-references-labels-and-finalizers)
  - [Owners and dependends](#owners-and-dependends)
    - [Owner references in object specifications](#owner-references-in-object-specifications)
    - [Ownership and finalizers](#ownership-and-finalizers)
<!-- /TOC -->

# Kubernetes objects
## Understanding Kubernetes objects
**Brief**. This note explains how Kubernetes objects are represented in the Kubernetes API, and how you can express them in .yaml format

### Understanding Kubernetes objects
**Kubernetes objects**. Persistent entities in the Kubernetes system, which are used by Kubernetes to represent the state of the cluster
* *Information described by Kubernetes objects*.
    * What containerized applications are running, and on which nodes
    * The resources available to those applications
    * The policies around how those applications behave, e.g. restart policies, upgrades, and fault-tolerance
* *Kubernetes object as a "record of intent"*. Once created the object, the Kubernetes system will constantly work to ensure that object exists
    
    $\to$ Creating an object effectively telling the Kubernetes system what we want our cluster's desired state
* *Working with Kubernetes objects*. We need to use Kubernetes API to create, modify, or delete objects
    * *Using `kubectl`*. When using the `kubectl` command-line interface, the CLI makes the necessary Kubernetes API calls for us
    * *Manual interaction*. We can use the Kubernetes API directly in our own programs using one of the Client Libraries

### Object spec and status
**Object spec and status**. Almost every Kubernetes object includes two nested object fields that govern the object's configuration, i.e. the object `spec` and the object `status`
* *Object `spec`*. For objects having a `spec`, we have to set this when creating the object to provide a description of the desired characteristics of the resource to have, i.e. its desired state
* *Object `status`*. Describe the current state of the object, supplied and updated by the Kubernetes system and its components
    * *Object status management*. The Kubernetes control plane continually and actively manages every object's actual state to match the supplied desired state

**Example**. In Kubernetes, a Deployment is an object representing an application running on the cluster
1. When creating the Deployment, we set the Deployment `spec` to specify that we want three replicas of the application to be running
2. The Kubernetes system reads the Deployment `spec` and starts three instances of our desired application
3. The Kubernetes system updates the status to match our spec
4. If any of those instances should fail, i.e. a status change, the Kubernetes system responds to the difference between `spec` and `status` by making a correction
    
    $\to$ In this case, it starts a replacement instance

### Describing a Kubernetes object
**Brief**. When creating an object in Kubernetes, we must provide the object `spec` to describe its desired state, as well as some basic information about the object, e.g. a name

**Describing an object via Kubernetes API**. When using the Kubernetes API to create the object, either directly or via `kubectl`

$\to$ The API request must include the `spec` as JSON in the request body
* *`yaml` file for `spec`*. Most often, we provide the information to kubectl in a `.yaml` file
    
    $\to$ `kubectl` converts the information to JSON when making the API request

* *Example `.yaml` file*.

    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
        name: nginx-deployment
    spec:
        selector:
            matchLabels:
                app: nginx
        replicas: 2 # tells deployment to run 2 pods matching the template
        template:
            metadata:
                labels:
                    app: nginx
            spec:
                containers:
                - name: nginx
                    image: nginx:1.14.2
                    ports:
                    - containerPort: 80
    ```

* *Example `kubectl` command-line*. Use the `kubectl apply` command in the `kubectl` command-line interface, passing the `.yaml` file as an argument

    ```bash
    kubectl apply -f https://k8s.io/examples/application/deployment.yaml
    ```

#### Required Fields
**Required Fields**.
* *`apiVersion`*. Which version of the Kubernetes API used to create this object
* *`kind`*. What kind of object to create
* *`metadata`*. Data helping to uniquely identify the object, including a name string, UID, and optional namespace
* *`spec`*. The desired state for the object

**Object `spec` format**. The precise format is different for every Kubernetes object, and contains nested fields specific to that object
* *Reference*. The Kubernetes API Reference can help finding the `spec` format for all of the objects to create using Kubernetes

## Kubernetes object management
**Brief**. The `kubectl` command-line tool supports ways to create and manage Kubernetes objects

>**NOTE**. A Kubernetes object should be managed using only one technique. Mixing and matching techniques for the same object results in undefined behavior

| Management technique | Operates on | Recommended environment | Learning curve |
| --- | --- | --- | --- |
| Imperative commands | Live objects | Development projects | Lowest |
| Imperative object configuration | Individual files | Production projects | Moderate |
| Declarative object configuration | Directories of files | Production projects | Highest |

### Imperative commands
**Imperative commands**. When using imperative commands, a user operates directly on live objects in a cluster

$\to$ The user provides operations to the `kubectl` command as arguments or flags

>**NOTE**. This is the recommended way to get started or to run a one-off task in a cluster
>
>* *Explain*. This technique operates directly on live objects, it provides no history of previous configurations

**Examples**. Run an instance of the nginx container by creating a Deployment object

```bash
kubectl create deployment nginx --image nginx
```

**Trade-offs**.
* *Advantages compared to object configuration*.
    * Commands are expressed as a single action word
    * Commands require only a single step to make changes to the cluster
* *Disadvantages compared to object configuration*.
    * Commands do not integrate with change review processes
    * Commands do not provide an audit trail associated with changes
    * Commands do not provide a source of records except for what is live
    * Commands do not provide a template for creating new objects

### Imperative object configuration
**Imperative object configuration**. The `kubectl` command specifies the operation, e.g. create, replace, etc., optional flags and at least one file name

$\to$ The file specified must contain a full definition of the object in YAML or JSON format

**Examples**. 
* Create the objects defined in a configuration file

    ```bash
    kubectl create -f nginx.yaml
    ```

* Delete the objects defined in two configuration files

    ```bash
    kubectl delete -f nginx.yaml -f redis.yaml
    ```

* Update the objects defined in a configuration file by overwriting the live configuration

    ```bash
    kubectl replace -f nginx.yaml
    ```

**Trade-offs**.
* *Advantages compared to imperative commands*.
    * Object configuration can be stored in a source control system such as Git
    * Object configuration can integrate with processes such as reviewing changes before push and audit trails
    * Object configuration provides a template for creating new objects
* *Disadvantages compared to imperative commands*.
    * Object configuration requires basic understanding of the object schema
    * Object configuration requires the additional step of writing a YAML file
* *Advantages compared to declarative object configuration*.
    * Imperative object configuration behavior is simpler and easier to understand
    * As of Kubernetes version 1.5, imperative object configuration is more mature
* *Disadvantages compared to declarative object configuration*
    * Imperative object configuration works best on files, not directories
    * Updates to live objects must be reflected in configuration files, or they will be lost during the next replacement

### Declarative object configuration
**Declarative object configuration**. A user operates on object configuration files stored locally, without defining the operations to be taken on the files

$\to$ Create, update, and delete operations are automatically detected per-object by `kubectl`
* *Consequence*. This enables working on directories, where different operations might be needed for different objects

**Examples**. Process all object configuration files in the `configs` directory, and create or patch the live objects

$\to$ We can first diff to see what changes are going to be made, and then apply

```bash
kubectl diff -f configs/
kubectl apply -f configs/
```

* *Recursively process directories*.

    ```bash
    kubectl diff -R -f configs/
    kubectl apply -R -f configs/
    ```

**Trade-offs**.
* *Advantages compared to imperative object configuration*.
    * Changes made directly to live objects are retained, even if they are not merged back into the configuration files
    * Declarative object configuration has better support for operating on directories and automatically detecting operation types, i.e. create, patch, or delete, per-object
* *Disadvantages compared to imperative object configuration*.
    * Declarative object configuration is harder to debug and understand results when they are unexpected
    * Partial updates using diffs create complex merge and patch operation

## Object names and IDs
**Object names and IDs**.
* *Names*. Each object in a cluster has a Name unique for that type of resource
    * *Example*.
        * We can only have one Pod named `myapp-1234` within the same namespace
        * We can have one Pod and one Deployment that are each named `myapp-1234`
* *UID*. Every Kubernetes object has a UID unique across the whole cluster

>**NOTE**. For non-unique user-provided attributes, Kubernetes provides labels and annotations

### Names
**Names**. A client-provided string referring to an object in a resource URL, e.g. `/api/v1/pods/some-name`
* *Uniqueness within type*. Only one object of a given kind can have a given name at a time
    
    >**NOTE**. If we delete the object, you can make a new object with the same name

    >**NOTE**. When objects represent a physical entity, e.g. a Node representing a physical host, when the host is re-created under the same name without deleting and re-creating the Node
    >
    >$\to$ Kubernetes treats the new host as the old one, which may lead to inconsistencies

**Types of commonly used name constraints for resources**.
* *DNS Subdomain Names*. Most resource types require a name, which can be used as a DNS subdomain name as defined in RFC 1123, i.e. the name must
    * Contain no more than 253 characters
    * Contain only lowercase alphanumeric characters, `-` or `.`
    * Start with an alphanumeric character
    * End with an alphanumeric character
* *RFC 1123 Label Names*. Some resource types require their names to follow the DNS label standard as defined in RFC 1123, i.e. the name must
    * Contain at most 63 characters
    * Contain only lowercase alphanumeric characters or `-`
    * Start with an alphanumeric character
    * End with an alphanumeric character
* *RFC 1035 Label Names*. Some resource types require their names to follow the DNS label standard as defined in RFC 1035, i.e. the name must
    * Contain at most 63 characters
    * Contain only lowercase alphanumeric characters or `-`
    * Start with an alphabetic character
    * End with an alphanumeric character
* *Path Segment Names*. Some resource types require their names to be able to be safely encoded as a path segment
    
    $\to$ The name may not be `.` or `..` and the name may not contain `/` or `%`

>**NOTE**. Some resource types have additional restrictions on their names

### UIDs
**UIDs**. A Kubernetes systems-generated string to uniquely identify objects

$\to$ Every object created over the whole lifetime of a Kubernetes cluster has a distinct UID

* *Usage*. Intended to distinguish between historical occurrences of similar entities
* *UUIDs*. Kubernetes UIDs are universally unique identifiers, i.e. UUIDs, which are standardized as ISO/IEC 9834-8 and as ITU-T X.667

## Namespaces
**Namespaces**. Provide a mechanism for isolating groups of resources within a single cluster

$\to$ Names of resources need to be unique within a namespace, but not across namespaces
* *Usage*. 
    * Namespace-based scoping is applicable only for namespaced objects, e.g. Deployments, Services, etc.
    * Namespace-based scoping is not applicable for cluster-wide objects, e.g. StorageClass, Nodes, PersistentVolumes, etc.

### When to use multiple namespaces
**Brief**. Namespaces are intended for use in environments with many users spread across multiple teams, or projects

$\to$ Namespaces are a way to divide cluster resources between multiple users, via resource quota

**Namespaces**. Provide a scope for names, i.e. names of resources need to be unique within a namespace, but not across namespaces
* *Nested namespace*. Namespaces cannot be nested inside one another
* *Namespace and Kubernetes*. Each Kubernetes resource can only be in one namespace

**Abusement of namespaces**.
* For clusters with a few to tens of users, you should not need to create or think about namespaces at all

    $\to$ Start using namespaces when you need the features they provide
* It is not necessary to use multiple namespaces to separate slightly different resources, e.g. different versions of the same software
    
    $\to$ Use labels to distinguish resources within the same namespace

### Working with namespaces
**Brief**. Creation and deletion of namespaces are described in the Admin Guide documentation for namespaces

>**NOTE**. Avoid creating namespaces with the prefix `kube-`, since it is reserved for Kubernetes system namespaces

**Viewing namespaces**. We can list the current namespaces in a cluster using

```bash
kubectl get namespace
NAME              STATUS   AGE
default           Active   1d
kube-node-lease   Active   1d
kube-public       Active   1d
kube-system       Active   1d
```

**Default namespaces**. Kubernetes starts with four initial namespaces
* *`default`*. Default namespace for objects with no other namespace
* *`kube-system`*. Namespace for objects created by the Kubernetes system
* *`kube-public`*. Created automatically and readable by all users, including those not authenticated
    * *Purposes*. Mostly reserved for cluster usage, in case some resources should be visible and readable publicly throughout the whole cluster
    
    >**NOTE**. The public aspect of this namespace is only a convention, not a requirement

* *`kube-node-lease`*. Hold Lease objects associated with each node
    * *Explain*. Node leases allow the kubelet to send heartbeats so that the control plane can detect node failure
    * *Reference*. https://kubernetes.io/docs/concepts/architecture/nodes/

**Setting the namespace for a request**. To set the namespace for a current request, use the `--namespace` flag
* *Example*.

    ```bash
    kubectl run nginx --image=nginx --namespace=<insert-namespace-name-here>
    kubectl get pods --namespace=<insert-namespace-name-here>
    ```

**Setting the namespace preference**. We can permanently save the namespace for all subsequent `kubectl` commands in that context

```bash
kubectl config set-context --current --namespace=<insert-namespace-name-here>
# Validate it
kubectl config view --minify | grep namespace:
```

### Namespaces and DNS
**Namespace and DNS**. When creating a Service, it creates a corresponding DNS entry of the form `<service-name>.<namespace-name>.svc.cluster.local`
* *Namespace resolving*. 
    * If we use only `<service-name>`, i.e. Service's name
        
        $\to$ The DNS will automatically resolve to the full address of the Service local to our namespace
        * *Example*. `database` is used to connect to the `database` service in the current namespace
    * If you need to access a Service in another Namespace, use the Service name plus the Namespace name, i.e. full form
        * *Example*. `database.test` is used to connect to the `database` service in the `test` namespace
* *Consequence*. This is useful for using the same configuration across multiple namespaces, e.g. Development, Staging and Production
    
    $\to$ To reach across namespaces, we need to use the fully qualified domain name (FQDN)

**Namespace naming convention**. As a result, all namespace names must be valid RFC 1123 DNS labels

**Cautions**. By creating namespaces with the same name as public top-level domains

$\to$ Services in these namespaces can have short DNS names that overlap with public DNS records
* *Consequence*. Workloads from any namespace performing a DNS lookup without a trailing dot will be redirected to those services, taking precedence over public DNS
* *Solution*. Limit privileges for creating namespaces to trusted users
    
    $\to$ If required, we could additionally configure third-party security controls, e.g. admission webhooks, to block creating any namespace with the name of public TLDs

### Not all objects are in a Namespace
**Brief**. 
* Most Kubernetes resources, e.g. pods, services, replication controllers, etc., are in some namespaces
* Namespace resources are not themselves in a namespace
* Low-level resources, e.g. nodes and `persistentVolumes`, are not in any namespace

**Example**. To see which Kubernetes resources are and are not in a namespace

```bash
# In a namespace
kubectl api-resources --namespaced=true

# Not in a namespace
kubectl api-resources --namespaced=false
```

## Labels and selectors
**Labels**. Key/value pairs attached to objects, e.g. pods
* *Usage*. Used to specify identifying attributes of objects, which are meaningful and relevant to users
    
    >**NOTE**. Labels do not directly imply semantics to the core system
    
    $\to$ Labels can be used to organize and to select subsets of objects
* *Creating and adding labels to objects*. Labels can be attached to objects at creation time and subsequently added and modified at any time 
* *Label structure*. Each object can have a set of key/value labels defined
    
    >**NOTE**. Each Key must be unique within a given object

    * *Example*.
        
        ```json
        "metadata": {
            "labels": {
                "key1" : "value1",
                "key2" : "value2"
            }
        }
        ```

* *Conclusion*. Labels allow for efficient queries and watches and are ideal for use in UIs and CLIs

>**NOTE**. Non-identifying information should be recorded using annotations

### Motivation
**Brief**. Labels enable users to map their own organizational structures onto system objects in a loosely coupled fashion, without requiring clients to store these mappings

**Motivation**. Service deployments and batch processing pipelines are often multi-dimensional entities
* *Examples*. 
    * Multiple partitions or deployments
    * Multiple release tracks
    * Multiple tiers
    * Multiple micro-services per tier
* *Problem*. Management often requires cross-cutting operations
    
    $\to$ This breaks encapsulation of strictly hierarchical representations, especially rigid hierarchies determined by the infrastructure rather than by users

**Example pf commonly used labels**.

```json
"release" : "stable", "release" : "canary"
"environment" : "dev", "environment" : "qa", "environment" : "production"
"tier" : "frontend", "tier" : "backend", "tier" : "cache"
"partition" : "customerA", "partition" : "customerB"
"track" : "daily", "track" : "weekly"
```

>**NOTE**. We are free to develop your own conventions

### Syntax and character set
**Label syntax**. Labels are key/value pairs
* *Valid label keys*. Have two segments, i.e. an optional prefix and name, separated by a slash `/`
    * *Name segment*. 
        * Required and must be 63 characters or less
        * Beginning and ending with an alphanumeric character, i.e. `[a-z0-9A-Z]` with dashes `-`, underscores `_`, dots `.`, and alphanumerics between
    * *Prefix segment*. Optional
        * If specified, the prefix must be a DNS subdomain
            * *DNS subdomain*. A series of DNS labels separated by dots `.`, not longer than 253 characters in total, followed by a slash `/`
        * If omitted, the label `Key` is presumed to be private to the user
        
    >**NOTE**. Automated system components, e.g. `kube-scheduler`, `kube-controller-manager`, `kube-apiserver`, `kubectl`, or other third-party automation, which add labels to end-user objects must specify a prefix

    >**NOTE**. The `kubernetes.io/` and `k8s.io/` prefixes are reserved for Kubernetes core components

* *Valid label value*.
    * Must be 63 characters or less, and can be empty
    * Unless empty, must begin and end with an alphanumeric character, i.e. `[a-z0-9A-Z]`, could contain dashes `-`, underscores `_`, dots `.`, and alphanumerics between
* *Example*. Consider a configuration file for a Pod with labels `environment: production` and `app: nginx` 

    ```yaml
    apiVersion: v1
    kind: Pod
    metadata:
    name: label-demo
    labels:
        environment: production
        app: nginx
    spec:
    containers:
    - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
    ```

### Label selectors
**Label selector**.
* *Uniqueness of labels*. Unlike names and UIDs, labels do not provide uniqueness
    
    $\to$ In general, we expect many objects to carry the same label(s)
* *Label selector*. Allow the client/user to identify a set of objects
    
    $\to$ The label selector is the core grouping primitive in Kubernetes
* *Types of label selectors*. The API currently supports two types of selectors, i.e. equality-based and set-based

**Multiple- and empty-requirement label selectors**.
* *Multiple-requirement selection*. A label selector can be made of multiple requirements which are comma-separated
    * *Explain*. All requirements must be satisfied so the comma separator acts as a logical `AND` operator
* *Empty-requirement selection*. 
    * The semantics of empty or non-specified selectors are dependent on the context
    * API types using selectors should document the validity and meaning of them

>**NOTE**. For both equality-based and set-based conditions there is no logical OR operator
>
>$\to$ Ensure our filter statements are structured accordingly

#### Equality-based requirement
**Object matching**. Equality- or inequality-based requirements allow filtering by label keys and values
* *Idea*. Matching objects must satisfy all of the specified label constraints, though they may have additional labels
* *Types of operators*. `=`, `==`, `!=`
* *Example*.

    ```
    environment = production
    tier != frontend
    ```

* *Composite filtering for resources*. Use comma operator, e.g. `environment=production,tier!=frontend`

**Example**. Consider a Pod selecting nodes with the label `accelerator=nvidia-tesla-p100`

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: cuda-test
spec:
  containers:
    - name: cuda-test
      image: "k8s.gcr.io/cuda-vector-add:v0.1"
      resources:
        limits:
          nvidia.com/gpu: 1
  nodeSelector:
    accelerator: nvidia-tesla-p100
```

#### Set-based requirement
**Set-based label requirements**. Allow filtering keys according to a set of values
* *Types of operators*. `in`, `notin` and `exists`
* *Example*.

    ```
    environment in (production, qa)
    tier notin (frontend, backend)
    partition
    !partition
    ```

* *Composite filtering for resources*. Use the comma separator as an AND operator

**Combination of set-based requirements and equality-based requirements*. These types of requirements can be mixed
* *Example*. `Ppartition in (customerA, customerB),environment!=qa`.

### API
#### LIST and WATCH filtering
**LIST and WATCH operations**. Specify label selectors to filter the sets of objects returned using a query parameter

$\to$ Both types of requirements are permitted

#### Set references in API objects
**Brief**. Some Kubernetes objects, e.g. services and replicationcontrollers, also use label selectors to specify sets of other resources, e.g. pods

**Service and ReplicationController**.
* *Pods selected by a `service`*. The set of pods that a service targets is defined with a label selector
* *Pods selected by a `replicationcontroller`*. The population of pods that a replicationcontroller should manage is defined with a label selector
    * *Reference*. https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller/
* *Labels selectors for `service` and `replicationcontroller`*. Defined in `json` or `yaml` files using maps
    
    >**NOTE**. Only equality-based requirement selectors are supported

    ```json
    "selector": {
        "component" : "redis",
    }
    ```

    or

    ```yaml
    selector:
        component: redis
    ```

**Resources that support set-based requirements**. Newer resources, such as `Job`, `Deployment`, `ReplicaSet`, and `DaemonSet`, support set-based requirements, e.g.

```yaml
selector:
  matchLabels:
    component: redis
  matchExpressions:
    - {key: tier, operator: In, values: [cache]}
    - {key: environment, operator: NotIn, values: [dev]}
```

* *`matchLabels`*. A map of `{key,value}` pairs, each of which is equivalent to an element of `matchExpressions`, whose 
    * Key field is "key"
    * Operator is "In"
    * Values array contains only "value"
* *`matchExpressions`*. A list of pod selector requirements
    * *Valid operators*. `In`, `NotIn`, `Exists`, and `DoesNotExist`
    * *Values set*. Must be non-empty in the case of `In` and `NotIn`
* *Idea*. All of the requirements, from both `matchLabels` and `matchExpressions` are ANDed together

    $\to$ They must all be satisfied in order to match

**Selecting sets of nodes**. One use case for selecting over labels is to constrain the set of nodes, onto which a pod can schedule


## Annotations
**Kubernetes annotations**. Used to attach arbitrary non-identifying metadata to objects

$\to$ Clients, e.g. tools and libraries, can retrieve this metadata

### Attaching metadata to objects
**Labels and annotations**. We can use either labels or annotations to attach metadata to Kubernetes objects
* *Labels*. 
    * Can be used to select objects
    * Can be used to find collections of objects satisfying certain conditions
* *Annotations*. 
    * Not used to identify and select objects
    * Can be small or large, structured or unstructured, and can include characters not permitted by labels

**Annotation structure**. Key/value maps
* *Example*.

    ```json
    "metadata": {
    "annotations": {
        "key1" : "value1",
        "key2" : "value2"
    }
    }
    ````

>**NOTE**. The keys and the values in the map must be strings
>
>$\to$ We cannot use numeric, boolean, list or other types for either the keys or the values

* *Examples of information recorded in annotations*.
    * Fields managed by a declarative configuration layer
        * *Explain*. Attaching these fields as annotations distinguishes them from 
            * Default values set by clients or servers, and
            * Auto-generated fields and fields set by auto-sizing or auto-scaling systems
    * Build, release, or image information
        * *Examples*. Timestamps, release IDs, git branch, PR numbers, image hashes, and registry address
    * Pointers to logging, monitoring, analytics, or audit repositories
    * Client library or tool information that can be used for debugging purposes
        * *Examples*. name, version, and build information
    * User or tool/system provenance information
        * *Examples*. URLs of related objects from other ecosystem components.
    * Lightweight rollout tool metadata
        * *Examples*. Config or checkpoints
    * Phone or pager numbers of persons responsible, or directory entries that specify where that information can be found
        * *Example*. a team web site
    * Directives from the end-user to the implementations to modify behavior or engage non-standard features

**Annotation versus database for metadata storage**. Instead of using annotations

$\to$ We can store metadata in an external database or directory
* *Drawback*. It is much harder to produce shared client libraries and tools for deployment, management, introspection, etc.

### Syntax and character set
**Valid annotation keys**. Have two segments, i.e. an optional prefix and name, separated by a slash `/`
* *Name segment*. Required
    * Must be 63 characters or less
    * Must begin and end with an alphanumeric character `[a-z0-9A-Z]` with dashes `-`, underscores `_`, dots `.`, and alphanumerics between
* *Prefix*. Optional
    * If specified, the prefix must be a DNS subdomain
    * If the prefix is omitted, the annotation Key is presumed to be private to the user
    
    >**NOTE**. Automated system components, e.g. `kube-scheduler`, `kube-controller-manager`, `kube-apiserver`, `kubectl`, etc., which add annotations to end-user objects must specify a prefix

**Reserved prefixes**. `kubernetes.io/` and `k8s.io/` prefixes are reserved for Kubernetes core components

## Field selector
**Field selectors**. Used to select Kubernetes resources based on the value of one or more resource fields
* *Example of field selector queries*.
    * `metadata.name=my-service`
    * `metadata.namespace!=default`
    * `status.phase=Pending`
* *Example `kubectl` command*. This kubectl command selects all Pods for which the value of the `status.phase` field is `Running`

    ```bash
    kubectl get pods --field-selector status.phase=Running
    ```

>**NOTE**. Field selectors are essentially resource filters

>**NOTE**. By default, no selectors/filters are applied, i.e. all resources of the specified type are selected
>
>$\to$ This makes the kubectl queries `kubectl get pods` and `kubectl get pods --field-selector ""` equivalent

### Supported fields
**Supported field selectors**. Vary by Kubernetes resource type

>**NOTE**. All resource types support the `metadata.name` and `metadata.namespace` fields

>**NOTE**. Using unsupported field selectors produces an error

### Supported operators
**Supported operators with field selectors**. `=`, `==`, and `!=` operators with field selectors

>**NOTE**. `=` and `==` mean the same thing

* *Example*.

    ```bash
    kubectl get services  --all-namespaces --field-selector metadata.namespace!=default
    ```

### Chained selectors
**Chained selectors**. As with label and other selectors, field selectors can be chained together as a comma-separated list
* *Example*. 

    ```bash
    kubectl get pods --field-selector=status.phase!=Running,spec.restartPolicy=Always
    ```

### Multiple resource types
**Brief**. We can use field selectors across multiple resource types
* *Example*.

    ```bash
    kubectl get statefulsets,services --all-namespaces --field-selector metadata.namespace!=default
    ```

## Finalizers
**Finalizers**. Namespaced keys telling Kubernetes to wait until specific conditions are met, before it fully deletes resources marked for deletion

>**NOTE**. Finalizers alert controllers to clean up resources the deleted object owned

* *Work flow*. When telling Kubernetes to delete an object that has finalizers specified for it
    1. The Kubernetes API marks the object for deletion by populating `.metadata.deletionTimestamp`
    2. The Kubernetes API returns a `202` status code, i.e. HTTP "Accepted"
    3. The target object remains in a terminating state while the control plane, or other components, take the actions defined by the finalizers
    4. After these actions are complete, the controller removes the relevant finalizers from the target object
    5. When the `metadata.finalizers` field is empty, Kubernetes considers the deletion complete and deletes the object
* *Usage*.
    * Control garbage collection of resources
        * *Example*. Define a finalizer to clean up related resources or infrastructure before the controller deletes the target resource
    * Control garbage collection of resources by alerting controllers to perform specific cleanup tasks before deleting the target resource

**Finalizer structure**. Finalizers do not usually specify the code to execute

$\to$ They are typically lists of keys on a specific resource similar to annotations

>**NOTE**. Kubernetes specifies some finalizers automatically, but you can also specify our own

### How finalizers work
**Finalizer specification**. When creating a resource using a manifest file

$\to$ We can specify finalizers in the `metadata.finalizers` field

**Workflow**. When we attempt to delete the resource
1. The API server handling the delete request notices the values in the finalizers field and does the following
    * Modifies the object to add a `metadata.deletionTimestamp` field with the time we started the deletion
    * Prevents the object from being removed until its `metadata.finalizers` field is empty
    * Returns a `202` status code, i.e. HTTP "Accepted"
2. The controller managing that finalizer notices the update to the object setting the `metadata.deletionTimestamp`, indicating deletion of the object has been requested
3. The controller attempts to satisfy the requirements of the finalizers specified for that resource
4. Each time a finalizer condition is satisfied, the controller removes that key from the resource's finalizers field
5. When the finalizers field is emptied, an object with a `deletionTimestamp` field set is automatically deleted

>**NOTE**. We can use finalizers to prevent deletion of unmanaged resources

### Owner references, labels, and finalizers
**Owner references**. Describe the relationships between objects in Kubernetes, i.e. like labels, but are used for a different purpose, i.e.
* *Labels*. When a controller manages objects like Pods
    
    $\to$ It uses labels to track changes to groups of related objects
* *Owner references*. The Job controller adds owner references to those Pods, pointing at the Job that created the Pods
    * *Consequence*. If we delete the Job while these Pods are running
        
        $\to$ Kubernetes uses the owner references to determine which Pods in the cluster need cleanup

**Finalizer and owner references**. Kubernetes processes finalizers when it identifies owner references on a resource targeted for deletion
* *Problem*. Finalizers can block the deletion of dependent objects
        
    $\to$ This can cause the targeted owner object to remain for longer than expected without being fully deleted
* *Solution*. In these situations, we should check finalizers and owner references on the target owner and dependent objects to troubleshoot the cause
* *Manual removal of finalizers*. In cases where objects are stuck in a deleting state, avoid manually removing finalizers to allow deletion to continue
    * *Explain*. Finalizers are usually added to resources for a reason, hence forcefully removing them can lead to issues in the cluster
    * *Consequence*. This should only be done when the purpose of the finalizer is understood and is accomplished in another way

## Owners and dependends
**Ownership**. In Kubernetes, some objects are owners of other objects
* *Example*. A ReplicaSet is the owner of a set of Pods
    
    $\to$ These owned objects are dependents of their owner
* *Purposes of owner references*. Help different parts of Kubernetes avoid interfering with objects they do not control

### Owner references in object specifications
**Owner references in object specifications**. Dependent objects have a `metadata.ownerReferences` field that references their owner object
* *Valid owner reference*. Consist of the object name and a UID within the same namespace as the dependent object
* *Default owner reference*. Kubernetes sets the value of this field automatically for objects, which are dependents of other objects
    * *Examples*. ReplicaSets, DaemonSets, Deployments, Jobs and CronJobs, and ReplicationControllers
* *Manually set owner reference*. We can configure owner references manually
    
    >**NOTE**. We usually do not need to and can allow Kubernetes to automatically manage the relationships

**Owner deletion prevention**. Dependent objects have an `ownerReferences.blockOwnerDeletion` field taking a boolean value

$\to$ This field controls whether specific dependents can block garbage collection from deleting their owner object
* *Default mode*. Kubernetes automatically sets this field to true if a controller sets the value of the `metadata.ownerReferences` field
* *Manual configuration*. We can set the value of the `blockOwnerDeletion` field manually to control which dependents block garbage collection
* *Protection*. A Kubernetes admission controller controls user access to change this field for dependent resources, based on the delete permissions of the owner
    
    $\to$ This control prevents unauthorized users from delaying owner object deletion

### Ownership and finalizers
**Ownership and finalizers**. When telling Kubernetes to delete a resource

$\to$ The API server allows the managing controller to process any finalizer rules for the resource
* Finalizers prevent accidental deletion of resources the cluster may still need to function correctly
    * *Example*. If we try to delete a PersistentVolume, which is still in use by a Pod
        
        $\to$ The deletion does not happen immediately, since the PersistentVolume has the `kubernetes.io/pv-protection` finalizer on it
        * *Consequence*. The volume remains in the Terminating status until Kubernetes clears the finalizer
            
            $\to$ This only happens after the PersistentVolume is no longer bound to a Pod
* Finalizers are added to an owner resource when we use either foreground or orphan cascading deletion
    * *Foreground deletion*. The controller must delete dependent resources that also have `ownerReferences.blockOwnerDeletion=true` before it deletes the owner
    * *Orphan deletion*. The controller ignores dependent resources after it deletes the owner object