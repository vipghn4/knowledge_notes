<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Dirichlet distribution](#dirichlet-distribution)
  - [Introduction](#introduction)
  - [Dirichlet distribution](#dirichlet-distribution-1)
    - [Definitions](#definitions)
    - [Intuitive interpretations of the parameters](#intuitive-interpretations-of-the-parameters)
- [Dirichlet process](#dirichlet-process)
  - [Introduction](#introduction-1)
  - [Theory](#theory)
- [Appendix](#appendix)
  - [Concepts](#concepts)
<!-- /TOC -->

# Dirichlet distribution
## Introduction
**Dirichlet distribution**. Denoted as $\text{Dir}(\alpha)$, is a family of continuous multivariate distributions parameterized by a vector $\alpha$ of positive reals
* *Dirichlet distribution versus Beta distribution*. Dirichlet distribution is a multivariate generalization of the Beta distribution

    $\to$ An alternative name of Dirichlet distribution is multivariate Beta distribution (MBD)
* *Usage*. Prior distributions in Bayesian satistics
    * *Explain*. Dirichlet distribution is the conjugate prior of categorial distribution and multinomial distribution

        $\to$ Just as Beta distribution is a conjugate prior of binomial distribution

**Dirichlet process**. The infinite-dimensional generalization of the Dirichlet distribution

## Dirichlet distribution
### Definitions
**Probability density function**.
* *Assumptions*.
    * $K\geq 2$ is an integer
    * $\alpha_1,\dots,\alpha_K>0$ are real numbers
    * $B(\mathbf{\alpha}) = \frac{\prod_{i=1}^K \Gamma(\alpha_i)}{\Gamma(\sum_{i=1}^K \alpha_i)}$ is the multivariate beta function
* *PDF of the Dirichlet distribution of order $K$ with parameters $\alpha_1,\dots,\alpha_K$*.

    $$f(x_1,\dots,x_K;\alpha_1,\dots,\alpha_K) = \frac{1}{B(\mathbf{\alpha})} \prod_{i=1}^K x_i^{\alpha_i - 1}$$

    where $\{x_k\}_{k=1}^K$ belong to the standard $K-1$ simplex, i.e.

    $$\sum_{i=1}^K x_i=1,\quad \forall i \in \{1,\dots,K\},x_i\geq 0$$

* *Concentration parameters*. $\alpha_1,\dots,\alpha_K$
    * *Intuition*. The rate of occurrences of each class within a categorial distribution
* *Usage*. Model the distribution of the probabilities of classes $(p_1,\dots,p_K)$ in a categorial distribution

**Support**. The set of $K$-dimensional vectors $\mathbf{x}$, whose entries are real numbers within $(0,1)$ such that $\|\mathbf{x}\|_1 = 1$

**Special cases**.
* *Symmetric Dirichlet distribution*. A common special case of Dirichlet distribution, where $\alpha_1=\alpha_2=\dots=\alpha_K$
    * *Usage*. When a Dirichlet over components is called for, but there is no prior favoring one component over another
* *Flat Dirichlet distribution*. When a Dirichlet distribution is symmetric with $\alpha_1=\alpha_2=\dots=\alpha_K=1$

### Intuitive interpretations of the parameters
**The concentration parameter**. Consider symmetric Dirichlet distribution, where $\alpha_1=\dots=\alpha_K=\alpha$

<div style="text-align:center">
    <img src="https://i.imgur.com/Fu7W7Yt.png">
    <figcaption>Concentration parameter's effects</figcaption>
</div>

* *Concentration parameter*. $\alpha$
* *Intuition*. If the sample space of the Dirichlet distribution is interpreted as a discrete probability distribution

    $\to$ $\alpha$ determines how "concentrated" the probability mass of a sample from a Dirichlet distribution is likely to be
* *Effects of $\alpha$*.
    * $\alpha$ can be understood as an inverse variance

        $\to$ The larger $\alpha$ is, the smaller the variance, and the DP will concentrate more of its mass around the mean
    * If $\alpha = 1$, the symmetric Dirichlet distribution is equivalent to a uniform distribution, over the open standard $(K-1)$-simplex

# Dirichlet process
## Introduction
**Dirichlet process**. A family of stochastic processes, whose observations are probability distributions
* *Usage*. 
    * Used in Bayesian inference to describe the prior knowledge about the distribution of random variables
    * Used when modeling data which tends to repeat previous values in a "rich get richer" fashion
* *Idea*. The Dirichlet process is specified by a base distribution $H$ and a real number $\alpha > 0$, called the concentration parameter
    * *Base distribution $H$*. The expected value of the process
        * *Explain*. The Dirichlet process draws distributions around the base distribution, in the way a normal distribution draws a real numbers around its mean
    * *Scaling factor*. Specify how strong the discretization is
        * *Explain*. Even if $H$ is a continuous distribution, the distributions drawn from the Dirichlet process are almost surely discrete
            * *Extreme values of $\alpha$*.
                * *$\alpha \to 0$*. The realizations are all concentrated at a single value
                * *$\alpha \to \infty$*. The realizations become continuous
            * *Other values of $\alpha$*. The realizations are less and less concentration as $\alpha$ increases

**Motivation and background**.
* *Probabilistic models in machine learning*. Probabilistic models are used throughout machine learning to model distribution over observed data
    * *Traditional parametric model $f(x;\theta)$*. Use a fixed and finite number of parameters
        * *Drawback*. Can suffer from over- or under-fitting of data when there is a misfit between model complexity and the amount of data available
            
            $\to$ Model selection is often an important issue in parametric modeling
    * *Bayesian nonparametric approach*. An alternative to parametric modeling and selection
        * *Avoiding underfitting*. By using a model with an unbounded complexity
        * *Avoiding overfitting*. By using the full posterior over parameters
* *Philosophical motivation*. Typically, we assume that we have an underlying and unknown distribution, which we wish to infer given some observed data
    * *Assumptions*.
        * $x_1,\dots,x_n$ are our i.i.d observations
        * $x_i\sim F$ where $F$ is unknown
    * *Bayesian approach*. Place a prior over $F$, then compute the posterior over $F$ given data
        * *Traditional approach*. $F$ is constrained by a parametric family
        * *Nonparametric approach*. Use a prior over distributions with wide support, typically the support being the space of all distributions

            $\to$ Since the distribution space is large, it is important that posterior computations are tractable
* *Dirichlet process*. Currently one of the most popular Bayesian nonparametric models
    * *Origin*. Fisr formalized for general Bayesian statistical modeling, as a prior over distributions with wide support yet tractable posteriors
    * *Drawback*. 
        * Draws of a Dirichlet process are discrete distributions
      * Generalizations to more general priors did not have tractable posterior inference until the development of Markov chain Monte Carlo (MCMC) techniques

## Theory
**Dirichlet process**. A stochastic process, whose sample paths are probability measures with probability one

$\to$ Draws from a DP can be interpreted as random distributions
* *Stochastic process (in this context)*. Distribution over function spaces, with sample paths being random functions drawn from the distribution

**Intuitive explanation of the DP as an infinite dimensional generalization of Dirichlet distribution**.
* *Assumptions*.
    * Consider a Bayesian mixture model of $K$ components

        $$\begin{aligned}
        &\pi|\alpha \sim \text{Dir}(\frac{\alpha}{K},\dots,\frac{\alpha}{K}) & \theta^*_k|H \sim H\\
        &z_i|\pi \sim \text{Mult}(\pi) & x_i|z_i,\{\theta_k^*\} \sim F(\theta_{z_i}^*)
        \end{aligned}$$

    * $\pi$ is the mixing proportion
    * $\alpha$ is the pseudocount hyperparameter of the Dirichlet prior
    * $H$ is the prior distribution over the component parameters $\theta_k^*$
    * $F(\theta)$ is the component distribution parametrized by $\theta$
* *Observations*. For large $K$, due to the way we parametrized the Dirichlet prior over $\pi$

    $\to$ The number of components typically used to model $n$ data items becomes independent of $K$ and is approximately $O(\alpha \log n)$
    * *Consequence*. The mixture model stays well-defined as $K\to\infty$, leading to an infinite mixture model
* *Usage*. First proposed as 
    * A way to sidestep the difficult problem of determining the number of components in a mixture
    * A nonparametric alternative to finite mixtures, whose size can grow naturally with the number of data items
* *DP mixture model*. The more modern definition of the probabilistic model above
    * *DP as infinite mixture model*. The DP appears as the $K\to\infty$ limit of the random discrete probability measure

        $$\sum_{k=1}^K \pi_k \delta_{\theta_k^*}$$

        where $\delta_\theta$ is a point mass centered at $\theta$

# Appendix
## Concepts
**Almost surely event**. An event is said to happen almost surely if it happens with probability $1$
* *Explain*. The set of possible exceptions may be non-empty, but it has probability 0