---
title: Study plan
tags: Plans
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
* [Objective and plan](#objective-and-plan)
* [Background](#background)
  * [Current task](#current-task)
  * [Pending](#pending)
  * [Characteristics of good software](#characteristics-of-good-software)
    * [Maintainability](#maintainability)
    * [Correctness](#correctness)
    * [Reusability](#reusability)
    * [Reliability](#reliability)
    * [Portability](#portability)
    * [Efficiency](#efficiency)
<!-- /TOC -->

# Objective and plan
**Be able to implement good software before the age of 25**

# Background
## Current task
- [ ] Learn about digital image processing (first prioritized)
- [ ] Learn about common software patterns (second prioritized)
- [ ] Learn how to write a good Dockerfile (third prioritized)

## Pending
- [ ] How to write good instructions for annotators

## Characteristics of good software
### Maintainability
The ease with which changes can be made to satisfy new requirements or to correct deficientcies

**Required skills**.
* Good Doxygen documentation and README
    - [x] Get used to DoxygenToolkit of vim
    - [x] Find a good reference to the structure of a good README file
* Good software architecture design
    - [ ] Learn common software patterns
    - [ ] Read about architectures of open source softwares (AOSA)
    - [ ] Read code [LibJPEG](https://github.com/LuaDist/libjpeg/blob/master/jdcoefct.c)
    - [ ] Read code OpenBLAS
* Good version control
    - [x] Practice pulling before pushing
    - [x] Practice solving merging conflicts
    - [ ] Finish learning Git (PENDING)
* Good coding convention
    - [x] Find supporting coding convention plugins for C++ and Python in Vim
    - [ ] Investigate Fan Wang's source code
    - [ ] Read about [GNU coding standard](https://www.gnu.org/prep/standards/html_node/index.html#SEC_Contents)

### Correctness
The degree with which software adheres to its specified requirements

**Required skills**.
* Mathematics
    * Linear algebra
    * Calculus
    * Optimization
    * Information theory
* Classical computer vision
    * Image processing
        - [ ] Finish Digital image processing by Rafael
    * Computer vision
        - [ ] Finish a book in computer vision
* Deep learning for computer vision
    - [ ] Up to date with recent trends and approaches in machine learning for computer vision
        - [ ] How to find best matched open source repos for machine learning problems
        - [ ] Up-to-date with image classification, object detection, segmentation
            - [ ] Image classification
            - [ ] Object detection
            - [ ] Segmentation
        - [ ] Get recent trends in Computer Vision
    - [ ] Finish deep learning boot camp
        - [x] Data management
        - [ ] Training and debugging
        - [x] Testing and deployment

### Reusability
The ease with which software can be reused in developing other software

**Required skills**.
* Good software architecture design (mentioned above)
* Good Doxygen doc strings
    - [x] Find supporting doc string convention plugins for C++ and Python in Vim
    - [x] Learn how to write good doc string
    - [x] Refer to doc string of famous open source C++ and Python repos
* Good coding convention (mentioned above)
* Good conventions for writing libraries, e.g. CMake convention
    - [ ] Learn about conventions for writing libraries in C++ and Python
    - [ ] Refer to famous open source libraries

### Reliability
The frequency and criticality of software failure, where failure is an unacceptable effect or behavior occurring under permissible operating conditions

**Required skills**.
* Unit test
    - [ ] Learn about test design (PENDING)

### Portability
The ease with which software can be used on computer configurations other than its current one

**Required skills**.
* Good Dockerfile
    - [ ] Learn about how to write good Dockerfile, which results in minimal Docker images (PENDING)

### Efficiency
The degree with which software fulfills its purpose without waste of resources

**Required skills**.
* Algorithm and data structures
    - [x] Complete a cheet sheat about frequently used algorithms and data structures in VNOI
* CUDA programming
    - [ ] Study a course about GPU programming
    - [ ] Finish a book about computer architecture
    - [ ] Get used to Deepstrea
