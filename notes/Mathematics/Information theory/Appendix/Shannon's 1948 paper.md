<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Discrete noiseless systems](#discrete-noiseless-systems)
  - [Discrete noiseless channel](#discrete-noiseless-channel)
    - [General discrete noiseless channel](#general-discrete-noiseless-channel)
  - [Discrete source of information](#discrete-source-of-information)
  - [Choice, uncertainty, and entropy](#choice-uncertainty-and-entropy)
  - [Entropy of an information source](#entropy-of-an-information-source)
- [BONUS](#bonus)
<!-- /TOC -->

# Introduction
**Fundamental problem of communication**: reproduce, at one point, either exactly or approximately a message, selected at another point

**Aspects of a message in communication**:
* Message meaning: the messages refer to, or are correlated according to, some system with certain physical or conceptual entities

$\hspace{1.0cm} \rightarrow$ These semantic aspects of communication are irrelevant to the engineering problem
* Message selection: the actual message is one selected from a set of possible messages

$\hspace{1.0cm} \rightarrow$ This is the significant aspect

**Ideal communication system**: be able to operate for each possible selection, not just the one, which will actually be chosen
* Explain: the message is unknown at the time of system design

**Information measurement**: if the number of messages in the set is finite

$\hspace{1.0cm} \rightarrow$ This number, or any monotonic function of this number, can be regarded as a measure of the information produced, when one message is chosen from the set, and all choices being equally likely
* Hartley's idea: logarithmic function is the most natural choice for several reasons
    * It's practically more useful
        * Explain: parameters of engineering importance (e.g. time, bandwidth, number of relays, etc.) tend to vary linearly with the logarithm of the number of possibilities
    * It's nearer to our intuitive feeling as to the proper measure
        * Explain: we intuitively measure entities by linear comparison with common standards
        * Example: two punched cards should have twice the capacity of one, for information storage
    * It's mathematically more suitable
        * Explain: many of the limiting operations are simple in terms of the logarithm, but would require clumsy re-statement in terms of the number of possibilities
* Logarithm base: correspond to the choice of a unit for measuring information
    * Base $2$: units are represented by binary digits (or *bits*)

**Communication system**: Information source $\to$ Transmitter $\to$ Channel $\to$ Receiver $\to$ Destination
* Information source: produce a message, or sequence of messages, to be communicated to the receiving terminal
    * Types of messages:
        * A sequence of letters (e.g. telegraph)
        * A function of time $f(t)$ (e.g. radio)
        * A function of time and other variables $f(x, y, t)$ (e.g. black-and-white TV)
        * Two or more functions of time $f(t), g(t)$, and $h(t)$ (e.g. image)
        * Several functions of several variables (e.g. color television)
        * Various combinations
* Transmitter: operate on the message in some way to produce a signal suitable for transmission over the channel
    * Example: 
        * Merely change sound pressure into a proportional electrical current
        * Encode messages into a sequence of dots, dashes, and spaces
        * Sample the signal, compress, quantize, and encode, then finally interleave the signal properly construct the signal
* Channel: merely the medium used to transmit the signal from the transmitter to receiver
    * Example: wires, cable, a band of radio frequencies, etc.
* Receiver: ordinarily perform the inverse operation done by the transmitter, reconstructing the message from the signal
* Destination: the person (or thing) for whome the message is intended

# Discrete noiseless systems
## Discrete noiseless channel
**Discrete channel**: a system where a sequence of choices, from a finite set of elementary symbols $S_1, ..., S_n$, can be transmitted from one point to another
* $S_i$ have a certain duration in time $t_i$ seconds
    * Example: dots and dashes in telegraphy
* All possible sequences of $S_i$ aren't necessarily be capable of transmission on the system
    * Explain: certain sequences only maybe allowed

**Task**: measure the capacity of such channel to transmit information

**Capacity $C$ of a discrete channel**: 
* Assumptions:
    * $N(T)$ is the number of allowed signals of duration $T$ (measured in bits)
* Discrete channel capacity: $C = \lim_{T \to \infty} \frac{\log N(T)}{T}$
* Example: there are $32$ allowed symbols of equal duration and each symbol represents $5$ bits of information

$\hspace{1.0cm} \rightarrow$ If the system transmits $n$ symbols per second, the channel has a capacity of $5n$ bits per second

**Computing $N(t)$**:
* Assumptions:
    * $S_1, ..., S_n$ are allowed symbols
    * $S_i$ has duration $t_i$
* Conclusion: $N(t) = N(t - t_1) + N(t - t_2) + ... + N(t - t_n)$
* Explain:
    * At time $t$, there are $N(t)$ possible signals of length $t$
    * There are $n$ symbols, thus if the last symbol was $S_k$

    $\hspace{1.0cm} \rightarrow$ There are $N(t - t_k)$ possible signals leading up to $S_k$, which take time $t - t_k$, plus the length $t_k$ of $S_k$
    * From above, adding up over all symbols, we get $N(t) = \sum_{i=1}^n N(t - t_i)$

**Convenient formulation of $C$**:
* Observations:
    * $N(t) = N(t - t_1) + N(t - t_2) + ... + N(t - t_n)$ is a finite difference equation
        * Guess $N(t) = X^t$

        $\hspace{1.0cm} \rightarrow$ We need to solve $X$ for $X^{-t_1} + X^{-t_2} + ... + X^{-t_n} = 1$
    * From above, $N(t) \approx X_0^t$ for large $t$
        * $X_0$ is the largest real solution of the characteristic equation $X^{-t_1} + X^{-t_2} + ... + X^{-t_n} = 1$
* Conclusion: $C = \log X_0$

### General discrete noiseless channel
**Communication system description**:
* $a_1, ..., a_m$ are possible states of the communication system
* At each state, only certain symbols from $S_1, ..., S_n$ can be transmitted
* After transmitting a symbol, the system state changes depending on the old state and the transmitted symbol

**The growth of the number of blocks of symbols with a finite state condition**:
* Assumptions:
    * $b^{(s)}_{ij}$ is the duration of the $s^\text{th}$ symbol, which is allowable in state $i$ and leads to state $j$
    * $N_i(L)$ is the number of blocks of symbols of length $L$ ending in state $i$

    $\hspace{1.0cm} \rightarrow N_j(L) = \sum_{i, s} N_i(L - b^{(s)}_{ij})$
    * $N_j = \lim_{L \to \infty} N_j(L)$
* Guess solution: $N_j = a_j W^L$
* Characteristic equation: $a_j = \sum_{i, s} a_i W^{- b^{(s)}_{ij}}$
    * $\forall j$, $\sum_i a_i (\sum_s W^{-b^{(s)}_{ij}} - \delta_{ij}) = 0$
    * Let $D = \begin{bmatrix} \sum_s W^{-b^{(s)}_{11}} - \delta_{11} & \cdots & \sum_s W^{-b^{(s)}_{1m}} - \delta_{1m} \\ \vdots & \ddots & \vdots \\ \sum_s W^{-b^{(s)}_{m1}} - \delta_{m1} & \cdots & \sum_s W^{-b^{(s)}_{mm}} - \delta_{mm} \end{bmatrix}$

    $\hspace{1.0cm} \rightarrow$ The above equation implies $a^T D = 0$ for some $a = \begin{bmatrix} a_1 & \cdots & a_m \end{bmatrix}$
    * From above, $D$ is a singular matrix, which implies that $\det D = 0$

    $\hspace{1.0cm} \rightarrow$ Solving $\det D = 0$ gives us solutions for $W$ and we will choose the largest one
* Channel capacity: $C = \lim_{L \to \infty} \frac{\log [\sum_j N_j(L)]}{L} = \log W$

**Theorem**:
* Assumptions:
    * $b^{(s)}_{ij}$ is the duration of the $s^\text{th}$ symbol, which is allowable in state $i$ and leads to state $j$
    * $W$ is the largest real root of $\det \bigg(\begin{bmatrix} \sum_s W^{-b^{(s)}_{11}} - \delta_{11} & \cdots & \sum_s W^{-b^{(s)}_{1m}} - \delta_{1m} \\ \vdots & \ddots & \vdots \\ \sum_s W^{-b^{(s)}_{m1}} - \delta_{m1} & \cdots & \sum_s W^{-b^{(s)}_{mm}} - \delta_{mm}\end{bmatrix}\bigg) = 0$
        * $\delta_{ij} = \begin{cases} 1 & i = j \\ 0 & i \neq j\end{cases}$
* Channel capacity: $C = \log W$

## Discrete source of information
**Questions**:
* How is an information source to be described mathematically
* How much information, in bits, per second is produced in a given source

**Main point**: the effect of statistical knowledge about the source, in reducing the required capacity of the channel, by the use of proper encoding of the information

**Idea**: a discrete source can be thought of as generating message, symbol by symbol
* The source chooses successive symbols according to certain probabilities depending on
    * The preceding choices
    * The particular symbols in the question

**Discrete source as a stochastic process**: we can represent a discrete source by a stochastic process
* Approximating natural language
    * Zero-order approximation: choose all letters with the same probability and independently
    * First-order approximation: sample successive $W_i$ with $P(W_i)$ independently
    * Second-order approximation: sample successive $W_i$ with $P(W_i|W_{i-1})$ independently
    * Higher-order approximation: in the same manner

>**NOTE**: a sufficiently complex stochastic process will give a satisfactory representation of a discrete source

**Markov process**: the type of stochastic process described above for discrete information source approximation

## Choice, uncertainty, and entropy
**Question**: 
* How to measure the information produced by a stochastic process
* What rate information is produced

**Idea**:
* Assumptions:
    * $p_1, ..., p_n$ are probabilities of occurrence of $n$ events
    * $p_i$ is known in advance
* Task: 
    * Measure how much "choice" is involved in the selection of the event
    * How uncertain we are of the outcome

**Axioms on the measure $H(p_1, ..., p_n)$**:
* $H$ should be continuous in $p_i$
* If $p_i = \frac{1}{n}$ $\forall i$, $H$ should be monotonic increasing function of $n$
    * Intuition: with equally likely events, there is more choice when there are more possible events
* If a choice is broken into two successive choice, $H$ should be the weighted sum of individual values of $H$
    * Formal: $H(X_1, X_2) = p_1 H(X_1) + p_2 H(X_2)$
        * $p_1$ is the probability of having to make choice on $X_1$
        * $p_2$ is the probability of having to make choice on $X_2$

        >**NOTE**: $p_1 + p_2$ need not to be $1$
    
    * Example: consider a game where player have to flip a coin until he comes up with a head, and let $p$ be the probability of obtaining a head from a coin flip
        * The player always has to flip a coin once

        $\hspace{1.0cm} \rightarrow H = H(p)$
        * In case the player failed (with probability $1 - p$), he has to flip the coin once more

        $\hspace{1.0cm} \rightarrow H = H(p, 1-p) + (1 - p) \cdot H(p, 1-p)$
        * In case he failed again, he has to flip the coin once more

        $\hspace{1.0cm} \rightarrow H = H(p, 1-p) + (1 - p) \cdot H(p, 1-p) + (1 - p)^2 \cdot H(p, 1-p)$
        * If he failed for a large number of times, he has to flip the coin again and again

        $\hspace{1.0cm} \rightarrow H = H = H(p, 1-p) + (1 - p) \cdot H(p, 1-p) + (1 - p)^2 \cdot H(p, 1-p) + \dots$

**Theorem**: 
* Statement: the only $H$ satisfying the axioms above is $H = -K \log_{i=1}^n p_i \log p_i$ where $K > 0$ is a constant
    * $K$ amounts to a choice of a unit of measure
* Derivation:
    * For any sample space of possibilities with probabilities $p_1, ..., p_n$

    $\hspace{1.0cm} \rightarrow$ We are always able to divie the sample space into infinitely  many equally likely possibilities 
    * Let $A(n) = H(\frac{1}{n}, ..., \frac{1}{n})$
    * Equally likely possibilities case: direct prove with "hamburger" theorem
        * Consider dividing $s^m$ equally likely possibilities into leaves of a $s$-ary tree with heigh $m$ where $m$ is sufficiently large

        $\hspace{1.0cm} \rightarrow A(s^m) = m A(s)$
        * Consider dividing $t^n$ equally likely possibilities into leaves of a $t$-ary tree with heigh $n$ where $n$ is sufficiently large

        $\hspace{1.0cm} \rightarrow A(t^n) = n A(t)$
        * By axiom (3), if $s^m \leq t^n \leq s^{m+1}$,
        
        $\hspace{1.0cm} \rightarrow m A(s) \leq n A(t) \leq (m + 1) A(s)$
        * Consider the inequality $s^m \leq t^n \leq s^{m+1}$
            * $m \log s \leq n \log t \leq (m + 1) \log s$

            $\hspace{0.3cm} \leftrightarrow \frac{m}{n} \log s \leq \log t \leq \frac{m}{n} \log s + \frac{1}{n} \log s$

            $\hspace{0.3cm} \leftrightarrow \frac{m}{n} \leq \frac{\log t}{\log s} \leq \frac{m}{n} + \frac{1}{n}$

            $\hspace{0.3cm} \leftrightarrow \frac{\log t}{\log s} \approx \frac{m}{n}$
        * Consider $m A(s) \leq n A(t) \leq m A(s) + A(s)$
            * $\frac{m}{n} A(s) \leq A(t) \leq \frac{m}{n} A(s) + \frac{1}{n} A(s)$

            $\hspace{0.3cm} \leftrightarrow \frac{m}{n} \leq \frac{A(t)}{A(s)} \leq \frac{m}{n} + \frac{1}{n}$

            $\hspace{0.3cm} \leftrightarrow \frac{A(t)}{A(s)} \approx \frac{m}{n}$
        * From above, $\frac{A(t)}{A(s)} \approx \frac{\log t}{\log s}$
        * Suppose $A(t) = K \log t$

        $\hspace{1.0cm} \rightarrow$ To ensure that $A(t)$ is monotonically increasing in $n$, $K$ must be positive
    * General case of arbitrary probability $p_1, ..., p_n$: direct prove with the law of large numbers
        * First divide the sample space into infinitely many equally likely possibilities and cluster these possibilities into $n$ clusters
            * Cluster $i$ has $p_i \times 100\%$ percent of elements
        * Let $N$ be the number of divided possibilities
        
        $\hspace{1.0cm} \rightarrow$ The entropy of cluster $i$ is $A(p_i N) = K \log (p_i N)$
        * By axiom (3), the entropy of the whole sample space is $K \log N = H(p_1, ..., p_n) + K \sum_{i=1}^n p_i \log (p_i N)$
            * Explain: decompose the choice into two successive choices
                * Step 1: choose cluster among $n$ clusters
                * Step 2: choose an element in the chosen cluster
            * Consequence: $H(p_1, ..., p_n) = - K \sum_{i=1}^n p_i \log p_i$

>**NOTE**: initially, Shannon defines "entropy" just to lend certain plausibility to some of his later definitions

**Entropy of the set of probabilities $p_1, ..., p_n$**: $H = - \sum_{i=1}^n p_i \log p_i$
* Interpretation: measure information, choice, and uncertainty
* "Entropy": the form of $H$ is recognized as "entropy" in statistical mechanics

**Entropy of a discrete random variable**: $H(X)$ where $X \sim \{p_1, ..., p_n\}$

**Properties of $H$**:
* $H = 0$ if and only if all $p_i$ but one are zero
    * Intuition: only when we are certain of the outcome, $H$ will vanish, otherwise $H$ is positive
* Given $n$, $H$ is a maximum and equal to $\log n$ when $p_i = \frac{1}{n}$ $\forall i$
* If $X$ and $Y$ are two events with $m$ and $n$ possibilities (respectively), then $H(X, Y) \leq H(X) + H(Y)$
    * Intuition: the uncertainty of a joint event is no greater than the sum of individual uncertainties
* Any change towrad equalization of $p_1, ..., p_n$ increases $H$

**Conditional entropy of $Y$ given $X$**: $H(Y|X) = - \sum_{x, y} p(x, y) \log p(y|x)$
* Original notation: $H_X(Y)$
* Another equivalent formulation: $H(X, Y) = H(X) + H(Y|X)$
* Intuition: uncertainty of the joint event $X, Y$ is the uncertainty of $Y$ plus the uncertainty of $Y|X$
* Comparison to entropy: $H(Y) \geq H(Y|X)$
    * Intuition: 
        * The uncertainty of $Y$ is never increased by knowing $X$
        * The uncertainty of $Y$ will be decreased unless $X$ and $Y$ are independent

## Entropy of an information source
**Entropy of information source**:
* Assumptions:
    * $p_i(j)$ is the probability of producing various possible symbols $j$, for state $i$
    * $H_i$ is the entropy for state $i$
* Per-symbol entropy of information source : $H = \sum_i p_i H_i$
    * $p_i$ is the probability of occurrence of states in question
* Per-second entropy of information source: $H' = 
  \sum_i f_i H_i = m H$
    * $f_i$ is the average frequency (occurrences per second) of state $i$
    * $m$ is the average number of symbols produced per second

**Theorem**:
* Assumptions:
    * Consider the information source with finite state as described above
    * $\epsilon > 0$
    * $\delta > 0$
* Conclusion: we can find $N_0$ so that any sequences of length $N \geq N_0$ fall into two classes
    * A set whose probability is less than $\epsilon$
    * The remainder, whose all members have proabbilities satisfying $|\frac{\log(1/p)}{N} - H| < \delta$
* Prove: direct prove using the law of large numbers

**Theorem**:
* Assumptions:
    * Consider a set $S$ of sequences of length $N$ 
        * $S$'s elements are arranged in order of decreasing probability
    * $n(q)$ is the number needed to take from $S$, from the most probable one, to accumulate a total probability $p$
* Conclusion: $\lim_{N \to \infty} \frac{\log n(q)}{N} = H$ when $q \notin \{0, 1\}$
* Interpretation: the rate of growth, of $\log n(q)$, is given by $H$
    * When we only consider the most probable sequences with total probability $q$
    
    $\hspace{1.0cm} \rightarrow \log n(q)$ is the number of bits required to specify the sequence
    * $\frac{\log n(q)}{N}$ is the number of bits per symbol for the specification
* Corollary: we can treat long sequences as if there are $2^{HN}$ of them, each with probability $2^{-HN}$

---

# BONUS
* Linear homogeneous difference equation: $\sum_{t=1}^n a_t X(t) = 0$
    * Idea:
        * Guess $X(t) = x^t$ and solve $\sum_{t=0}^n a_t x^t = 0$ for solutions $x_1, ..., x_n$
    * General solution: $\sum_{i=1}^n c_i x_i$
        * Explain: due to linearity of the equation and the difference operation
* Linear inhomogeneous difference equation: $\sum_{t=1}^n a_t X(t) = b$
    * Idea:
        * Solve $\sum_{t=1}^n a_t X(t) = 0$ for $x_1, ..., x_n$
        * Find a particular solution $x_0$ for $\sum_{t=1}^n a_t X(t) = b$
    * General solution: $x_0 + \sum_{i=1}^n c_i x_i$