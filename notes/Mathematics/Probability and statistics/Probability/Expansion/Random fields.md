<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Background](#background)
- [Markov random field (MRF)](#markov-random-field-mrf)
  - [Introduction](#introduction)
  - [Definition](#definition)
- [Conditional random field (CRF)](#conditional-random-field-crf)
  - [Introduction](#introduction-1)
  - [Description](#description)
  - [Variants](#variants)
<!-- /TOC -->

# Background
**Random field**: a random function defined on a set of points in a multi-dimensional space (e.g. graph, image, etc.)
* Another definition: a stochastic process indexed by a spatial variable

# Markov random field (MRF)
## Introduction
**Markov random field**: a set of random variables having a Markov property described by an undirected graph
* Other names:
    * Markov network
    * Undirected graphical model

**Comparison from Bayesian network**:
* Similarity: both use the same representation of dependencies
* Differences: 
    * Bayesian networks are directed and acyclic
    * Markov networks are undirected and maybe cyclic

**Gibbs random field**: Markov random field when the joint probability density of the random variables is strictly positive

## Definition
**Markov random field**:
* Assumptions:
    * $G = (V, E)$ is an undirected graph
    * $X = \{X_v\}_{v \in V}$ is a set of random variables
* Markov random field: $X$ form a Markov random field w.r.t $G$ if $X$ satisfy the local Markov properties

**Local Markov properties**:
* Pairwise Markov property: $X_u$ and $X_v$ are conditionally independent given all other variables if they are non-adjacent
    * *Formula*. $X_u \perp X_v | X_{V\setminus\{u,v\}}$
* Local Markov property: $X_u$ is conditionally independent of all other variables given its neighbors
    * *Formula*. $X_v\perp X_{V\setminus N[v]}|X_{N(v)}$
        * $N(v)$ is the set of neighbors of $v$
        * $N[v] = v\cup N(v)$ is the closed neighborhood of $v$
* Global Markov property: any two subsets of variables are conditionally independent given a separating subset
    * *Formula*. $X_A\perp X_B | X_S$ where every path from a node in $X$ to a node in $B$ passes through $S$

# Conditional random field (CRF)
## Introduction
**Conditional random fields (CRFs)**. A class of statistical modeling methods often applied in pattern recognition and machine learning and used for structured prediction
* *Advantages over traditional classifier models*. 
    * A traditional classifier predicts a label for a single sample without considering neighbouring samples
    * A CRF can take context into account
* *Idea*. The predictions are modelled as a graphical model, which represents the presence of dependencies between the predictions
    
    >**NOTE**. What kind of graph is used depends on the application

* *Examples*. 
    * In natural language processing, linear chain CRFs are popular, for which each prediction is dependent only on its immediate neighbours
        * *Reference*. https://pages.cs.wisc.edu/~jerryzhu/cs838/CRF.pdf
    * In image processing, the graph typically connects locations to nearby and/or similar locations to enforce that they receive similar predictions

## Description
**Conditional random field**:
* Assumptions:
    * $\textbf{X}$ are the observations
    * $\textbf{Y}$ are the random variables
    * $G = (V, E)$ is a graph such that $\textbf{Y} = \{\textbf{Y}_v\}_{v \in V}$
    * $w \sim v$ means $w$ and $v$ are neighbors in $G$
* Conditional random field on $\textbf{X}$ and $\textbf{Y}$: $(\textbf{X}, \textbf{Y})$ when $\textbf{Y}_v$, conditioned on $\textbf{X}$, obey the Markov property w.r.t $G$
    * Formal: $P(\textbf{Y}_v|\textbf{X}, \textbf{Y}_w, w \neq v) = P(\textbf{Y}_v|\textbf{X}, \textbf{Y}_w, w \sim v)$
* Interpretation: a CRF is an undirected graphical model (i.e. Bayesian network) whose nodes can be divided into exactly two disjoint sets $\textbf{X}$ and $\textbf{Y}$
    * Observed variables: $\textbf{X}$
    * Output variables: $\textbf{Y}$

**Inference**. Basically the same as for an MRF and the same arguments hold

>**NOTE**. For general graphs, the problem of exact inference in CRFs is intractable

* *Feasibility of CRF inference*. There exist special cases for which exact inference is feasible
    * If the graph is a chain or a tree, message passing algorithms yield exact solutions
        
        $\to$ The algorithms are analogous to the forward-backward and Viterbi algorithm for the case of HMMs
    * If the CRF only contains pair-wise potentials and the energy is submodular, combinatorial min cut/max flow algorithms yield exact solutions
    * If exact inference is impossible, several algorithms can be used to obtain approximate solutions

Loopy belief propagation
Alpha expansion
Mean field inference
Linear programming relaxations

**Parameter learning**: $\theta$ is learned by maximizing $P(Y_i|X_i; \theta)$ (i.e. maximum likelihood learning)

## Variants
**Higher-order CRFs and semi-Markov CRFs**.
* *Higher-order CRFs*. CRFs can be extended into higher order models by making $Y_i$ dependent on a fixed number $k$ of previous variables $Y_{i-k},\dots,Y_{i-1}$ 

    $\to$ Training and inference are only practical for small values of $k$, e.g. $k\leq 5$
    * *Explain*. The computational costr increases exponentially with $k$
* *Semi-Markov CRF (semi-CRF)*. Model variable-length segmentations of the label sequence $Y$

**Latent-dynamic CRF (LDCRF)**. A type of CRFs for sequence tagging tasks
* *Assumptions*.
    * $\mathbf{x}=(x_1,\dots,x_n)$ are observations
    * $\mathbf{y}=(y_1,\dots,y_n)$ are labels
    * $\mathbf{h}$ are random latent variables
* *Chain rule of probability*. $P(\mathbf{y}|\mathbf{x})=\sum_{\mathbf{h}} P(\mathbf{y}|\mathbf{h},\mathbf{x}) P(\mathbf{h}|\mathbf{x})$

    $\to$ This allows capturing latent structure, between the observations and labels