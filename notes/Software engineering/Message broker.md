<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Message broker](#message-broker)
  - [Introduction](#introduction)
  - [Message brokers in cloud architectures](#message-brokers-in-cloud-architectures)
  - [Message brokers and APIs](#message-brokers-and-apis)
  - [Message brokers and event streaming platforms](#message-brokers-and-event-streaming-platforms)
- [Appendix](#appendix)
  - [Discussion](#discussion)
  - [References](#references)
<!-- /TOC -->

# Message broker
## Introduction
**Message broker**. An inter-application communication technology to help build a common integration mechanism to support cloud native, microservices-based, serverless, and hybrid cloud architectures
* *Purpose*. Enable applications, systems, and services to communicate with each other and exchange information by translate messages between formal messaging protocols

    $\to$ This alows interdependent services to talk with one another directly, even if they are written in different languages, or implemented on different platforms

**Message broker as software modules**. Message brokers are software modules within messaging middleware, or message-oriented middleware (MOM) solutions
* *Purpose*. Provide developers with standardized means of handling the flow of data between application's components

    $\to$ The application can focus on its core logic
* *Functionalities*. Validate, store, route, and deliver messages to the appropriate destinations

    $\to$ Message brokers serve as intermediaries between other applications

**Main features**.
* *Message queue*. To provide reliable message storage and guaranteed delivery, message brokers often rely on a message queue
    * *Purpose*. Store and order the messages until the consuming application can process them
    * *Message order in the queue*. Exactly the same as the order, in which they were transmitted and remain in the queue until receipt is confirmed
* *Asynchronous messaging*. The type of inter-application communication, which message brokers make possible
    * *Purpose*. Guarantee that messages will be delivered once and once only, in the correct order relative to other messages
        * Prevent the loss of valuable data
        * Enable systems to continue functioning even in the face of the intermittent connectivity or latency issues common on public networks

**Overall organization**.
* *Queue managers*. Handle the interactions between multiple message queues
* *Functionalities services*. Data routing, message translation, persistence, and client state management functionalities

## Message brokers in cloud architectures
**Benefits of cloud computing**. Flexibility, scalability, and rapid development
* *Micro-services*. Cloud applications are made up of small, discrete, reusable microservices
    * *Characteristics*. Each microservice is deployed and can run independently of others

        $\to$ Any of them can be updated, scaled, or restarted without affecting other services in the system
    * *Micro-service packaging*. Microservices are often packaged in conatiners

        $\to$ Microservices work together to comprise a whole application
    
    >**NOTE**. This is where Kubernetes comes in

* *Communication between microservices*. There must be a means for communication between microservices

    $\to$ Message brokers are one mechanism they use to create shared communication backbone

**Benefits of using message broker in cloud applications**.
* Give increased control over interservice communications
* Ensure that data is sent securely, reliably, and efficiently between microservices
* Message brokers can play a similar role in integrating multicloud environments

    $\to$ This enables communication between workloads and runtimes residing on different platforms

## Message brokers and APIs
**REST APIs**. Commonly used for communications between microservices
* *Terminologies*.
    * *Representational state transfer (REST)*. Define a set of principles and constraints which developers can follow when building web services

        $\to$ Any service which adhere to them will be able to communicate via a set of uniform shared stateless operators and requests, e.g. `GET`, `POST`, etc.
    * *Application programming interface (API)*. Denote the underlying code that, if it conforms to REST rules, allows the services to talk to one another
* *Communication protocol*. REST APIs use Hypertext Transfer Protocol (HTTP) to communicate

    $\to$ REST APIs are widely known, frequently used, and broadly interoperable
    * *Explain*. HTTP is the standard transport protocol of the public Internet
    * *Usage*. Best used in situations which call for a synchronous request / reply

        $\to$ Services making requests via REST APIs must be designed to expect an immediate response
        * *Consequence*. If the client receiving the response is down

            $\to$ The sending service will be b locked while it awaits the reply
    * *Consequence*. Failover and error handling logic should be built into both services

**Benefits of using message broker**. Enable asynchronous communication between services 

$\to$ The sending service need not wait for the receiving service's reply
* *Benefits*. 
    * Improve fault tolerance and resiliency in the system
    * Easier to scale systems, since a pub / sub messaging pattern can readily support changing number of services
    * Possible to keep track of consumers' states

## Message brokers and event streaming platforms
**Event streaming platforms' drawbacks**. 
* Event streaming platforms only offer pub/sub-style distribution patterns

    $\to$ While message brokers can support two or more messaging patterns, including message queues and pub/sub
* For pub/sub mode, event streaming platforms cannot guarantees message delivery or track, which consumers have received messages

**Usage of event streaming**. Designed for highly volumes of messages, i.e. event streaming platforms are readily scalable

$\to$ Event streaming platforms can recorder streams or records into categories called *topics* and storing them for a predetermined amount of time

# Appendix
## Discussion
**Most commonly used message brokers**.
* *RabbitMQ*. Support advanced and complex routing options
* *AmazonMQ*. Provided by AWS to reduce user's operational responsibilities by managing the setup and maintenance of a message broker for us
* *Apache Kafka*. First created to track website activities, which requires a massive load of data for a long period of time

    $\to$ This is what Kafka is good at
    * *Usage*. Stream data to storage systems
* *Redis*. An in-memory data structure store
    * *Pros*. Extremely fast
    * *Cons*. Data durability and data loss

## References
* https://www.ibm.com/cloud/learn/message-brokers