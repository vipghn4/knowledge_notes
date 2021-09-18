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
* Pairwise Markov property: $X_u$ and $X_v$ are conditionally independent given all other variables
* Local Markov property: $X_u$ is conditionally independent of all other variables given its neighbors
* Global Markov property: any two subsets of variables are conditionally independent given a separating subset

# Conditional random field (CRF)
## Introduction
**Conditional random field**: a class of statistical modeling method used in for structured prediction in pattern recognition

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

**Parameter learning**: $\theta$ is learned by maximizing $P(Y_i|X_i; \theta)$ (i.e. maximum likelihood learning)