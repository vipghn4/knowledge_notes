<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [The infinite Gaussian mixture model](#the-infinite-gaussian-mixture-model)
  - [Introduction](#introduction)
  - [Finite hierarchical](#finite-hierarchical)
- [Reference](#reference)
<!-- /TOC -->

# The infinite Gaussian mixture model
## Introduction
**Major advantage in the Bayesian methodology**. Overfitting is avoided

$\to$ The difficult task of adjusting model complexity vanishes

**Proposed approach**. A Markov chain Monte Carlo (MCMC) implementation of a hierarchical  infinite Gaussian mixture model is presented

## Finite hierarchical
**Finite Gaussian mixture model with $k$ components**.
* *Assumptions*.
    * $\mathcal{N}(\mu_j,s_j^{-1})$ is the $j$th normalized Gaussian
        * $\mu_j$ is the mean
        * $s_j$ is the precision, i.e. inverse variance
        * $\pi_j$ is the mixing proportion for Gaussian $j$
    * $y$ is a scalar observation
    * $\mathbf{y}=\{y_1,\dots,y_n\}$ is the training data
* *Finite Gaussian mixture model*. $p(y|\mu_1,\dots,\mu_k,s_1,\dots,s_k,\pi_1,\dots,\pi_k) = \sum_{j=1}^k \pi_j \mathcal{N}(\mu_j, s_j^{-1})$

**Gibbs sampling**. A well known technique for generating samples from complicate multivariate distributions, which is often used in Monte Carlo procedures
* *Simplest form application*. Used to update each variable in turn from its conditional distribution, given all other variables in the system
* *Theorem*.
    * Gibbs sampling generates samples from the joint distribution
    * The entire distribution is explored, as the number of Gibbs sweeps grows large

# Reference
* https://groups.seas.harvard.edu/courses/cs281/papers/rasmussen-1999a.pdf