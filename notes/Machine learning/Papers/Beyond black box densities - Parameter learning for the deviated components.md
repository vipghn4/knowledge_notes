<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Beyond black box densities - Parameter learning for the deviated components](#beyond-black-box-densities---parameter-learning-for-the-deviated-components)
  - [Introduction](#introduction)
  - [Related works](#related-works)
- [Appendix](#appendix)
  - [Concepts](#concepts)
<!-- /TOC -->

# Beyond black box densities - Parameter learning for the deviated components
## Introduction
**Typical data-driven learning process**. Consist of iterative steps, including model training and fine-tuning
* *Continual learning*. More data in-take leading to further model re-training and refinement
    * *Explain*. As more samples come in and exhibit more complex patterns
        
        $\to$ The initial model may be obsolete, risks being discarded or absorbed into a richer class of models to adapt better to increased complexity
* *Problems*. 
    * Much resources are required to train complex models on a rich data population
    * Many practical models have become so complex that make them hard to properly evaluate and interpret
        
        $\to$ Aside from the predictive performance they may as well be considered as black boxes
* *Desiderata*. As data populations evolve and so must the learning models, several desiderata remain worthy
    * The ability to adapt to new complexity while retaining aspects of old wise model
    * The ability to interpret the changes

**Brief about the paper**. Investigate a class of complex models for density estimation, which are receptive to adaptation, reuse, and interpretability
* *Assumptions*. 
    * There is an existing distribution $h_0$, which may have been obtained a priori by some means, for the data population of interest

        $\to$ $h_0$ may be difficult to interpret
    * As more samples come in, and data population changes

        $\to$ The true density may deviate from $h_0$
* *Problem of interest*. Learn and interpret the deviation from $h_0$

**Mathematical modeling**. Use deviating mixture model, i.e. a mixture distribution, to represent the deviation
* *Assumption*.
    * $x\in\mathbb{R}^d$ is a random variable
    * $F(x,G_*) = \sum_{i=1}^{k_*} p^*_i[f(x|\theta_i^*)]$ is the mixture distribution for the density components deviating from $h_0$
        * Deviating components are from a known family of density function $f$
* *Deviating mixture model*.

    $$p_{\lambda^* G_*}(x) = (1 - \lambda^*) h_0(x) + \lambda^* F(x,G_*)$$

* *Model parameters*. 
    * *Mixing proportion*. $\lambda^*\in[0,1]$
    * *Mixing measure*. $G_* = \sum_{i=1}^{k_*} p^*_i \delta_{\theta^*_i}$ where $k_*\geq 1$ is the number of deviated components
        
        $\to$ $G_*$ represents heterogeneous patterns of the deviation
* *Conclusion*. The choice of $F(x,G_*)$ allows to express complex deviation from $h_0$

## Related works
**Dominant approach in classical statistics to address increased complexity of data populations**. Use hypothesis testing
* *Idea*. 
    * *Alternative (possibly composite) hypothesis*. Represented by a class of distributions
    * *Null hypothesis*. Represented by $h_0$
* *Drawback*. Due to the constraint for obtaining simple and theoretically valid test statistics, i.e. to accept or reject the null hypothesis
    
    $\to$ The testing approaches were restricted to simple choices of distribution for the null and alternative hypotheses

**Classs of contaminated mixture models for density estimation**.
* *Idea*. The data are assumed to be sample from a mixture of unknown distributions $P_0$ and $Q$

    $\to$ $P_0$ and $Q$ are then estimated
* *Formal*. 
    * *Scenario*. A distribution $F_b$, for which reasonable assumptions can be made, is contaminated by an arbitrary distribution $F_s$

        $\to$ This results in $F(x) = \alpha F_s(x) + (1-\alpha) F_b(x)$
    * *Assumptions*.
        * $F_b$ is a known background c.d.f
        * $\alpha\in[0,1]$ is unknown mixing proportion
        * $F_s\neq F_b$ is an unknown signal c.d.f
    * *Mixture model of interest*.

        $$F(x) = \alpha F_s(x) + (1-\alpha) F_b(x)$$

    * *Problem of interest*. Given a random sample from $F$, nonparametrically estimate $F_s$ and $\alpha$
    * *Reference*. https://arxiv.org/pdf/1204.5488.pdf
* *Drawback*. This method does not always guarantee the identifiability, i.e. uniqueness, of the mixing weight or mixture components $P_0,Q$

    $\to$ It is virtually impossible to interpret the model parameters for the data domain

**Estimating parameters of mixture distributions**. An essential problem in mixture models



# Appendix
## Concepts
**Mixing measure**. A discrete probability measure $G$ of the form

$$G=\sum_{i=1}^k p_i \delta_{\theta_i}$$

* *Mixture model from mixing measure*. Given a family $f(x;\theta_i)$ of distributions, we can construct a mixture model as

    $$f(x;G) = \int_\Omega f(x|\theta) dG(\theta)=\sum_{i=1}^k p_i f(x;\theta_i)$$