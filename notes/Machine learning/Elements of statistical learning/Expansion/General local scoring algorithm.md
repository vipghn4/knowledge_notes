<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [General local scoring algorithm](#general-local-scoring-algorithm)
  - [Backfitting algorithm](#backfitting-algorithm)
  - [General local scoring algorithm](#general-local-scoring-algorithm-1)
<!-- /TOC -->

# General local scoring algorithm
## Backfitting algorithm
**Additive models**.
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

**Backfitting algorithm**. A simple iterative procedure used to fit a generalized additive model
* *Intuition*. If the additive model is correct, then, for any $k$

    $$E(Y - \alpha - \sum_{j\neq k} f_j(X_j)|X_k) = f_k(X_k)$$

    * *Idea*. Assume that we have good estimates $\hat{f}_1,\dots,\hat{f}_{p-1}$, i.e. $E[\hat{f}_j(X_j) - f_j(X_j)]\approx 0$, then

        $$E(Y - \hat{\alpha} - \sum_{j=1}^{p-1} \hat{f}_j(X_j)|X_p) = f_p(X_p)$$
    
    * *Explain*. We choose $f_p$ to minimize the MSE

        $$E(\|Y - \hat{\alpha} - \sum_{j=1}^{p-1} \hat{f}_j(X_j)\|^2)$$
* *Initialization*. 

    $$\hat{\alpha} = \frac{1}{N} \sum_{i=1}^N y_i,\quad \forall j\in\{1,\dots,p\}, \hat{f}_j = 0$$

* *Iteration*. Iterate the following steps until $\hat{f}_j$ converges
    * *Backfitting step*. 
        
        $$\hat{f}_j = \text{Smooth}[\{y_i - \hat{\alpha} - \sum_{k\neq j} \hat{f}_k(x_{ij}) \}_{i=1}^N]$$

    * *Mean centering of estimated function*. Motivated by the common rectification constraint above

        $$\hat{f}_j = \hat{f}_j - \frac{1}{N} \sum_{i=1}^N \hat{f}_j (x_{ij})$$

        >**NOTE**. Theoretically, this step is not required, since the function estimates are constrained to sum to zero. However, we still carry out this step due to numerical issues

* *Termination*. When

    $$\frac{1}{n}\sum_{i=1}^n \|y_i - \alpha - \sum_{j=1}^p \hat{f}_j (x_{ij})\|^2$$

    fails to decrease, or satisfies the convergence criterion
* *Smooth operator*. Typically chosen to be cubic spline smoother, or other appropriate fitting operation, e.g.
    * Average smoothing
    * Local polynomial regression
    * Kernel smoothing methods
* *Reference*. 
    * https://en.wikipedia.org/wiki/Backfitting_algorithm
    * http://rafalab.github.io/pages/754/section-07.pdf

**Convergence criterion for GAM**.

$$\frac{\sum_{i=1}^n \sum_{j=1}^p [\hat{f}_j^{(m-1)}(x_{ij}) - \hat{f}_j^{(m)}(x_{ij})]^2}{1 + \sum_{i=1}^n \sum_{j=1}^p \hat{f}^{(m-1)}_j (x_{ij})^2}\leq \epsilon$$

## General local scoring algorithm
**Idea**. The estimating procedure for generalized additive models consists of two loops
* *Outer loop*. Local scoring algorithm
* *Inner loop*. A weighted backfitting algorithm

**General local scoring algorithm**.
* *Initialization*.
    
    $$\hat{\alpha} = \frac{1}{N} \sum_{i=1}^N y_i,\quad \forall j\in\{1,\dots,p\}, \hat{f}_j = 0$$
    
* *Iteration*.
    1. Compute predictor

        $$\eta_i = \hat{\alpha} + \sum_{j=1}^p \hat{f}_j(x_{ij})$$

    2. Compute mean, given the relationship $g(\mu) = \eta$
        
        $$\mu_i = g^{-1}(\eta_i)$$
    
    3. Compute weights 
        
        $$w_i = E[(Y_i - \mu_i)^2]^{-1} \cdot \bigg[\bigg(\frac{\partial \mu}{\partial \eta}\bigg)_i\bigg]^2$$
    
    4. Compute adjusted dependent variable

        $$z_i = \eta_i + (y_i - \mu_i)\cdot \bigg(\frac{\partial\eta}{\partial\mu}\bigg)_i$$
    
    5. Fit an additive model to $z$ using the backfitting algorithm with weights $w$ to obtain estimated $\hat{f}_j$
* *Termination*. The convergence is satisfied, or the deviance fails to decrease
* *Reference*. https://documentation.sas.com/doc/en/pgmsascdc/9.4_3.3/statug/statug_gam_details06.htm

**Convergence criterion for GAM**.

$$\frac{\sum_{i=1}^n w_i \sum_{j=1}^p [\hat{f}_j^{(m-1)}(x_{ij}) - \hat{f}_j^{(m)}(x_{ij})]^2}{\sum_{i=1}^n w_i [1 + \sum_{j=1}^p \hat{f}^{(m-1)}_j (x_{ij})^2]}\leq \epsilon$$