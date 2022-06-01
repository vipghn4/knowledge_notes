<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Probabilistic context-free grammars](#probabilistic-context-free-grammars)
  - [Introduction](#introduction)
  - [Probabilistic context-free grammars (PCFGs)](#probabilistic-context-free-grammars-pcfgs)
    - [Basic definitions](#basic-definitions)
    - [Definition of PCFGs](#definition-of-pcfgs)
    - [Deriving a PCFG from a corpus](#deriving-a-pcfg-from-a-corpus)
    - [Parsing with PCFGs](#parsing-with-pcfgs)
      - [Parsing using the CKY algorithm](#parsing-using-the-cky-algorithm)
      - [Iside algorithm for summing over trees](#iside-algorithm-for-summing-over-trees)
- [Appendix](#appendix)
  - [References](#references)
<!-- /TOC -->

# Probabilistic context-free grammars
## Introduction
Ambiguity is an astonishingly severe problem for natural languages. When
researchers first started building reasonably large grammars for languages such as
English, they were surprised to see that sentences often had a very large number
of possible parse trees: it is not uncommon for a moderate-length sentence (say 20
or 30 words in length) to have hundreds, thousands, or even tens of thousands of
possible parses.

## Probabilistic context-free grammars (PCFGs)
### Basic definitions
**Basic definitions**. Consider a CFG $G=(V,\Sigma,R,S)$
* *Assumptions*.
    * $\mathcal{T}_G$ is the set of all possible left-most derivations, i.e. parse trees, under $G$
    * For any derivation $t\in\mathcal{T}_G$, $\text{yield}(t)$ is the string $s\in\Sigma^*$, which is the yield of $t$
    * For any $s\in\Sigma^*$, $\mathcal{T}_G(s)$ denotes the set

        $$\{t:t\in\mathcal{T}_G\land \text{yield}(t)=s\}$$

* *Ambiguous sentence*. $s$ is ambiguous if $|\mathcal{T}_G(s)|>1$
* *Grammatical sentence*. $s$ is grammatical if $|\mathcal{T}_G(s)|>0$

**Key idea in PCFGs**. Extend the definition of CFGs to give a probability distribution over possible derivations
* *Formal idea*. Define a distribution over parse trees $p(t)$ so that

    $$\forall t\in\mathcal{T}_G,p(t)\geq 0,\quad \sum_{t\in\mathcal{T}_G} p(t)=1$$

* *Motivation*. Each parse tree $t$ is a complex tree, and $\mathcal{T}_G$ can be infinite

    $\to$ However, there is a very simple extension to CFGs allowing us to define $p(t)$
* *Needs for PCFGs*. Once we have a function $p(t)$, we have a ranking over $t\in\mathcal{T}_G(s)$, i.e. given any $s\in\Sigma^*$, we can return

    $$\arg\max_{t\in\mathcal{T}_G(s)} p(t)$$

    as the output from our parser
    * *Consequence*. $p(t)$ is an effective way of dealing with ambiguity

**Problems of interest**.
* *Modeling*. How to define $p(t)$
* *Training*. How to learn the parameters of our model of $p(t)$ from training examples
* *Inference*. Given $s\in\Sigma^*$, how to parse (or decode) $s$, i.e. 

    $$\arg\max_{t\in\mathcal{T}_G(s)} p(t)$$

### Definition of PCFGs
**PCFGs**. PCFGs assumes that parse trees are generated stochastically
* *PCFG*. A PCFG $(V,\Sigma,R,S,q)$ consists of
    * A CFG $G=(V,\Sigma,R,S)$
    * A parameter $q(\alpha\to\beta)$ for each rule $\alpha\to\beta\in R$
        * *Interpretation*. Given that the non-terminal being expanded is $\alpha$
            
            $\to$ $q(\alpha\to\beta)$ is the conditional probability of choosing $\alpha\to\beta$ in a left-most derivation
        * *Constraints on $q(\alpha\to\beta)$*.

            $$\sum_{(\alpha\to\beta)\in R:\alpha=X}q(\alpha\to\beta)=1,\quad \forall(\alpha\to\beta)\in R,q(\alpha\to\beta)\geq 0$$

* *Probability of $t$ under the PCFG*.

    $$p(t)=\prod_{i=1}^n q(\alpha_i\to\beta_i)$$

### Deriving a PCFG from a corpus
**Formulation of PCFG from a corpus**. 
* *Training data*. Consider a training data, i.e. a set of parse trees $t_1,\dots,t_m$ satisfying 
    * Each $t_i$ is a sequence of context-free rules
    * Each $t_i$ has $S$ at its root, i.e. starting symbol
* *Formulation of PCFG*. A PCFG $(V,\Sigma,R,S,q)$ where
    * $V$ is the set of all non-terminals seen in $t_1,\dots,t_m$
    * $\Sigma$ is the set of all words seen in $t_1,\dots,t_m$
    * $S$ is the start symbol
    * $R$ is the set of all rules $\alpha\to\beta$ seen in $t_1,\dots,t_m$
* *Maximum-likelihood parameter estimates*.
    
    $$q_{ML}(\alpha\to\beta)=\frac{\text{Count}(\alpha\to\beta)}{\text{Count}(\alpha)}$$

### Parsing with PCFGs
**CKY algorithm**. A dynamic programming algorithm for finding

$$\arg\max_{t\in\mathcal{T}(s)} p(t)$$

given a PCFG in Chomsky normal form (CNF)

#### Parsing using the CKY algorithm
**Overview of CKY algorithm**.
* *Inputs*. A PCFG $G=(V,\Sigma,R,S,q)$ in CNF, and a sentence $s=x_1\dots x_n$ of words
* *Outputs*. 
    
    $$\arg\max_{t\in\mathcal{T}_G(s)} p(t)$$

* *Key definitions*.
    * For a given sequence $x_1\dots x_n$ and $X\in V$, $\mathcal{T}(i,j,X)$ is the set of all parse trees for words $x_i\dots x_j$, where $X$ is the root of the tree
    * $\pi(i,j,X)=\max_{t\in\mathcal{T}(i,j,X)} p(t)$ and $\pi(i,j,X)=0$ if $\mathcal{T}(i,j,X)=\emptyset$

        $\to$ $\pi(i,j,X)$ is the highest score for any parse tree dominating words $x_i\dots x_j$ with root $X$
    * The score for a tree $t$ containing rules $\alpha_1\to\beta_1,\dots,\alpha_m\to\beta_m$ is given as

        $$p(t)=\prod_{i=1}^m q(\alpha_i\to\beta_i)$$
* *Key observation*. We can use a recursive definition of $\pi$, which allows a simple bottom-up dynamic programming algorithm
    * *Dynamic programming idea*. Fill $\pi(i,j,X)$ for the cases where $i=j$, then the cases where $j=i+1$, and so on

**CKY algorithm**.
* *Base case*. For all $i=1\dots n$, and for all $X\in V$

    $$\pi(i,i,X)=\begin{cases}
    q(X\to x_i)& X\to x_i\in R\\
    0&\text{otherwise}
    \end{cases}$$

* *Recursive definition*. For all $(i,j)$, where $1\geq i<j\geq n$, and for all $X\in V$

    $$\pi(i,j,X)=\max_{X\to YZ\in R,s\in\{i\dots (j-1)\}} [q(X\to YZ)\cdot \pi(i,s,Y)\cdot\pi(s+1,j,Z)]$$

    * *Interpretation*. Try all possibilities of splitting $x_i\dots x_j$ into subtrees
* *Backpointer*. For all $(i,j,X)$, $\text{bp}(i,j,X)$ stores the split-point $s$ leading to the highest scoring parse tree

    $\to$ This allows recovery of the highest scoring parse tree for the sentence

#### Iside algorithm for summing over trees
**Brief**. This section describes an algorithm, called inside algorithm, which sums the probabilities for all parse trees for a given sentence

$\to$ This is used to calculate the probability of the sentence under the PCFG

**Inside algorithm**. Similar to CKY algorithm, with maximum replaced by summation

# Appendix
## References
* http://www.cs.columbia.edu/~mcollins/courses/nlp2011/notes/pcfgs.pdf