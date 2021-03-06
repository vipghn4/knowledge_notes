<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Neural machine translation by jointly learning to align and translate](#neural-machine-translation-by-jointly-learning-to-align-and-translate)
  - [Background - Neural machine translation](#background---neural-machine-translation)
    - [RNN encoder-decoder](#rnn-encoder-decoder)
  - [Learning to align and translate](#learning-to-align-and-translate)
    - [Decoder - General description](#decoder---general-description)
    - [Encoder - Bidirectional RNN for annotating sequences](#encoder---bidirectional-rnn-for-annotating-sequences)
  - [Results](#results)
- [Appendix](#appendix)
  - [References](#references)
<!-- /TOC -->

# Neural machine translation by jointly learning to align and translate
**Neural machine translation**. A newly emerging approach to machine translation
* *Objective*. Build and train a single, large neural network that reads a sentence and outputs a correct translation

**Recently proposed neural machine translation models**. Belong to a family of encoder-decoders
* *Variations*.
    * *Option 1*. Use an encoder and a decoder for each language
    * *Option 2*. Use a language-specific encoder applied to each sentence, whose outputs are then compared
* *Network architecture*. 
    * An encoder neural network reads and encodes a source sentence into a fixed-length vector
    * A decoder then outputs a translation from the encoded vector
* *Training algorithm*. The whole encoder–decoder system, which consists of the encoder and the decoder for a language pair, is jointly trained to maximize the probability of a correct translation given a source sentence
* *Drawback*. A neural network needs to be able to compress all the necessary information of a source sentence into a fixed-length vector
    
    $\to$ This may make it difficult for the neural network to cope with long sentences, especially those that are longer than the sentences in the training corpus
    * *Evidences*.
        * Cho et al. (2014b) showed that indeed the performance of a basic encoder-decoder deteriorates rapidly as the length of an input sentence increases

**Proposed approach**. Use an extension of the encoder–decoder model, which learns to align and translate jointly
* *Idea*. Each time the proposed model generates a word in a translation
    1. It soft-searches for a set of positions in a source sentence, where the most relevant information is concentrated
    2. The model predicts a target word based on the context vectors associated with these source positions and all the previous generated target words

**Most important difference from previous approaches**. This approach does not attempt to encode a whole input sentence into a single fixed-length vector
* *Explain*. It encodes the input sentence into a sequence of vectors
    
    $\to$ It then chooses a subset of these vectors adaptively while decoding the translation
* *Consequence*. A neural translation model is freed from having to squash all the information of a source sentence, regardless of its length, into a fixed-length vector

## Background - Neural machine translation
**Translation under a probabilistic perspective**. Translation is equivalent to finding a target sentence $y$  maximizing the conditional probability of $y$ given a source sentence $x$

$$\arg\max_y p(y|x)$$

* *Neural machine translation*. 
    * *Training phase*. A parameterized model is used to maximize $p(y|x)$ using a parallel training corpus

        $\to$ The distribution $p(y|x)$ is learned by a translation model
    * *Inference phase*. Given a source sentence, a corresponding translation can be generated by searching for the sentence maximizing the $p(y|x)$

### RNN encoder-decoder
**RNN encoder-decoder - By Cho et al. (2014a)**.
* *Encoder*. Read the input sentence, i.e. a sequence of vectors $\mathbf{x}=(x_1,\dots,x_{T_x})$, into a vector $c$

    $\to$ The most common approach uses an RNN, i.e.
    * *Assumptions*.
        * $h_t\in\mathbb{R}^n$ is a hidden state at time $t$
        * $c$ is a vector generated from the sequence of $h_t$
        * $f$ and $q$ are non-linear functions
    * *Network architecture*. Sutskever et al. (2014) used an LSTM as $f$ and $q$

        $$h_t=f(x_t,h_{t-1}),\quad c=q(\{h_1,\dots,h_{T_x}\})$$

* *Decoder*. Trained to predict the next word $y_{t'}$, given the context vector $c$ and previously predicted words, i.e. $\{y_1,\dots,y_{t'-1}\}$
    * *Assumptions*.
        * $\mathbf{y}=(y_1,\dots,y_{T_y})$ is the translation
        * $g$ is a nonlinear, potentially multi-layered, function
        * $s_t$ is the hidden state of the RNN
    * *Idea*. The decoder defines a probability over $\mathbf{y}$ as

        $$p(\mathbf{y}) = \prod_{t=1}^T p(y_t|\{y_1,\dots,y_{t-1}\}, c)$$
    
    * *Network architecture*. With an RNN, each conditional probability is given as

        $$p(y_t|\{y_1,\dots,y_{t-1}, c\}) = g(y_{t-1}, s_t, c)$$

## Learning to align and translate
### Decoder - General description
**Model architecture**.
* *RNN hidden state*. $s_i=f(s_{i-1}, y_{i-1}, c_i)$
* *Conditional probability*. $p(y_i|y_1,\dots,y_{i-1}, \mathbf{x}) = g(y_{i-1}, s_i, c_i)$

**Context vector $c_i$**. Depend on a sequence of annotations $(h_1,\dots,h_{T_x})$, to which an encoder maps the input sequence
* *Annotation $h_i$*. Contain information about the whole input sequence with a strong focus on the parts surrounding the $i$-th word of the input sequence
* *Formulation*.

    $$c_i=\sum_{j=1}^{T_x} a_{ij} h_j$$

    where $a_{ij}$ is given as

    $$a_{ij}=\frac{\exp(e_{ij})}{\sum_{k=1}^{T_x} \exp(e_{ik})},\quad e_{ij}=a(s_{i-1}, h_j)$$

* *Alignment model $a$*. Score how well the inputs around position $j$ and the output at position $i$ match
    * *Network architecture*. A feedforward neural network, which is jointly trained with all the other components of the proposed system
    * *Difference from traditional machine translation*. In this model, the alignment is not a latent variable

        $\to$ It directly computes a soft alignment allowing the gradient of the cost function to be backpropagated through
* *Interpretation*. Taking a weighted sum of all the annotations can be seen as computing an expected annotation  over possible alignments

### Encoder - Bidirectional RNN for annotating sequences
**Model architecture**. A BiRNN consisting of a forward and a backward RNN
* *Forward RNN*. Read the input sequence in order and calculate a sequence of forward hidden states $\overset{\rightarrow}{h}_1,\dots,\overset{\rightarrow}{h}_{T_x}$
* *Backward RNN*. Read the input sequence in order and calculate a sequence of backward hidden states $\overset{\leftarrow}{h}_1,\dots,\overset{\leftarrow}{h}_{T_x}$
* *Annotation for $x_j$*. $h_j=[\overset{\rightarrow}{h}_j^T;\overset{\leftarrow}{h}_j^T]^T$

    $\to$ $h_j$ contains the summaries of the words around $x_j$

## Results
**Quantitative results**. The translation performances are measured in BLEU score

**Qualitative results**. 
* *Alignment visualization*. Sample alignments, i.e. annotation weights $a_{ij}$, are visualized
* *Long sentences*. Sample input-output pairs are shown

# Appendix
**Paper information**.
* *Authors*. KyungHyun Cho and Yoshua Bengio∗
* *Year of publication*. 2015

## References
* https://arxiv.org/pdf/1409.0473.pdf
* https://arxiv.org/pdf/1406.1078.pdf