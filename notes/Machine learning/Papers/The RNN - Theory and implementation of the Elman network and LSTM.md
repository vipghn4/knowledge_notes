<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [The RNN - Theory and implementation of the Elman network and LSTM](#the-rnn---theory-and-implementation-of-the-elman-network-and-lstm)
  - [Historical and theoretical background](#historical-and-theoretical-background)
    - [Hopfield network](#hopfield-network)
    - [Elman network](#elman-network)
  - [Interlude - Vanishing and exploding gradients in RNNs](#interlude---vanishing-and-exploding-gradients-in-rnns)
    - [LSTM network](#lstm-network)
    - [RNNs and cognition](#rnns-and-cognition)
  - [Mathematical formalization](#mathematical-formalization)
    - [Forget function](#forget-function)
    - [Input function and candidate memory function](#input-function-and-candidate-memory-function)
    - [Output function](#output-function)
    - [Memory cell function](#memory-cell-function)
    - [Hidden-state function](#hidden-state-function)
    - [Output function](#output-function-1)
    - [Cost function](#cost-function)
      - [Learning procedure - Backpropagation through time (BPTT)](#learning-procedure---backpropagation-through-time-bptt)
  - [Interlude - Sequence-data representation](#interlude---sequence-data-representation)
  - [Limitations](#limitations)
    - [Training RNNs is hard and costly](#training-rnns-is-hard-and-costly)
    - [Do RNNs really understand anything](#do-rnns-really-understand-anything)
- [Appendix](#appendix)
  - [References](#references)
<!-- /TOC -->

# The RNN - Theory and implementation of the Elman network and LSTM
## Historical and theoretical background
**Causal time series**.
* *Key characteristics*. Past-states have no influence in future-states
* *Examples*. Movement, speech production, planning, decision-making, etc. 

**Multilayer perceptrons and convolutional networks**. In principle, can be used to approach time-series-related problems (Cui et al, 2016)
* *Drawback*. Introducing time considerations in such architectures is cumbersome, and better architectures have been envisioned

**Recurrent neural networks (RNNs)**. The modern standard to deal with time-dependent and/or sequence-dependent problems
* *“Recurrent”*. The model can revisit or reuse past states as inputs to predict the next or future states, i.e. they have memory
    
    $\to$ Memory is what allows us to incorporate our past thoughts and behaviors into our future thoughts and behaviors

### Hopfield network
**Hopfield network**. One of the earliest examples of networks incorporating “recurrences” was introduced in 1982 by John Hopfield, at the time, a physicist at Caltech
* *Historical role*. Hopfield networks were important as they helped to reignite the interest in neural networks in the early ’80s
* *Problem to solve*. Address the fundamental question of emergence in cognitive systems
    
    >Can relatively stable cognitive phenomena, like memories, emerge from the collective action of large numbers of simple neurons?
    
    >**NOTE**. After all, such behavior was observed in other physical systems like vortex patterns in fluid flow. Brains seemed like another promising candidate

**Hopfield networks as an of energy-based network**. This is because their properties derive from a global energy-function (Raj, 2020)
* *Hopfield neurons*. In resemblance to the McCulloch-Pitts neuron, Hopfield neurons are binary threshold units, but with recurrent instead of feed-forward connections

    <div style="text-align:center">
        <img src="https://pabloinsente.github.io/assets/post-9/hopfield-net.png">
        <figcaption>Hopfield network</figcaption>
    </div>

    * *Network architecture*. Each unit is bi-directionally connected to each other
        * *Interpretation*. Each unit receives inputs and sends inputs to every other connected unit
        * *Consequence*. Weights values are symmetric, i.e. weights coming into a unit are the same as the ones coming out of a unit
    * *Formulation*. Each unit's value is computed as

        $$y_i=T(\sum_j w_{ij} y_j + b_i)$$

        where $T$ is a threshold function
* *Idea*. Each configuration of binary-values $C$ in the network is associated with a global energy value $−E$

**Training method**. Consider a network with five neurons with a configuration of $C_1=(0,1,0,1,0)$, which yields a global energy-value $E_1=2$
* *Training objective*. Minimize E by changing one element of the network $C_i$ at a time

    $\to$ By using the weight updating rule $\Delta w$, we can get a new configuration $C_2=(1,1,0,1,0)$, as new weights will cause a change in the activation values $(0,1)$
* *Conclusion*. By keep iterating with new configurations, the network will eventually settle into a global energy minimum, conditioned to the initial state of the network

**Hopfield networks and neuroscience**. Hopfield networks is closely based in neuroscience research about learning and memory, particularly Hebbian learning (Hebb, 1949)

$\to$ Hopfield (1982) proposed this model as a way to capture memory formation and retrieval
* *Idea*. The energy-minima of the network could represent the formation of a memory, which further gives rise to a property known as content-addressable memory (CAM)
    * *Computer analogy of CAM*. When accessing information stored in the random access memory of our computer (RAM)
        
        $\to$ We give the "address" where the "memory" is located to retrieve it
    * *CAM mechanism*. We give information about the content we are searching for
        
        $\to$ The computer should retrieve the “memory”
    * *Conclusion*. This is great, since this works even when we have partial or corrupted information about the content
        
        $\to$ This is a much more realistic depiction of how human memory works
* *More about human memory formation*. Hopfield networks evolves until they find a stable low-energy state
    
    $\to$ If we perturb the system, it will re-evolve towards its previous stable-state
    * *Analogy to memory formation*. The system “remembers” its previous stable-state (isn’t?)
        
        $\to$ This ability to “return” to a previous stable-state after the perturbation is why they serve as models of memory

### Elman network
**Brief**. The first successful example of a recurrent network trained with backpropagation was introduced by Jeffrey Elman, the so-called Elman Network (Elman, 1990)

**Jordan's research work**. 

<div style="text-align:center">
    <img src="https://pabloinsente.github.io/assets/post-9/jordan-net.png">
    <figcaption>Jordan's network</figcaption>
</div>


* *Idea*. Jordan’s network implements recurrent connections from the network output $\hat{y}$ to its hidden units $h$, via a “memory unit” $\mu$, i.e. equivalent to Elman’s “context unit”
* *Memory unit*. Keep a running average of all past outputs
    
    $\to$ This is how the past history is implicitly accounted for on each new computation
    
    >**NOTE**. There is no learning in the memory unit, i.e. the weights are fixed to 1

**Elman's research work**. In 1990, Elman published “Finding Structure in Time”, a highly influential work for in cognitive science
* *Problem of interest*. Represent “time” or “sequences” in neural networks
    
    $\to$ In his view, we could take either an “explicit” approach or an “implicit” approach
* *Explicit approach*. Represent time spacially
    * *Idea*. Consider a vector $x=[x_1,\dots,x_n]$ where element $x_i$ represents the $i$-th value of the sequence
        
        $\to$ The spacial location in $x$ is indicating the temporal location of each element
    * *Drawbacks*.
        * Although $x$ is a sequence, the network still needs to represent the sequence all at once as an input
            * *Explain*. The network needs $n$ input neurons to process $x$
        * The approach imposes a rigid limit on the duration of pattern, i.e. the network needs a fixed number of elements for every input vector $x$
            * *Example*. A network with five input units cannot accommodate a sequence of length six
            * *Consequence*. This is a problem for most domains, where sequences have a variable duration
        * The approach cannot easily distinguish relative temporal position from absolute temporal position
            * *Example*. Consider the sequence $s=[1,1]$ and a vector input length of four bits
                
                $\to$ $s$ can be presented in at least three variations, i.e. $(0,1,1,0), (0,0,1,1), (1,1,0,0)$, i.e. all are instances of $s$ but spatially displaced in the input vector
                * *Observation*. The three vectors are geometrically different, although representing the same instance
* *Implicit approach*. Represent time by its effect in intermediate computations
    * *Idea*. Use a context unit, i.e. memory, to save past computations and incorporate those in future computations
    * *Motivation*. The work of Michael I. Jordan on serial processing (1986)
    * *Elman's innovation*.
        * Recurrent connections between hidden units and memory (context) units
        * Trainable parameters from the memory units to the hidden units
    
    <div style="text-align:center">
        <img src="https://pabloinsente.github.io/assets/post-9/elman-net.png">
        <figcaption>Elman's network</figcaption>
    </div>

    * *Memory unit*. 
        * Have to remember the past state of hidden units, i.e. instead of keeping a running average

            $\to$ They clone the value at the previous time step $t-1$
        * Have to learn useful representations, i.e. weights, for encoding temporal properties of the sequential input
* *Benefits*. The network can take inputs of any length, without having to alter the network architecture at all
* *Other expiermental results*. The internal hidden representations learned by the network grouped into meaningful categories, i.e. semantically similar words group together when analyzed with hierarchical clustering

**Formulation**.
* *Assumptions*.
    * $x_t$ is input vector
    * $h_t$ is hidden layer vector
    * $y_t$ is output vector
    * $W,U,b$ are learnable parameters
    * $\sigma_h,\sigma_y$ are activation functions
* *Jordan network*.

    $$h_t=\sigma_h(W_h x_t + U_h y_{t-1} + b_h),\quad y_t=\sigma_y(W_y h_t + b_y)$$

* *Elman's network*.

    $$h_t=\sigma_h(W_h x_t + U_h h_{t-1} + b_h),\quad y_t=\sigma_y(W_y h_t + b_y)$$

## Interlude - Vanishing and exploding gradients in RNNs

### LSTM network

### RNNs and cognition

## Mathematical formalization

### Forget function

### Input function and candidate memory function

### Output function

### Memory cell function

### Hidden-state function

### Output function

### Cost function

#### Learning procedure - Backpropagation through time (BPTT)

## Interlude - Sequence-data representation
**Brief**. Working with sequence-data, like text or time-series, requires to pre-process it in a manner that is digestible for RNNs
* *Explain*. As with any neural network, RNN cannot take raw text as an input
    
    $\to$ We need to parse text sequences and then map them into vectors of numbers

**Tokenization**. The process of parsing text into smaller units, i.e. each resulting unit is called a token

<div style="text-align:center">
    <img src="https://pabloinsente.github.io/assets/post-9/text-pro.png">
    <figcaption>Hopfield network</figcaption>
</div>

* *Parsing methods*. Parsing can be done in multiple manners, the most common being
    * Using word as a unit, which each word represented as a vector
    * Using character as a unit, with each character represented as a vector
    * Using $n$-grams of words or characters as a unit, with each n-gram represented as a vector
        * *$n$-grams*. Sets of words or characters of size $n$ or less

**Word embedding**. Once a corpus of text has been parsed into tokens

$\to$ We have to map such tokens into numerical vectors
* *Word embedding methods*. Two common ways to do this are
    * One-hot encoding approach
        * *Pros*. Straightforward to implement and to provide a unique identifier for each token
        * *Cons*. The approach tends to create really sparse and high-dimensional representations for a large corpus of texts
    * Word embeddings approach
        * *Pros*. Significantly increments the representational capacity of vectors, reducing the required dimensionality for a given corpus of text compared to one-hot encodings
        * *Cons*. There is not an obvious way to map tokens into vectors as with one-hot encodings
            
            $\to$ Ideally, we want words of similar meaning mapped into similar vectors
* *Learning word embeddings*. We can preserve the semantic structure of a text corpus by learning from data
    
    $\to$ There are two ways to do this
    * Learning the word embeddings at the same time training the RNN
        * *Usage*. When semantic relationships among words tend to be context dependent
    * Utilizing pretrained word embeddings, i.e. embeddings learned in a different task
        
        $\to$ This is a form of transfer learning
        * *Usage*. When dealing with different languages
            
            >**NOTE**. Learning embeddings for every task sometimes is impractical
            >
            >* *Explain*. Since our corpus is too “small” (i.e., not enough data to extract semantic relationships), or too “large” (i.e., we do not have enough time and/or resources to learn the embeddings)

## Limitations
### Training RNNs is hard and costly
**Brief**. There are three well-known issues that make training RNNs really hard
* Vanishing gradients
* Exploding gradients
* Its sequential nature, which make them computationally expensive as parallelization is difficult

**Conclusion**. The quest for solutions to RNNs deficiencies has prompt the development of new architectures like Encoder-Decoder networks with “attention” mechanisms (Bahdanau et al, 2014; Vaswani et al, 2017)

$\to$ This architecture seems to be outperforming RNNs in many tasks

### Do RNNs really understand anything
**Brief**. Critics like Gary Marcus have pointed out the apparent inability of neural-networks based models to “really” understand their outputs (Marcus, 2018)

$\to$ This is prominent for RNNs since they have been used profusely used in the context of language generation and understanding
* *Example*. Even GPT-2 sometimes produce incoherent sentences

# Appendix
## References
* https://pabloinsente.github.io/the-recurrent-net