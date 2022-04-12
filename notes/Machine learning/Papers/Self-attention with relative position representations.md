<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Self-attention with relative position representations](#self-attention-with-relative-position-representations)
  - [Proposed architecture](#proposed-architecture)
    - [Relation-aware self-attention](#relation-aware-self-attention)
    - [Relative position representations](#relative-position-representations)
- [Appendix](#appendix)
<!-- /TOC -->

# Self-attention with relative position representations
**Positional encoding in RNNs**. RNNs typically compute a hidden state $h_t$ , as a function of their input $x_t$ and a previous hidden state $h_{t−1}$

$\to$ This captures relative and absolute positions along the time dimension directly through their sequential structure

**Positional encoding in non-recurrent models**. Do not necessarily consider input elements sequentially

$\to$ These models require explicitly encoding position information to be able to use sequence order

**Positional encoding in Transformer**. For the Transformer, without convolution nor recurrence, incorporating explicit representations of position information is an especially important consideration
* *Explain*. Otherwise, the model is entirely invariant to sequence ordering
    
    $\to$ Attention-based models have therefore used position encodings or biased attention weights based on distance

**Relative positional encoding in Transformer**. In this work we present an efficient way of incorporating relative position representations in the self-attention mechanism
* *Experimental results*. Even when entirely replacing its absolute position encodings
    
    $\to$ The approach results in significant improvements in translation quality on two machine translation tasks

**Generalization**. Our approach can be cast as a special case of extending the self-attention mechanism to considering arbitrary relations between any two input elements

## Proposed architecture
**Self-attention scoring function**. Use scaled dot-product attention

$$e_{ij}=\frac{(x_i W^Q) (x_j W^K)^T}{\sqrt{d_z}}$$

and the attention attention weights are given as

$$\alpha_{ij}=\frac{\exp e_{ij}}{\sum_{k=1}^n \exp e_{ik}}$$

### Relation-aware self-attention
**Brief**. We propose an extension to self-attention to consider the pairwise relationships between input elements

**Input modeling**. We model the input as a labeled, directed, fully-connected graph
* *Graph edge*. The edge between input elements $x_i$ and $x_j$ is represented by vectors $a_{ij}^V, a_{ij}^K\in\mathbb{R}^{d_a}$
    * *Motivation for learning two distinct edge representations*. $a^V_{ij}$ and $a^K_{ij}$ are suitable for use in the following equations, without requiring additional linear transformations.
* *Parameter sharing*. These representations can be shared across attention heads
* *Experiment settings*. We use $d_a = d_z$

**Modified output element**. 

$$z_i=\sum_{j=1}^n a_{ij} (x_j W^V + a^V_{ij})$$


* *Usage*. Important for tasks, where information about the edge types selected by a given attention head is useful to downstream encoder or decoder layers

**Modified attention score**.

$$e_{ij}=\frac{x_i W^Q (x_j W^K + a^K_{ij})^T}{\sqrt{d_z}}$$

* *Motivation for simple addition for edge incorporation*. Enable efficient implementation

### Relative position representations
**Relative position representations**. For linear sequences, edges can capture information about the relative position differences between input elements
* *Maximum relative position*. The maximum relative position we consider is clipped to a maximum absolute value of $k$
    * *Explain*. 
        * We hypothesized that precise relative position information is not useful beyond a certain distance
        * Clipping the maximum distance enables the model to generalize to sequence lengths not seen during training
    * *Conclusion*. We consider $2k + 1$ unique edge labels
* *Position representation*.

    $$\begin{aligned}
    a^K_{ij}&=w^K_{\text{clip}(j-i,k)}\\
    a^V_{ij}&=w^V_{\text{clip}(j-i,k)}\\
    \text{clip}(x,k)&=\max\{-k,\min\{k,x\}\}
    \end{aligned}$$

    where $w^K=(w^K_{-k},\dots,w_k^K)$ and $w^V=(w^V_{-k}, \dots, w^V_k)$ are learnable parameters with $w_i^K,w_i^V\in\mathbb{R}^{d_a}$

# Appendix
**Paper information**.
* *Authors*. Google
* *Year of publication*. 2018