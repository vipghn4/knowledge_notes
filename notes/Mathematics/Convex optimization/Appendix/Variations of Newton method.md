<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Gauss-Newton method](#gauss-newton-method)
  - [Introduction](#introduction)
  - [Derivation from Newton's method](#derivation-from-newtons-method)
  - [Implementation notes](#implementation-notes)
<!-- /TOC -->

# Gauss-Newton method
## Introduction
**General introduction**: a modification of Newton's method for minimizing a function

**Application**: solve non-linear least squares problems

**Advantages**: the second derivative, which can be challenging to compute, aren't required

## Derivation from Newton's method
**Idea**:
* Assumptions:
  * $S$ is the objective function, which is a sum of squares
    * Formal: $S = \sum_{i=1}^m r_i^2$ where $r_i$ is a function of $\beta$ (see below)
  * $\beta = (\beta_1, ..., \beta_n)$ is the parameters to be optimized
  * $J_r$ is the Jacobian of $(r_1, ..., r_m)$ w.r.t $\beta$
  * $H_r$ is the second derivative of $(r_1, ..., r_m)$ w.r.t $\beta$
    * Formal: ${H_r}_{ijk} = \frac{\partial^2 r_i}{\partial \beta_j \beta_k}$
  * $H$ is the Hessian matrix of $S$ w.r.t $\beta$
  * $g$ is the gradient vector of $S$ w.r.t $\beta$
* The update formula of Newton's method for minimizing $S$: $\beta^{(s+1)} = \beta^{(s)} - H^{-1} g$
* Observations:
  * $S = \sum_{i=1}^m r_i^2$
  
  $\hspace{1.0cm} \rightarrow g = (2 r^T J_r)^T = 2 J_r^T r$ (chain rule)
  
  $\hspace{2.0cm} H = 2 J_r^T J_r + 2 r^T H_r$ ($r^T H_r$ is a matrix whose element $ij$ is $r_i \frac{\partial_2 r_i^2}{\partial \beta_j \partial \beta_k}$)
* Idea of approximation: approximate $H$ by $\hat{H} = 2 J_r^T J_r$ (i.e. $2 r^T H_r$ is omitted)
* Gauss-Newton update formula: $\beta^{(s+1)} = \beta^{(s)} + \Delta$ where $\Delta = -\hat{H}^{-1} g$

**Convergence**: if the elements of $r^T H_r$ is so small compared to the corresponding elements of $J_r^T J_r$ (i.e. our approximation works well)

$\hspace{1.0cm} \rightarrow$ Gauss-Newton method acts similarly as Newton method
* Observation: the element $ij$-th of $r^T H_r$ is $r_i \frac{\partial_2 r_i^2}{\partial \beta_j \partial \beta_k}$, which is very small if
  * $r_i$ is small in magnitude, at least around the minimum
  * $\frac{\partial_2 r_i^2}{\partial \beta_j \partial \beta_k}$ is relative small in magnitude

## Implementation notes
**The invertibility of $J_r^T J_r$**: in order for $J_r^T J_r$ to be invertible

$\hspace{1.0cm} \rightarrow m \geq n$ is necessary

---