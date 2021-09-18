<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
  - [Mathematical optimization probelm](#mathematical-optimization-probelm)
  - [Solve optimization problems](#solve-optimization-problems)
- [BONUS](#bonus)
<!-- /TOC -->

## Mathematical optimization probelm
**Mathematical optimization problem (optimization problem)**:

$\hspace{1.0cm}$ minimize $f_0(x)$

$\hspace{1.0cm}$ subject to $f_i(x) \leq b_i, i = 1..m$

**Definitions**
  * Optimization variable: $x = (x_1, ..., x_n)$
  * Objective function: $f_0: \mathbf{R}^n \rightarrow \mathbf{R}$
  * Constraint functions: $f_i: \mathbf{R}^n \rightarrow \mathbf{R}, i = 1..m$
  * Constraint limits (bounds): $b_1, ..., b_m$
  * Optimal (solution): a vector $x^*$ satisfying
  
  $\hspace{1.0cm} f_i(x) \leq b_i, i = 1..m$
  
  $\hspace{1.0cm} f_0(x) \leq f_0(z)$ for any $z$ that $f_i(z) \leq b_i, i = 1..m$
  
**Types of optimization problems**
  * Linear program: $f_i$ are linear for $i = 0..m$
  * Non-linear program: $f_i$ isn't linear for some $i$
  * Convex optimization problem: $f_i$ are convex for $i = 0..m$

> **NOTE**: convex optimization is a generalization of linear programming

## Solve optimization problems
**Definitions**:
  * Instance of the problem: a particular problem from a class of problems
  * Solution method for a class of optimization problem: an algorithm that computes a solution, given an instance of the problem
  * The effectiveness of an algorithm: the ability to solve the optimization problems

***
# BONUS
**1. Types of functions**:
  * Linear functions: $f(\alpha x + \beta y) = \alpha f(x) + \beta f(y)$ 
  * Convex functions: $f(\alpha x + \beta y) \leq \alpha f(x) + \beta f(y)$
  
  $\hspace{1.0cm} x, y \in \mathbf{R}^n$
  
  $\hspace{1.0cm} \alpha, \beta \in \mathbf{R}$
  
  $\hspace{1.0cm} \alpha + \beta = 1$
  
  $\hspace{1.0cm} \alpha \geq 0, \beta \geq 0$

**2. Sparse problem**: problems where each constraint function depends on only a small number of variables 