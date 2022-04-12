<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Attention is all you need](#attention-is-all-you-need)
  - [Background](#background)
  - [Model architecture](#model-architecture)
    - [Encoder and decoder stacks](#encoder-and-decoder-stacks)
    - [Attention](#attention)
      - [Scaled dot-product attention](#scaled-dot-product-attention)
      - [Multihead attention](#multihead-attention)
      - [Applications of attention in the model](#applications-of-attention-in-the-model)
    - [Position-wise feed-forward networks](#position-wise-feed-forward-networks)
    - [Embeddings and softmax](#embeddings-and-softmax)
    - [Positional encoding](#positional-encoding)
  - [Why self-attention](#why-self-attention)
- [Appendix](#appendix)
<!-- /TOC -->

# Attention is all you need
## Background
**Recurrent models for sequential computation**. Recurrent models typically factor computation along the symbol positions of the input and output sequences

$\to$ This inherently sequential nature precludes parallelization within training examples, which becomes critical at longer sequence lengths, as memory constraints limit batching across examples

**Convolution for sequential computation**. The goal of reducing sequential computation forms the foundation of the Extended Neural GPU, ByteNet and ConvS2S
* *Idea*. Use convolutional neural networks as basic building block
    
    $\to$ This enables computing hidden representations in parallel for all input and output positions
* *Drawback*. The number of operations required to relate signals from two arbitrary input or output positions grows in the distance between positions
    * *Example*. The number of operations grows linearly for ConvS2S and logarithmically for ByteNet
        
        $\to$ It is difficult to learn dependencies between distant positions

**Self-attention (or intra-attention)**. An attention mechanism relating different positions of a single sequence to compute a representation of the sequence
* *Usage*. Reading comprehension, abstractive summarization, textual entailment and learning task-independent sentence representations

**End-to-end memory networks**. Based on a recurrent attention mechanism instead of sequencealigned recurrence

$\to$ This have been shown to perform well on simple-language question answering and language modeling tasks

## Model architecture
<div style="text-align:center">
    <img src="https://i.imgur.com/cY5afMx.png">
    <figcaption>Transformer model architecture</figcaption>
</div>

**Encoder-decoder architecture**. The Transformer follows this overall architecture using stacked self-attention and point-wise, fully connected layers for both the encoder and decoder
* *Encoder*. Map an input sequence of symbol representations $(x_1,\dots,x_n)$ to a sequence of continuous representations $\mathbf{z}=(z_1,\dots,z_n)$
* *Decoder*. Given $\mathbf{z}$, generate an output sequence $(y_1,\dots,y_m)$ of symbols one element at a time

    $\to$ At each step the model is auto-regressive, consuming the previously generated symbols as additional input when generating the next

### Encoder and decoder stacks
**Encoder**. Composed of a stack of $N = 6$ identical layers, each of which has two sub-layers
* *Sub-layers*.
    1. A multi-head self-attention mechanism
    2. A simple, positionwise fully connected feed-forward network
    3. A residual connection is used around each of the two sub-layers, followed by layer normalization
* *Formal architecture*. The output of each sub-layer is

    $$\text{LayerNorm}(x + \text{Sublayer}(x))$$
    
    where $\text{Sublayer}(x)$ is the function implemented by the sub-layer

* *Layer output dimension*. To facilitate these residual connections
    
    $\to$ All sub-layers in the model, as well as the embedding layers, produce outputs of dimension $d_\text{model} = 512$

**Decoder**. Composed of a stack of $N = 6$ identical layers
* *Layer architecture*. In addition to the two sub-layers in each encoder layer
    
    $\to$ The decoder inserts a third sub-layer performing multi-head attention over the output of the encoder stack
    * *Residual connection*. Similar to the encoder, we employ residual connections around each of the sub-layers, followed by layer normalization
    * *Modified self-attention for masking*. The self-attention sub-layer in the decoder stack is modified to prevent positions from attending to subsequent positions
        * *Purposes*. Ensure that the predictions for position $i$ can depend only on the known outputs at positions less than $i$

### Attention
<div style="text-align:center">
    <img src="https://i.imgur.com/CRCvPP2.png">
    <figcaption>Attention layer architecture</figcaption>
</div>

**Attention function**. A mapping a query and a set of key-value pairs to an output, where the query, keys, values, and output are all vectors
* *Output calculation*. The output is computed as a weighted sum of the values, where the weight assigned to each value is computed by a compatibility function of the query with the corresponding key

#### Scaled dot-product attention
**Scaled dot-product attention**.
* *Assumptions*.
    * $d_k$ is the dimension of input queries and input keys
    * $d_v$ is the dimension of input values
* *Output matrix calculation*.

    $$\text{Attention}(Q,K,V)=\text{softmax}(\frac{Q K^T}{\sqrt{d_k}}) V$$

**Comparison with other attention formulations**.
* *Dot-product attention*. $\text{score}(\boldsymbol{s}_t, \boldsymbol{h}_i) = \boldsymbol{s}_t^\top\boldsymbol{h}_i$

    $\to$ This is idential to the proposed method, except for the scaling factor $\frac{1}{\sqrt{d_k}}$
* *Additive attention*. $\text{score}(\boldsymbol{s}_t, \boldsymbol{h}_i) = \mathbf{v}_a^\top \tanh(\mathbf{W}_a[\boldsymbol{s}_t; \boldsymbol{h}_i])$

    $\to$ Attention scores are computed using a feed-forward network with a single hidden layer
* *Comparison between additive and dot-product attention*. 
    * Dot-product attention is much faster and more space-efficient in practice
        * *Explain*. It can be implemented using highly optimized matrix multiplication code
    * Additive attention outperforms dot-product attention witout scaling for large values of $d_k$
        * *Explain*. We suspect that for large $d_k$, the dot product grow large in magnitude

            $\to$ The softmax is pushed into regions with extremely small gradients
* *Conclusion*. We use dot-product attention scaled by $\frac{1}{\sqrt{d_k}}$
    * *Intuition*. $\TODO$

#### Multihead attention
**Multihead attention**. Instead of performing a single attention function with $d_\text{model}$-dimensional keys, values and queries

$\to$ It is found beneficial to linearly project the queries, keys and values $h$ times with different, learned linear projections to $d_k$, $d_k$ and $d_v$ dimensions
* *Parallel attention on projections*. On each of these projected versions of queries, keys and values 
    
    $\to$ We perform the attention function in parallel, yielding $d_v$-dimensional output values
* *Ouptut combination*. The $d_v$-dimensional outputs are concatenated and projected
    
    $\to$ Resulting in the final values
* *Purposes*. Allow the model to jointly attend to information from different representation
subspaces at different positions

**Formulation**.
* *Assumptions*.
    * $W_i^Q\in\mathbb{R}^{d_\text{model}\times d_k}, W_i^K\in\mathbb{R}^{d_\text{model}\times d_k}, W_i^V\in\mathbb{R}^{d_\text{model}\times d_v}$ are parameter matrices
    * $W_i^O\in\mathbb{R}^{hd_v\times d_\text{model}}$ is a parameter matrix
* *Formulation*.

    $$\begin{aligned}
    \text{MultiHead}(Q,K,V)&=\text{Concat}(\text{head}_1,\dots,\text{head}_h) W^O\\
    \text{head}_i(Q,K,V)&=\text{Attention}(QW_i^Q,KW_i^K, VW^V_i)
    \end{aligned}$$

* *Experiment settings*. 
    * $h=8$ is used
    * $d_k=d_v=d_\text{model}/h=64$ is used

#### Applications of attention in the model
**Applications of attention in the model**. The Transformer uses multi-head attention in three different ways
* In "encoder-decoder attention" layers, the queries come from the previous decoder layer, and the memory keys and values come from the output of the encoder
    
    $\to$ This allows every position in the decoder to attend over all positions in the input sequence
    * *Analogy to previous work*. This mimics the typical encoder-decoder attention mechanisms in sequence-to-sequence models
* The encoder contains self-attention layers
    
    $\to$ In a self-attention layer all of the keys, values and queries come from the same place, i.e. the output of the previous layer in the encoder
    * *Consequence*. Each position in the encoder can attend to all positions in the previous layer of the encoder
* Self-attention layers in the decoder allow each position in the decoder to attend to all positions in the decoder up to and including that position
    
    $\to$ We need to prevent leftward information flow in the decoder to preserve the auto-regressive property
    * *Implementation*. Implement inside of scaled dot-product attention by masking out, i.e. setting to $-\infty$, all values in the input of the softmax corresponding to illegal connections

### Position-wise feed-forward networks
**Position-wise feed-forward networks**. Each of the layers in our encoder and decoder contains a fully
connected feed-forward network, which is applied to each position separately and identically
* *Formulation*.

    $$\text{FFN}(x)=\max\{0,xW_1+b_1\}W_2 + b_2$$

* *Parameter sharing*. While the linear transformations are the same across different positions
    
    $\to$ They use different parameters from layer to layer
* *Interpretation*. This is a layer of two convolutions with kernel size 1.
* *Experiment settings*. The dimensionality of input and output is $d_\text{model} = 512$, and the inner-layer has dimensionality df $f = 2048$

### Embeddings and softmax
**Word embeddings**. We use learned embeddings to convert the input tokens and output tokens to vectors of dimension $d_\text{model}$

**Softmax**. We use the usual learned linear transformation and softmax function to convert the decoder output to predicted next-token probabilities

**Parameter sharing**. We share the same weight matrix between the two embedding layers and the pre-softmax
linear transformation

**Weight scaling**. In the embedding layers, we multiply those weights by $\sqrt{d_\text{model}}$
* *Intuition*. $\TODO$

### Positional encoding
**Motivation**. Since our model contains no recurrence and no convolution, in order for the model to make use of the
order of the sequence

$\to$ We must inject some information about the relative or absolute position of the tokens in the sequence

**Positional encoding**. Added to the input embeddings at the bottoms of the encoder and decoder stacks
* *Dimensionality*. Have the same dimension $d_\text{model}$ as the embeddings, i.e. the two can be summed
* *Choice of positional encoding*. There are many choices of positional encodings, learned and fixed
    
    $\to$ In this work, we use sine and cosine functions of different frequencies

    $$\begin{aligned}
    \text{PE}(\text{pos}, 2i)&=\sin(\text{pos}/1000^{2i/d_\text{model}})\\
    \text{PE}(\text{pos}, 2i+1)&=\cos(\text{pos}/1000^{2i/d_\text{model}})\\
    \end{aligned}$$

    where $\text{pos}$ and $i$ are the dimension
* *Assumption*. 
    * We hypothesized it would allow the model to easily learn to attend by relative positions
        * *Explain*. For any fixed offset $k$, $\text{PE}_{\text{pos} + k}$ can be represented as a linear function of $\text{PE}_\text{pos}$
    * We chose the sinusoidal version since it may allow the model to extrapolate to sequence lengths longer than the ones encountered during training

**Experiment results**. Experiments show that learned positional embeddings produced nearly identical results as fixed positional embeddings

## Why self-attention
**Desiderata of self-attention compared with convolution and recurrent networks**. Total complexity per layer, amount of computation which can be parallelized, and the path length between long-range dependencies

**Path length between long-range dependencies**. Learning long-range dependencies is a key challenge in many sequence transduction tasks
* *Key factor affecting the ability to learn dependencies*. The length of the paths forward and backward signals have to traverse in the network
    
    $\to$ The shorter these paths between any combination of positions in the input and output sequences, the easier it is to learn long-range dependencies
* *Self-attention layer*. Connect all positions with a constant number of sequentially executed operations
* *Recurrent layer*. Require $O(n)$ sequential operations

**Computational complexity**. Self-attention layers are faster than recurrent layers when the sequence
length $n$ is smaller than the representation dimensionality $d$

$\to$ This is most often the case with sentence representations used by state-of-the-art models in machine translations
* *Local self-attention*. To improve computational performance for tasks involving very long sequences
    
    $\to$ Self-attention could be restricted to considering only a neighborhood of size $r$ in the input sequence centered around the respective output position
    * *Consequence*. This would increase the maximum path length to $O(n/r)$

**Interpretability**. Self-attention could yield more interpretable models
* *Explain*. We can inspect attention distributions from our models

# Appendix
**Paper information**.
* *Authors*. Google Brain
* *Year of publication*. 2017