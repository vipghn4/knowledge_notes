---
title: Appendix
tags: Computer architecture
---

# Table of Contents
[toc]

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