<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [$\sigma$-algebra and probability assignment](#sigma-algebra-and-probability-assignment)
  - [Abstract measure spaces](#abstract-measure-spaces)
  - [Boolean algebra and $\sigma$-algebra](#boolean-algebra-and-sigma-algebra)
    - [$\sigma$-algebra](#sigma-algebra)
    - [Generated $\sigma$-algebra](#generated-sigma-algebra)
    - [Borel $\sigma$-algebra](#borel-sigma-algebra)
  - [Measure theory](#measure-theory)
    - [Measure and measurability](#measure-and-measurability)
    - [Lebesgue measure](#lebesgue-measure)
    - [Vitali set as an example of non-Lebesgue-measurable](#vitali-set-as-an-example-of-non-lebesgue-measurable)
  - [Probability assignment](#probability-assignment)
- [Appendix](#appendix)
  - [Concepts](#concepts)
<!-- /TOC -->

# $\sigma$-algebra and probability assignment
## Abstract measure spaces
**Requirements for definition of measure and integration on a general space $X$**.
* The set $X$ itself
* A collection $\mathcal{B}$ of subsets of $X$, which one is allowed to measure

    $\to$ $\mathcal{B}$ must obey a number of axioms, which make it a $\sigma$-algebra
* The measure $\mu(E)\in[0,\infty)$ one assigns to each measurable set $E\in\mathcal{B}$
    
    $\to$ $\mu$ must obey a number of axioms, i.e. most notably, a countable additivity axiom, to obtain a measure and integration theory comparable to Lebesgue theory on Euclidean spaces

**Measure space**. $(X,\mathcal{B}, \mu)$

$\to$ This has much the same role as vector spaces in abstract linear algebra

## Boolean algebra and $\sigma$-algebra
### $\sigma$-algebra
**Boolean algebra of sets**. A subset of semi-ring
* *Boolean algebra of sets*. A collection of sets $F$ is an algebra if
    * $\emptyset \in F$
    * If $A\in F$ then $A^C\in F$, i.e. closed under complementation
    * If $A,B\in F$ then $A\cup B\in F$, i.e. closed under pairwise
* *Interpretation*. Boolean algebra of a set is closed under two basic Boolean operations, i.e. complement (NOT) and finite union (OR)

    $\to$ Using the law of Boolean algebra, a Boolean algebra is also closed under other Boolean algebra operations, e.g. intersection (AND), set difference, and symmetric difference (XOR)

**$\sigma$-algebra (or $\sigma$-field)**. A stronger variant of Boolean algebra
* *Definition*. A class $\mathcal{A}$ satisfying
    * $\emptyset \in {\mathcal{A}}$
    * If $A_1, A_2, ... \in {\mathcal{A}}$ then $\bigcup_i A_i \in {\mathcal{A}}$
    * $A \in {\mathcal{A}}$ implies $A^c \in {\mathcal{A}}$
* *Terminology*.
    * *"$\sigma$"*. Indicate that the considered system of sets is closed under countable union
        * *Explain*. $\sigma$ [=Greek "s"] comes from the German words Summe, whose English translation is sum
    * *"Algebra"*. Closure under set operations
* *Motivations*.
    * *From Boolean algebra*. To obtain a measure and integration theory, which can cope well with limits

        $\to$ The finite union axiom of a Boolean algebra is insufficient
    * *From measure theory*. $\sigma$-algebra are closed under operations which one would expect for measurable sets
        * The complement of a measurable set is a measurable set
        * The countable union of measurable sets is a measurable set
* *Usage**. The collections of subsets, for which a given measure is defined, is necessarily a $\sigma$-algebra

**Relationship to Boolean algebra**. 
* $\sigma$-algebra is a special case of algebra, which must be closed under countably infinite unions, rather than pairwise unions
    * *Explain*. Closure under pairwise union does not necessarily imply closure under countable union
* Hence, we can treat algebra as surely being closure under finite union, and $\sigma$-algebra takes a further step by being closure under countable union

    $\to$ $\sigma$-algebra is required when dealing with more complicated systems, when closure under countable union is required
* We sticks with countable since it is very expressive and easy to deal with

**References**.
* https://www.quora.com/Why-do-we-need-sigma-algebra-to-define-measure
* http://www.stat.rice.edu/~dobelman/courses/texts/qualify/Measure.Theory.Tao.pdf

### Generated $\sigma$-algebra
**Intersection of $\sigma$-algebras**.
* *Assumptions*.
    * $X$ is a set
    * $I$ is an index set which is possibly infinite or uncountable
    * $A_\alpha$ is a $\sigma$-algebra for all $\sigma\in I$
* *Conclusion*. $A = \bigcap_{\alpha\in I}A_\alpha$ is a $\sigma$-algebra
* *Proof*. We have $X\in A$ is obvious and $A$ is closed under complement

    $\to$ It suffices to prove that $A$ is closed under countable union
    * Consider a sequence $\{S_n\}_{n\in\mathbb{N}}$ of subsets of $X$, where $S_n\in A$ for all $n\in\mathbb{N}$
    * Due to the definition of $\sigma$-algebra, we have that

        $$\forall \alpha\in I,\bigcup_{n\in\mathbb{N}} S_n\in A_\alpha$$
    
    * Hence, we have that $\bigcup_{n\in\mathbb{N}} S_n\in A$

**$\sigma$-algebra generated by $F$**.
* *Assumptions*. Let $F$ be an arbitrary family of subsets of $X$
* *Conclusion*. There exists a unique smallest $\sigma$-algebra containing every set in $F$, even if $F$ may or may not itself be a $\sigma$-algebra

    $\to$ This is the intersection of all $\sigma$-algebras containing $F$, and is denoted as $\sigma(F)$
* *Sample space and event*. The collection of possible events $\Sigma$, given the sample space $\Omega$, is the $\sigma$-algebra generated by $\Omega$

### Borel $\sigma$-algebra
**Borel $\sigma$-algebra**. The smallest $\sigma$-algebra holding every open set, i.e. the $\sigma$-algebra generated by the open sets
* *Generation of Borel $\sigma$-algebra*. The Borel $\sigma$-algebra on $\mathbb{R}$ is generated by any of the following collections of intervals

    $$\{(-\infty,b):b\in\mathbb{R}\},\quad \{(-\infty,b]:b\in\mathbb{R}\},\quad \{(a, \infty):a\in\mathbb{R}\},\quad \{[a,\infty):a\in\mathbb{R}\}$$

    * *Proof*.

**Measurability of real-valued functions**. The properties given in the following proposition are sometimes taken as the definition of a measurable function
* *Assumptions*. $(X,\mathcal{A})$ is a measurable space
* *Conclusion*. $f:X\to\mathbb{R}$ is measurable if and only if one of the following conditions holds
    
    $$\begin{aligned}
    \forall b\in\mathbb{R},\{x\in X:f(x)<b\}\in\mathcal{A}\\ 
    \forall b\in\mathbb{R},\{x\in X:f(x)\leq b\}\in\mathcal{A}\\
    \forall a\in\mathbb{R},\{x\in X:f(x)>a\}\in\mathcal{A}\\
    \forall a\in\mathbb{R},\{x\in X:f(x)\geq a\}\in\mathcal{A}
    \end{aligned}$$

## Measure theory
### Measure and measurability
**A measure on a set**. A systematic way to assign a number to each suitable subset of the set
* *Formal*. 
    * *Assumptions*.
        * $f: X \to [0, \infty)\cup \{\infty\}$ is a function
        * ${\mathcal{X}}$ is where $f$ is defined on 
        * $X$ is the set of certain subsets of ${\mathcal{X}}$, which form a $\sigma$-algebra over $\mathcal{X}$
    * *Conclusion*. $f$ is a measure if the following holds
        * *Non-negativity*. $f(x) \geq 0$ $\forall x \in X$
        * *Null empty set*. $f(\emptyset) = 0$
        * *Countable additivity (or $\sigma$ additivity)*. For all countable collections $\{x_k\}_{k=1}^\infty$ of pairwise disjoint sets in $X$

            $$f(\bigcup_k x_k) = \sum_k f(x_k)$$

* *Interpretation*. A measure on a set is assigning sizes to subsets of the set

**Measurability**. The sets in a $\sigma$-field ${\mathcal{A}}$ are measurable
* *Measurable sets*. Members of ${\mathcal{A}}$
* *Measurable space*. $(\Omega, {\mathcal{A}})$ is a measurable space
    * *Explain*. $\Omega$ and a $\sigma$-algebra defined on it
    * *Other notation*. $(\Omega, {\mathcal{A}}, f)$ where $f$ is the measure function
        * *Example*. probability space is a measurable space with a probability measure
* *Measurable map*. A random variable $X$ is a measurable map $X: \Omega \to \textbf{R}$
    * *Explain*. $\{\omega:X(\omega) \leq x\} \in {\mathcal{A}}$ $\forall x$

**Common types of measure**.
* *Counting measure*. The counting measure of a set is the cardinity of that set

    $\to$ All sets are measurable w.r.t the counting measure
    * *Explain*. 
        * The finite sets have as measure the number of elements
        * The infinite sets have measure $\infty$
* *Outer measure*. A measure which exhibits monotonicity
    * *Assumptions*. $X$ is a set with power set $\mathcal{P}(X)$
    * *Outer measure on $X$*. A mapping $\mu:\mathcal{P}(X)\to\mathbb{R}_{++}\cup\{\infty\}$ satisfying
        * *Null empty set*. $\mu(\emptyset)=0$
        * *Monotonicity*. 
            
            $$\forall A,B\in\mathcal{P}(X):A\subseteq B\implies\mu(A)\leq \mu(B)$$
        
        * *Countable subadditivity*. For all sequences $\{A_i\}_{i\in\mathbb{N}}\in\mathcal{P}(X)$

            $$\mu(\bigcup_{i=1}^\infty A_i)\leq \sum_{i=1}^\infty \mu(A_i)$$
* *Probability measure*. A measure $\mu$ on the measurable space $(S,\mathcal{S})$, where $\mu(S)=1$
* *Finite measure*. A measure $\mu$ on the measurable space $(S,\mathcal{S})$, where $\mu(S)<\infty$

### Lebesgue measure
**Lebesgue measure**. A standard way of assigning a measure to subsets of $n$-dimensional Euclidean space

$\to$ For $n=1,2,3$, it coincides with length, area, and volume
* *Lebesgue measure*.
    * *Assumptions*.
        * $l(I)=b-a$ is the length of any interval $I=[a,b]$ or $I=(a,b)$ in $\mathbb{R}$
        * For any subset $E\subseteq\mathbb{R}$, $\{I_k\}_{k\in\mathbb{N}}$ is a sequence of open intervals with

            $$E\in\bigcup_{k=1}^\infty I_k$$

    * *Lebesgue outer measure of $E$*.

        $$\lambda^*(E)=\inf\{\sum_{k=1}^\infty l(I_k)\}$$

* *Lebesgue measure and $\sigma$-algebra*. Given a $\sigma$-algebra $\Sigma$, the Lebesgue measure of any $E\in\Sigma$ is defined as

    $$\lambda(E)=\lambda^*(E)$$

* *Lebesgue-measurable set*. A set which can be assigned a Lebesgue measure

**Null set**. A subset $S\subseteq\mathbb{R}^n$ is a null set if, for every $\epsilon>0$, $S$ can be covered with countably many products of $n$ intervals, whose total volume is at most $\epsilon$

$\to$ A null set represents the concept of zero measure
* *Countable set and null set*. Any countable set is a null set
    * *Proof*. 
        * Let $S=\{s_0,s_1,s_2,\dots\}$ be a countable set, and define the $n$th cover interval as

            $$I_n=[s_n-\frac{\epsilon}{2^{n+2}},s_n+\frac{\epsilon}{2^{n+2}}]$$
        
            where $l(I_n)=\frac{\epsilon}{2^{n+1}}$
        
        * The length of the entire cover interval is given as

            $$l(I)=\sum_{i=1}^\infty l(I_i) \approx \frac{\epsilon}{2}$$
        
        * Since $S\subset I$, we have that

            $$l(A)<l(I)<\epsilon$$
* *Uncountable set and null set*. An uncountable set may not be a null set, e.g. consider $I=[-1,1]=\bigcup_{x\in[-1,1]} \{x\}$

### Vitali set as an example of non-Lebesgue-measurable
**Axiom of choice**.
* *Choice function (or selector, or selection)*. A function $f$ defined on a collection $X$ of non-empty sets so that

    $$\forall A\in X,f(A)\in A$$

* *Axiom of choice*. For any set $X$ of non-empty sets, there exists a choice function $f$ defined on $X$, which maps each set $A\in X$ to an element of the set
* *Interpretation*. Given any collection of bins, each containing at least one object

    $\to$ It is possible to make a selection of exactly one object from each bin, even if the collection is infinite

**Vitali set**. A subset $V$ of the interval $[0,1]$ of real numbers so that for each $r\in\mathbb{R}$, there exists exactly one $v\in V$ so that $v-r\in\mathbb{Q}$

>**NOTE**. There are uncountably many Vitali sets

* *Construction of a Vitali set*.
    * *Equivalence relation*. Consider the relation

        $$x\sim y\Leftrightarrow x-y\in\mathbb{Q}$$
        
        $\to$ This relation partitions $\mathbb{R}$ into equivalence classes
    * *Equivalence class*. $a,b$ belong to the same equivalence class if and only if $a\sim b$
    * *Construction of Vitali set*. By the axion of choice, we can select a representative of each single class

        $\to$ The Vitali set $V$ is the set of all selected representatives
* *Measurability*. A Vitali set is an elementary example of set of real numbers, which is not Lebesgue-measurable, i.e.
    * Let $\mathbb{Q}_{[-1,1]}=\mathbb{Q}\cap[-1,1]=\{q_1,q_2,\dots\}$ and

        $$\forall k=1,2,\dots,V_k=V+q_k=\{v:v+q_k:v\in V\}$$
    
    * We have that $V_1,V_2,\dots$ are pairwise disjoint, and

        $$[0,1]\subseteq\bigcup_k V_k\subseteq[-1,2]$$

        hence

        $$1\leq \sum_{k=1}^\infty \lambda(V_k)\leq 3$$
    
    * Since $\lambda(V_k)=\lambda(V)$ due to the translation invariance of Lebesgue measure, we have

        $$1\leq \sum_{k=1}^\infty \lambda(V)\leq 3$$

        which is impossible, since summing infinitely many copies of $\lambda(V)$ yields either $0$ or infinity depending on the value of $\lambda(V)$

## Probability assignment
**Assignment of probabilities**. It is not feasible to assign probabilities to all subsets of a sample space $\Omega$
* *Bad solution*. Restrict the class of valid measures
* *Good solution*. Restrict attention to a set of events called $\sigma$-algebra (or $\sigma$-field)

**Probability space**. $(\Omega, {\mathcal{A}}, P)$ is a probability space

>**NOTE**. The set of events must be a $\sigma$-algebra
>* *Explain*. Otherwise, they cannot be assigned a probability

# Appendix
## Concepts
**Countable set**. A set $S$ is countable if there exists an one-to-one function $f:S\to\mathbb{N}$ where $\mathbb{N}=\{0,1,2,\dots\}$
* *Explain*. Every in $S$ has the correspondence to a different element in $\mathbb{N}$

**Borel $\sigma$-field**. The smallest $\sigma$-field which contains all the open subsets of the real line

**Power set of a set $S$**. The set of all subsets of $S$, including $\emptyset$ and $S$
* *Axiom of power set*. Given any set $X$, there is a set $\mathcal{P}(x)$ so that

    $$\forall z,[z\in\mathcal{P}(x)\Leftrightarrow \forall w \in Z,w\in X]$$