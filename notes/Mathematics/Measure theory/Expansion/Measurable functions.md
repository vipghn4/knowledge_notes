<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Measurable functions](#measurable-functions)
  - [Measurable functions](#measurable-functions-1)
  - [Motivation](#motivation)
    - [Simple function](#simple-function)
    - [Pointwise convergence](#pointwise-convergence)
    - [Integral of function](#integral-of-function)
  - [Defining measurable functions by pre-images](#defining-measurable-functions-by-pre-images)
  - [Measurable functions and $\sigma$-fields](#measurable-functions-and-sigma-fields)
- [Appendix](#appendix)
  - [References](#references)
<!-- /TOC -->

# Measurable functions
## Measurable functions
**Measurable function**.
* *Informal*. A measurable function is a function between the underlying sets of two measurable spaces, which preserves the structure of the spaces
    * *Explain*. The preimage of any measurable set is measurable
    * *Analogy*. Continuous function between topological spaces preserves the topological structure, i.e. the preimage of any open set is open
* *Assumptions*. $(X,\Sigma)$ and $(Y,T)$ are measurable spaces
* *Conclusion*. $f:X\to Y$ is measurable if

    $$\forall E\in T,f^{-1}(E)=\{x\in X:f(x)\in E\}\in \Sigma$$

    that is, $\sigma(f)\subseteq \Sigma$
* *Notation*. If $f:X\to Y$ is measurable, we write $f:(X,\Sigma)\to(Y,T)$ or $f$ is $(\Sigma, T)$-measurable
    * *Explain*. We want to emphasize the dependency on $\Sigma$ and $T$

**Measure function and probability space**.
* *Assumptions*.
    * $(\Omega,\mathcal{F},P)$ is a probability space
    * $(S,\mathcal{A})$ is a measurable space
* *Question of interest*. Can we use $f:\Omega\to S$ to construct a measure on $(S,\mathcal{A})$
    * *Example*. Consider $f:\Omega\to S$ then, for some $A\in\mathcal{A}$, what is the probability that the image of $f$ is in $A$

## Motivation
### Simple function
**Simple function**. A finite linear combination of indicator functions of measurable sets
* *Assumptions*.
    * $(X,\Sigma)$ is a measurable space
    * $A_1,\dots,A_n\in\Sigma$ is a sequence of disjoint measurable sets
    * $a_1,\dots,a_n$ is a sequence of real or complex numbers
    * $\mathbf{1}_A$ is the indicator function of the set $A$ 
* *Simple function*. A function $f:X\to\mathbb{C}$ of the form

    $$f(x)=\sum_{k=1}^n a_k\mathbf{1}_{A_k}(x)$$

* *Integration of simple functions*. If a measure $\mu$ is defined on $(X,\Sigma)$, the integral of $f$ w.r.t $\mu$ is

    $$\int_X fd\mu=\sum_{k=1}^n a_k\mu(A_k)$$

    if all summands are finite
* *Convention*. If $a_k=0,\mu(A_k)=\infty$ then $0\cdot\infty=0$

**Measurability of simple functions**. A simple function $f:X\to\mathbb{R}$ is measurable

>**NOTE**. $f:X\to\mathbb{C}$ is measurable in the same manner

* *Proof*. To prove the measurability of $f$, it suffices to prove that $f^{-1}(s_a)$ is measurable for all $a\in\mathbb{R}$, where $s_a=(-\infty, a]$
    * We have that

        $$f^{-1}(s_a)=\bigcup \{A_k:k\in\{1,\dots,n\},a_k\leq a\}$$

    * Hence $f^{-1}(s_a)$ is measurable

### Pointwise convergence
**Pointwise convergence**.
* *Assumptions*.
    * $(f_n)$ is a sequence of function with $f_i:X\to Y$
* *Pointwise convergence*. $(f_n)$ converges pointwise to $f:X\to Y$ if and only if

    $$\forall x\in \textbf{dom } f, \lim_{n\to\infty}f(x)=f(x)$$

    and $f$ is said to be the pointwise limit function of $(f_n)$
* *Almost everywhere (a.e.) convergence*. In measure theory, one talks about almost everywhere convergence of a sequence of measurable functions defined on a measurable space
    * *Pointwise convergence almost everywhere*. Refer to pointwise convergence on a subset of domain, whose complement has zero measure

**Pointwise consequence of measurable function**.
* *Assumptions*.
    * $\{f_n:n\in\mathbb{N}\}$ is a sequence of measurable functions $f_n:X\to\bar{\mathbb{R}}$
    * $\sup_{n\in\mathbb{N}}\{f_n(x)\} = \big(\sup_{n\in\mathbb{N}} f_n\big)(x)$
* *Conclusion*. The following functions are measurable extended real-valued functions on $X$

    $$\sup_{n\in\mathbb{N}} f_n,\quad\inf_{n\in\mathbb{N}} f_n,\quad \lim_{n\to\infty}\sup f_n,\quad \lim_{n\to\infty}\inf f_n$$

* *Reference*. https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch3.pdf

### Integral of function
**Integral of $f$**. Consider a function $f:X\to\mathbb{R}$
* *Integration of $f$*. To integrate $f$, we have to approximate it by easy-to-integrate simple functions

    $\to$ To approximate the integral of $f$ by simple functions, we need $f$ to be measurable

    >**NOTE**. In fact, this is how we define $\int_X fd\mu$

* *Integral of $f$*. $\int_X fd\mu$ is computed by finding a sequence of simple functions $s_n$ converging pointwise almost everywhere to $f$ so that $\int s_n$ converges to $\int f$, i.e.

    $$\int_X fd\mu = \sup\{\int_X sd\mu:0\leq s\leq f,s\text{ is simple}\}$$

    >**NOTE**.  In contrast with the definition of the Riemann integral, it is not necessary to approximate a measurable function from both above and below in order to define its integral

* *Integrability of $f$*. $f$ is $\mu$-integrable if it is measurable and $\int_X fd\mu<\infty$
    * *Explain*. $f$ must be measurable since a sequence of measurable functions is measurable

        $\to$ $f$ must be measurable to ensure the convergence of $s_n$

**References**.
* https://math.stackexchange.com/questions/966076/motivation-for-definition-of-measurable-function
* https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf
* https://math.stackexchange.com/questions/3501034/understanding-measurable-functions-and-their-definition-based-on-pre-images

## Defining measurable functions by pre-images
**Measurable function**. A function $f$ being measurable does not imply that $f(B)$ is measurable for all $B\in\mathcal{F}$, i.e.

$$\forall B\in\mathcal{F},f(B)\in\mathcal{A}$$

* *Consequence*. Measurable functions cannot be described in terms of preimages, since that does not work

**Commutivity of set operations**.
* *Assumptions*. $\{A_\alpha\}_{\alpha\in I}$ is a collection of mesurable subsets of $S$, indexed by an arbitrary set $I$
* *Conclusion*.
    * $f^{-1}(A^C)=[f^{-1}(A)]^C$
    * $f^{-1}(\bigcup_{\alpha\in I} A_\alpha)=\bigcup_{\alpha\in I} f^{-1}(A_\alpha)$
    * $f^{-1}(\bigcap_{\alpha\in I} A_\alpha)=\bigcap_{\alpha\in I} f^{-1}(A_\alpha)$
* *Proof*.

## Measurable functions and $\sigma$-fields
**$\sigma$-field generated by measurable functions**.
* *Assumptions*.
    * $f:\Omega\to S$, where $(S,\mathcal{A})$ is a measurable space
* *$\sigma$-field generated by $f$*. $\sigma(f)=f^{-1}(\mathcal{A})$
* *Interpretation*. $\sigma(f)$ is the smallest $\sigma$-field so that $f$ is $[\sigma(f),\mathcal{A}]$-measurable

**Lemma**.
* *Assumptions*.
    * $(\Omega,\mathcal{F})$ and $(S,\mathcal{A})$ are measurable spaces
    * $f:\Omega\to S$ is a function
    * $\mathcal{A}=\sigma(\mathcal{C})$ for some collection of sets $\mathcal{C}$
* *Conclusion*. $f$ is $(\mathcal{F},\mathcal{A})$-measurable if and only if

    $$f^{-1}(\mathcal{C})=\{f^{-1}(c):c\in\mathcal{C}\}\subseteq\mathcal{F}$$

**Corollary**. If $f$ is a continuous function from one topological space to another, each with Borel $\sigma$-fields, then $f$ is measurable

# Appendix
## References
* https://www.stat.cmu.edu/~arinaldo/Teaching/36710-36752/Scribed_Lectures/Scribed_Lecture05_Sep16(W).pdf
* https://www.stat.cmu.edu/~arinaldo/Teaching/36752/S18/Scribed_Lectures/Feb8.pdf