---
title: A modular architecture for object tracking and migration in self-organized distributed systems
tags: Case studies from large systems
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
* [A modular architecture for object tracking and migration in self-organized distributed systems](#a-modular-architecture-for-object-tracking-and-migration-in-self-organized-distributed-systems)
  * [Problem formulation](#problem-formulation)
  * [Architecture of an invididual node](#architecture-of-an-invididual-node)
  * [Modular architecture for object tracking and migration](#modular-architecture-for-object-tracking-and-migration)
    * [Stand-alone node](#stand-alone-node)
    * [Communicating nodes](#communicating-nodes)
  * [Use-case](#use-case)
<!-- /TOC -->

# A modular architecture for object tracking and migration in self-organized distributed systems
## Problem formulation
**Overall system architecture**. There is a self-organizing, networked system consisting of a large amount of nodes as defined following

<div style="text-align:center">
    <img src="/media/kZ6zq2d.png">
    <figcaption>Network topology and local surroundings of each node</figcaption>
</div>

>**NOTE**. All objects within a node's local surrounding can be detected

**Problem**. Track all objects moving within the observed area

**Challenges**.
* To track all objects in the network, each node must be able to track all objects in its surroundings and propagate objects to neighboring nodes

    $\to$ All data corresponding to an object should be migrated from one node to another
* The algorithm should have the flexibility to be adapted when changes in communication / processing capacity, hardware, or environmental circumstances occur

## Architecture of an invididual node
**Node data structure**.
* *Node ID*. The identifier of the node, used for sending and receiving data
* *Data-out set*. Data sent by the node
* *Data-in set*. Data received by the node
* *Static data*. Contain local information
    * *Examples*. Node's position, local surroundings, neighboring nodes, transformatiEon matrices to world-coordinates, etc.
    * *Neighbors of a node*. All nodes having a one-hop communication link with that node

**Objects at a node**. The set of locally tracked objects, each of which has the following structure
* *Object ID*. Globally unique number identifier of the object
* *Track*. Trajectory of the object, i.e. estimated positions at certain time instants, in world-coordinates
* *Datenum*. Time corresponding to each estimated position of the object's track
* *Detections*. The detections which were associated to the object with their corresponding position and time
* *Probability*. The probability that the tracked object is, in fact, an object
* *Propagate*. Information whether the object was sent to other nodes in the network
* *Take-over*. Information whether the object is tracked or detected at other nodes in the network
* *Other fields*. More fields can be added to this set if a particular tracking methodology is used

## Modular architecture for object tracking and migration
### Stand-alone node
**Tracking algorithm**. Consists of the basic tracking tracking functions

<div style="text-align:center">
    <img src="/media/mGA3R5q.png">
    <figcaption>Architecture of a node's tracking algorithm without communication</figcaption>
    <figcaption>The dashed line represents objects</figcaption>
</div>

* *Next sample time*. Determine the next sample instant depending on current time, detections and objects
* *Associate detections*. Identifies which detections correspond to which object
* *Detections-to-object*. Add the detections to their corresponding object and initialize new objects if needed
* *Probability update*. Update the probability of each object and determine which objects should be deleted, i.e. not tracked anymore
* *Track update*. Update the track and / or state of each object

### Communicating nodes

<div style="text-align:center">
    <img src="/media/Kf7BunG.png">
    <figcaption>Architecture of a node's tracking algorithm with communication</figcaption>
</div>

>**NOTE**. To keep the architecture as general as possible, no initial communication restrictions on the network's capacity are assumed

**Usage of communication by a node**.
* To improve the estimation of an object's track by fusing a node's local detections and / or estimated tracks with those of neighboring nodes
* Guarantee correct object migration through the networked system by propagating objects to neighboring nodes

**Additional required functionalities**.
* *Fusion of detections and tracks*. For fusion purpose, processed detections and tracks must be sent by each node to their neighboring nodes
    * *Additional node fields*.
        * *Fuse-out detections*. Data of a node's local detections, associated with a node ID of the receiving node(s)
        * *Fuse-out tracks*. Data of a node's local objects, associated with a node ID of the receiving node(s)

            >**NOTE**. Some methods require that detections are sent right after they were produced
            >$\to$ We should distinguish between processed detections sent after each instant, and raw detections sent independent of sampling instants

        * *Fuse-in detections and tracks*. Detections and tracks received from neighboring nodes
    * *Additional operations*.
        * *Send raw detections*. Add each new detection of fuse-in data to fuse-out data
        * *Send processed detection*. Build both fuse-out detections and fuse-out tracks based on detections and tracked, at each sample instant
        * *Receive fuse*.
            * Stack the diffrerent detections of fuse-in data into one local set of received detections
            * Stack the diffrerent tracks of fuse-in data into one local set of received tracks
        * *Detect fusion*. Fuse the local detections with the received ones to determine the fused detection set
        * *Track fusion*. Fuse the local tracks with the received ones to determine the fused track set
* *Migration of objects*.

    <div style="text-align:center">
        <img src="/media/LdpnPsr.png">
        <figcaption>Node architecture for object tracking and migration</figcaption>
    </div>

    <div style="text-align:center">
        <img src="/media/4sVEYhL.png">
        <figcaption>Architecture for sending and receiving functions</figcaption>
    </div>

    * *Additional tasks performed by a node*.
        * When it should propagate object-data and to which neighbors
        * Based on what information and criteria should it remove an object
    * *Performing the first task*. The following functions are required
        * *When to propagate*. Check which objects fit the criteria for propagation to neighboring nodes

            $\to$ If an object fits the criteria, then it is copied to the set of propagate objects, and the receiving node ID is added to the object
        * *Add objects*. Add received objects of propagate objects set properly to a node's local set objects
    * *Performing the second task*. To decide when to remove an object, a node can receive information from neighboring nodes
        * *Example*.
            * A neighboring node can notify that an object, which the current node propagated, is currently detected
            *  A node can check the recevied set, i.e. fuse-in, on whether one of its propagated objects was detected at a neighboring node
        *  *Consequence*. The following functions must be defined
            *  *Help object migration*.
                1. Check which local objects, which fit certain criteria, contain useful information for the neighboring node which propagated the object
                2. Add this information in the object's take-over field
            * *Successful object migration*. Update certain fields of local objects, e.g. take-over field, using the received object take-over sets and fuse-in data

## Use-case

![](/media/kcV9Dna.png)

![](/media/zEKW9tR.png)
