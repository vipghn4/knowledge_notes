<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [SCSI](#scsi)
  - [Introduction](#introduction)
  - [SCSI bus operation](#scsi-bus-operation)
<!-- /TOC -->

# SCSI
## Introduction
**Small computer systems interface (SCSI)**. A more flexible parallel interface

<div style="text-align:center">
    <img src="https://i.imgur.com/bA2OkAu.png">
    <figcaption>SCSI</figcaption>
</div>

* *Characteristics*.
    * Can control up to 8 to 16 devices from the same interface, depending on the version
    * Can transfer data both to- and from- the peripheral
    * Can control many different devices
* *SCSI standard*. Define conceptual models and commands for ten classes of devices, including disk drives, tape drivers, tape drives, printers, scanners, etc.

## SCSI bus operation
**SCSI bus**. Connect a host adapter in a computer, with one or more peripheral controllers attached to peripherals, e.g. disk drives
* *Initiator*. The host adapter is called an initiator, since it initiates an I/O procedure
* *Target*. The controller is called a target, since it is the target of the host's commands

**SCSI ID**. Each device on the SCSI bus is assigned an address, or SCSI ID, by means of a switch

<div style="text-align:center">
    <img src="https://i.imgur.com/oyUP6eY.png">
    <figcaption>SCSI switches</figcaption>
</div>

* *Number of IDs*.

    | Bus width | ID width | IDs available |
    | --- | --- | --- |
    | 8-bit | 3-bit | 8 |
    | 16-bit | 4-bit | 16 |

* *Logical units*. Each controller can support up to 8 logical units (LUN - logical unit number)
    * *SCSI-2 bus*. Typically, controller is built into disk, and there are 1 LUN / target

        $\to$ But bridge controllers can manage multiple physical devices

**Logical unit number (LUN)**. A number used to identify a logical unit
* *Representation*. A LUN can be used with any device supporting read/write operations, e.g. a tape drive, but is most often to refer to a logical disk, as created on a storage area network (SAN)
    * *Rule of thumb*. Though not technically correct, the term "LUN" is often also used to refer to the logical disk itself
        * *Logical disk (logical volume or virtual disk)*. A virtual device providing an area of usable storage capacity on one or more physical disk drive(s) in a computer system
* *Example*. A typical multi-disk drive has multiple physical SCSI ports, each with one SCSI target address assigned

    $\to$ An administrator may format the disk array as a RAID, then partition this RAID into several separate storage-volumes
    * *Volume representation*. To represent each volume, a SCSI target is configured to provide a logical unit

        $\to$ Each SCSI target may provide multiple logical units representing multiple volumes

        >**NOTE**. This does not mean that the volumes are concatenated
    
    * *Volume access on the disk array*. The computer, which accesses a volume on the disk array, identifies which volume to read or write with the LUN of the associated logical unit
* *LUN selection*. 
    * *Early versions of SCSI*. An initiator delivers a command descriptor block (CDB), as given below, to a target, i.e. physical unit

        $\to$ Within the CDB is a 3-bit LUN field to identify the logical unit within the target
    * *Current SCSI*. The initiator delivers the CDB to a particular logical unit, thus LUN appears in the transport-layer data structures, not the CDB
* *LUN and SCSI targets*. Many SCSI targets contain only one LUN, while others have a small number of LUNs corresponding to separate physical devices 

**SCSI connectors**. Each device on the SCSI bus has two 50-pin connectors, which allow devices to be daisy-chained into a parallel bus

**SCSI requests**. A request is a command from initiator to target
* *Bus control*. Once the request is transmitted, target has control of bus

    >**NOTE**. Target may disconnect from bus, and later reconnect, i.e. important for multiple targets or even multitasking

* *Command structure*.
    * *Task identifier*. Initiator ID, target ID, LUN, and tag
    * *Command descriptor block*. For example, reach 10 blocks at position $N$
    * *Task attribute (optional)*. SIMPLE, ORDERD, HEAD OR QUEUE, etc.
    * *Input/output buffer and sense data (optional)*
    * *Status byte*. GOOD, CHECK CONDITION, etc.
* *Command execution*. Each LUN maintains a queue of tasks
    * *Task management commands to initiator*. Abort / terminate task, reset target, etc.
    * *Linked commands*. Initiator can link commands, thus no intervening tasks

        $\to$ We can use to implement atomic read-modify-write
        * *Intermediate commands*. Return status byte INTERMEDIATE