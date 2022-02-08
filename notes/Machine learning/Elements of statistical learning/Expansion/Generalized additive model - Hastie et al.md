<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Generalized additive model](#generalized-additive-model)
  - [Introduction](#introduction)
  - [Additive model](#additive-model)
  - [The curse of dimensionality](#the-curse-of-dimensionality)
- [Appendix](#appendix)
  - [References](#references)
<!-- /TOC -->

# Generalized additive model
## Introduction
**Likelihood-based regression models**. Important tools in data analysis
* *Typical scenario*. 
    * A likelihood is assumed for a response variable $Y$,
    * The mean or some other parameter is modeled as a linear function $\sum_{j=1}^p \beta_j X_j$ of a set of covariates $X_1,\dots,X_p$
* *Parameter estimation*. The parameters of the linear function are then estimated by maximum likelihood, i.e. least square

**Trending**. Move away from linear functions and model the dependence of $Y$ on $X_1,\dots,X_p$ in a more nonparametric fashion

$$Y=s(X) + \epsilon$$

where $s(X)$ is an unspecified smooth function
* *Estimating $s(X)$*. Use scatterplot smoother, e.g. running mean, running median, running least-square line, kernel estimate, etc.
* *Formal*. For the $p$ covariates $\mathbf{X}=(X_1,\dots,X_p)$
    * We can use a $p$-dimensional scatterplot smoother to estimate $s(\mathbf{X})$, or
    * Assume a less general model, e.g. the additive model

        $$s(\mathbf{X}) = \sum_{j=1}^p s_j(X_j)$$

        and estimate it in an iterative manner

**Generalized additive model**. Replace the linear function $\sum_{j=1}^p \beta_j X_j$ by an additive function $\sum_{j=1}^p s_j(X_j)$
* *Local scoring algorithm*. The technique for estimating $s_j(\cdot)$'s, i.e. use scatter-plot smoothers to generalize the usual Fisher scoring procedure for computing MLE
    * *Example*. Consider the linear logistic model for binary data specifying

        $$\log \frac{p(\mathbf{X})}{1 - p(\mathbf{X})} = \beta_0 + \beta_1 X_1 + \dots + \beta_p X_p$$

        where $p(\mathbf{X}) = P(Y=1|\mathbf{X})$

        $\to$ This is generalized to

        $$\log \frac{p(\mathbf{X})}{1 - p(\mathbf{X})} = \sum_{j=1}^p s_j(X_j)$$

        with local scoring procedure providing nonparametric, smooth estimates of $s_j(\cdot)$'s
    * *Consequence*. The smooth functions produced by the local scoring procedure can be used as a data description, for prediction, or to suggest covariate transformations
* *Semi-parametric model*. We can allow a smooth estimate for all of the covariates, or force a linear fit for some of them
    * *Usage*.
        * Naturally arise if categorial covariates are present
        * Useful if, for reasons specific to data at hand, a linear fit was desired for certain covariates

**Extensions of generalized additive model**.
* *Projection pursuit regression model*.

    $$E(Y|\mathbf{X}) = \sum_{j=1}^p s_j(\mathbf{\alpha}_j^T \mathbf{X})$$

    where $\mathbf{\alpha}_j$ are found by numerical search, and $s_j(\cdot)$'s are estimated by smoothers

* *Alternating conditional expectation (ACE) model*. Generalize the additive model by estimating a transformation $\theta$ of the response, i.e.

    $$E(\theta(Y)|\mathbf{X}) = \sum_{j=1}^p s_j(X_j)$$

## Additive model
**Additive model**. A compromise between parametric linear and non-linear regression
* *Motivation*. With multiple covariates, non-linear regression requires prohibitively large amounts of data and becomes difficult to visualize, i.e. the curse of dimensionality
* *Idea*. Replace the linear predictor

    $$X_1\beta_1 + \dots + X_p \beta_p$$

    by

    $$f_1(X_1) + \dots + f_p(X_p)$$

    where $f_1,\dots,f_p$ are smooth data-driven transformations

* *Model assumption*. The ground-truth can be modeled as

    $$Y=\sum_{j=1}^p f_j(X_j) + \epsilon$$

    where $\epsilon_i$ is a random noise
* *Drawback*. Additive models only have good statistical and computational behavior when $p$ is not large relative to $n$

    $\to$ Their usefulness is limited in the high-dimensional setting

## The curse of dimensionality
**Linear regression**. 
* *Convergence rate*. $\sigma^2 + a_\text{linear} + O(n^{-1})$
    * *Intrinsic noise around the true regression function*. $\sigma^2$
    * *Squared approximation bias*. $a_\text{linear}$
    * *Estimation variance*. $O(n^{-1})$

    >**NOTE**. Other parametric models generally converge at the same rate

* *Pros*. The model converges very quickly as we get more data
* *Cons*. The true regression function is hardly ever linear

    $\to$ The model may underfit the data

**Completely non-parametric regression models**. Kernel regression, local polynomials, k-NN, etc.
* *Convergence rate*. $\sigma^2 + O(n^{-\frac{4}{p+4}})$

    $\to$ As $p$ grows, the rate get slower and slower
* *Pros*. The limiting approximation bias is zero, at least for some reasonable regression function
* *Cons*. The convergence rate is lower
    * *Explain.*. We need to use the data to 
        * Figure out the coefficients of a parametric model
        * Figure out the sheer shape of the regression function

**Reasoning for slow convergence of non-parametric models**.
* *Model of interest*. The smoothing method $\hat{r}(x)$ is an average over $y_i$ for $x_i$ near $x$
    
    $\to$ The volume within $\epsilon$ of $x$ is $O(\epsilon^p)$
* *Consequence*. To get the same density, i.e. points per unit volume, around $x$

    $\to$ Exponentially more data is required, as $p$ grows
* *Conclusion*. Completely unstructured non-parametric regressions won’t work very well in high dimensions, at least not with plausible amounts of data

**Additive models and curse of dimensionality**. 
* *Idea*. We can estimate each $f_j$ by a simple one-dimensional smoothing
    
    $\to$ Each individual estimation has convergence rate of $O(n^{-4/5})$
* *Convergence rate*. $\sigma^2 + a_\text{additive} + O(n^{-4/5})$
    * *Comparison with linear model*. Since linear models are a sub-class of additive models, we have

        $$a_\text{additive} \leq a_\text{linear}$$
    
    * *Consequence*. The only time to prefer linear models to additive models is when $n$ is so small, that $O(n^{-4/5})\geq O(n^{-1})+\epsilon$
* *Drawback*. Not every regression function is additive

    $\to$ Additive models have, even asymptotically, some approximation bias

# Appendix
## References
* *Genearlized additive models* - T. J. Hastie and R. J. Tibshirani (1986)
* https://www.stat.cmu.edu/~cshalizi/350/lectures/21/lecture-21.pdf