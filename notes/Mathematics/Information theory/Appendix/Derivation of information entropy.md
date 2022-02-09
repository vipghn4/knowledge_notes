<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Derivation of information entropy](#derivation-of-information-entropy)
  - [Motivation and assumptions](#motivation-and-assumptions)
  - [Derivation of information entropy](#derivation-of-information-entropy-1)
  - [Information entropy](#information-entropy)
<!-- /TOC -->

# Derivation of information entropy
## Motivation and assumptions
**Motivation**. 
* How to measure the information produced by a stochastic process
* What rate information is produced

**Idea**.
* *Assumptions*.
    * $p_1, ..., p_n$ are probabilities of occurrence of $n$ events
    * $p_i$ is known in advance
* *Task*.
    * Measure how much "choice" is involved in the selection of the event
    * How uncertain we are of the outcome

**Axioms on the measure $H(p_1, ..., p_n)$**.
* $H$ should be continuous in $p_i$
* If $p_i = \frac{1}{n}$ $\forall i$, $H$ should be monotonic increasing function of $n$
    * *Intuition*. With equally likely events, there is more choice when there are more possible events
* If a choice is broken into two successive choice, $H$ should be the weighted sum of individual values of $H$
    * *Assumptions*.
        * $p_1$ is the probability of having to make choice on $X_1$
        * $p_2$ is the probability of having to make choice on $X_2$

            >**NOTE**. $p_1 + p_2$ need not to be $1$
    
    * *Conclusion*. 
        
        $$H(X_1, X_2) = p_1 H(X_1) + p_2 H(X_2)$$
    
    * *Example*. Consider a game where player have to flip a coin until he comes up with a head, and let $p$ be the probability of obtaining a head from a coin flip
        * The player always has to flip a coin once

            $\to H = H(p)$
        * In case the player failed (with probability $1 - p$), he has to flip the coin once more

            $\to H = H(p, 1-p) + (1 - p) \cdot H(p, 1-p)$
        * In case he failed again, he has to flip the coin once more

            $$H = H(p, 1-p) + (1 - p) \cdot H(p, 1-p) + (1 - p)^2 \cdot H(p, 1-p)$$
        
        * If he failed for a large number of times, he has to flip the coin again and again

            $$H = H(p, 1-p) + (1 - p) \cdot H(p, 1-p) + (1 - p)^2 \cdot H(p, 1-p) + \dots$$

## Derivation of information entropy
**Theorem**. The only $H$ satisfying the axioms above is $H = -K \log_{i=1}^n p_i \log p_i$ where $K > 0$ is a constant
    
$\to$ $K$ amounts to a choice of a unit of measure

**Derivation of the theorem above**.
* For any sample space of possibilities with probabilities $p_1, ..., p_n$

    $\to$ We are always able to divie the sample space into infinitely  many equally likely possibilities 
* Let $A(n) = H(\frac{1}{n}, ..., \frac{1}{n})$
* Equally likely possibilities case: direct prove with "hamburger" theorem
    * Consider dividing $s^m$ equally likely possibilities into leaves of a $s$-ary tree with heigh $m$ where $m$ is sufficiently large

        $\to A(s^m) = m A(s)$
    * Consider dividing $t^n$ equally likely possibilities into leaves of a $t$-ary tree with heigh $n$ where $n$ is sufficiently large

        $\to A(t^n) = n A(t)$
    * By axiom (3), if $s^m \leq t^n \leq s^{m+1}$, then
    
        $$m A(s) \leq n A(t) \leq (m + 1) A(s)$$
    
    * Consider the inequality $s^m \leq t^n \leq s^{m+1}$
        
        $$\begin{aligned}
        &m \log s \leq n \log t \leq (m + 1) \log s\\
        \leftrightarrow &\frac{m}{n} \log s \leq \log t \leq \frac{m}{n} \log s + \frac{1}{n} \log s\\
        \leftrightarrow &\frac{m}{n} \leq \frac{\log t}{\log s} \leq \frac{m}{n} + \frac{1}{n}\\
        \leftrightarrow &\frac{\log t}{\log s} \approx \frac{m}{n}
        \end{aligned}$$
    
    * Consider $m A(s) \leq n A(t) \leq m A(s) + A(s)$
        
        $$\begin{aligned}
        &\frac{m}{n} A(s) \leq A(t) \leq \frac{m}{n} A(s) + \frac{1}{n} A(s)\\
        \leftrightarrow &\frac{m}{n} \leq \frac{A(t)}{A(s)} \leq \frac{m}{n} + \frac{1}{n}\\
        \leftrightarrow &\frac{A(t)}{A(s)} \approx \frac{m}{n}
        \end{aligned}$$
    * From above, $\frac{A(t)}{A(s)} \approx \frac{\log t}{\log s}$, now suppose $A(t) = K \log t$

        $\to$ To ensure that $A(t)$ is monotonically increasing in $n$, $K$ must be positive
* *General case of arbitrary probability $p_1, ..., p_n$*. Direct prove with the law of large numbers
    * First divide the sample space into infinitely many equally likely possibilities and cluster these possibilities into $n$ clusters
        * Cluster $i$ has $p_i \times 100\%$ percent of elements
    * Let $N$ be the number of divided possibilities
        
        $\to$ The entropy of cluster $i$ is $A(p_i N) = K \log (p_i N)$
    * By axiom (3), the entropy of the whole sample space is $K \log N = H(p_1, ..., p_n) + K \sum_{i=1}^n p_i \log (p_i N)$
        * *Explain*. Decompose the choice into two successive choices
            1. Choose cluster among $n$ clusters
            2. Choose an element in the chosen cluster
        * *Consequence*. 
            
            $$H(p_1, ..., p_n) = - K \sum_{i=1}^n p_i \log p_i$$

>**NOTE**. Initially, Shannon defines "entropy" just to lend certain plausibility to some of his later definitions

## Information entropy
**Entropy of the set of probabilities $p_1, ..., p_n$**: $H = - \sum_{i=1}^n p_i \log p_i$
* Interpretation: measure information, choice, and uncertainty
* "Entropy": the form of $H$ is recognized as "entropy" in statistical mechanics

**Entropy of a discrete random variable**: $H(X)$ where $X \sim \{p_1, ..., p_n\}$