---
title: Appendix
tags: NVIDIA GPU programming
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
* [Appendix](#appendix)
  * [C++](#c)
    * [Types of pointers](#types-of-pointers)
    * [Types of data type casting](#types-of-data-type-casting)
  * [TensorRT](#tensorrt)
    * [General workflow](#general-workflow)
  * [GPU coding](#gpu-coding)
    * [Image processing](#image-processing)
  * [Memory optimization with CUDA](#memory-optimization-with-cuda)
    * [Minimizing data transfer](#minimizing-data-transfer)
    * [Overlapping data transfers](#overlapping-data-transfers)
    * [Efficient memory access](#efficient-memory-access)
      * [Data structure alignment](#data-structure-alignment)
      * [Efficient memory access in CUDA](#efficient-memory-access-in-cuda)
  * [Execution configuration optimizations](#execution-configuration-optimizations)
    * [Occupancy](#occupancy)
    * [Tricks](#tricks)
  * [Advanced technologies by NVIDIA](#advanced-technologies-by-nvidia)
  * [Concepts](#concepts)
  * [External resources](#external-resources)
<!-- /TOC -->

# Appendix
## C++
### Types of pointers
**`auto_ptr`**. A smart pointer managing an object obtained via `new` expression and deletes the object when `auto_ptr` itself is destroyed
* *Structure*. A pointer to an allocated object, which ensures that when it goes out of scope

    $\to$ The pointed object must get automatically destroyed
* *Exclusive ownership model*. `auto_ptr` is based on exclusive ownership model
* *Example code*.

    ```c=
    #include <memory>

    auto_ptr<ClassName> ptr(new ClassName);
    ```
* *Why deprecated*. Due to exclusive ownership model, assignment or copy transfers ownership and resets the `rvalue` of the auto pointer to `nullptr`

    $\to$ `auto_ptr` cannot be used within STL containers since it cannot be copied

**`unique_ptr`**. A replacement of `auto_ptr`, with improved security, i.e. no fake copy assignments, added features, i.e. deleters, and support for arrays
* *Structure*. A container for raw pointers
* *Features*.
    * `unique_ptr` cannot be copied, i.e.

        ```c=
        unique_ptr<A> ptr1 (new A);
        unique_ptr<A> ptr2 = ptr1; // ERROR: cannot copy unique_ptr
        ```
    * `unique_ptr` can be moved with `std::move()`, i.e.

        ```c=
        unique_ptr<A> ptr2 = std::move(ptr1);
        ```
* *Usage*. When we want to have exclusive ownership of the resource

**`shared_ptr`**. A container for raw pointers, based on reference counting ownership model
* *Usage*. When we want to share ownership of a resource

**`weak_ptr`**. A copy of `shared_ptr`. It provides access to an object, which is owned by one or more `shared_ptr` instances, but does not participate in reference counting
* *Usage*. To avoid cyclic dependency
    * *Cyclic dependency*. Consider the graph below with three shared pointers A, B, and C

        ```
        The rest of the program  --> object A --> object B
                                    ^     |
                                     \    |
                                      \   v
                                        object C
        ```

        If the rest of the program is destroyed, the reference count of A reduces from `2` to `1`, and A, B, and C are not destroyed. But in fact, we want everything to be destroyed

### Types of data type casting
**Implicit conversion**.
* *Use cases*. Automatically performed when a value is copied to a compatible type
* *Types of implicit conversion*.
    * *Standard conversion*. Convert from child data type to parent data type
    * *Promotion*. Convert from parent data type to child data type
* *Implicit conversion between classes*.
    * *Invoking operations*.
        * *Single-argument constructors*. Implicitly convert a particular type to initialize an object, i.e.

        ```c=
        class A {};

        class B {
        public:
            B (const A& x) {}
        }
        ```

        * *Assignment operator*. Implicitly convert a particular type on assignments, i.e.

        ```c=
        B& operator= (const A& x) {return *this;}
        ```

        * *Type-cast operator*. Implicitly convert to a particular type, i.e.

        ```c=
        operator A() {return A();}
        ```

* *Special cases*.
    * Null pointers can be converted to pointers of any type
    * Pointers to any type can be converted to void pointers
    * Pointers to a derived class can be converted, i.e. upcast, to a pointer of an accessible and unambiguous base class

**Type casting**.
* *Traditional type casting*.

    ```c=
    (new_type) expression // C-like type casting
    new_type (expresion) // functional type casting
    ```
* *Dynamic casting*.
    * *Ability*.
        * Pointer upcast, in the same way as allowed in implicit conversion
        * Downcast polymorphic classes, i.e. those with virtual members, if and only if the pointed object is a valid complete object of the target type
        * Implicit cast null pointers between pointers types
        * Cast pointer of any type to a `void*` pointer
    * *Usage*. Only be used with pointers and references to classes, or with `void*`
    * *Example*.

        ```c=
        Base *pba = new Derived;
        Base *pbb = new Base;
        Derived *pd;

        pd = dynamic_cast<Derived*> (pbb);
        ```
* *Static casting*. Perform conversions between pointers to related clases, both upcast and downcast

    >**NOTE**. No checks are performed during runtime to guarantee that the converted object is a full object of the destination type
    >$\to$ Programmers must check this, but static casting does not have the overhead of type-safety checks of dynamic casting

    * *Ability*.
        * Explicitlly call a single-argument constructor or a conversion operator
        * Convert to rvalue references
        * Convert enum class values into integers or floating-point values
        * Convert any type to `void`, evaluating and discarding the value
    * *Difference from dynamic casting*.
        * `static_cast` performs no runtime checks. If a type cannot be casted to another type, it just raise errors
        * `dynamic_cast` performs runtime checks. If a type cannot be casted to another type, it will return a null pointer

* *Reinterpret casting*. Convert any pointer type to any other pointer type, even of unrelated classes
    * *Mechanism*. Use a simple binary copy of the value from one pointer to the other
* *Const casting*. Manipulate the constness of the object pointed by a pointer, i.e. either to be set or to be removed

## TensorRT
### General workflow

<div style="text-align:center">
    <img src="/media/JLc2L0o.png">
    <figcaption>TensorRT workflow</figcaption>
</div>

**Loading engines**.
1. Create IRuntime instance `runtime`
2. Deserialize a binary string to ICudaengine `engine`

**Infer with engines**.
1. Create cuda stream for async execution
    * Comments: Different streams may run concurrently and asynchronously
2. Create IExecutionContext `exe_context`
    * Comments: One model can have multiple execution contexts
3. Copy host input buffer to device input buffer
4. Pass associated I/O buffers to `exe_context.enqueue()` (async) to execute inference
    * *Alternative methods*.
        * `exe_context.enqueueV2()` (async)
        * `exe_context.execute()` (sync)
        * `exe_context.executeV2()` (sync)
5. Synchronize CUDA stream
6. Copy device output buffer to host input buffer

**Cautions**.
* Using IReduceLayer from TRT is expensive and makes following computations of the model denser

    $\to$ If we use the implementation from cuda/samples, the reduction operation will be cheaper and the model computation will be more sparse
* When adding a plugin to a TRT model, TRT will automatically run every method of the added plugin with dummy inputs, e.g. zero tensors

    $\to$ We must prepare for this

## GPU coding
**Tools for CUDA coding**.
* *STL-like library*. `thrust`
* *Image processing with CUDA*. `npp`

### Image processing
**Fundamental**.
* *Image representation in GPU*. A continuous array of pixel values
* *Basic flow*.
    1. Copy image array from host to device
    2. Process image array on the device
    3. Copy the image array from device to host
* *Example code*. Resize a RGB image with NPP and CUDA kernels

    ```c=
    float* decimate_cuda(
        float* readbuff, uint32_t nSrcH, uint32_t nSrcW,
        uint32_t nDstH, uint32_t nDstW
    ) {
        size_t  srcStep;
        size_t  dstStep;
        // rows = height; columns = width

        NppiSize oSrcSize = {nSrcW, nSrcH};
        NppiRect oSrcROI = {0, 0, nSrcW, nSrcH};
        float *devSrc;
        CUDA_CALL(cudaMallocPitch(
            (void**)&devSrc, &srcStep, 3 * nSrcW * sizeof(float), nSrcH
        ));
        CUDA_CALL(cudaMemcpy2D(
            devSrc, srcStep,
            readbuff, 3 * nSrcW * sizeof(Npp32f), 3*nSrcW * sizeof(Npp32f), nSrcH, cudaMemcpyHostToDevice
        ));

        NppiSize oDstSize = {nDstW, nDstH};
        NppiRect oDstROI = {0, 0, nDstW, nDstH};
        float *devDst;
        CUDA_CALL(cudaMallocPitch(
            (void**)&devDst, &dstStep, 3 * nDstW * sizeof(float), nDstH
        ));

        NppStatus result = nppiResize_32f_C3R(
            devSrc, srcStep, oSrcSize, oSrcROI,
            devDst, dstStep, oDstSize, oDstROI,
            NPPI_INTER_SUPER
        );
        if (result != NPP_SUCCESS) {
            std::cerr << "Unable to run decimate_cuda, error " << result << std::endl;
        }

        Npp64s writesize;
        Npp32f *hostDst;
        writesize = (Npp64s) nDstW * nDstH * 3;          // RGB
        if(NULL == (hostDst = (Npp32f *)malloc(writesize * sizeof(Npp32f)))){
            printf("Error : Unable to alloctae hostDst in decimate_cuda, exiting...\n");
            exit(1);
        }

        CUDA_CALL(cudaMemcpy2D(hostDst, nDstW*3 * sizeof(Npp32f), devDst, dstStep, nDstW*3 * sizeof(Npp32f),nDstH, cudaMemcpyDeviceToHost));

        CUDA_CALL(cudaFree(devSrc));
        CUDA_CALL(cudaFree(devDst));
        return(hostDst);
    }        // source - 3 x 32f, interleaved RGBRGBRGB...
    ```

## Memory optimization with CUDA

<div style="text-align:center">
    <img src="/media/JuPCfhp.png">
    <figcaption>Memory spaces on CUDA device</figcaption>
</div>

### Minimizing data transfer
**Pageable memory**. Host data allocations are pageable by default, but GPU cannot access data directly from pageable host memory

<div style="text-align:center">
    <img src="/media/NdlEzQu.png">
    <figcaption>Memory transfer from CPU to GPU</figcaption>
</div>

* *Data transfer from host to device*. When a data transfer from pageable host memory to device memory is invoked
    1. The CUDA driver must first allocate a temporary page-locked, or pinned, host array
    2. The driver then copy the host data to the pinned array
    3. The driver then transfer data from the pinned array to device memory
* *Consequence*. We can avoid the cost of intermediate data transfer by directly allocating our host arrays in pinned memory

    $\to$ This is where page-locked memory comes in

**Batching small transfers**. Due to the overhead associated with each transfer, it is preferable to batch many small transfers together into a single transfer
* *Idea*. Use a temporary array, preferably pinned, and pack it with the data to be transferred

### Overlapping data transfers
**Overlapping kernel execution and data transfer**.
* *Requirements*.
    * The device must be capable of "concurrently copy and execution"

        $\to$ This can be queried from `deviceOverlap` field of `cudaDeviceProp` struct
    * The kernel execution and data transfer to be overlapped must both occur in different, non-default streams
    * The host memory involved in the data transfer must be pinned memory
* *Approaches*.
    * Use multiple streams to carry out execution and data transfer
    * Split the big array into chunks and use different CUDA streams to transfer them
    * Batch similar operations together, issueing all host-to-device transfers first, followed by all kernel launches, and then all device-to-host transfers

### Efficient memory access
#### Data structure alignment
**Data structure alignment**. The way data is arranged and accessed in computer memory
* *Efficiency of data access*. The CPU in modern computer hardware performs reads and writes to memory most efficiently when the data is naturally aligned
    * *Explain*. Data's memory address is a multiple of data size
    * *Example*. In a 32-bit architecture, the data maybe aligned if the data is stored in 4 consecutive bytes, and the first byte lies on a 4-byte boundary
* *Data alignment*. The aligning of elements according to their natural alignment
    * *Padding*. To ensure natural alignment

        $\to$ It maybe required to insert some padding between structure elements or after the last element of a structure
    * *Packing*. Instead of padding, which may lead to slower access, we can pack the structure

**Data alignment**. Assume that each primitive datum is a power of 2 bytes long
* *Aligned memory address*. A memory address $a$ is said to be $n$-byte aligned when $a$ is a multiple of $n$ bytes, where $n$ is a power of $2$
* *Aligned memory access*. A memory access is said to be aligned when the data being accessed is $n$ bytes long and the datum address is $n$-byte aligned
* *Aligned memory pointer*. A memory pointer referring to primitive data is $n$ bytes long is said to be aligned if it is only allowed to contain addresses, which are $n$-byte aligned

**Problems**. The CPU accesses memory by a single memory word at a time

$\to$ As long as the memory word size is at least as large as the largest primitive data type supported by the computer, aligned accesses will always access a single memory word
* *Misaligned memory access*. If the highest and lowest bytes in a datum are not within the same memory word

    $\to$ The computer must split the datum acces into multiple memory accesses
    * *Consequence*. It requires a lot of complex circuitry to generate the memory access and coordinate misaligned memory accesses

>**NOTE**. Misaligned memory access may also lead to other problems, e.g. synchronization between reading and writing to memory cells

**Typical alignment of C structs on x86**.
* *Primitive types*.

    | Data type | Alignment |
    | --- | --- |
    | `char` | 1-byte aligned |
    | `short` | 2-byte aligned |
    | `int` | 4-byte aligned |
    | `double` | 8-byte aligned on Windows and 4-byte aligned on Linux |
    | `long long` | 4-byte aligned |
    | `long double` | 8-byte aligned with C++ builder, 2-byte aligned with DMC, 4-byte aligned with GCC |

* *Structures*.
    * *Before compilation*. Before compilation, the structure is 8-byte-sized

        ```c++
        struct MixedData
        {
            char Data1;
            short Data2;
            int Data3;
            char Data4;
        };
        ```

    * *After compilation*. After compilation, data structures will be supplemented with padding bytes to ensure a proper alignment for each of its members, i.e.

        ```c++
        struct MixedData  /* After compilation in 32-bit x86 machine */
        {
            char Data1; /* 1 byte */
            char Padding1[1]; /* 1 byte for the following 'short' to be aligned on a 2 byte boundary
        assuming that the address where structure begins is an even number */
            short Data2; /* 2 bytes */
            int Data3;  /* 4 bytes - largest structure member */
            char Data4; /* 1 byte */
            char Padding2[3]; /* 3 bytes to make total size of the structure 12 bytes */
        };
        ```

        >**NOTE**. The last member is padded with the number of bytes required so that the total size of the structure should be a multiple of the largest alignment of any structure member

        >**NOTE**. We can check the size after compilation with `sizeof`

* *Other tricks*. By reordering structure members, or changing the compiler's alignment of structure members

    $\to$ We can change the alignment of structures to reduce the memory they require
    * *Example*. The compiled size of the structure now matches the pre-compiled size of 8 bytes

        ```c++
        struct MixedData  /* after reordering */
        {
            char Data1;
            char Data4;   /* reordered */
            short Data2;
            int Data3;
        };
        ```

**Allocating memory aligned to cache lines**. It would be beneficial to allocate memory aligned to cache lines
* *Cache line*. The unit of data transfer between the cache and main memory
    * *Explain*. The processor will read or write an entire cache line when any location in the cache line region is read or written
    * *Typical cache line*. 64 bytes
* *Adapt to CUDA*. If an array is partitioned for more than one thread to operate on

    $\to$ Having the sub-array boundaries unaligned to cache lines could lead to performance degradation

#### Efficient memory access in CUDA
**Global memory coalescing**. Group of threads into warps is not only relevant to computation, but also to global memory accesses
* *Global memory accesses*. The device coalesces global memory loads and stores issued by threads of a warp into as few transactions as possible to minimize DRAM bandwidth

    >**NOTE**. We should ensure that global memory accesses are coalesced whenever possible

    * *Access requirements for coalescing*.
        * *Compute capability 6.0 or higher*. The concurrent accesses of the threads of a warp will coalesce into a number of transactions equal to the number of 32-byte transactions required to service all of the threads of the warp

            >**NOTE**. In these devices, L1-caching is default

        * *Compute capability 3.5, 3.7, and 5.2*. If L1-caching is enabled

            $\to$ The number of required transactions is equal to the number of required 128-byte aligned segments

        >**NOTE**. Choosing sensible block sizes, e.g. multiple of the warp size, facilitates memory accesses by warps, which are properly aligned

* *Misaligned data access*. Misaligned data accesses can reduce the bandwidth of the data transfer
    * *Global memory layout*. Arrays allocated in device memory are aligned to 256-byte memory segments by the CUDA driver for efficiency
        * *Explain*. The pointers which are allocated by using any of the CUDA Runtime's device memory allocation functions e.g `cudaMalloc` or `cudaMallocPitch` are guaranteed to be 256 byte aligned, i.e. the address is a multiple of 256

        >**NOTE**. This alignment may differ across different devices

    * *Global memory transactions*. The device can access global memory via 32-, 64-, or 128-byte transactions which are aligned to their size
* *Strided memory access*. Large strided memory access may lead to poor effective bandwidth
    * *Explain*. When concurrent threads simultaneously access memory addresses, which are very far away in physical memory

        $\to$ There is no chance for the hardware to combine the accesses
    * *Consequence*. When accessing multidimensional arrays, it is often necessary for threads to index the higher dimensions of the array

        $\to$ Strided access is simply unavoidable
        * *Solution*. Use shared memory, which is an on-chip memory shared by all threads in a thread block
        * *Example*. Use shared memory to extract a 2D tile of a multidimensional array from global memory in a coalesced fashion into shared memory

            $\to$ Then have contiguous threads stride through the shared memory tile

## Execution configuration optimizations
### Occupancy
**Occupancy**. The ratio of the number of active warps per multiprocessor to the maximum number of possible active warps

$\to$ This is the percentage of the hardware's ability to process warps that is actively in use

* *Query for maximum number of possible active warps*. `deviceQuery`
* *Values of occupancy*.
    * *High occupancy*. Do not always equate to higher performance, i.e. there is a point above which additional occupancy does not improve performance
    * *Low occupancy*. Always interfere with the ability to hide memory latency, resulting in performance degradation

        >**NOTE**. Low occupancy will have more registers available per thread than higher one, which may result in less spilling to local memory

**Maximum block size**. Per thread resources required by a CUDA kernel might limit the maximum block size in an unwanted way

$\to$ To maintain forward compatbility to future hardware and toolkits, and to ensure that at least one thread block can run on an SM, we should include `__launch_bounds__(maxThreadsPerBlock)`
* **`__launch_bounds__(maxThreadsPerBlock)`**. Specify the largest block size which the kernel will be launched with

### Tricks
**Hiding register dependencies**. To hide latency arising from register dependencies, maintain sufficient numbers of active threads per multiprocessor, i.e. sufficient occupancy
* *Register dependencies*. Arise when an instruction uses a result stored in a register written by an instruction before it
    * *Consequence*. The latency of most arithmetic instructions is typically 4 cycles on devices of compute capability 7.0

        $\to$ Threads must wait approximately 4 cycles before using an arithmetic result
* *Solution*. Hide the latency caused by register dependencies by the execution of threads in other warps

**Thread and block heuristics**. The number of threads per block should be a multiple of 32 threads, since it provides optimal computing efficiency and facilitates coalescing
* *Motivation*. Latency hiding and occupancy depend on the number of active warps per multiprocessor, which is implicitly determined by the execution parameters along with the resources, i.e. register and shared memory

    $\to$ Choosing execution parameters is a matter of striking a balance between latency hiding and resource optimization
* *The number of blocks per grid*. The primary concern is keeping the entire GPU busy

    $\to$ The number of blocks in a grid should be larger than the number of SMs
    * *Explain*.
        * All SMs have at least one block to execute
        * There should be multiple active blocks for SM

            $\to$ Blocks, which are not waiting for a `__syncthreads()`, can keep the hardware busy

    >**NOTE**. To scale to future devices, the grid size per kernel launch should be in the thousands

* *Block size*. Multiple concurrent blocks can reside on a SM

    $\to$ Occupancy is not determined by block size alone

    >**NOTE**. A larger block size does not imply a higher occupancy

    * *Rules of thumps*.
        * Threads per block should be a multiple of warp size to avoid wasting computation on under-populated warps, and to facilitate coalescing
        * A minimum of 64 threads per block should be used, and only if there are multiple concurrent blocks per SM
        * Between 128 and 256 threads per block is a good initial range for experimentation with different block size
        * Use several smaller thread blocks, rather than one large thread block per SM if latency affects performance

            >**NOTE**. This is beneficial particularly to kernels which frequently call `__syncthreads()`

    >**NOTE**. When a thread block allocates more registers than are available on a SM
    >$\to$ The kernel launch fails

**Effects of shared memory**.
* *Usages of shared memory*.
    * Help to coalesce or eliminate redundant access to global memory
    * Act as a constraint on occupancy, i.e. increasing the shared memory per block will effectively reduce the occupancy of the kernel
* *Determining the sensitivity of performance to occupancy*. Through experimentation with the amount of dynamically allocated shared memory

**Concurrent kernel execution**. CUDA streams can be used to
* Overlap kernel execution with data transfers
* Execute multiple kernels simultaneously to more fully take advantage of the device's SMs (on device with concurrent kernel execution ability only)

    $\to$ We can query for this information of the device from `concurrentKernels` field of `cudaDeviceProp`

**Multiple contexts**.
* *CUDA context*. CUDA work occurs within a process space for a particular GPU
    * *Usage*. Encapsulate kernel launches and memory allocations for the corresponding GPU and supporting constructs, e.g. page tables

    >**NOTE**. The context is explicit in the CUDA Driver API, but is entirely implicit in the CUDA runtime API, which creates andmanages contexts automatically

* *Multiple contexts*. If multiple CUDA application processes access the same GPU concurrently, this almost always implies multiple contexts
    * *Explain*. A context is tied to a particular host process, unless multi-process service is in use
    * *Drawback*. Only one of the contexts can execute work at any given moment on a GPU

        $\to$ Contexts sharing the same GPU are time-sliced
    * *Consequence*. It is best to avoid multiple contexts per GPU within the same CUDA application

## Advanced technologies by NVIDIA
**Tensor cores**. Each tensor core is a programmable compute unit specialzed for accelerating machine learning workloads
* *Functionality*. Each tensor core can complete a single $4\times 4$ matrix-multiply-and-accumulation (MACC) each clock cycle
    * *Formal*. $D = A \times B + C$ where $A, B, C$ are $4\times 4$ matrices
* *References*.
    * *Modeling Deep Learning Accelerator Enabled GPUs* by Md Aamir Raihan, Negar Goli, and Tor M. Aamodt

**Deep learning accelerator (DLA)**.


## Concepts
**Ownership models for C++ pointers**.
* *Exclusive ownership model*. Two pointers of the same type cannot point to the same resource, at the same time
* *Reference counting ownership model*. There is a reference count for the contained pointer in cooperation with all copies of the `shared_ptr`

    $\to$ Each time a new pointer points to the resource, the counter increases

**Virtual function**. A member function declared within a base class and is re-defined, i.e. overriden, by a derived class

$\to$ When we refer to a derived class object using a pointer, or a reference to the base class, we can call a virtual function for that object and execute the derived class' version of the function

**CMake**. A cross-platform free and open-source software tool for managing the build process of software using a compiler-independent method

## External resources
**CUDA**.
* [CUDA documentation](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__MEMORY.html#group__CUDART__MEMORY_1g85073372f776b4c4d5f89f7124b7bf79)
* [CUDA streams and concurrency](https://developer.download.nvidia.com/CUDA/training/StreamsAndConcurrencyWebinar.pdf)
* [CUDA memory transfer optimization](https://developer.nvidia.com/blog/how-optimize-data-transfers-cuda-cc/)

**TensorRT**.
* [TensorRT quick guide](https://docs.nvidia.com/deeplearning/tensorrt/developer-guide/index.html)
* [TensorRT API documentation](https://docs.nvidia.com/deeplearning/tensorrt/api/c_api/classnvinfer1_1_1_i_execution_context.html#a16b3aeb1359f8d53890e8a96bf6637a8)

**Misc**.
* Nsight Systems to profile CUDA cod
