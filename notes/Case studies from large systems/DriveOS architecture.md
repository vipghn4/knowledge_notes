---
title: DriveOS architecture
tags: Case studies from large systems
---

# NVIDIA DRIVE OS 5.1 Linux SDK
## Platform software stacks
**Drive OS stack**.

<div style="text-align:center">
    <img src="/media/NJiMpYO.png">
    <figcaption>DRIVE OS stack</figcaption>
</div>

### Foundation service stack
**Foundation service stack**. Provide infrastructure for all the components of the platform

$\to$ Multiple guest OSes can run on the hardware, with the Hypervisor managing use of hardware resources

<div style="text-align:center">
    <img src="/media/dMcDpZg.png">
    <figcaption>Foundation service stack</figcaption>
</div>

**Components**.
* *Hypervisor*. Software server separating the system into partitions, each of which can contain an OS or a bare-metal application
    * *Managed aspects*.
        * Guest OS partitions and the isolation between them
        * Partitions' virtual views of the CPU and memory resources
        * Hardware interactions
        * Run-lists
        * Channel recovery
* *I/O sharing server*. Allocate peripherals which Guest OS need to control
* *Storage*. Virtualize storage devices on SoC
* *GPU/MM/AVIO sharing*. Manage isolated hardware services for
    * Graphics and computation, i.e. GPU
    * Codecs, i.e. MM
    * Display, video capture, and audio I/O, i.e. AVIO
* *Partition monitor*. Monitor partitions, i.e.
    * Dynamically load / unload and start / stop partitions and virtual memory allocations
    * Log partition use
    * Provide interactive debugging of guest OSes

### Foundation virtualization stack
**Foundation virtualization stack**. Provide virtualization stack technology, which enables running multiple OS stacks with different security and safety requirements on a single device

**Components**.
* *Hypervisor kernel*. Provide implementation for the virtualization features specific to the OS
* *Partition configuration table*. A concatenated set of header files, which represents a virtual configuration
    * *Image*. The binary image of the partition configuration table is appended to the Hypervisor image

        $\to$ When loaded on the target platform, the concatenated image runs multiple guest OSs
* *Partition loader*. Load the Guest OS
* *Monitor partition*. Maintain and monitor the per-guest health using Watchdog timer
* *Resource manager server partition*. Manage the server partitions for the various virtualized component servers
* *Boot and power manager processor (BPMP)*. 
    * During boot, BPMP executes the boot ROM code, and controls the SoC boot sequence
    * After boot, BPMP runs power management functions
* *Audio*. Provide Audio Server which para-virtualizes the Audio Processing Engine (APE) of the Tegra device
* *I2C*. 
    * Allow multiple guests to access the same I2C controller, without requiring prior information
    * Provide a framework to assign slaves to one or more guests
* *Virtual system configuration storage*. Manage the storage configuration files, which are required for flashing script to identify the hypervisor and guest partitions to be flashed
* *Security engine*. Enable para-virtualization of the Tegra SoC, making it available to the software of a virtual machine through a similar virtualized interface
* *Watchdog timer*. A framework consisting of system-wide WDT monitor service, running in a privileged monitor partition, and one or more WDT clients, each running in a guest partition
* *System manager*. Coordinate the ordering of state transition of each partition during a system state transition
* *Inter-VM communication infrastructure*. Provide event and data exchange between the OSes running on top of the hypervisor architecture

### NvMedia architecture
#### NvMedia stack
<div style="text-align:center">
    <img src="/media/EF2VVhc.png">
    <figcaption>NvMedia stack</figcaption>
</div>

**Supported interaction types**.
* *Applications*. Call the NvMedia Framework components to string together a sequence of processing steps for images
* *NvMedia Framework*. Call low-level hardware drivers to interact with the SoC (system on chip) components on the Tegra chip

**Hardware components**.
* *Video input (VI)*. Receive CSI (camera serial interface) data from the camera
* *Image signal processor (ISP)*. Produce a processed image from image data captured from an image sensor
    * *Example*. Invert pixel bits, auto exposure, etc.
* *NVIDIA encoder (NVENC)*. Convert raw image data into one of the supported image formats
* *NVIDIA decoder (NVDEC)*. Convert encoded image data into raw image data
* *Video interlace compositor (VIC)*. Convert video data for deinterlacing, composition, and format conversion
* *Programmable vision accelerator (PVA)*. Accelerate computer vision algorithms via the NvMediaVPI APIs

#### NvMedia API architecture
<div style="text-align:center">
    <img src="/media/EF2VVhc.png">
    <figcaption>NvMedia API architecture</figcaption>
</div>

**APIs**.
* *Video API library*. Support interlaced video for human-machine interface (HMI) applications
* *Image API library*. Support RAW camera processing using image signal processing (ISP) and progressive image processing for advanced driver assistance systems (ADAS) development

**NvMedia video surface**. Define and handle YUV, RGB, progressive, and interlaced processing
* *Components*.
    * *Capture*. Capture video CSI data
    * *Decode*. Decode frame level bitstream
        * *Supported formats*. Progressive and interlaced formats
    * *Encode*. Encode NVMedia video surface inputs, e.g. YUV420, RGBA, to H264/H265 format
    * *Mixer*. Support deinterlacing, format conversion, scaling, and advanced post processing
    * *Display*. Provide the ability to render the YUV/RGB surfaces on the selected display device
    * *Interoperability of EGLSStream*. Provide OpenGL and CUDA interoperability to share camera data processed by the GPU

**NvMedia image surface**. Define and handle YUV, RGB, and RAW (progressive only) image processing
* *Other functionalities*.
    * Carry the image sensor register data for embedded line information
    * Carry per-image specific metadata, which does not have to be per-processing handle
* *Components*.
    * *Image sensor control (ISC)*. Provide the ability to control serializer / deserializer (SerDes) blocks and image sensors
    * *IPP framework*. Process incoming image data with AE, AWB controls, and include the ISP processing capability

        >**NOTE**. IPP framework supports camera tuning tools
    
    * *Image signal processor (ISP)*. Provide the ability to capture data over the CSI interface
    * *Image 2D*. Provide the ability to perform manipulation of image data, e.g. cropping, scaling, copying, and converting format
    * *Image encode processing (IEP)*. Provide the ability to encode processed YUV-420 or RGB surface inputs to H264, H265, and JPEG formats
    * *Image display processing (IDP)*. Provide the ability to render the YUV or RGB surfaces on the selected display device
    * *Interoperability of EGLSStream*. Provide OpenGL and CUDA interoperability to share camera data processed by the GPU

# Appendix
## Concepts
**IPP**. Stand for "image processing pipeline"

**Interlaced video**. Also known as interlaced scan, is a technique for doubling the pecevied frame rate of a video display, without consuming extra bandwidth
* *Deinterlacing*. The process of converting interlaced video into a non-interlaced or progressive form

**Progressive image**. The image will start with low quality, and will continue to improve in resolution with each additional pass
* *Benefits* .
    * User does not have to wait until the complete image is loaded to see what it is
    * When the image is no more interesting, the user can stop the data transmission process

**Serialization**.
* *Serialization*. Turn data into a stream of bytes
* *Deserialization*. Turn a stream of bytes back into a copy of the original object

**AE, AF, AWB**. Auto-exposure, auto-focus, auto-white-balance

**QNX**. A commercial UNIX-like realtime OS, aimed primarily at the embedded systems market

**AVIO**. Audio visual input/output

**Hypervisor**. Also called virtual machine monitor (VMM), or virtualizer. A kind of emulator, which can be a computer software, firmware, or hardware creating and running virtual machine