# Appendix
## Short notes
**Firmware, OS, and OS kernel**.

<div style="text-align:center">
    <img src="https://i.imgur.com/sitaeGw.png">
    <figcaption>Hardware-software stack of a computer</figcaption>
</div>

* *Firmware*. A program, or a set of programs, written to ROM of a computing device at the time of manifacturing
    * *Immutability*. Firmware cannot be changed or deleted by end-user without the aid of special programs
    * *Lifetime*. Firmware remains on the device even when the device is off
    * *Device containing firmware*. Embedded systems, e.g. traffic lights, consumer appliances, etc.
* *Operating system*. The software providing the base management of a computer
    * *Example*. Setting up the computer during bootup, managing hardware via device drivers, prodiving access to hardware and other system resources, etc.
* *Kernel*. A set of programs following the concepts of the OS

    $\to$ Kernel is a fundamental part of a modern computer's OS and used to initialize and manage critical resources
    * *Difference from firmware*.
        * *Firmware*. A minimal piece of functional code, which performs the basic functions of the intended device
        * *Kernel*. A much larger entity involving multiple layers, e.g. memory management, process management, file systems, etc. 