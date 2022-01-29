<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Generalized additive model](#generalized-additive-model)
  - [Introduction](#introduction)
  - [Additive model](#additive-model)
- [Appendix](#appendix)
  - [Concepts](#concepts)
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
* *Estimating $s(X)$. Use scatterplot smoother, e.g. running mean, running median, running least-square line, kernel estimate, etc.
* *Formal*. For the $p$ covariates $\mathbf{X}=(X_1,\dots,X_p)$
    * We can use a $p$-dimensional scatterplot smoother to estimate $s(X)$, or
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

* *Alternating conditional expectation (ACE) model*.

    $$E(\theta(Y)|\mathbf{X}) = \sum_{j=1}^p s_j(X_j)$$

    where $\theta(\cdot)$ is a transformation of the response

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

# Appendix
## Concepts
**Backfitting algorithm**. A simple iterative procedure used to fit a generalized additive model
* *Assumptions*.
    * $X_1,\dots,X_p$ is a variable in our $p$-dimensional predictor $X$
    * $Y$ is our outcome variable
    * $\epsilon$ is the inherent error, which is assumed to have mean zero
    * $f_j$ represents unspecified smooth functions of $X_j$
    * $\alpha$ is left unidentifiable as one can add any constants to any of $f_j$ and subtract this value from $\alpha$
* *Additive models*. A class of non-parametric regression models of the form

    $$Y = \alpha + \sum_{j=1}^p f_j(X_j) + \epsilon$$

    * *Common rectification*. Constrain

        $$\forall j\in\{1,\dots,p\},\sum_{i=1}^N f_j (X_{ij}) = 0$$

        and leave

        $$\alpha = \frac{1}{N} \sum_{i=1}^N y_i$$

* *Backfitting algorithm*.
    * *Initialization*. 
    
        $$\hat{\alpha} = \frac{1}{N} \sum_{i=1}^N y_i,\quad \forall j\in\{1,\dots,p\}, \hat{f}_j = 0$$
    
    * *Iteration*. Iterate the following steps until $\hat{f}_j$ converges
        * *Backfitting step*. 
            
            $$\hat{f}_j = \text{Smooth}[\{y_i - \hat{\alpha} - \sum_{k\neq j} \hat{f}_k(x_{ij}) \}_{i=1}^N]$$

        * *Mean centering of estimated function*. 

            $$\hat{f}_j = \hat{f}_j - \frac{1}{N} \sum_{i=1}^N \hat{f}_j (x_{ij})$$

            >**NOTE**. Theoretically, this step is not required, since the function estimates are constrained to sum to zero. However, we still carry out this step due to numerical issues

* *Smooth operator*. Typically chosen to be cubic spline smoother, or other appropriate fitting operation, e.g.
    * Local polynomial regression
    * Kernel smoothing methods
* *Reference*. https://en.wikipedia.org/wiki/Backfitting_algorithm

**Local scoring algorithm**. Analogous to the iterative reweighted least squares algorithm for solving likelihood and nonlinear regression equations
* *Idea*. At each iteration, an adjusted dependent variable is formed and an additive regression model is fit using the backfitting algorithm

**Generalized linear model (GLM)**.

**Cox model**.

## References
* *Genearlized additive models* - T. J. Hastie and R. J. Tibshirani (1986)