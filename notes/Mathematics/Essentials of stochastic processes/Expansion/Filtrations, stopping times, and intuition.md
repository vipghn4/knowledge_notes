<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Filtrations, stopping times, and intuition](#filtrations-stopping-times-and-intuition)
  - [Observable events](#observable-events)
  - [Stopping times w.r.t natural filtration](#stopping-times-wrt-natural-filtration)
  - [Stopping time w.r.t general filtration](#stopping-time-wrt-general-filtration)
- [Appendix](#appendix)
  - [Concepts](#concepts)
  - [References](#references)
<!-- /TOC -->

# Filtrations, stopping times, and intuition
**Scenario**.
* *Assumptions*.
    * $(\Omega, \mathcal{F}, P)$ is a probability space
    * $\{X_n\}_{n\in\mathbb{N}}$ is a stochastic process on $(\Omega, \mathcal{F}, P)$, where $n$ denotes time
* *Objective*. Capture the information we get from observing the process up to time $n$
    * *Indistinguishable outcomes*. If $\omega,\omega'\in\Omega$ satisfies $X_i(\omega)=X_(\omega')$ for all $i\leq n$

        $\to$ We cannot distinguish $\omega$ from $\omega'$ based on our observations up to time $n$
    * *Consequence*. We want to make a decision at time $n$ based on our observations so far

        $\to$ The prediction has to be the same in case $\omega$ as in case $\omega'$

## Observable events
**Indistinguishable outcomes**. $\omega,\omega'\in\Omega$ are indistinguishable at time $n$ if $X_i(\omega)=X_i(\omega')$ for all $i\leq n$
* *Notations*. 
    * If $\omega$ and $\omega'$ are indistinguishable then we write $\omega\sim_n\omega'$
    * The set of all $\omega'$, which are indistinguishable from $\omega$ at time $n$ is denoted as

        $$[\omega]_n=\{\omega'\in\Omega:\omega'\sim_n\omega\}$$

**Observable event**. An event $A\in\mathcal{F}$ is observable at time $n$ if whenever $\omega\in A$, then $[\omega]_n\subseteq A$

$\to$ If $\omega\in A$, all $\omega'$ indistinguishable from $\omega$ at time $n$ are also in $A$
* *Interpretation*. "An event $A\in\mathcal{F}$ is observable at time $n$" means that we can decide whether an $\omega\in\Omega$ belongs to $A$ by looking at the observations $X_1(\omega),\dots,X_n(\omega)$
    * *Proof*. If there exists some $\omega'\in[\omega]_n$ so that $\omega'\notin A$, when we observe $x=X_i(\omega)=X_i(\omega')$ for some $i\leq n$

        $\to$ We cannot tell if $X^{-1}(x)$ belongs to $A$ or not, hence cannot tell if $A$ occurred or not
* *Intuition*. $A$ is observable if for all $\omega\in A$, the occurence of $X_i(\omega)$ for some $i\leq n$ implies the occurrence of $A$

**Observable events and $\sigma$-algebra**. The events which are observable at time $n$ form a $\sigma$-algebra, which is denoted by $\mathcal{A}_n$
* *Prove that $\emptyset\in\mathcal{A}_n$*. This is obvious
* *Prove that $\mathcal{A}_n$ is closed under complementation*. Assume that there is some $\omega\in A^C$ so that $[\omega]_n\cap A\neq \emptyset$

    $\to$ By definition of $A$, we have that $[\omega]_n\in A$ means $\omega\in A$, leading to contradiction
* *Prove that $\mathcal{A}_n$ is closed under countable union*. Consider $A=\bigcup_{k\in\mathbb{N}} A_k$
    * If $\omega\in A$ then $\omega\in A_k$ for some $k\in\mathbb{N}$
    * Since $A_k\in\mathcal{A}_n$, we have that $[\omega]_n\subseteq A_k$, hence $[\omega]_n\in A$

**Sequence of observable events at time $n$**. $\{\mathcal{A}_n\}_{n\in\mathbb{N}}$ is an increasing sequence of $\sigma$-algebra, and $X_n$ is $\mathcal{A}_n$-measurable for all $n$

## Stopping times w.r.t natural filtration
**Idea of stopping time**. Stopping time is a decision we can make based on the information we have available at the time

$\to$ If $T(\omega)=n$ and $\omega'\sim_n\omega$, we should also have $T(\omega')=n$, i.e. $T=n$ is observable at everytime $n$
* *Explain*. At time $n$, we cannot distinguish between $\omega$ and $\omega'$

**Stopping time**.
* *Assumption*. $T:\Omega\to\mathbb{N}\cup\{\infty\}$ is a random variable
* *Conclusion*. If whenever $T(\omega)=n$ and $\omega'\sim_n\omega$ then $T(\omega')=n$
    
    $\to$ $T$ is a stopping time w.r.t $\{\mathcal{A}_n\}$
* *Interpretation*. $T$ is a stopping time w.r.t $\{\mathcal{A}_n\}$ if $\{\omega:T(\omega)=n\}$ is observable

    $\to$ In other words, $\{T=n\}\in\mathcal{A}_n$ for all $n\in\mathbb{N}$
    * *Explain*. Consider the event $E=\{\omega:T(\omega)=n\}$, we have that if whenever $\omega\in E$ then $[\omega]_n\in E$

        $\to$ $E$ is observable
* *Drawback*. This definition makes perfect sense for the filtration $\mathcal{A}_n$, but it is hard to generalize to other filtrations

**Reformulated definition of stopping time**. A random variable $T:\Omega\to\mathbb{N}\cup\{\infty\}$ is a stopping time if and only if

$$\forall n\in\mathbb{N},\{\omega:T(\omega)\leq n\}\in\mathcal{A}_n$$
* *Proof*. Since $\{\mathcal{A}_n\}$ is an increasing sequence, and 
    
    $$\forall n\in\mathbb{N},\{\omega:T(\omega)=n\}\in\mathcal{A}_n$$

* *Interpretation*. $T$ is a stopping time w.r.t $\{\mathcal{A}_n\}$ if $\{T\leq n\}\in\mathcal{A}_n$, i.e. we know at time $n$ that the stopping moment has happened or not

**Observable event at stopping time**. The $\sigma$-algebra $\mathcal{A}_T$ generated by a stopping $T$ consists of sets, which are observable at time $T$, i.e.
* *Assumptions*. $T$ is an $\{A_n\}$-stopping time
* *Conclusion*. If whenever $T(\omega)=n$ and $\omega\in A$ then $[\omega]_n\subseteq A$
    
    $\to$ An event $A$ is observable at $T$

* *Notation*. $\mathcal{A}_T$ denotes the collection of all sets observable at $T$

**Observable event at stopping time and $\sigma$-algebra**. $\mathcal{A}_T$ is a $\sigma$-algebra

**Theorem**. The following definition of $\mathcal{A}_T$ is easier to generalize to other filtrations
* *Assumptions*. $T$ is an $\{A_n\}$-stopping time
* *Conclusion*. $A\in\mathcal{A}_T$ if and only if

    $$\forall n\in\mathbb{N},A\cap\{\omega:T(\omega)\leq n\}\in\mathcal{A}_n$$ 

**Conclusion**.
* We have introduced a natural filtration $\{\mathcal{A}_n\}$
* We have defined stopping times and $\sigma$-algebras generated by stopping times in ways that make intuitive sense

## Stopping time w.r.t general filtration
**Definition of stopping time w.r.t more general filtration**.
* *Filtration $\{\mathcal{F}_n\}$*. An increasing sequence of $\sigma$-algebras so that

    $$\forall n\in\mathbb{N},\mathcal{F}_n\subseteq\mathcal{F}$$

* *Assumptions*.
    * $\{\mathcal{F}_n\}$ is a filtration
    * $T:\Omega\to\mathbb{N}\cup\{\infty\}$
* *Conclusion*. $T$ is a stopping time w.r.t $\{\mathcal{F}_n\}$ if and only if

    $$\forall n\in\mathbb{N},\{\omega:T(\omega)\leq n\}\in\mathcal{F}_n$$

**$\sigma$-algebra generated by a stopping time**.
* *Assumptions*.
    * $\{\mathcal{F}_n\}$ is a filtration
    * $T:\Omega\to\mathbb{N}\cup\{\infty\}$ is a stopping time w.r.t $\{\mathcal{F}_n\}$
* *$\sigma$-algebra $\mathcal{F}_T$ generated by $T$*. Consist of all events $A$ so that

    $$\forall n\in\mathbb{N},A\cap\{\omega:T(\omega)\leq n\}\in\mathcal{F}_n$$

# Appendix
## Concepts
**Realization of a random variable**. The result of applying the random variable $X$, i.e. a function, to an observed outcome $\omega$ of a random experiment

**Adapted process (or non-anticipating or non-anticipative process)**. A process which cannot see into the future
* *Assumptions*.
    * $(\Omega, \mathcal{F}, \mathbb{P})$ is a probability space
    * $I$ is an index set with total order $\leq$, which is often $\mathbb{N},\mathbb{N}_0,[0,T],[0,+\infty)$F
    * $\mathbb{F}=(\mathcal{F}_i)_{i\in I}$ is a filtration of $\mathcal{F}$
    * $(S,\Sigma)$ is a measurable space, i.e. the state space
    * $X:I\times \Omega\to S$ is a stochastic process
* *Conclusion*. $X$ is adapted to the filtration $(\mathcal{F}_i)_{i\in I}$ if the random variable $X_i:\Omega\to S$ is a $(\mathcal{F}_i,\Sigma)$-measurable function for each $i\in I$
* *Interpretation*. $X$ is adapted if and only if, for every realization $X=x$ and every $n$, $X_n$ is known at time $n$

## References
* https://www.uio.no/studier/emner/matnat/math/STK-MAT3710/h19/stkmat3710stoppingtimes.pdf