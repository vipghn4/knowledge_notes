<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Moments](#moments)
  - [Mean, median, and mode](#mean-median-and-mode)
  - [Interpreting moments](#interpreting-moments)
- [Moment generating functions](#moment-generating-functions)
  - [Moment generating functions](#moment-generating-functions-1)
  - [Probability generating functions](#probability-generating-functions)
- [Discussion](#discussion)
<!-- /TOC -->

# Introduction
**Reference**: Introduction to probability (Joseph K. Blitzstein & Jessica Hwang)

# Moments
## Mean, median, and mode
**Descriptive statistics**:
* Mode: 
    * Useful case: when the distribution is approximately normal (i.e. there are just a few modes)
    * Useless case: when the distribution is approximately uniform (i.e. there are many modes)
* Median:
    * Useful case: find typical value of a random variable
        * Explain: less sensitive to extreme values (compared to the mean)
    * Useless case: find the total value of random variables

**Predictive statistics**: using mean, median, or mode are based on how we evaluate the predicted result

## Interpreting moments
**Skewness**: $\text{Skew}(X) = E(\frac{X - \mu}{\sigma})^3$
* Purpose: measure the symmetry of the distribution
* Why third central moment for symmetry measurement:
    * First standardized moment: always $0$
    * Higher-order moments: harder to calculate, and more sensitive to outliers

**Kurtosis**: $\text{Kurtosis}(X) = E(\frac{X - \mu}{\sigma})^4$

# Moment generating functions
## Moment generating functions
**Generating functions**: a powerful tool in combinatorics and probability
* Explain: it bridge between sequences of numbers and the world of calculus
* Idea of generating function:
    * Step 1: start with a sequence of numbers
    * Step 2: create a continuous function (i.e. the generating function) which encodes the sequence
* Consequence: we have all the tools of calculus for manipulating the generating function
* Examples:
    * Moment generating function (MGF)
    * Probability generating function (PGF)

**Moment generating function**: $M(t) = E(e^{t X})$
* The function of $t$: a book-keeping device that we introduce so that we can use calculus instead of working with a discrete sequence of moments
* Importance of MGF:
    * MGF encodes the moments of a random variable
    * MGF determines the distribution of a random variable
    * MGF makes it easy to find the distribution of a sum of independent random variables
        * Formal: if $X$ and $Y$ are independent then $M_{X + Y}(t) = M_X(t) M_Y(t)$
        * Method:
            * Step 1: calculate the MGF of $X + Y$
            * Step 2: look up on available MGFs to see the family of distribution of $X + Y$ 

**Characteristic function**: $\phi(t) = E(e^{i t X})$

>**NOTE**: this is the Fourier transform for non-statisticians

## Probability generating functions
**Probability generating functions**: $E(t^X)$ where $X$ is a random variable taking non-negative integers only
* From PGF to probability: $P(X = k) = \frac{1}{k!} \frac{\partial^k E(t^X)}{\partial^k t}(0)$
* Usage: conquer a seemingly intractable counting problem
    * Step 1: write $E(t^{\sum_i X_i}) = \sum_{i=0}^\infty \alpha_i t^i$
    * Step 2: calculate $P(X = k) = \alpha_k$
* Relationship to MGFs: $E(t^X) = E(e^{X \log t})$ (i.e. the MGF evaluated at $\log t$)

**Conquer a seemingly intractable counting problem**:
* Problem: calculate the probability that the sum of $6$ rolling dices is $18$
* Naive solution: hard counting (i.e. take too much time)
* Solution using PGFs:
    * Inputs: $X_1, ..., X_6$ are individual rolls
    * Step 1 - expression reduction: the PGF of $X_1$ is $E(t^{X_1}) = \frac{1}{6} \sum_{x=1}^6 t^x$

    $\hspace{1.0cm} \rightarrow E(t^{\sum_i X_i}) = \frac{t^6}{6^6} (\sum_{x=0}^5 t^x)^6$
    * Step 2 - polynomial extraction: $E(t^{\sum_i X_i}) = \frac{t^6}{6^6} \frac{(t^6 - 1)^6}{(t - 1)^6}$
        * $(t^6 - 1)^6 = \sum_i \binom{6}{i} (-1)^{6-i} t^{6i}$
        * Since we only care about $t \to 0$, it's clear that $t < 1$ and we can conclude that $1 - t^\infty \approx 1$

        $\hspace{1.0cm} \rightarrow \frac{1}{(1 - t)^6} = (\sum_{i=0}^\infty t^i)^6 = \sum_k a_k t^k$ ($a_k$ can be easily found)
    * Step 3: from above, we can easily find the coefficient of $t^{18}$

# Discussion
* Mean isn't the only useful notion of average and variance isn't the only useful notion of spread