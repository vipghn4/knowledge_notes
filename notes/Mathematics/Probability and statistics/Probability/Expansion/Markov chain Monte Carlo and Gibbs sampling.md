<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Markov Chain Monte Carlo and Gibbs sampling](#markov-chain-monte-carlo-and-gibbs-sampling)
  - [Introduction](#introduction)
  - [Monte Carlo integration](#monte-carlo-integration)
    - [Importance sampling](#importance-sampling)
  - [Introduction to Markov chains](#introduction-to-markov-chains)
- [Reference](#reference)
<!-- /TOC -->

# Markov Chain Monte Carlo and Gibbs sampling
## Introduction
**Major limitations towards widespread implementation of Bayesian approaches**. Obtaining the posterior distribution often requires the integration of high-dimensional functions

$\to$ This can be computationally very difficult

**Markov chain Monte Carlo (MCMC) methods**. Attempt to simulate direct draws from some complex distribution of interest
* *Meaning of method name*. One uses the previous sample values to random generate the next sample value

    $\to$ This is essentially generating a Markov chain
    * *Explain*. The transition probabilities between sample values are only a function of the most recent sample value
* *Origin*. MCMC methods originates from the Metropolis algorithm, an attempt by physicists to compute complex integrals 
    * *Idea of Metropolis algorithm*. 
        * Express complex integrals as expectations of some distribution
        * Estimate the expectation by drawing samples from the distribution

**Gibbs sampler**. A MCMC method, which is very widely applicable to a broad class of Bayesian problems
* *Origin*. Originate from image processing

## Monte Carlo integration
**Monte Carlo integration**. The original Monte Carlo approach 
* *Motivation*. A method developed by physicists to use random number generation to compute integrals
* *Idea*. Suppose we wish to compute a complex integral $\int_a^b h(x) dx$
    1. We (hopefully) decompose $h(x)$ into the production of a function $f(x)$ and a p.d.f $p(x)$ defined over the interval $(a,b)$, then

        $$\int_a^b h(x)dx = \int_a^b f(x) p(x) dx = E_{p(x)}[f(x)]$$
    
    2. We then draw a large number $x_1,\dots,x_n$ of random variables from $p(x)$, then

        $$\int_a^b h(x)dx = E_{p(x)}[f(x)] \approx \frac{1}{n}\sum_{i=1}^n f(x_i)$$
* *Usage*. Approximate posterior, or marginal posterior, distributions required for a Bayesian analysis
    * *Assumptions*. 
        * The integral $I(y) = \int f(y|x) p(x) dx$ is the one we want to approximate, i.e. by

            $$\hat{I}(y) = \frac{1}{n} \sum_{i=1}^n f(y|x_i)$$

        * $x_i$ are draws from $p(x)$
    * *The estimated Monte Carlo standard error*. The sample variance of $\{f(y|x_i)\}_{i=1}^n$ divided by $n$

        $$\begin{aligned}
        \text{SE}^2[\hat{I}(y)] &= \text{Var}[\hat{I}(y)-I(y)]\\
        &\approx\frac{1}{n} \bigg(\frac{1}{n-1} \sum_{i=1}^n \big(f(y|x_i) - \hat{I}(y)\big)^2\bigg)
        \end{aligned}$$

### Importance sampling
**Importance sampling**. A general technique for estimating properties of a particular distribution, while only having samples generated from a different distribution than the distribution of interest

**The method of importance sampling**.
* *Assumptions*.
    * $p(x)$ is a rough approximation of $q(x)$, i.e. the density of interest
    * $x_i$ are drawn from $p(x)$
* *Observation*.

    $$\begin{aligned}
    \int f(x)q(x)dx &= \int f(x) \frac{q(x)}{p(x)} p(x) dx\\
    &=E_{p(x)}\bigg[f(x) \frac{q(x)}{p(x)}\bigg]
    \end{aligned}$$

* *Importance sampling*.

    $$\int f(x) q(x) \approx \frac{1}{n} \sum_{i=1}^n f(x_i) \frac{q(x_i)}{p(x_i)}$$

* *Terminologies*.
    * *Likelihood ratio*. $q(x)/p(x)$
    * *Importance distribution*. $p(x)$
    * *Nomial distribution*. $q(x)$
* *Requirement on $p(x)$*. $p(x)>0$ whenever $f(x)q(x)\neq 0$

**Self-normalized importance sampling**.
* *Problem*. Sometimes, we can only compute an unnormalized version of $q$ or $p$, i.e.

    $$q_u(x) = cq(x),\quad p_u(x)=bp(x)$$

    where $c > 0$ and $b > 0$ are unknown

* *Idea*. Compute $w_u(x)=\frac{q_u(x)}{p_u(x)} = (c/b) \cdot \frac{q(x)}{p(x)}$ then consider

    $$\frac{\sum_{i=1}^n w_u(x_i) f(x_i)}{\sum_{i=1}^n w_u(x_i)}$$

    where $x_i\sim q$ are independent

* *Theorem*. Let $w_i=\frac{q(x_i)}{p(x_i)}$

    $$\int f(x)q(x)dx \approx \hat{I} =\sum_{i=1}^n \frac{w_i f(x_i)}{\sum_{i=1}^n w_i}$$

    * *Proof*.
        * $\lim_{n\to\infty} \frac{1}{n}\sum_{i=1}^n w_i f(x_i) = E_{q(x)}[f(x)]$
        * $\lim_{n\to\infty} \frac{1}{n}\sum_{i=1}^n w_i=E_{q(x)}[1]=1$

* *Monte Carlo variance*. 

    $$\text{Var}(\hat{I})=\sum_{i=1}^n \frac{w_i (f(x_i) - \hat{I})^2}{\sum_{i=1}^n w_i}$$

* *Requirement on $p(x)$*. $p(x)>0$ whenever $q(x)>0$, even if $f(x)$ is zero with high probability

**Reference**. https://statweb.stanford.edu/~owen/mc/Ch-var-is.pdf

## Introduction to Markov chains
**Markov chain (recall)**.
* *Assumptions*.
    * $X_t$ is the value of a random variable at time $t$
    * $\pi_j(t)=P(X_t=s_j)$ is the probability that the chain is in state $j$ at time $t$
    * $\mathbf{\pi}(t)$ is the row vector of the state space probabilities at step $t$
    * $p_{ij}^n=P(X_{t+n}=s_j|X_t=s_i)$ is the $n$-step transition probability from state $i$ to state $j$
* *State space*. The range of possible $X$ values
* *Markov process*. $X_t$ is a Markov process if the transition probabilities between different values in the state space depend only on the random variable's current state, i.e.

    $$P(X_{t+1}=s_j|X_0=s_k,\dots,X_t=s_i)=P(X_{t+1}=s_j|X_t=s_i)$$

* *Markov chain*. A sequence of random variables $(X_0,\dots,X_n)$ generated by a Markov process
* *Transition probabilities (or transition kernel)*. $P(i,j)=P(i\to j)=P(X_{t+1}=s_j|X_t=s_i)$
* *Initial probability vector*. $\mathbf{\pi}(0)$
    * *Typical value*. Zero except for a single element of $1$, corresponding to the process starting at the particular state

**Chapman-Kolomogrov equation**. The probability that a Markov chain has state value $s_i$ at time $t+1$

$$\begin{aligned}
\pi_i(t+1)&=P(x_{t+1}=s_i)\\
&=\sum_k P(X_{t+1}=s_i|X_t=s_k) \cdot P(X_t = s_k)
\end{aligned}$$

* *Compact form*. $\mathbf{\pi}(t+1)=\mathbf{\pi}(t) \cdot \mathbf{P} = \mathbf{\pi}(0) \cdot \mathbf{P}^t$

**Irreducible Markov chain**. If there exists a positive integer such that $p_{ij}(n_{ij}) > 0$ for all $(i,j)$
* *Explain*. All states communicate with each other, as one can always go from any state to any other state

**Aperiodic Markov chain**. When the number of steps required to move between two states is not required to be multiple of some integer
* *Explain*. The chain is not forced into some cycle of fixed length between certain states
* *Period $d(k)$ of a state $k$ of a Markov chain*. $d(k)=\text{gcd}\{m\geq 1:p_{kk}^m>0\}$
    
    $\to$ $p^m_{kk}=0$ whenever $m$ is not divisible by $d$
* *Aperiodic state*. State $k$ is aperiodic if When $d(k)=1$
* *Aperiodic Markov chain*. A Markov chain whose all states are aperiodic

**Stationary distribution $\mathbf{\pi}^{*}$**. The distribution satisfying $\mathbf{\pi}^*=\mathbf{\pi}^* \mathbf{P}$

$\to$ $\mathbf{\pi}^*$ is the left eigenvector associated with the eigenvalue $\lambda=1$ of $\mathbf{P}$
* *Conditions for a stationary distribution*. The chain is irreducible and aperiodic
    * *Explain*.
* *Sufficient condition for a unique stationary distribution*. The detailed balance equation holds, for all $i$ and $j$, i.e.

    $$P(i\to j)\pi_j^*=P(k\to j)\pi_k^*$$

# Reference
* http://www.stat.columbia.edu/~liam/teaching/neurostat-spr11/papers/mcmc/mcmc-gibbs-intro.pdf
* https://ocw.mit.edu/courses/aeronautics-and-astronautics/16-90-computational-methods-in-aerospace-engineering-spring-2014/probabilistic-methods-and-optimization/error-estimates-for-the-monte-carlo-method/