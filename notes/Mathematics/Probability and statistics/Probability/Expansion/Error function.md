---
title: 4. Delay, loss, and throughput in packet-switched networks
tags: Computer networking
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Error function](#error-function)
  - [Introduction](#introduction)
  - [Name](#name)
  - [Applications](#applications)
<!-- /TOC -->

# Error function
## Introduction

<div style="text-align:center">
    <img src="https://i.imgur.com/Yw0mLzm.png">
    <figcaption>Error function plot</figcaption>
</div>

**Error function (Gauss error function)**. A complex function of a complex variable defined as

$$\text{erf}(z)=\frac{2}{\sqrt{\pi}} \int_0^z e^{-t^2}dt$$

* *Interpretation of error function in statistics for non-negative values of $x$*. For a variable $Y\sim\mathcal{N}(0,\frac{1}{\sqrt{2}})$

    $\to$ $\text{erf}(x) = P(Y\in[-x,x])$

**Related functions**.
* *Complementary error function*. $\text{erfc}(z) = 1-\text{erf}(z)$
* *Imaginary error function*. $\text{erfi}(z)=-i\text{erf}(iz)$

## Name
**History**. The term "error function" and its abbreviation $\text{erf}$ were proposed by J. W. L. Glaisher in 1871 on account of its connection with the theory of probability, and notably the theory of errors
* *Law of facility of errors*. The error density is given as 
    
    $$f(x)=\sqrt{\frac{c}{\pi}} e^{-cx^2}$$

* *Change of error lying between $p$ and $q$*. 

    $$\sqrt{\frac{c}{\pi}} \int_p^q e^{-cx^2}dx=\frac{1}{2} [\text{erf}(q\sqrt{c}) - \text{erf}(p\sqrt{c})]$$

## Applications
**Probability of error**. When the results of a series of measurements are described by a Gaussian $\mathcal{N}(0,\sigma)$

$\to$ $\text{erf}(\frac{a}{\sigma \sqrt{2}})$ is the probability that the error of a single measurement lies within $[-a,a]$ for positive $a$

**Result estimation**. The error function and its approximations can be used to estimate results which hold with high probability or with low probability