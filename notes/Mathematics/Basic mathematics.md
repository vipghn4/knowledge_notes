<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Mathematical distance](#mathematical-distance)
  - [Introduction](#introduction)
  - [Definition](#definition)
- [Mathematical function](#mathematical-function)
  - [Introduction](#introduction-1)
  - [Definition](#definition-1)
    - [Formal definition](#formal-definition)
    - [Relational approach](#relational-approach)
    - [Cartesian product approach](#cartesian-product-approach)
    - [Notations of functions](#notations-of-functions)
  - [Function specification](#function-specification)
  - [Function space](#function-space)
- [Mathematical proof - from Wikipedia](#mathematical-proof---from-wikipedia)
  - [Introduction](#introduction-2)
  - [Methods](#methods)
    - [Direct proof](#direct-proof)
    - [Mathematical induction](#mathematical-induction)
    - [Proof by contraposition](#proof-by-contraposition)
    - [Proof by contradiction](#proof-by-contradiction)
    - [Proof by construction](#proof-by-construction)
    - [Proof by exhaustion](#proof-by-exhaustion)
    - [Non-constructive proof](#non-constructive-proof)
<!-- /TOC -->

# Mathematical distance
## Introduction
**Metric (or distance) function**: a function which defines a distance between each pair of elements in a set

**Metric space**: a set with a metric

**Metrizable topological space**: topological space whose topology can be described by a metric

## Definition
**Metric on a set $X$**: a function $d: X \times X \to [0, \infty)$ satisfying the axioms below
* Separation axiom: $d(x, y) \geq 0$ $\forall x, y \in X$
* Identity of indiscernibles: $d(x, y) = 0 \leftrightarrow x = y$
* Symmetry: $d(x, y) = d(y, x)$ $\forall x, y$
* Triangle inequality: $d(x, y) \leq d(x, z) + d(z, y)$

**Ultrametric**: a metric $d$ satisfying $d(x, z) \leq \max [d(x, y), d(y, z)]$ $\forall x, y, z$
* Explain: points can never fall between other points

**Intrinsic metric**: a metric $d$ where any $x, y \in X$ can be joined with a curve with length arbitrarily close to $d(x, y)$

# Mathematical function
## Introduction
**Function**: a relation between sets, which associates to every element of a first set exactly one element of the second set
* Formal: a process, or a relation, which associates each $x \in X$ to a single $y \in Y$
    * Domain: $X$
    * Co-domain of the function: $Y$
    * Range of $f$: $\{f(x):x \in \textbf{dom } f\}$
* Notation: $y = f(x)$ - read as "value of $f$ of $x$"
    * Argument (or input) of $f$: $x$
    * Value (or output) of $f$: $y$
        * Another name: the image of $x$ by $f$ 

>**NOTE**: the domain and co-domain aren't always explocitly given when a function is defined, and, without some computation, one knows only that the domain is contained in a larger set
* Example: when refer to $f: X \to Y$ in mathematical analysis, we often refer a function whose domain is a proper subset of $X$ as domain

**History**: functions were originally the idealization of how a varying quantity depends on another quantity

**Graph of a function $f$**: $\{(x, f(x)):x \in \textbf{dom } f\}$

## Definition
### Formal definition
**Formal definition**: a function $f: X \to Y$ is defined by a set $G$ of ordered pairs $(x, y)$ where 
* $x \in X$ and $y \in Y$
* For every $x \in X$ is the first component of exactly one ordered pair in $G$

**Map (or mapping)**: another name of "function"
* Differences between a function and a map (proposed by some author): map is a function with some sort of special structure (e.g. maps of manifolds)

**Function equality**: 
* Assumptions:
    * $f: X \to Y$
    * $g: X \to Y$
* Conclusion: $f = g$ if $f(x) = g(x)$ $\forall x \in X$

### Relational approach
**Binary relation between $X$ and $Y$**: any subset of the Cartesian product $X \times Y$
* Notation: $R \subseteq X \times Y$
* Converse relation: $R^T \subseteq Y \times X$

**Univalent (or functional) relation**: a relation $R$ so that $(x, y) \in \textbf{R} \land (x, z) \in \textbf{R} \implies y = z$ $\forall x \in X$ and $y, z \in Y$
* Identifying univalent relation: use functions with co-domain $Y$ and domain $\tilde{X} \subseteq X$

**Total relation**: a relation $R$ so that $\forall x \in X, \exists y \in Y: (x, y) \in R$

**Function**: 
* Functions: relations, which are both univalent and total
* Partial function: relations, which are not total but univalent

### Cartesian product approach
**Function as an element of a Cartesian product over a domain**:
* Assumptions:
    * $X, Y$ are two domains
* Conclusion: any $f: X \to Y$ is an element of $\prod_X Y = Y^X$
    * Explain: an element of the Cartesian product of copies of $Y$s over $X$
    * Intuition: for each $x \in X$, $f$ picks some $y \in Y$, namely $f(x)$

### Notations of functions
**Functional notation**: $y = f(x)$

**Arrow notation**: 
* "to" notation: $f: X \to Y$ or $X \overset{f}{\to} Y$
* "map to" notation: $x \mapsto f(x)$

**Index notation**: $f_x$

**Dot notation**: $f(\cdot)$

## Function specification
**By listing function values**: given $X = \{x_1, ..., x_n\}$, $f: X \to Y$ is defined by $f(x_i) = y_i$

**By a formula (closed form)**: $f(x) = \sqrt{1 + x^2}$
* Advantage: allow computing $f(x)$ from any $x \in X$
* Drawback: 
    * The determination of $\textbf{dom } f$ is sometimes difficult
    * Sometimes, $f$ cannot be expressed in a closed form

**Inverse and implicit functions**:
* Bijective function: $f: X \to Y$ where for every $y \in Y$, there's only one $x \in X$ so that $y = f(x)$
* Inverse function of bijective function $f$: $f^{-1}: Y \to X$ where maps $y \in Y$ to $x \in X$ where $y = f(x)$
* Inverse of non-bijective function $f$: 
    * Step 1: choose $E \subseteq X$ and $F \subseteq Y$ so that $f$ is a bijection from $E$ to $F$
    * Step 2: inverse $f$ according to $E$ and $F$
* Implicit function:
    * Assumptions:
        * $R$ is a binary relation between $X$ and $Y$
        * $E \subseteq X$ so that $\forall x \in E, \exists y \in Y, x R y$
            * $x R y$ means $x$ corresponds to $y$ w.r.t $R$
    * Conclusion: if we have a criteria allowing selecting such $y$ for every $x \in E$

    $\hspace{1.0cm} \rightarrow$ This defines $f: E \to Y$ called "implcit function"
    * Interpretation: $f$ is implicitly defined by $R$

**Using differential calculus**: define $f$ as the anti-derivative of another function $g$

**By recurrence**:
* Sequences: functions whose domain are non-negative integers
* Example: $f(n) = f(n-1) + f(n-2)$ (i.e. Fibonacci numbers)

## Function space
**Function space**: a set of scalar-valued or vector-valued functions, which share a specific property and form a topological vector space

# Mathematical proof - from Wikipedia
## Introduction
**Theorems and axioms**:
* Theorems: previously established statements used for proof
* Axioms: basic or original assumptions, which can be used to construct proof

**Conjecture and hypothesis**:
* Conjecture: an unproven proposition, which is believed to be true
* Hypothesis: the proposition, which is frequently used as an assumption to build upon similar mathematical work

**Reasoning**:
* Deductive reasoning: the process of reasoning from one or more statements to reach a logically certain conclusion
* Inductive reasoning: the process of reasoning from one or more truths about the conclusion, based on some given evidence

## Methods
### Direct proof
**Direct proof**: established by logically and straightforward combining the axioms, definitions, and earlier theorems, without making any further assumptions

**Example**:
* Assumptions:
    * $x = 2 a$
    * $y = 2 b$
* Task: prove that $x + y$ is even
* Solution: since $x$ is even, $y$ is even, then $x + y$ is even

### Mathematical induction
**Mathematical induction**:
* Idea:
    * A single "base case" is proved
    * An "induction rule" is proved that establishes that any arbitrary case implies the next case
* Generalization: originally mathematical induction is working as chain structure (i.e. given $P(n)$ is true, then prove $P(n+1)$ is true)
    * Structural: use tree-like structure (i.e. like dynamic programming on tree)
* Applications: correctness proof in Computer Science

**Variations**:
* Induction basis other than $0$ and $1$: base case starts at some $n \notin \{0, 1\}$
* Induction on more than one counter: like state dynamic programming
* Prefix induction: in the inductive step, prove $\forall k, (P(k) \to P(2k) \land P(2k+1))$
    * Another interpretation: $\forall k, (P(\lfloor \frac{k}{2} \rfloor) \to P(k))$
    * "prefix": each step proves something about a number, from something about the "prefix" of that number
    * Variation: $\forall k, (P(\lfloor \sqrt{k} \rfloor) \to P(k))$
* Complete (strong) induction: prove $P(m+1)$ under the assumption that $P(n)$ holds for $n < m+1$
    * Weak form: prove $P(m+1)$ under the assumption that $P(m)$ holds
* Forward-backward induction: prove that $P(n-1)$ is true, given $P(n)$ is true
* Transfinite induction: applied to well-ordered sets
    * Zero case: prove $P(0)$ is true
    * Successor case: prove $P(m+1)$ is true, given $P(m)$ is true and $P(n)$ for all $n < m$ (if needed)
    * Limit case: prove that, for any limit ordinal $\lambda$, $P(\lambda)$ follows from $P(m)$ for all $m < \lambda$

### Proof by contraposition
**Contraposition**: prove "if $P$ then $Q$" by showing that "if not $Q$ then not $P$"

### Proof by contradiction
**Proof by contradiction**: establish the truth of a proposition, by showing that assuming the proposition to be false leads to a contradiction
* Commented by "G. H. Hardy": one of a mathematician's finest weapons

### Proof by construction
**Proof by construction**: construct a concrete example, with a property to show that something having that property exists

### Proof by exhaustion
**Proof by exhaustion**: divide the main statement into a finite number of cases and prove each one separately

### Non-constructive proof
**Non-constructive proof**: prove a certain mathematical object with a certain property exists, without explaining how the object is found