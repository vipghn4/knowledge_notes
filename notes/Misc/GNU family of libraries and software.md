---
title: GNU family of libraries and software
tags: Misc
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
* [GNU family of libraries and software](#gnu-family-of-libraries-and-software)
  * [Introduction](#introduction)
<!-- /TOC -->

# GNU family of libraries and software
## Introduction
**GNU and GNOME projects**.
* *GNU project*. A free software, mass collaboration project announced by Richard Stallman on 27 Sep 1983
    * *Goal*. Give computer users freedom and control in their use of their computers and computing devices
* *GNOME project*. A community behind the GNOME desktop environment and the software platform upon which it is based

    >**NOTE**. GNOME project is no longer part of the GNU project

    * *Motivation*. Founded to deal with administrative tasks and press interest, and to act as a contact point for companies interested in developing GNOME software

**GNU**. An extensive collection of free software, which can be used as an OS or can be used in parts with other OSes
* *Softwares*.
    * *GNU compiler collection (GCC)*. An optimizing compiler produced by the GNU project supporting various programming languages, hardware architectures, and OSes
    * *GNU network object model environment (GNOME)*. A free and open-source desktop environment for UNIX-like OSes
    * *GNU image manipulation program (GIMP)*. A free and open-source raster graphics editor
        * *Usages*. Image manipulation and image editing, free-form drawing, transcoding between image file formats, and more specialized tasks
    * *GIMP tool kit (GTK)*. A GUI toolkit developed to facilitate the development of GIMP
        * *GTK+*. Redesigned version of GTK, which uses object-oriented programming techniques

**GLib**. A bundle of low-level system libraries written in C and developed mainly by the GNOME project
* *Introduction from gitlab*. GLib is the low-level core library that forms the basis for projects such as GTK and GNOME
    * *Features*. Provide data structure handling for C, portability wrappers, and interfaces for such runtime functionality as an event loop, threads, dynamic loading, and an object system
    * *Gitlab link*. `https://gitlab.gnome.org/GNOME/glib`
* *History*. GLib is originally part of GTK, however, before releasing GTK+ version 2, the project's developers decided to separate code from GTK, which was not for GUIs

    $\to$ GLib was created as software bundle
* *Features*.
    * *Data structures*.
        * Memory chunks, doubly and single linked lists, hash tables
        * Dynamic strings and string utilities, e.g. lexical scanner, string chunks, i.e. groups of strings
        * Dynamic arrays, balanced binary trees, N-ary trees
        * Quarks, i.e. a two-way association of a string and a unique integer identifier
        * Keyed data lists, relations, and tuples
    * *Functions*.
        * Threads, thread programming, and related facilities
            * *Example*. Primitive variable access, mutexes, asynchronous queues, secure memory pools, message passing and logging, hook functions, i.e. callback registering, and timers
        * Message passing facilities, e.g. byte-order conversion and I/O channels
        * Other features such as standard macros, warning and assertions, and dynamic loading of modules
* *Components*. GObject, GLib, GModule, GThread, and GIO
* *Similar projects*. Libraries below provide low-level functions and implementations of data structures
    * *Standard template library (STL)*. C++ library for data structures and algorithms
    * *Boost*. Provide some functions for C++, e.g. threading primitives, similar to what GLib does for C
* *Tutorial*. https://developer.gnome.org/gtk-tutorial/stable/c2023.htm
