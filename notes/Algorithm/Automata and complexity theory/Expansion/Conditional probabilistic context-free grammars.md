<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Conditional probabilistic context-free grammars](#conditional-probabilistic-context-free-grammars)
  - [Introduction](#introduction)
  - [CPCFGs](#cpcfgs)
    - [Definition](#definition)
    - [Features](#features)
  - [Inference](#inference)
    - [Parsing](#parsing)
    - [Computing $Z(x)$](#computing-zx)
- [Appendix](#appendix)
  - [Concepts](#concepts)
<!-- /TOC -->

# Conditional probabilistic context-free grammars
## Introduction
**Conditional probabilistic context-free grammars (CPCFGs)**. A discriminative framework for learning distributions over parse trees of context-free languages

**Statistical parsing models**.
* *Generative models*. Estimate the joint distribution $p(t, x)$ over parse trees $t$ and strings $x$
* *Discriminative models*. We are not interested in generating strings $x$, i.e. given a string $x$, we want to find the most likely parse 
    
    $$t^∗ = \arg\max_t p(t|x)$$
        
    * *Consequence*. It suffices to estimate $p(t|x)$, i.e. a discriminative model 

**Drawbacks of generative models**.
* Generative models often have difficulty incorporating arbitrary, overlapping features of the input, e.g. including capitalization, word suffixes, and semantic features from WordNet
    
    $\to$ In a discriminative model, incorporating such features is easier, i.e. we do not have to model their distribution
    * *Consequence*. Discriminatively-trained models have outperformed generatively-trained models in several tasks, including part-of-speech tagging and noun-phrase segmentation
* In generative models, much effort is spent on smoothing, with the best-performing techniques often using complex interpolation or backoff schemes that require hand tuning
    * *Smoothing*. Combining probabilities from distributions that use different evidence
    * *Smoothing in log-linear model*. Accomplished simply by adding features of various specificity
        
        $\to$ The weights are determined in the course of the maximum likelihood estimation

**Previous works on discriminative parsing**. Aim to achieve the advantages of discriminative parsing by training a chain of classifiers to make the decisions needed by a parser
* *Drawbacks*. Using a chain of classifiers raises a label bias issue
    * *Label bias*. Since each classifier in the chain is trained separately
        
        $\to$ Earlier classifiers cannot adjust their weights to avoid mistakes that become apparent later in the sequence
* *Solution with random fields*. RFs avoid this since their training takes into account a global normalization factor
    
    $\to$ This factor implicitly causes weights for earlier decisions to be affected by later decisions

## CPCFGs
### Definition
**Conditional probabilitstic context-free grammars (CPCFGs)**. A context-free grammar annotated with features and weights on each production
* *Weights of a CPCFG*. Consider a parse tree $t$
    * *Node weights*. Every node $v \in t$ is assigned a weight, computed from 
        * The features and weights of the production used to expand $v$, and
        * The terminal sequence that $v$ spans
    * *Tree weights*. The weight of the entire tree $t$ is the product of the weight of all its nodes, and the tree’s probability $p(t|x)$ is its weight, normalized over all legal parse trees for $\mathbf{x}$
* *Features of a CPCFG*. 
    * *Production feature*. Each production $N^p \to N^sN^t$ is annotated with 
        * A set of feature functions $\{f_k(N^p , N^sN^t , \mathbf{x}, i, j)\}$, and
        * Associated real-valued weights $\{\lambda_k\}$
    * *Feature function $f_k$*. Take as input a production and a segment of the sentence, and return some feature of the parse tree spanning $x_{i:j}$ using the production $N^p \to N^sN^t$
    * *Function weight $\lambda_k$*. A real number indicating how much $f_k$ should contribute to the weight of the production as a whole
        
        $\to$ High weights mean that a production is more likely

**Node weights from features**. The weight of a node $v\in t$ with children $\text{ch}(v)$ is computed from the features and weights as

$$w(v,t)=\exp\{\sum_k\lambda_kf_k(v,\text{ch}(v), \text{span}(v))\}$$

where $\text{span}(v)$ is the portion of $\mathbf{x}$ spanned by $v$

**Inference with CPCFGs**.
* *Intuition*. Writing a derivation for a CFG with a rewrite rule, i.e. we pay a cost equal to the negative of the logarithm of the weight

    $\to$ The most likely tree in the CPCFG corresponds to the minimum cost derivation
* *Probability of a parse tree $t$ given a string $\mathbf{x}$ in a CPCFG $G$*.
    
    $$p(t|\mathbf{x})\propto \prod_{v\in t}\exp\{\sum_k\lambda_kf_k(v,\text{ch}(v),\text{span}(v))\}$$

### Features
**Brief**. One of the main potential advantages of CPCFGs is their potential to include arbitrary features of the current context and the input string

## Inference
**Main algorithmic problems for CPCFGs**.
* Finding the most likely parse of a string $\mathbf{x}$
* Computing the normal factor $Z(\mathbf{x})$

### Parsing
**Parsing problem for CPCFGs**. Given a sentence $\mathbf{x}$, find the most likely parse tree $t^*=\arg\max_t p(t|\mathbf{x})$
* *Assumptions*.
    * $\mathcal{T}(p,i,j)$ is the set of all parse trees for $\mathbf{x}_{i:j}$ starting with $N^p$
    * For every nonterminal $N^p$ and every $\mathbf{x}_{i:j}$, the weight of the most likely tree $N^p\overset{*}{\implies}\mathbf{x}_{i:j}$ is given as

        $$b_p(i,j)=\max_{t\in\mathcal{T}(p,i,j)}\prod_{v\in t}\exp\{\sum_k\lambda_kf_k(v,\text{ch}(v),\text{span}(v))\}$$

* *Algorithm idea*. We can compute $b$ efficiently to yield $b_1(1,m)=w(t^*)$
    * Consider expanding $N^p$ using some production $N^p\to N^qN^r$
        
        $\to$ $w(t)$ is the cost for using that production, times the weight of the subtrees, i.e. like CKY algorithm
    * Hence, we can maximize over all possible expansions in turn

### Computing $Z(x)$
**Idea**. Use Inside algorithm as for PCFGs

# Appendix
## Concepts
* https://homepages.inf.ed.ac.uk/csutton/publications/cscfg.pdf