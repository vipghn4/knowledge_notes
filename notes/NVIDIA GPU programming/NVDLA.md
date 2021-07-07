---
title: NVDLA
tags: NVIDIA GPU programming
---

# The NVIDIA Deep Learning Accelerator (NVDLA)
## NVDLA primer
### Abstract
**Major mathematical operations in deep learning**. Convolution, activations, pooling, and normalization
* *Characteristics*. They are particularly well suited for special-purpose hardware implementation
    * Their memory access patterns are extremely predictable
    * They are readily parallelized

**NVDLA**. Promote a standardized, open architecture to address the computational demands of inference
* *Characteristics*.
    * Scalable and highly configurable
    * Flexibility and simplied integration due to modular design

### Accelerating Deep Learning Inference using NVDLA
**NVDLA hardware building blocks**.
* *Convolution Core*. Optimized high-performance convolution engine
* *Single Data Processor*. Single-point lookup engine for activation functions
* *Planar Data Processor*. Planar averaging engine for pooling
* *Channel Data Processor*. Multi-channel averaging engine for advanced normalization functions
* *Dedicated Memory and Data Reshape Engines*. Memory-to-memory transformation acceleration for tensor reshape and copy operations

**Features of NVDLA**.
* *Configurability of NVDLA blocks*. Each blocks are separate and independently configurable
    * *Example*. 
        * A system which does not need pooling can remove the planar averaging engine entirely
        * A system which needs additional convolutional performance can scale up the performance of the convolution unit without modifying other units in the accelerator
* *Scheduling operations for each unit*. Delegated to a co-processor or CPU
    * *Fine-grain scheduling*. Units operate on extremely fine-grained scheduling boundaries and they operate independently
    * *Implementation*. 
        * *Option 1 - Headed implementation*. Implemented as part of the NVDLA sub-system with the addition of a dedicated management coprocessor
        * *Option 2 - Headless implementation*. Fused with the higher-level driver implementation on the main system processor
    * *Consequence*. NVDLA hardware architecture can serve a variety of implementation sizes

**NVDLA interface**. NVDLA hardware utilizes standard practices to interface with the rest of the system
* *Control channel*. A control channel is actually an I/O processor, i.e. a processor with a specialized instruction set tailored for I/O and local memory
    * *Details*. A control channel implements a register file and interrupt interface
    * *Register file*. An array of processor registers in a CPU
* *AXI bus*. A pair of standard AXI bus interfaces are used to interface with memory
* *Memory interfaces*.
    * *Primary memory interface*. Intended to connect to the system's wider memory system, including system DRAM

        >**NOTE**. This memory interface should be shared with the system's CPU and I/O peripherals
    
    * *Secondary memory interface (optional)*. Allow for a connection to higher-bandwidth memory, which may be dedicated to NVDLA or to a computer vision subsystem in general
        * *Purpose*. Enable additional flexibility for scaling between different types of host systems
* *Keywords*. DMA, I/O channels, I/O modules

**Typical inference flow**.
* *Iteration*.
    1. The NVDLA management processor sends down the configuration of one hardware layer, i.e. a layer, e.g. a convolution layer, in an optimized network of hardware layer, along with an `activate` command
        * *Management processor of NVDLA*.
            * *For headed implementation*. A microcontroller
            * *For headless implementation*. The main CPU
    2. If data dependencies do not preclude this, i.e. if there exists another layer whose inputs do not depend on the output from the previous layer
        
        $\to$ Multiple hardware layers can be sent down to different engines, and activated at the same time
    3. Since every engine has a double-buffer for its configuration registers

        $\to$ It can also capture a second layer's configuration to begin immediately processing when the activate layer has completed, i.e. prefetching
    4. Once a hardware engine finishes its active task, it will issue an interrupt to the management processor to report the completion
* *Termination*. The above steps repeat until inference on the entire network is complete

### Implementations of NVDLA
**Types of NVDLA implementation**.

<div style="text-align:center">
    <img src="https://i.imgur.com/Hyx3ISb.png">
    <figcaption>Headless (small) and headed (large) NVDLA systems</figcaption>
</div>

* *Types of NVDLA implementation*.
    * *Headless*. Unit-by-unit management of the NVDLA hardware happens on the main system processor
        * *Usage*. Used for a more cost-sensitive purpose built device
    * *Headed*. Delegate the high-interrupt-frequency tasks to a computation microcontroller, which is tightly coupled to the NVDLA sub-system
        * *Details*. There is an additional dedicated control coprocessor with high-bandwidth SRAM to support the NVDLA sub-system
        * *Usage*. Used for high-performance IoT devices which may run many tasks at once
* *Terminologies*.
    * *IRQ*. Interrupt request
    * *CSB*. Configuration space bus, i.e. used by the host machine to access NVDLA registers
    * *SRAMIF*. SRAM connection interface, i.e. used as cache
    * *DBBIF*. Data backbone, i.e. an AMBA AXI-4 compliant which associates the DRAM memory to the DMA engine

**Small NVDLA model**. Good fit for cost-sensitive connected IoT class devices
* *Neural network models*. Can be pre-compiled and performance optimized, allowing larger models to be cut down and reduced in load complexity

    $\to$ This enables a scaled down NVDLA implmentation, where models consume less storage and take less time for system software to load and process
* *Performance trade-off*. The systems using small DLA typically execute only one task at a time

    $\to$ Sacrificing system performance while NVDLA is operating is generally not a strong concern
    * *Explain*. Typically, systems following the small NVDLA model will not include the optional second memory interface

        $\to$ When overall system performance is less of a priority, the impact of not having a high-speed memory path is unlikely to be critical
* *Context switches*. The relatively inexpensive context switches associated with systems using small NVDLA result in the main processor not being overly burdened by servicing a large number of NVDLA interrupts, i.e. due to layer switching in a neural network
    * *Root of context switches*.
        * As a result of processor architectural choices
        * As a result of using a system like FreeRTOS for task management
    * *Consequence*. 
        * This removes the need for an additiona microcontroller
        * The main processor performs both the coarse-grained scheduling, memory allocation, and fine-grained NVDLA management
* *Lack of SRAM*. Make the NVDLA more power-efficient to use the system memory as a computational cache

**Large NVDLA model**. A better choice when the primary emphasis is on high performance and versality
* *Problems*.
    * *System flexibility*. Performance-oriented IoT systems may perform inference on many different network topologies

        $\to$ It is important that these systems maintain a high degree of flexibility
    * *Power consumption*. Performance-oriented IoT systems may be performing many tasks at once, rather than serializing inference operations

        $\to$ Inference operations must not consume too much processing power on the host
* *Solution*. 
    * Include a second (optional) memory interface for a dedicated high-bandwidth SRAM
    * Enable the ability to interface with a dedicated contorl coprocessor, i.e. microprocessor, to limit the interrupt load on the main processor
* *Optional secondary SRAM*. A high-bandwidth SRAM is connected to a fast-memory bus interface port on NVDLA
    * *Role*. Used as a cache by NVDLA

    >**NOTE**. This SRAM may be shared by other high-performance computer-vision-related components on the system to further reduce traffic to the main system memory, i.e. the system DRAM
* *Microprocessor*. When using a microprocessor, the host processor still handles some tasks associated with managing NVDLA
    * *Example*.
        * The host will do coarse-grained scheduling on the NVDLA hardware, and the microprocessor is responsible for scheduling and fine-grained programming the NVDLA hardware
        * The host is responsible for I/O MMU (I/O memory management unit) mapping of NVDLA memory access (as necessary)
            * *I/O MMU*. A MMU connecting a DMA-capable I/O bus to the main memory
        * The host is responsible for memory allocation of input data and fixed weight arrays on NVDLA
        * The host is responsible for synchronization between other system components and tasks running on NVDLA

### Hardware architecture

<div style="text-align:center">
    <img src="https://i.imgur.com/6wyhRPm.png">
    <figcaption>Internal architecure of NVDLA core</figcaption>
</div>

**Operation modes of NVDLA architecture**.
* *Independent mode*. When operating independently
    * *Explain*. 
        * Each functionl block is configured for when and what it executes
        * Each block works on its assigned task, ie akin to independent layers in Deep Learning framewok
    * *Begins and ends*. Independent operation begins and ends with the assigned block performing memory-to-memory operations, in and out of main system memory or dedicated SRAM memory
* *Fused mode*. Similar to independent operation, but some blocks can be assembled as a pipeline

    $\to$ This improves performance by bypassing the round trip through memory, instead having blocks communicate with each other through smal FIFOs
    * *Example*. The following pipeline is typical for CNNs 
        1. Convolution core
        2. Single data point processor (for activation functions)
        3. Planar data processor (for pooling)
        4. Cross-channel data processor (for channel-wise operations)

**Connections to the rest of the system**. There are three major connections
* *Configuration space bus (CSB) interface*.  This interface is a synchronous, low-bandwidth, low-power, 32-bit control bus
    * *Usage*. Used by the CPU to access the NVDLA configuration registers

        $\to$ NVDLA functions as a slave on the CSB interface
    * *Interface protocol*. CSB implements a very simple interface protocol so it can be easily converted to AMBA, OCP, or any other system bus with a simple shim layer
* *Interrupt interface*. NVDLA hardware includes a 1-bit level-driven interrupt
    * *Interrupt assertion*. The interrupt line is asserted when a task has been completed or when an error occurs
* *Data backbone interface*. Connect NVDLA and the main memory subsystems
    * *Hardware characteristics*. A synchronous, high-speed, and highly configurable data bus
    * *Configurability of the interface*. The DBBIF can be specified to have different address sizes, different data sizes, and to issue different sizes of requests depending on the requirements of the system
    * *Interface protocol*. The DBBIF is a simple interface protocol which is similar to AXI
* *Optional second connection to second memory path*. The DBBIF has an optional second connection which can be used when there is a second memory path available
    * *Hardware design*. Identical in design to the primary DBBIF, and is intended for use with an on-chip SRAM which can provide higher throughput and lower access latency

### Components
**NVDLA components**. Each component in the NVDLA architecture exists to support specific operations integral to inference on deep neural networks

**Convolution**.
* *Data to be worked on*.
    * A set of offline-trained weights
    * A set of input feature data
* *Convolution engine parameters*. Used to map many different sizes of convolutions onto the hardware with high efficiency
* *Features*.
    * Optimizations to improve performance over a naive convolution implementation
    * Support for sparse weight compression to save memory bandwidth
    * Built-in Winograd convolution support to improve compute efficiency for certain sizes of filters
    * Batch convolution to save additional memory bandwidth by reusing weights when running multiple inferences in parallel
* *Convolution buffer*. To avoid repeated accesses to system memory, the NVDLA convolution engine has an internal RAM reserved for weight and input feature storage

    $\to$ This design greatly improves memory efficiency over sending a request to the system memory controller for each independent time a weight or feature is required

**Single data point processor (SDP)**. Allow for the application of both linear and non-linear functions onto individual data points
* *Usage*. Commonly used immediately after convolution in CNN systems, i.e. activation functions
* *Lookup table*. The SDP has a lookup table to implement non-linear functions
* *Simple bias and scaling*. Used for linear functions

**Planar data processor (PDP)**. Support specific spatial operations which are common in CNN applications
* *Configurability*. The PDP is configurable at runtime to support different pool group sizes
* *Supported pooling functions*. Maximum-pooling, minimum-pooling, and average-pooling

**Cross-channel data processor (CDP)**. A specialized unit built to apply the local response normalization (LRN) function

**Data reshape engine**. Perform data format transformation, e.g. splitting, slicing, merging, contraction, reshape-transpose, etc.

**Bridge DMA (BDMA**. Provide a data copy engine to move data between the system DRAM and the dedicated high-performance memory interface, where present

$\to$ This is an accelerated path to move data between these two otherwise non-connected memory systems

### Software design
**NVDLA software ecosystem**. NVDLA has a full software ecosystem supporting it
* *Components*.
    * On-device software stack
    * Part of the NVDLA open source release
    * A full training infrastructure to build new models which incorporate Deep Learning, and to convert existing models to a form usable by NVDLA software
* *Groups of components*.
    * *Compilation tools*. Used for model conversion
    * *Runtime environment*. Runtime software to load and execute networks on NVDLA

**General work flow with NVDLA**.

<div style="text-align:center">
    <img src="https://i.imgur.com/zANBK8W.png">
    <figcaption>Internal architecure of NVDLA core</figcaption>
</div>

**Compilation tools - Mdoel creation and compilation**. Compilation tools include compiler and parser
* *Compilation process*. A compartmentalized multi-step process which can be broken down into parsing and compiling

    >**NOTE**. Compilation steps are performed offline and might be perform on the device containing the NVDLA implementation

* *Compiler and parser*.
    * *Parser*. Can be relatively simple
        * *Functionality*. It can read a pretrained Caffe model and create an "intermediate representation" of a network to pass to the next step of compilation
    * *Compiler*. Create a sequence of hardware layers which are optimized for a given NVDLA configuration

        $\to$ Having an optimized network of hardware layers increases performance by reducing model size, load, and run times
        * *Functionality*. Take the prased intermediate representation and the hardware configuration of an NVDLA implementation and generate a network of hardware layers

        >**NOTE**. This phase is also responsible for quantizing models to lower precision, and for allocating memory regions for weights

* *Compilation and hardware configuration of NVDLA implementation*. Knowing about the hardware configuration of an NVDLA implementation enables the compiler to generate appropriate layers for the features which are available
    * *Example*. To select between different convolution operation modes

**Runtime environment - Model inference on device**. Involve running a model on compatible NVDLA hardware
* *Layers of runtime environment*.
    * *User mode driver (UMD)*. The main interface with user-mode programs
        * *Functionality*. After parsing the neural network, compiler compiles the network layer by layer and converts it into a file format called `NVDLA Loadable`

            $\to$ User mode runtime driver loads this loadable and submits inference job to kernel mode driver
    * *Kernel mode driver (KMD)*. Consists of drivers and firmware doing the work of scheduling layer operations on NVDLA and programming the NVDLA registers to configure each functional block
* *NVDLA loadable network*. The runtime execution starts with a stored representation of the network, i.e. an NVDLA loadable image
    * *NVDLA functional blocks in the view of a loadable*. Represented by a layer in software
        * *Attached information*. 
            * Information about dependencies
            * Information about input tensors in memory
            * Information about output tensors in memory
            * The specific configuration of each block for an operation
    * *NVDLA loadable format*. Standardized across compiler implementations and UMD implementations

        >**NOTE**. All implementations complying with the NVDLA standard should be able to at least understand any NVDLA loadable image
* *UMD API for processing loadable images*. UMD has a standard API for processing loadable images, binding input and output tensors to memory locations, and running inference
    * *Functionality*. This layer loads the network into memory in a defined set of data structures, and passes it to the KMD in an implementation-defined fashion
    * *Example*. On Linux, UMD can use `ioctl()` to pass data from the UMD to the KMD
* *KMD functionality*. KMD's main entry point receives an inference job in memory, selects from multiple available jobs for scheduling, and submits it to the core engine scheduler
    * *Core engine scheduler*. Responsible for handling interrupts from NVDLA, scheduling layers on each individual functional block, and updating any dependencies for that layer based on the completion of a task from a previous layer
        * *Scheduling mechanism*. Use information from the dependency graph to determine when subsequent layers are ready to be scheduled

            $\to$ The compiler can decide scheduling of layers in an optimized way, and avoid performance differences from different implementations of KMD

### NVDLA system integration
**Idea**. NVDLA can be configured for a wide range of performance levels

$\to$ Choosing these parameters depends on the requirements for CNNs which will be executed

**Time estimation**.
* *The time required to run each layer*. The maximum amount of time required for data input, output, and the time required to perform the multiply-accumulate (MAC) operations
    * *Multiply-accumulate operation*. $a=a+(b\times c)$
* *The time required to run the network*. Equal to the sum of times for all layers

**Key performance parameters**.
* The correct number of MAC units
* The convolutional buffer size
* The on-chip SRAM size

# Appendix
## Discussions
**Purpose of NVDLA**. NVDLA is designed specifically for the deep learning use case and is used to offload the GPU's inference effort
* *Objectives*. Improve energy efficiency and free up the GPU to run more complex networks or dynamic tasks implemented by the users

    $\to$ It does not target for performance but energy efficiency

>**NOTE**. Experiments show that DLA's performance is worse than GPU's performance

**Example integration of NVDLA on embedded devices**.

<div style="text-align:center">
    <img src="https://i.imgur.com/2cYEwyv.png">
    <figcaption>Integration of NVDLA on FPGA</figcaption>
</div>

**NVDLA hardware and software architecture**.

<div style="text-align:center">
    <img src="https://i.imgur.com/FY0dk6a.png">
    <figcaption>Hardware architecture of NVDLA</figcaption>
</div>

<div style="text-align:center">
    <img src="https://i.imgur.com/6K7hyIz.png">
    <figcaption>Full software stack of NVDLA</figcaption>
</div>

**NVDLA workflow**.`

<div style="text-align:center">
    <img src="https://i.imgur.com/mstMwsY.png">
    <figcaption>Workflow of NVDLA</figcaption>
</div>

**Reading materials**.
* https://cs217.stanford.edu/
* http://eyeriss.mit.edu/tutorial.html
* https://towardsdatascience.com/how-to-make-your-own-deep-learning-accelerator-chip-1ff69b78ece4