<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Memory-mapped I/O](#memory-mapped-io)
  - [Motherboard chipsets and the memory map](#motherboard-chipsets-and-the-memory-map)
  - [Memory-mapped I/O](#memory-mapped-io-1)
  - [Overview](#overview)
- [Appendix](#appendix)
  - [Concepts](#concepts)
<!-- /TOC -->

# Memory-mapped I/O
## Motherboard chipsets and the memory map
**CPU-environment interactions**. The CPU does not know anything about what it is connected to
* *Explain*. It talks to the outside world via its pins, but does not care what that outside world is

    $\to$ It may be a motherboard in a computer, but can be a toaster, network router, etc.
* *Main ways by which the CPU and the outside communicate*. Memory address space, I/O address space, and interrupts

    $\to$ We only care about motherboards and memory for now
* *CPU's gateway to the world in a motherboard*. The font-side bus connecting it to the northbridge

    $\to$ Whenever the CPU needs to read or write memory, it does so via this bus
    * *Explain*. 
        * It uses some pins to transmit the physical memory address it wants to write or read
        * It uses some other pins to send the value to be written or receive the value being read

**Address routing by CPU**.
* *Memory access*. Most of the memory requests from the processor are routed to RAM modules by the northbridge, but not all of them

    $\to$ Physical memory addresses are also used for communication with assorted devices on the motherboard, i.e. memory-mapped I/O
* *Physical memory handling by the northbridge*. When the northbridge receives a physical memory request, it decides where to route it
    * *Memory address map*. The routing is decided via the memory address map
    * *Idea*. For each region of physical memory addresses, the memory map knows the device owning the region
    * *`/proc/iomem`*. Neatly lists the address range mappings
* *Address translation inside the CPU*. Inside the CPU, e.g. in the programs we run and write, the memory addresses are logical and they must be translated by the CPU into a physical address, before memory is accessed on the bus
    * *Logical-to-physical address translation rule*. Complex and depend on the mode, in which the CPU is running

## Memory-mapped I/O
**Methods of performing I/O between the CPU and peripheral devices**.
* Memory-mapped I/O (MMIO)
* Port-mapped I/O (PMIO)
* Dedicated I/O processor, i.e. channels on mainframe computers, which execute their own instructions

**Memory-mapped I/O**. Use the same address space to address both memory and I/O devices
* *Idea*. The memory and registers of the I/O devices are mapped to, i.e. associate with, address values

    $\to$ A memory address may refer to either a portion of physical RAM, or to memory of the I/O device
    * *Consequence*. The CPU instructions used to access memory can also be used for accessing devices
* *Implementation*. Each I/O device monitors the CPU's address bus and responds to CPU access of address assigned to that device

    $\to$ The I/O device connects the data bus to the desired device's hardware register
    * *Explain*. The device snoops on the address bus, and when it sees the address targetting for it

        $\to$ It will just receive the data on the data bus
* *Address reservation*. To accommodate the I/O devices, areas of addresses used by the CPU must be reserved for I/O, and must not be available for normal physical memory
    * *Type of reservation*. The reservation may be permanent, or temporary, as achieved via bank switching

**Port-mapped I/O**. Often use a special class of CPU instructions designed specifically for performing I/O, e.g. the `in` and `out` instructions
* *I/O address space*. I/O devices have a separate address space from general memory accomplished by 
    * An extra "I/O" pin on the CPU's physical interface, or
    * An entire bus dedicated to I/O

## Overview
**DMA and CPU-to-device communication**. Different CPU-to-device communication methods, e.g. memory mapping, do not affect the direct memory access (DMA) for a device
* *Explain*. DMA is a memory-to-device communication method, which bypasses the CPU

**Interrupt-based CPU-device communication**. Interrupt are always treated separately
* *Explain*. 
    * An interrupt is device-initiated, as opposed to the methods above, which are CPU-initiated
    * An interrupt is unidirectional, as information flows only device to CPU
    * Each interrupt line carries only one bit of information with a fixed meaning, i.e. an event which requires attention has occurred in a device on this interrupt line

**I/O bus in port-mapped I/O**. I/O operations can slow memory access if the address and data buses are shared
* *Explain*. The peripheral device is usually much slower than main memory

    $\to$ In some architectures, port-mapped I/O operates via a dedicated I/O bus, alleviating the problem

**Memory-mapped I/O**.
* *Benefits*. 
    * By discarding the extra complexity brought by port I/O
        
        $\to$ A CPU requires less internal logic, and thus cheaper, faster, easier to build, consumes less power, and can be physically smaller
    * Since regular memory instructions are used to address devices,
        * All of the CPU's addressing modes are available for the I/O and the memory
        * Instructions performing an ALU operation directly on a memory operand can be uesd with I/O device registers as well

# Appendix
## Concepts
**Bank switching**. A technique used in computer design to increase the amount of useable memory beyond the amount directly addressable by the processor instructions

$\to$ It can be used to configure a system differently at different times
* *Address decoding*. Any computer system with more than one memory device needs hardware, which is usually external to the CPU, to determine which device to access for any particular address

    <div style="text-align:center">
        <img src="https://i.imgur.com/W1IqiGf.png">
        <figcaption>Address decoder in memory-mapped I/O</figcaption>
    </div>

    * *Simplest case*. Address decoder is a single device looking at the address and making the decision like
        * If address is less than `$c000`, then access the RAM chip by 
            * Setting the chip select signal for the RAM chip `on`
            * Setting the chip select signal for the ROM chip `off`
        * If address is larger than `$e000`, then access the ROM chip by 
            * Setting the chip select signal for the RAM chip `off`
            * Setting the chip select signal for the ROM chip `on`
* *Bank switching*. Extend address decoding by changing which device is accessed in a programmable way
    * *Latch*. Basically a one-bit memory location, which is like a switch toggling the address space that the computer processor is using
        * *Purpose*. Toggle between multiple banks of memory
        * *Implementation*. Hardware or software, and set up separate from the processor

            $\to$ The bank switching in the hands of an external operation
        * *Example setting*.
            * When the latch contains a zero, any access to `$e000` to `$ffff` will access ROM chip #0
            * When the latch contains a one, any access to `$e000` to `$ffff` will access ROM chip #1
    * *Consequence*. Using this technique, we can access more than `0x10000` memory locations, even when we have only `0x10000` addresses available, by 
        * Having multiple devices at the same memory address, and
        * Choosing them based on further information, e.g. the latch