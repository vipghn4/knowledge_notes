---
title: Industrial problems
tags: Case studies from large systems
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
* [Industrial problems](#industrial-problems)
  * [Camera processing nodes synchronization](#camera-processing-nodes-synchronization)
<!-- /TOC -->

# Industrial problems
## Camera processing nodes synchronization
**Problem of interest**. A camera transmits frames to processing nodes, each node processes the frames and sends the output to a central server independently

$\to$ How can a server synchronizes outputs of the processing nodes

**Solution from Sinh**.
* *Key ideas*.
    * Keep the processing time of the processing nodes uniform with each other
        * *Method*.
            * Increase processing time of the faster nodes, i.e. by doing more tasks
            * Decrease processing time of slower nodes, i.e. via optimization
    * For each frame to be displayed, the server must wait until outputs from all nodes are available
* *Buffering results from nodes*. Can be used, but must avoid out-of-memory exception
