<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Golomb coding](#golomb-coding)
- [Appendix](#appendix)
<!-- /TOC -->

# Golomb coding
**Context**.
* *Context*. Consider a sequence of games, each of which consists of a sequence of favorable events, i.e. event 1, terminated by the first occurrence of an unfavorable event, i.e. event 0
* *Assumptions*.
    * $p$ is the probability of favorable event
    * $q=1-p$ is the probability of unfavorable event
* *Problem*. Minimize the number of bits required to communicate blow-by-blow description of the game results
* *Edge cases*.
    * *$p = q = 1/2$*. The best can be done via using 0 and 1 to represent two possible outcomes
    * *$p \gg q$*. The probability of a run-length of $n$ is $p^nq$, which is the familiar geometric distribution
        * *Idea*. Encode the run lengths between successive unfavorable events
* *Problem with Huffman coding*. Cannot handle infinite list of different symbols
    * *Solution*. If the probabilities follow a distribution law, then we have a shortcut

**Mathematical reasoning**.
* *Assumptions*.
    * $m=\log_p \frac{1}{2}$

        >**NOTE**. The results will be most readily applicable for those $p$ such that $m\in\mathbf{Z}$

        >**NOTE**. The resulting coding scheme is especially simple when $m$ is a power of $2$, but any integer $m$ is favorable
    
    * $k$ is the smallest positive integer such that $2^k \geq 2m$, i.e.

        $$k = \lceil\log_2 m\rceil + 1$$
* *Key idea*. A run of length $n+m$ is half as likely as a run of length $n$, i.e. $p^{m+n}q = \frac{1}{2} p^n q$

    $\to$ The codeword for run-length $n+m$ should be one bit longer than the codeword for run-length $n$
    * *Explain*. $\log \frac{1}{p^{m+n}q} = \log \frac{1}{p^n q} + 1$
* *Observations*.
    * Therefore, there should be $m$ codewords of each possible word length, i.e. $m$ codewords of length $l$ for each $l$, except for 
        * The shortest word lengths, which are not used if $m > 1$
        * Possibly one transitional word length, which is used fewer than $m$ times
    * Consider the signal space ${\cal{X_k}} = \{x:l(x)\geq k\}$ where $l(x)$ represents the code length of $x$ after being encoded

        $$\begin{aligned}
        P({\cal{X_k}})&=\sum_{i=k}^{\infty} \frac{m}{2^i}\\
        &\approx \frac{m}{2^{k-1}}
        \end{aligned}$$

        leaving 
        
        $$\begin{aligned}
        1-P({\cal{X_k}})&=1 - \frac{m}{2^{k-1}}\\
        & = \frac{2^{k-1}-m}{2^{k-1}}
        \end{aligned}$$
        
        unused, which means that $2^{k-1}-m$ words of length $k-1$ may be adjoined
* *Code directory*. Contain exactly 
    * $m$ words of every word length $l \geq k$
    * $2^{k-1}-m$ words of length $k-1$
* *Why choose $k$*. The shortest code length is $k-1$, which is sufficient to encode the first $2^{k-1}-m$ words

>**NOTE**. If $m \notin \mathbf{Z}$, then the best dictionary will oscillate between $\lfloor m\rfloor$ and $\lfloor m\rfloor + 1$

>**NOTE**. For every large $m$, there is very little penalty for picking the nearest integer when designing the code

**Estimating parameter $p$**. Based on sampling or simulation methods
* *Expected value for geometric distribution*. $E(X)=\sum_{x=0}^\infty (1 - p) p^x x = \frac{p}{1 - p}$
    * *Proof*. View the summation as the derivative of some other function an work on that function
        $$\begin{aligned}
        E(X)&=p (1 - p) \sum_{x=0}^\infty p^{x-1} x\\
        &=p (1 - p) \frac{\partial}{\partial p} \bigg(\sum_{x=1}^\infty p^{x}\bigg)\\
        &=p (1 - p) \frac{\partial}{\partial p} \frac{1}{1 - p}\\
        &=\frac{p}{1 - p}
        \end{aligned}$$
* *Estimate $p$*. $p = \frac{E(X)}{1 + E(X)}$

**Golomb coding procedure**. The Golomb coding procedure given in textbooks are just an example given by Golomb in his paper on 1966

$\to$ Feel free to design other codes based on the idea above also

**Pros and cons**.
* *Pros*. 
    * Optimal for geometric distribution, i.e. $p(x) = p^x (1 - p)$
    * Do not require sophisticated code table
* *Cons*. Do not suit for bounded run-lengths, ie. code words allocated for case $i > n$ are wasted

    $\to$ Golomb code is unattractive many short lists of integers drawn from limited ranges, or when the range of $n$ is narrowed down by a recursive algorithm

# Appendix
**Run-length encoding (RLE)**. A form of lossless data compression, in which runs of data, i.e. sequence in which the same data value occurs in many consecutive data elements, are stored as a single data value and count
* *Example*. `WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW` to `12W1B12W3B24W1B14W`

**Signal space**. The space of signals which is to be encoded