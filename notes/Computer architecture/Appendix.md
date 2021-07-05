---
title: Appendix
tags: Computer architecture
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
* [Cache prefetching](#cache-prefetching)
  * [Introduction](#introduction)
  * [Challenges in prefetching](#introduction)
  * [Software prefetching](#software-prefetching)
  * [Hardware prefetching](#hardware-prefetching)
  * [Advances techniques](#advance-techniques)
  * [Prefetching in multicore](#prefetching-in-multicore)
* [Hardware specs understanding](#hardware-specs-understanding)
  * [CPU](#cpu)
  * [Other specs](#other-specs)
<!-- /TOC -->

## Cache prefetching
**References**.
* [Main reference](https://course.ece.cmu.edu/~ece740/f11/lib/exe/fetch.php?media=wiki:lectures:onur-740-fall11-lecture24-prefetching-afterlecture.pdf)

### Introduction
**Cache prefetching**. Fetch instructions or data from their original storage in slower memory to a faster local memory before it is actually needed
* *Motivation*.
    * Memory latency is high. Thus, if we can prefetch accurately and early enough

        $\to$ We can reduce or eliminate that latency
    * Prefetching can eliminate compulsory cache misses
* *Problem*. Predicting which address will be required in the future

>**NOTE**. Prefetching only works if programs have predictable miss address patterns

**Correctness of prefetching**. Prefetched data at a mispredicted address is simply not used

$\to$ There is no need for state recovery

**Types of cache prefetching**.
* *Classified by what to be prefetched*.
    * *Data prefetching*. Fetch data before it is required
    * *Instruction prefetching*. Fetch instructions before they are required
* *Classified by how to prefetch*.
    * *Hardware-based prefetching*. Typically accomplished by having a dedicated hardware mechanism in the processor
        * *Idea*. 
            * The hardware watches the stream of instructions or data being requested by the executing program
            * The hardware then recognizes the next few elements which the program might need, based on this stream
            * The hardware then prefetches the predicted elements into the processor's cache
    * *Software-based prefetching*. Typically accomplished by having the compiler analyze the code and insert additional "prefetch" instructions in the program during compilation itself

**Basics**.
* *Prefetching granularity*. In modern systems, prefetching is usually done in cache block granularity
* *Effects of prefetching*. Reduce cache miss rate and miss latency
* *Implementations of prefetching*. Prefetching can be done by hardware, compiler, or programmer

**Flow chart of prefetching in memory system**.

<div style="text-align:center">
    <img src="https://i.imgur.com/q2Pw1cX.png">
    <figcaption>Cache prefetching flow chart</figcaption>
</div>

### Challenges in prefetching
**What addresses to prefetch**. Accurate prediction of addresses to prefetch is important
* *Prefetch accuracy*. $\text{prefetch\_accuracy} = \frac{\text{used\_prefetches}}{\text{sent\_prefetches}}$
* *Explain*. Prefetching useless data wastes resources, which could all be utilized by demand requests or more accurate prefetch requests, i.e.
    * Memory bandwidth
    * Cache or prefetch buffer space
    * Energy consumption
* *How to decide what to fetch*.
    * *Option 1*. Predict based on paste access patterns
    * *Option 2*. Use the compiler's knowledge of data structures
* *Prefetching algorithm*. Determine what to fetch

**When to initiate a prefetch request**.
* *Moments of prefetching*.
    * *Prefetching too early*. Prefetched data might not be used before being evicted from storage
    * *Prefetching too late*. Prefetching might not hide the whole memory latency
* *Prefetcher timeline*. When a data item is prefetched affects the timeliness of the prefetcher
    * *Making prefetcher more timely*. There are two options
        * *Hardware option*. Make the prefetcher more aggressive, i.e. try to stay far ahead of the processor's access stream
        * *Software option*. Move the prefetch instructions earlier in the code

**Where to place the prefetched data**.
* *In cache*. 
    * *Pros*. Simple design, no need for separate buffers
    * *Cons*. Can evict useful demand data, thus cause cache pollution
* *In separate prefetch buffer*.
    * *Pros*. Protect demand data from prefetches, thus prevent cache pollution
    * *Cons*. More complex system design, i.e.
        * Where to place the prefetch buffer
        * When to access the prefetch buffer, i.e. parallel or serial with cache
        * When to move the data from prefetch buffer to cache
        * How to size the prefetch buffer
        * How to keep the prefetch buffer coherent
* *Modern system implementation*. Many modern systems place prefetched data into the cache
    * *Example*. Intel Pentium 4, Core2's, AMD systems, IBM POWER 4, etc.
* *Problems*.
    * *Which level of cache to prefetch into*. Memory-to-L2 or memory-to-L1, or L2-to-L1?
    * *Where to place the prefetched data in the cache*. Do we treat prefetched blocks the same as demand-fetched blocks?
    * *Do we skew the replacement policy so that it favors the demand-fetched blocks*
    * *Where to place the hardware prefetcher in the memory hierarchy*. In other words, what access patterns does the prefetcher see?  More complete access pattern will
        * Lead to potential better accuracy and coverage in prefetching
        * Prefetcher needs to examine more requests, i.e. this is bandwidth intensive

**How to prefetch**.
* *Software prefetching*. Usually works well only for regular access patterns
    * *Option 1*. ISA provides prefetch instructions
    * *Option 2*. Programmer or compiler inserts prefetch instructions
* *Hardware prefetching*. Hardware monitors process accesses
    * *Option 1*. Memorizes or finds patterns / strides
    * *Option 2*. Generate prefetch addresses automatically
* *Execution-based prefetchers*. 
    * A thread is executed to prefetch data for the main program
    * Prefetch instructions can be generated by either software / programmer or hardware

### Software prefetching
**Idea**. Compiler or programmer places prefetch instructions into appropriate places in code

**Fetching location**.
* *Binding*. Prefetch into a register, using a regular load
    * *Pros*. No need for a separate prefetch instruction
    * *Cons*. 
        * Registers can be taken up
        * What if another processor modifies the data value before it is used
* *Non-binding*. Prefetch into cache, using a special instruction
    * *Pros*. No coherence issues since caches are coherent
    * *Cons*. Prefetches are treated differently from regular loads

**Example**.
* *Example 1*.

    ```c
    for (int i = 0; i < N; i++) {
        __prefetch(a[i+8]);
        __prefetch(b[i+8]);
        sum += a[i] * b[i];
    }
    ```

* *Example 2*.

    ```c
    while(p) {
        __prefetch(p->next->next);
        work(p->data);
        p = p->next;
    }
    ```

**Pros and cons**.
* *Pros*. Can work for very regular array-based access patterns
* *Cons*. 
    * Prefetch instructions take up processing and execution bandwidth
    * Difficult to determine how early to prefetch
    * Need special prefetch instructions in ISA
    * Not easy to do for pointer-based data structures

### Hardware prefetching
**Idea**. Specialized hardware observes load / store access patterns and prefetches data based on past access behavior
* *Pros*.
    * Can be tuned to system implementation
    * No code portability issues, in terms of performance variation between implementation
    * Do not waste instruction execution bandwidth
* *Cons*. More hardware complexity to detect patterns

**Next-line prefetcher**. Always prefetch next $N$ cache lines after a demand access, or a demand miss
* *Pros*.
    * Simple to implement, and no need for sophisticated pattern decision
    * Work well for sequential and streaming data patterns
* *Cons*.
    * Can waste bandwidth with regular patterns, e.g. when stride is not 1
    * Cannot work if the program traverses memory from higher to lower addresses

**Stride prefetchers**.
* *Instruction PC based*.
    * *Idea*. Record the distance between the memory addresses referenced by a load instruction, i.e. the stride of the load, and the last address referenced by the load

        $\to$ Next time the same load instruction is fetched, prefetch `last_address + stride`
    * *Problems*.
        * How far can this get ahead? and How much of the miss latency can be the prefetch cover?
        * Initiate the prefetch when the load is fetched the next time can be too late
    * *Solutions*.
        * Use look-ahead PC to index the prefetcher table
        * Prefetch ahead, i.e. prefetch `last_address + N * stride`
        * Generate multiple prefetches
* *Cache block address based*. Stream buffers are a special case of cache block address based stride prefetching, where $N=1$
    * *Stream buffers*. Proposed by Jouppi at ISCA 1990, which is one of the most common hardware-based prefetching techniques in use
        * *Idea*. Each stream buffer holds one stream of sequentially prefetched cache lines
            * On a cache load miss, check the head of all stream buffers for an address match
                * If hit, pop the entry from FIFO, and update the cache with data
                * If miss, allocate a new stream buffer to the new miss address, e.g. recycle a stream buffer following LRU policy
            * Stream buffer FIFOs are continuously topped-off with subsequent cache lines whenever there is room and the bus is not busy
        * *Improvements*. Can incorporate stride prediction mechanisms to support non-unit stride streams
    * *Pros*.
        * Can exploit strides which occur due to the interaction of multiple instructions
        * Can more easily get further ahead of the processor access stream
        
            $\to$ No need for look-ahead PC
        * More hardware intensive

**Locality-based prefetchers**. In many applications, patterns are not perfectly strided

### Advance techniques
**Feedback-directed prefetcher throttling**.
* *Idea*. Monitor prefetcher performance metrics by
    * Throttle the prefetcher aggressiveness up or down based on past performance
    * Change the location prefetches are inserted in cache, based on past performance

**More irregular access patterns**.
* *More irregular access patterns*.
    * Indirect array accesses
    * Linked data structures
    * Multiple regular strides, e.g. 1, 2, 3, 1, 2, 3, 1, 2, 3, etc.
    * Random patterns
* *Solutions*.
    * Correlation-based prefetchers
    * Content-directed prefetchers
    * Precomputation or execution-based prefetchers

### Prefetching in multicore
**Problems**.
* Prefetching shared data
* Prefetch efficiency is a lot more important

**Drawbacks of local prefetcher throttling**. Local-only prefetcher control techniques have no mechanism to detect inter-core interference

**Ideas for coordinating different prefetchers' actions**.
* *Utility-based prioritization*. Prioritize prefetchers providing the best marginal utility on system performance
* *Cost-benefit analysis*. Compute cost-benefit of each prefetcher to drive prioritization
* *Heuristic-based methods*. Global controller overrides local controller's throttling decision based on interference and accuracy of prefetchers

## Hardware specs understanding
### CPU
**CPU core and threads**.
* *CPU core*. A complete microprocessor on a silicon die

    $\to$ This term dates from the introduction of multicore processors in early 2000s
* *CPU thread*. A reference to what Intel calles hyperthreading, which was introduced as another technique for getting more work out of a single CPU
    * *Idea*. A hyperthreaded CPU has two pipelines, i.e.
        * While a process is running off of one of the pipelines

            $\to$ The other is being populated with data and instructions for the next process to be given a CPU time slice
        * When the pending process is allowed to run

            $\to$ Its pipeline is already full and the processor stays busy
    * *Example*. If a CPU specification says it has 16 cores and 32 threads

        $\to$ There are 16 independent physical processors on the CPU die, and each of which has two pipelines

    >**NOTE**. Threads are officially defined as the virtual components or codes, which divide the physical core of a CPU into virtual multiple cores

**CPU base frequency and max turbo frequency**.
* *Base frequency*. Modern processing components are designed to run as a slower clock rate to reduce power consumed and lessen the amount of produced heat
* *Max turbo frequency*. Whenever the processor notices a lot of actual requests for calculation

    $\to$ They change the clock rate to higher Hz to perform requests as faster speed

* *Thermal velocity boost frequency*. A feature which opportunistically and automatically increases clock frequency above turbo boost frequency
    * *Idea*. Based on how much the processor is operating below its maximum temperatur, and whether turbo power budget is available

>**NOTE**. It does not mean the processor will always run that quickly

>**NOTE**. Max turbo clock is the maximum clock rate the processor can achieve if there is enough power available, and it is cool enough

**Thermal design power (TDP)**. The average power, it Watts, the processor dissipates when operating at base frequency with all cores active under an Intel-defined, high-complexity workload

### Other specs
**Frequency of monitors**. The number of images displayed per second every time the monitor refreshes
* *Unit of measurement*. Hertz (Hz)
* *Example*. A 60Hz monitor will refresh images and return 60 images per secon
