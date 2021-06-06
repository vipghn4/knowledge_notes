---
title: Netflix architecture
tags: Case studies from large systems
---

# A design analysis of cloud-based micro-services architecture at Netflix
## Introduction
**Netflix**. One of the best online subscription-based video streaming services in the world up to 2021
* *Scale at 2019*. 
    * *Subscribers*. 167M subscribers, 5M new subscribers added every quarter, and over 200 countries
    * *Requests*. 165M hours of watching over 4K films and 47K episodes daily
* *Consequence*. Netflix technical teams have design such an amazing video streaming system with very high availability and scalability to serve their customers globally

**Netflix IT infrastructure**.
* *Historical reasons*. The infrastructure transformation at Netflix began, after a service outage in its own data centers shutting the entire DVD renting services down for 3 days

    $\to$ Netflix needs a more reliable infrastructure with no single point of failure
    * *Solution*. Netflix made two important decisions
        * Migrate the IT infrastructure from its data center to a public cloud
        * Replace monolithic programs, with small manageable software components, by microservices architecture
* *Cloud service*. Netflix had chosen AWS cloud to migrate its IT infrastructure
    * *Explain*. AWS could offer highly reliable databases, large-scale cloud storage, and multiple data centers around the globe

        $\to$ Netflix do not do the undifferentiated heavy lifting work of building data centers, but focusing more on its core business of providing high quality video streaming user experience
    * *Pros and cons*.
        * *Pros*. Netflix had to rebuild the whole technology to allow it run smoothly on AWS cloud
        * *Cons*. Significant improvement in  scalability and service availability
* *Microservices*. Microservices targets the problems of monolith software design by encouraging separation of concerns
    * *Separation of concerns*. Big programs are broken into smaller software components by modularity with data encapsulation on its own
    * *Benefits*. 
        * Increase the scalability via horizontal scaling and workload partitioning
        * Engineers can easily change any services which lead to faster deployments
        * Engineers can track the performance of each service, and quickly isolate its issues from other running services

## Architecture
**External tools**. AWS and Open Connect, i.e. its in-house content delivery network

**Main parts**.
* *Client*. Any supported browsers on a laptop or desktop or a Netflix app on smartphones or smart TVs
    * *Netflix application*. Developed by Netflix to provide the best viewing experience for each and every client and device

        $\to$ By controlling their apps and other devices through its SDK, Netflix can adapt its streaming services transparently under certain circumstances, e.g. slow networks ro overloaded servers
* *Backend*. Include services, databases, storages running entirely on AWS cloud
    * *Purpose*. Handle everything not involving streaming videos
    * *Components*.
        * Scalable computing instances
        * Scalable storage
        * Business logic microservices
        * Scalable distributed databases
        * Big data processing and analytics jobs
        * Video processing and transcoding
* *Open Connect CDN*. A network of servers called Open Connect Appliances (OCAs) optimized for storing and streaming large videos
    * *Location*. Placed inside Internet service providers (ISPs) and Internet exchange locations (IXPs) networks around the world
    * *Purpose*. Stream videos directly to clients

## Playback architecture
<div style="text-align:center">
    <img src="/media/kJz9xGb.png">
    <figcaption>Playback architecture for streaming videos</figcaption>
</div>

**Overview**. When subscribers click the Play button on their apps or devices

$\to$ The client will talk to both backend on AWS, and OCAs on Netflix CDN to stream videos
* *Observations*. Netflix' playback architecture is somewhat similar to Google file system (GFS)

    $\to$ The backend acts as the master node, and the OCAs act as chunk nodes

**Details**.
1. OCAs constantly send health reports about their workload status, routability, and available videos to the Cache control service running in AWS EC2 backend for Playback Apps to update the latest healthy OCAs to clients

    $\to$ Health check is very important
2. A Play request is sent from the client device to Netflix's Playback Apps service running on the backend to get URLs for streaming videos
3. Playback Apps service must determine that Play request would be valid to view the particular video
    * *Play request validation*. Check subscriber's plan, licensing of the video in different countries, etc.
4. Steering service running in AWS EC2 backend uses the client's IP address, and ISPs information to identify a set of suitable OCAs work best for the client
5. Playback Apps service talks to Steering service to get the list of appropriate OCAs server of the requested video
6. From the list of 10 different OCAs servers returned by Playback Apps service, the client tests the network connections quality to these OCAs and select the fastest, most reliable OCA to request video files for streaming

    $\to$ This is a bit to Jeff Dean's solution to cope with tail performance in large systems
7. The selected OCA server accepts requests from the client, and starts streaming videos

## Backend architecture
<div style="text-align:center">
    <img src="/media/FUQU1FI.png">
    <figcaption>A reference of backend architecture based on various sources</figcaption>
</div>

**Backend's roles**. Handle almost everything, e.g. sign up, login, billing, video transcoding, personalized recommendations, etc.
* *Microservices' roles*. Support lightweight and heavy workloads running on the same underlying infrastructure

**Data flow**.
1. The client sends a Play request to Backend running on AWS. The request is then handled by AWS Load balancer (ELB)
2. AWS ELB forwards the request to API Gateway Service running on AWS EC2 instances

    $\to$ The request will be applied to some predefined filters corresponding to business logics, then is forwarded to Application API for further handling
3. Application API is the core business logic behind Netflix operations
    * *Types of API*. Signup API, Recommendation API for retrieving video recommendation, etc.

    >**NOTE**. In this case, the forwarded request from API Gateway Service is handled by Play API

4. Play API calls a microservice or a sequence of microservices to fulfill the request
    * *Example of microservices*. Playback Apps service, Steering service, and Cache control service
5. The result of the microservices after run can be cached in a memory-based cache to allow faster access for those critical low latency requests
    * *Microservices communication*. Microservices are mostly stateless small programs, which can call each other

        $\to$ To control its cascading failure and enable resilience, each microservice is isolated from the caller process by Hystrix
    * *Data communication between microservices and data stores*. Microservices can save to or get data from a data store during its process
    * *User activities tracking*. Microservices can send events for tracking user activities or other data to the Streaming Processing Pipeline
        * *Purpose*. Used for real-time processing of personalized recommendation, or batch processing of business intelligence tasks
        * *Dat storage*. Data coming out of the Stream Processing Pipeline can be persistent to other data stores, e.g. AWS S3, Hadoop HDFS, Cassandra

**Netflix API Gateway Service**. Built by Netflix to allow dynamic routing, traffic monitoring and security, resilience to failures at the edge of the cloud deployment

## Components

## Design goals

## Tradeoffs

## Resilience

## Scalability

## Conclusion

# Appendix
## Concepts
**Scaling strategies**. Think of a rack of servers, where machines are located vertically
* *Horizontal scaling*. Scale by adding more machines into the resource pool
* *Vertical scaling*. Scale by adding more power, i.e. CPU and RAM, to an existing machine

## References
* *Main*. https://medium.com/swlh/a-design-analysis-of-cloud-based-microservices-architecture-at-netflix-98836b2da45f
* https://github.com/Netflix/hystrix
* AWS S3, Hadoop HDFS, Cassandr