<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Learning phrase representations using RNN encoder-decoder for statistical machine translation](#learning-phrase-representations-using-rnn-encoder-decoder-for-statistical-machine-translation)
  - [Related work](#related-work)
    - [Learning to align](#learning-to-align)
    - [Neural networks for machine translation](#neural-networks-for-machine-translation)
  - [RNN encoder-decoder](#rnn-encoder-decoder)
    - [Recurrent neural networks](#recurrent-neural-networks)
    - [RNN encoder-decoder](#rnn-encoder-decoder-1)
    - [Hidden unit which adaptively remembers and forgets](#hidden-unit-which-adaptively-remembers-and-forgets)
  - [Statistical machine translation](#statistical-machine-translation)
    - [Scoring phrase pairs with RNN encoder-decoder](#scoring-phrase-pairs-with-rnn-encoder-decoder)
- [Appendix](#appendix)
  - [References](#references)
<!-- /TOC -->

# Learning phrase representations using RNN encoder-decoder for statistical machine translation
**RNN encoder-decoder**. The proposed network architecture for statistical machine translation (SMT) consisting of two RNNs acting as an encoder and a decoder pair
* *Network architecture*.
    * The encoder maps a variable-length source sequence to a fixed-length vector
    * The decoder maps the vector representation back to a variable-length target sequence
* *Training algorithm*. The two networks are trained jointly to maximize the conditional probability of the target sequence given a source sequence

## Related work
### Learning to align
**Graves (2013)**. A similar approach of aligning an output symbol with an input symbol was proposed recently by Graves (2013) in the context of handwriting synthesis
* *Handwriting synthesis*. The model is asked to generate handwriting of a given sequence of characters
* *Idea*. Use a mixture of Gaussian kernels to compute the weights of the annotations, where the location, width
and mixture coefficient of each kernel was predicted from an alignment model
* *Drawback*. The alignment was restricted to predict the location, i.e. the location increases monotonically

**Difference from the proposed method**.
* In (Graves, 2013), the modes of the weights of the annotations only move in one direction
    
    $\to$ In the context of machine translation, this is a severe limitation, as long-distance reordering is often needed to generate a grammatically correct translation
* In the proposed approach, the annotation weight of every word in the source sentence is computed, for each word in the translation

### Neural networks for machine translation
**Bengio (2003)**. Use a neural probabilistic language model, i.e. use a neural network to model the conditional probability of a word given a fixed number of the preceding words

## RNN encoder-decoder
### Recurrent neural networks
**Recurrent neural networks (RNN)**. A neural netweork consisting of a hidden state $\mathbf{h}$ and an optional output $\mathbf{y}$ operating on a variable-length sequence $\mathbf{x}=(x_1,\dots,x_T)$
* *Formulation*. At each time step $t$, $\mathbf{h}_t$ is given as

    $$\mathbf{h}_t = f(\mathbf{h}_{t-1}, x_t)$$

    where $f$ is a non-linear activation function, e.g. elementwise logistic sigmoid funciton, or a LSTM, etc.

* *Probabilistic modeling with RNN*. An RNN can learn a probability distribution over a sequence by being trained to predict the next symbol in a sequence
    
    $\to$ The output at each timestep $t$ is the conditional distribution

    $$p(x_t|x_{t-1},\dots,x_1)$$

    * *Consequence*. From the learned distribution, it is straightforward to sample a new sequence by iteratively sampling a symbol at each time step\

### RNN encoder-decoder
**RNN encoder-decoder under probabilistic perspective**. The model is a general method to learn the conditional distribution

$$p(y_1, \dots, y_{T'} | x_1,\dots,x_T )$$

* *Encoder*. An RNN reading each symbol of the input $\mathbf{x}$ sequentially
    
    $\to$ As it reads each symbol, the hidden state of the RNN changes as
    * *Encoder output*. After reading the end of the sequence, i.e. marked by an end-of-sequence symbol
        
        $\to$ The hidden state of the RNN is a summary $c$ of the whole input sequence
* *Decoder*. An RNN trained to generate the output sequence by predicting the next symbol $y_t$ given the hidden state $\mathbf{h}_t$
    * *Decoder hidden state*. Given an activation function $f$

        $$\mathbf{h}_t=f(\mathbf{h}_{t-1}, y_{t-1}, \mathbf{c})$$
    
    * *Conditional distribution of the next symbol*. Given an activation function $g$ producing valid probabilities

        $$p(y_t|y_{t-1},\dots,y_1,\mathbf{c}) = g(\mathbf{h}_t, y_{t-1}, \mathbf{c})$$

* *Training algorithm*. The two components of the network are jointly trained to maximize the log-likelihood

    $$\max_\theta \frac{1}{N}\sum_{n=1}^N \log p_\theta(\mathbf{y}_n|\mathbf{x}_n)$$

    where $\mathbf{\theta}$ is the set of model parameters, and $(\mathbf{x}_n,\mathbf{y}_n)$ are training pairs

* *Inference method*.
    * *Option 1*. Use the model to generate a target sequence, given an input sequence
    * *Option 2*. Use the model to score a given pair of input and output sequences, i.e. $p_\theta(\mathbf{y}|\mathbf{x})$

### Hidden unit which adaptively remembers and forgets
**Proposed network architecture**. Consider the $j$-th hidden unit
* *Reset gate*.
    * *Assumptions*.
        * $\sigma$ is the logistic sigmoid function
        * $\mathbf{x}$ and $\mathbf{h}_{t-1}$ are the input and the previous hidden state
        * $\mathbf{W}_r$ and $\mathbf{U}_r$ are weight matrices to learn
    * *Formulation*.

        $$r_j=\sigma([\mathbf{W}_r\mathbf{x}]_j + [\mathbf{U}_r\mathbf{h}_{t-1}]_j)$$

    * *Purposes*. Affectively allow the hidden state to drop any information irrelevant later in the future, allowing a more compact representation
* *Update gate*.

    $$z_j=\sigma([\mathbf{W}_z\mathbf{x}]_j + [\mathbf{U}_z \mathbf{h}_{t-1}]_j)$$

    * *Purposes*. Control how much information from the previous hidden state will carry over to the current hidden state

        $\to$ This is similar to the memory cell in the LSTM, helping the RNN to remember long-term information
* *Activation of $h_j$*. Each hidden unit has separate reset and update gates, and will learn to capture dependencies over different time scales

    $$h_j^{(t)} = z_j h_j^{(t-1)} + (1-z_j) \tilde{h}_j^{(t)}$$

    where

    $$\tilde{h}_j^{(t)} = \phi([\mathbf{W}\mathbf{x}]_j + [\mathbf{U} (\mathbf{r} \odot \mathbf{h}_{t-1})]_j)$$

## Statistical machine translation
**Statistical machine translation**.
* *Objective*. Find a translation $\mathbf{f}$ given a source sentence $\mathbf{e}$, which maximizes

    $$p(\mathbf{f}|\mathbf{e}) \propto p(\mathbf{e}|\mathbf{f}) p(\mathbf{f})$$

    * *Translation model*. $p(\mathbf{e}|\mathbf{f})$
    * *Language model*. $p(\mathbf{f})$
* *Practical model*. Most SMT systems model the objective as

    $$\log p(\mathbf{f}|\mathbf{e}) = \sum_{n=1}^N w_n f_n(\mathbf{f}, \mathbf{e}) + \log Z(\mathbf{e})$$

    where $f_n$ and $w_n$ are the $n$-th feature and weight respectively, and $Z(\mathbf{e})$ is a normalization constant independent of the weights

**Phrase-based SMT framework**. Introduced by Koehn et al. (2003) and Marcu and Wong (2002)
* *Idea*. $\log p(\mathbf{e}|\mathbf{f})$ is factorized into the translation probabilities of matching phrases in the source and target sentences

    $\to$ These probabilities are considered additional features in $\log p(\mathbf{f}|\mathbf{e})$, and are weighted accordingly to maximize the BLEU score

### Scoring phrase pairs with RNN encoder-decoder
**Model training and inference method**. Train the RNN encoder-decoder on a table of phrase pairs, and use its scores as additional features in $\log p(\mathbf{f}|\mathbf{e})$ when tuning the SMT decoder
* *Training strategy*. When training the RNN encoder-decoder, we ignore the normalized frequencies of each phrase pair in the original corpora
    * *Purposes*. This was taken to
        * Reduce the computational expense of randomly selecting phrase pairs from a large phrase table according to the normalized frequencies
        * Ensure that the RNN encoder-decoder does not simply learn to rank the phrase according to their numbers of occurrences
    * *Motivation*. The existing translation probability in the phrase table already reflects the frequencies of the phrase pairs in the original corpus
* *Learning objective*. With a fixed capacity of the RNN Encoder–Decoder, we try to ensure that most of the capacity of the model is focused toward learning 
    * Linguistic regularities, i.e., distinguishing between plausible and implausible translations, or
    * The “manifold”, i.e. region of probability concentration, of plausible translations
* *Tuning method*. Once the RNN Encoder–Decoder is trained, we add a new score for each phrase pair to the existing phrase table
    * *Purposes*. Allow the new scores to enter into the existing tuning algorithm with minimal additional overhead in computation
* *Replacement of phrase table with the proposed model*. It is possible to completely replace the existing phrase table with the proposed RNN encoder-decoder
    
    $\to$ For a given source phrase, the RNN encoder-decoder will need to generate a list of good target phrases
    * *Drawback*. This requires an expensive sampling procedure to be performed repeatedly
        
        $\to$ We only consider rescoring the phrase pairs in the phrase table

# Appendix
**Paper information**.
* *Authors*. KyungHyun Cho and Yoshua Bengio
* *Year of publication*. 2015

## References
* https://aclanthology.org/N03-1017.pdf