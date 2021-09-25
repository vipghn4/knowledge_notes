---
title: 1. Introduction and review about computer system
tags: Operating system
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [File descriptor](#file-descriptor)
- [Appendix](#appendix)
  - [Concepts](#concepts)
  - [Reference](#reference)
<!-- /TOC -->

# File descriptor
**What an open file represents**. The value returned by an `open` call is termed a file descriptor, and is essentially an index to an array of open files kept by the kernel

$\to$ The file descriptor is the gateway into the kernel's abstractions of underlying hardware

<div style="text-align:center">
    <img src="https://i.imgur.com/QkuYRXj.png">
    <figcaption>File descriptor as an abstraction of hardware</figcaption>
</div>

**Lowest-level concepts**. The OS requires a programmer to create a device driver to be able to communicate with a hardware device

$\to$ This device driver is written to an API provided by the kernel
* *Functions of device driver*. The device driver will provide a range of functions, which are called by the kernel, in response to various requirements
    * *Example*. `read` and `write` functions, which will be called in response to the analogous operations on the file descriptor

        $\to$ The device driver knows how to convert these generic requests into specific requests or commands or a particular device
* *Device layer*. To provide the abstraction to the user-space, the kernel provides a file-interface via what is generically termed a device layer
    * *`/dev` directory*. Physical devices on the host are represented by a file in a special file system, e.g. `/dev`

        $\to$ In UNIX-like systems, device nodes have what are termed a major and minor number, which allow the kernel to associate particular nodes with their underlying driver

    * *Example code of major and minor numbers*.

        ```bash
        $ ls -l /dev/null /dev/zero /dev/tty
        crw-rw-rw- 1 root root 1, 3 Aug 26 13:12 /dev/null
        crw-rw-rw- 1 root root 5, 0 Sep  2 15:06 /dev/tty
        crw-rw-rw- 1 root root 1, 5 Aug 26 13:12 /dev/zero
        ```

**File descriptor**. The handle user-space uses to talk to the underlying device
* *Broad sense view*. When a file is `open`ed, the kernel is using the path information to map the file descriptor with something providing an appropriate `read` and `write`, etc. API
    * *`open` a device*. When this `open` is for a device, e.g. `/dev/sr0`, the major and minor number of the opened device node provides the information the kernel needs to find the correct device driver and complete the mapping
        
        $\to$ The kernel will now know how to route further calls, e.g. `read`, to the underlying functions provided by the device driver
    * *`open` non-device file*. Operate similarly, although there are more layers in between
* *Mount point*. The heart of abstraction of file descriptor
    * *Mounting a file system*. Have the dual purpose of setting up a mapping so that 
        * The file system knows the underlying device providing the storage
        * The kernel knows what files opened under that mount-point should be directed to the file system driver

**Redirection**. Often, we do not want the standard file descriptors, e.g. `stdin` and `stdout`, to point to their default places
* *Example*. 
    * We may wish to capture all the output of a program into a file on disk, or have it reads its commands from a file we prepared earlier
    * We may wish to pass the output of one program to the input of another
* *File direction commands*.

    | Name | Command | Description | Example |
    | --- | --- | --- | --- |
    | Redirect to a file | `> filename` | Take all output from `stdout` and place it into `filename` | `ls > filename` |
    | Read from a file | `< filename` | Copy all data from the file to the standard input of the program | `echo < filename` |
    | Pipe | `program1 \| program2` | Take everything from `stdout` of `program1`, and pass it to `stdin` of `program2` | `ls \| more` |

# Appendix
## Concepts
**File descriptor (FD)**. A unique identifier, i.e. handle, for a file or other I/O resource
* *File descriptor table*. In the traditional implementation of UNIX, file descriptors index into a per-process file descriptor table maintained by the kernel

    $\to$ This table, in turn, indexes into a system-wide table of files opened by all processes, called file 
    * *Set of file descriptors open in a process in UNIX*. Recorded under the path `/proc/PID/fd`
* *File table*. 
    * Record the mode, with which the file, or other resources has been opened, i.e. for reading, writing, appending, etc.
    * Index into another table, i.e. the inode table, which describes the actual underlying file
* *I/O with file descriptor*. To perform I/O, the process passes the file descriptor to the kernel through a system call

    $\to$ The kernel will access the file, on behalf of the process

    >**NOTE**. The process does not have direct access to the file, or inode tables

**Some other points about file descriptor**.
* *File descriptors as stream representation*. When we open a file, OS creates a stream to that file, and connect that stream to opened file

    $\to$ The descriptor in fact represents the stream
    * *Example*. There are some default streams created by the OS, which are connected to our terminal, instead of files, e.g.
        * When we write something in terminal, it goes to `stdin` stream and OS
        * When we write `ls` command on terminal, the OS writes the output to `stdout` stream

            $\to$ `stdout` stream is connected to our monitor terminal, so we can see the output there
    * *Reference*. https://stackoverflow.com/questions/5256599/what-are-file-descriptors-explained-in-simple-terms

## Reference
https://www.bottomupcs.com/file_descriptors.xhtml