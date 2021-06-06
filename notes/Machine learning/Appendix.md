---
title: Appendix
tags: Machine learning
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
* [Data collection](#data-collection)
  * [Tricks](#tricks)
<!-- /TOC -->

# Data collection
## Tricks
**Sample size**
* If the accuracy $\sigma$ is a function of the number of data examples $x$ then this function should look like a sigmoid-like function
    * *Explain*. Initially collected data is very useful for increasing model accuracy, but after the sample size exceeds a certain number, the accuracy will saturate

**Definition of classes**
* Visually distinguishable objects should be divided into different classes

    $\to$ This helps increase the accuracy of classification mode
