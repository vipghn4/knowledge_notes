---
title: Jeff Dean advices for building large systems
tags: Case studies from large systems
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Case studies from large systems](#case-studies-from-large-systems)
  - [Designs, lessions and advice from building large distributed systems - Jeff Dean](#designs-lessions-and-advice-from-building-large-distributed-systems---jeff-dean)
    - [Indexing systems](#indexing-systems)
    - [System building experiences](#system-building-experiences)
    - [Patterns](#patterns)
    - [Other notes](#other-notes)
  - [Software engineering advice from building large-scale distributed systems - Jeff Dean](#software-engineering-advice-from-building-large-scale-distributed-systems---jeff-dean)
    - [Google engineering environment](#google-engineering-environment)
    - [Appendix](#appendix)
      - [Tricks](#tricks)
<!-- /TOC -->

# Case studies from large systems
## Designs, lessions and advice from building large distributed systems - Jeff Dean
### Indexing systems
**Indexing system**. Indexing is a data structure allowing us to quickly retrieve records from a database file
* *Index*. A small table having only two columns, i.e.
    * One comprises a copy of the primary or candidate key of a table
    * One comprises metadata of the corresponding objects

**Google file system**.

<div style="text-align:center">
    <img src="/media/Dn6aPCW.png">
    <figcaption>Google file system</figcaption>
</div>

* *Motivation*.
    * Indexing system clearly needs a large-scale distributed file system

        $\to$ We want to treat the whole cluster as a single file system
* *Key ideas*. There are master nodes and chunkservers
    * Master node manages metadata
    * Data transfers are directly between clients and chunkservers
    * Files are broken into chunks of typically 64 MB
    * Chunks are replicated across multiple machines for usually 3 times
* *Operations on GFS*.
    * *Chunk modification*. The modified chunkserver, which is always the primary chunk holder, propagates the changes to the chunkservers with the backup copies

        $\to$ Chnages are not saved until all chunkservers acknowledge, thus guaranteeing the completion and atomicity of the operation
    * *Chunk access*.
        1. The program queries the master server for the locations of the desired chunks
        2. If the chunks are not being operated on, i.e. no outstanding leases exist

            $\to$ The master replies with locations
        3. The program then contacts and receives the data from the chunkserver directly
* *Workspace*. Unlike most other file systems, GFS is not implemented in the kernel of an OS, but is provided as a userspace library

**MapReduce**.
* *Motivation*. In 2003, Jeff Dean et. al. started working on re-writing Google's indexing system
    * *Phases of indexing*. Start with raw page contents on disk
        * Eliminate duplications
        * Extract anchor texts
        * Identify language
        * Generate index shard
        * etc.
    * *End result*. Data structures for index and docs serving
    * *Problem*. Each phase was hand-written parallel computation
* *MapReduce*. A simple programming model applied to many large-scale computing problems
    * *Usage*. Used at Google to completely regenerate Google's index of WWW, and other usages as following
        * Distributed pattern-based searching
        * Distributed sorting
        * Web link-graph reversal
        * Singular value decomposition
        * Inverted index construction
        * Document clustering
    * *Well-supported environments*.
        * Many-core systems
        * Multi-cluster systems
        * Dynamic cloud environments
        * Mobile environments
        * High-performance computing environments
    * *Benefits*.
        * Allow us to express all phases of our indexing system
        * Since used across broad range of CS areas, plus other scientific fields
        * Hadoop open-source implementation seeing significant usage
    * *Hidden messy details in MapReduce runtime library*.
        * Automatic parallelization
        * Load balancing
        * Network and disk transfer optimizations
        * Handling of machine failures
        * Robustness
        * Improvement to core library benefits all users of library
* *Typical outline for MapReduce*. User writes Map and Reduce functions to fit their problems, while the outline stays the same
    1. Read a lot of data
    2. *Map*. Extract something we care about from each record

        >**NOTE**. Maps can be performed in parallel, provided that each mapping oepration is independent of the others

    3. Shuffle and sort
    4. *Reduce*. Aggregate, summarize, filter, or transform
    5. Write the results

**BigTable**

### System building experiences
**Building system with many internal services**.
* *Key ideas*. Break large complex systems down into many services
* *Software engineering perspective*. Make things simpler, i.e.
    * Few dependencies, clearly specified
    * Easy to test and deploy new versions of individual services
    * Ability to run lots of experiments
    * Easy to re-implement service without affecting clients
    * Development cycles largely decoupled, thus
        * Small teams can work independently
        * Easier to have many engineering offices around the world

**Protocol description language**. Widely used at Google for storing and interchanging all kinds of structured information

$\to$ This serves as a basis for custom remote procedure call (RPC) system, which is used for nearly all inter-machine communication at Google
* *Objectives*. Extensible, efficient, compact, easy-to-use, cross-language, and self-describing
* *Example*. Protocol buffers (`protobuf`)
    * *Idea*.
        * Data structures (messages) and services are described in a `.proto` file and compiled with `protoc`

            $\to$ The compiler generates code which can be invoked by a sender or recipient of these data structures
        * Messages are serialized into a binary wire format, which is compact, forward- and backward-compatible, but not self-describing
            * *Self-describing*. The ability of telling names, meaning, or full data types of fields without an external specification

    >**NOTE**. Though the primary purpose of `protobuf` is to facilitate network communication
    >$\to$ Its simplicity and speed make it an alternative to data-centric C++ classes and structs

* *Features of protocol buffers*.
    * *Automatically generated wrappers*. C++, Java, Python, etc.
    * *Graceful client and server upgrades*. Servers ignore tags they do not understand, but pass the information through

        $\to$ No need to upgrade intermediate servers
    * *Serialization and deserialization*.
        * High performance, i.e. 200+ MB per second for encoding and decoding
        * Fairly compact, i.e. variable-length encodings, binary format
        * Format used to store persistently, not just for RPCs

**Designing efficient systems**. The most important skill is the ability to estimate performance of a system design, without actually having to build it
* *Know the basic building blocks*. We must know libraries' interfaces, and their implementations, at least at a high level

    $\to$ Otherwise, we cannot do decent back-of-the-envelope calculations
    * *Consequence*. Implementations with unpredictable 1000x variations in performance are not very helpful if latency or throughput matters

**Designing and building infrastructure**.
* *General idea*. Identify common problems, and build software system to address them in a general way
* *Key notes*.
    * Not try to be all things to all people, i.e.
        * Clients might be demanding 8 things
        * Doing 6 of them is easy
        * Handling 7 of them requires real thought
        * Dealing with all 8 usually results in a worse system
    * Do not build infrastructure just for its own sake, i.e.
        * Identify common needs and address them
        * Do not imagine unlikely potential needs which are not really there
* *Best approach*. Use our own infrastructure, especially at first

    $\to$ If not possible, at least work very closely with initial client team

**Design for growth**. Try to anticipate how requirements will evolve

$\to$ Keep likely features in mind as we design base system

* *Scalability*. Do not design to scale infinitely

    >**NOTE**. 5x to 50x growth is good to consider

    >**NOTE**. More than 100x probably requires rethink and rewrite

### Patterns
**Single master, 1000s of workers**.
* *Idea*.
    * Master controls global operation of systems, e.g. load balancing, work assignment, failure handling, etc.
    * Client interaction with master is fairly minimal
* *Examples*. GFS, BigTable, MapReduce, transfer service, cluster scheduling system, etc.
* *Data transfer*. Directly between clients and workers
* *Pros and cons*.
    * *Pros*. Simpler to reason about state of system with centralized master
    * *Cons*.
        * Careful design required to keep master out of common case ops
        * Scales to 1000s of workers, but not 100,000 of workers

**Canary requests**.
* *Problems*. Odd requests sometimes cause server to crash

    $\to$ Testing can help reduce probability, but cannot eliminate
* *Solution*. Send canary request first to one machine
    * If RPC finishes successfully, go ahead and send to all the rest
    * If RPC fails unexpectedly, try another machine
    * If failed $K$ times, reject request
* *Consequence*. Crash only a few servers, not 1000s

**Tree distribution of requests**.
* *Problem*. Single machine sending 1000s of RPCs overloads network interface controller (NIC) on machine when handling replies
    * *Consequences*.
        * Wide fan-in causes TCP drops / retransmits, resulting in significant latency
        * CPU becomes bottleneck on single machine
* *Solution*. Use tree distribution of requests / responses
    * *Benefits*.
        * Fan-in at root is smaller
        * Cost of processing leaf responses spread across many parents
        * The parent can be collocated with leaves on one rack

            $\to$ This keeps all that traffic off our data center networks
    * *Use cases*. When parent processing can trim / combine leaf data
* *Implementation at Google*. Mimic MapReduce
    * Leaves generate their best 10 or 15 responses
    * Parents return the best 20 - 30 responses out of the 30 leaves the parent is responsible for
    * This is a large degree of data reduction, compared to the case where the root has to process all the data directly

**Backup request to minimize latency**.
* *Problems*.
    * *Motivation*. When serving high volumes of traffic, even a miniscule fraction of requests corresponds to a large number of operations
        * Latency has a huge impact on service quality
        * Looking at the average service latency is insufficient
    * *Consequence*. Folks running high-performance systems at large-scale look to the tail the measuring their performance
    * *Observations*. High variance often hides in distribution tails
        * *Example*. 95 percentile latency is 24ms but 99.9 percentile latency is 994ms
* *Solution*. If we send the same request to multiple servers

    $\to$ We are going to get the answer back faster than waiting for a single one
    * *Explain*. Due to variance in modern service components
* *Benefits*.
    * Useful when variance is unrelated to specifics of request
    * Increase overall load by a tiny percentage
    * Decrease latency tail significantly

**Multiple smaller units per machine**.
* *Objectives*.
    * We want to minimize recovery time when machine crashes
    * We want do fine-grained load balancing
* *Problems*. Having each machine manage a unit of work is inflexible
    * Slow recovery, i.e. new replica must recover data, which is $O(\text{n_machine_states})$ in size
    * Load balancing is much harder
* *Solution*. Have each machine manage many smaller units of work / data
    * *Typical number of units*. 10 - 100 units / machine
* *Benefits*.
    * Allow fine-grain load balancing, i.e. shed or add one unit
    * Fast recovery from failure, i.e $N$ machines, each of which picks up a unit
* *Example*. GFS chunks, MapReduce tasks, etc.
* *Range distribution of data rather than hash*.
* *Problem*. We want to manage growing set of keys / values in distributed systems, i.e.
    * We need to spread data out across $K$ machines
    * We need to adapt to $K+1$ machines as data grows
* *Hashing approach*. Consistent hashing of keys to map to machines
    * *Pros*. Nice even distribution of data across machines
    * *Cons*. Hard for users to generate or understand locality across multiple different keys
    * *Usage*. Good at maximizing write throughput
* *Range distribution*. Break space of keys into multiple ranges

    $\to$ Machines manage a small number of different ranges at a time
    * *Pros*. User can reason about and control locality across keys
    * *Cons*. Harder to implement than hashing, e.g. string ranges, etc.
    * *Usage*. Avoid issues of unbounded tablet growth
* *Multi-level partitioning*. Can be used to combine hash partitioning and range partitioning

**Elastic systems**.
* *Problems*. Planning for exact peak load is hard
    * *Overcapacity*. Lead to wasted resources
    * *Undercapacity*. Lead to meltdown
* *Solution 1*. Design system to adapt, i.e.
    * Automatically shrink capacity during idle period
    * Automatically grow capacity as load grows
* *Solution 2*. Make system resilient to overload, i.e.
    * Do something reasonable even up to 2x planned capacity
    * More aggressive load balancing, when imbalance more severe

**One interface, multiple implementations**.
* *Problem*. Some system is very difficult to accomplish in single implementation
    * *Example*. Google web search system wants all of these
        * Freshness, i.e. update documents ~ 1 second
        * Massive capacity, i.e. 10,000s of requests per second
        * High quality retrieval, i.e. lots of information about each document
        * Massive size, i.e. billions of documents
* *Solution*. Partition problem into several subproblems, with different engineering tradeoffs
    * *Example*.
        * Realtime system, i.e. few docs, ok to pay lots of money per doc
        * Base system, i.e. high number of docs, optimized for low money per doc
        * Realtime and base, i.e. high number of docs, fresh, low money per doc

### Other notes
**Add sufficient monitoring / status / debugging hooks**.
* *Google's case study*. All of Google's servers
    * Export HTML-based status pages for easy  diagnosis
    * Export a collection of key-value pairs via a standard interface

        $\to$ Monitoring systems periodically this from running servers
    * RPC subsystem collects sample of all requests, all error requests, all requests > 0.0s, > 0.05s, > 0.1s, > 0.5s, > 1s, etc.
* *Profiling*. The system should support low-overhead online profiling, i.e. CPU, memory, and lcok contention profiling

**Adaptivity in world-wide systems**.
* *Challenge*. Automatic, dynamic world-wide placement of data and computation to minimize latency and / or cost, given constraints
    * *Constraints*. Bandwidth, packet loss, power, resource usage, failure modes, etc.
* *Users' high-level desires*.
    * 99%ile latency for accessing data should be less than 50ms
    * Store this data on at least 2 disks in EU, 2 in U.S, and 1 is Asia
    * Store three replicas in three different data centers less than 20ms apart

**Building applications on top of weakly consistent storage systems**.
* *Consistent storage system*.
    * *Weakly consistent storage system*. When applications access data

        $\to$ We want the option of providing them with stale data, in exchange for better performance
    * *Consistent storage system*. Read operations will reflect all writes which complete before the read was issued
* *Problems*. Many applications need state replicated across a wide area, i.e. for reliability and availability
* *Choices*.
    * *Consistent operations*. Often impose additional latency for common case
    * *Inconsistent operations*. Better performance and availability, but apps harder to write and reason about in this model

    >**NOTE**. Many apps need to use a mix of both of these
    >* *Example*. In Gmail, marking a message as read is asynchronous, sending a message is a heavier-weight consistent operation

* *Objectives*.
    * Build a general model of consistency choices, explained, and codified
    * Build an easy-to-use abstractions for resolving conflicting updates to multiple versions of a piece of state

**Distributed systems abstractions**. We need high-level tools, languages, or abstractions, for building distributed systems
* *Example*. For batch processing

    $\to$ MapReduce handles parallelization, load balancing, fault tolerance, I/O scheduling automatically within a simple programming model
* *Objective*. Are there unifying abstractions for other kinds of distributed systems problems

**Sharing in storage and retrieval systems**. Storage and retrieval systems with mix of private, semi-private, widely shared, and public documents
* *Example*. Email, shared doc among 10 people, messages with group with 100,000 members, or public web pages
* *Objective*. Building storage and retrieval systems, which efficiently deal with access control lists (ACLs) varying widely in size

    >**NOTE**. Best solution for doc shared with 10 people is different than for doc shared with the world

    >**NOTE**. Sharing patterns of a document might change over time


## Software engineering advice from building large-scale distributed systems - Jeff Dean
### Google engineering environment
**Distributed systems' motivation**.
* Data or request volume or both are too large for single machine
    * *Consequence*,
        * Careful design abouthow to partition problems
        * Need high capacity systems, even within a single data center
* Multiple data centers, all around the world

    $\to$ Almost all products deployed in multiple locations
* Products are mostly services, not shrink-wrapped software
    * *Explain*.
        * Services used heavily, even internally, e.g. web search might touch 50 separate services, thousands of machines
        * Simpler from software engineering standpoint, i.e.
            * Fewer dependencies, clearly specified
            * Easy to test new versions
            * Ability to run lots of experiments
        * Development cycles of products are largely decoupled, i.e.
            * Small teams can work independently
            * Easier to have many engineering offices around the world

**Tradeoffs when designing software systems**. Simplicity, scalability, performance, reliability, generality, and features

**Interfaces**. Think carefully about interfaces in our systems
* *Tricks*.
    * Imagine other hypothentical clients trying to use our interface
    * Document precisely, but avoid constraining implementation

        >**NOTE**. It it very important to be able to re-implement

    * Get feedback on our interfaces before implementing
    * Best way to learn is to look at well-designed interfaces

**Consistency issues**. Multiple data centers implies dealing with consistency issues, i.e.
* Disconnected or partitioned operation relatively common
    * *Example*. Data center down for maintenance
* Insisting on strong consistency likely undesirable
* Most products with mutatble state gravitating towards eventual consistency model

**Threads**. If we are not using threads, we are wasting ever larger fractions of typical machines
* *Explain*. Threading our application can help both throughput and latency

**Understanding data access**.
* *Data access*.
    * *Disks*. Seesk, sequential reads, etc.
    * *Memory*. Caches, branch predictors, etc.
* *RPCs*.
    * Know how much data we are sending or receiving
    * Will we saturate our machine's network interface?
    * What about rack switch?

**Data encoding**. CPUs are fast while memory bandwidth are precious
* *Solutions*. Variable-length encodings, compression, compact in-memory representations

>**NOTE**. Compression is a very important aspect of many systems

* *Libraries for data encoding and compression*. There are many tradeoffs, e.g. space, encoding / decoding speeds, etc.

**System robustness to failures**.
* *Possible solutions*.
    * Canary requests
    * Failover to replicas or data centers
    * Bad backend detection, i.e. stop using for live requests until behavior gets better
    * More aggressive load balancing when imbalance is more severe

>**NOTE**. Make our apps do something reasonable even if not all is right

>**NOTE**. It is better to give users limited functionality than an error page

**Source code philosophy**.
* *Google's source code philosophy*. Google has one large shared source base, i.e.
    * Lots of lower-level libraries used by almost everything
    * Higher-level app or domain-specific libraries
    * Application specific code
* *Benefits*.
    * Improvements in core libraries benefit everyone
    * Easy to reuse code which someone else has written in another context
* *Drawbacks*. Reuse sometimes leads to tangled dependencies
* *Source code searching*. Essential to be able to easily search whole source base
    * *Tools*. `gsearch`, i.e. internal tool for fast searching of source code
    * *Benefits*.
        * Huge productivity boost, i.e. easy to find uses, defs, examples, etc.
        * Make large-scale refactoring or renaming easier

**Software engineering hygiene**.
* Code reviews
* Design reviews
* Lost of testing, e.g. unit tests, larger tests for whole systems, continuous testing system

**Programming languages**.
* *C++*. Used for performance critical systems, e.g. everything for a web query
* *Java*. Used for lower volume apps, e.g. advertising front-end, parts of gmail, etc.
* *Python*. Used for configuration tools, etc.

### Appendix
#### Tricks
**Getting advices**. We should get advice early
* *When to get advice*. Before writing any code, or any lengthy design documents
* *Getting advice methods*.
    1. Jot down some rough ideas, with a few paragraphs
    2. Go find some people and chat at a whiteboard, especially people familiar with buidling similar systems
    3. It is even better to discuss a few different potential designs and evaluate

**Designing efficient systems**.
* *Important skill 1*. Given a basic problem definition, how do we choose the best solution
* *Important skill 2*. Ability to estimate performance of a system design, without actually having to build it

**Writing micro-benchmarks**. It is great to understand performance to build intuition for back-of-the-envelope calculations

$\to$ This reduces cycle time to test performance improvements

**Design for low latency**.
* Judicious use of caching can help
* Use higher priorities for interactive requests
* Use parallelis