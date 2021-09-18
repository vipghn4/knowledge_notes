<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Convergence of estimators](#convergence-of-estimators)
- [Discussion](#discussion)
<!-- /TOC -->

# Convergence of estimators
**Convergence of MLE**:
* Assumptions:
    * $p = (p_1, ..., p_n)$ is the true probability vector of the data indexed by the true $\theta$
        * Formal: $p_i = f(x_i|\theta)$
    * $f$ is the true parametrization of the data distribution
    * $\hat{p} = (\hat{p}_1, ..., \hat{p}_n)$ is the probability vector indexed by the estimate $\hat{\theta}$ of $\theta$
        * Formal: $\hat{p}_i = \hat{f}(x_i|\hat{\theta})$
    * $\hat{f}$ is the chosen parametrization of the data distribution
* Observations:
    * The likelihood function (w.r.t $\hat{f}$) is $\hat{f}_n(\textbf{x}|\hat{\theta}) = \prod_i \hat{f}(x_i|\hat{\theta})^{n_i}$ where $n_i$ is the number of observations of type $i$ in the observed data
        * $\log \hat{f}_n(\textbf{x}|\hat{\theta}) = \sum_i n_i \log \hat{f}(x_i|\hat{\theta}) = n \sum_i \frac{n_i}{n} \log \hat{f}(x_i|\hat{\theta})$
        * As $n \to \infty$, $\log \hat{f}_n(\textbf{x}|\hat{\theta}) \to n \sum_i p_i \log \hat{f}(x_i|\hat{\theta})$
    * Maximizing $\hat{f}_n(\textbf{x}|\hat{\theta})$ is equivalent to minimizing $- \sum_i p_i \log \hat{f}(x_i|\hat{\theta})$
        * The minimum value of $\sum_i p_i \log \hat{f}(x_i|\hat{\theta})$ is $H(p)$, which is achieved when $\hat{f}(x_i|\hat{\theta}) = p_i$ $\forall i$
            * Formal: $f, \theta = \arg \max_{\hat{f}, \hat{\theta}} \hat{f}_n(\textbf{x}|\hat{\theta})$
    * In fact, the optimal $\hat{\theta}$ should minimize $- \sum_i p_i \log \hat{p}_i$, or equivalently minimize $D(p\|\hat{p})$ (i.e. KL divergence of $\hat{p}$ from $p$)
        * $\hat{f}$ defines a set of probability vectors $\hat{P}$
        * Optimizing $\hat{\theta}$ is equivalent to choosing the optimal $\hat{p} \in \hat{P}$
* Conclusion:
    * If $\hat{f} = f$ then the sequence of MLEs will converge to $\theta$ in probability as $n \to \infty$
    * If $\hat{f} \neq f$ then the sequence of MLEs will converge to $\arg \min_{\hat{\theta}} D(p\|\hat{p})$ in probability as $n \to \infty$
* Corollary: if $\hat{f}$ isn't chosen carefully (i.e. $\min_{\hat{\theta}} D(p\|\hat{p})$ is large), we cannot obtain a reasonable hypothetical distribution of the data

**Convergence of Bayes estimator**:
* Assumptions:
    * $p = (p_1, ..., p_n)$ is the true probability vector of the data indexed by the true $\theta$
        * Formal: $p_i = f(x_i|\theta)$
    * $f$ is the true parametrization of the data distribution
    * $\hat{p} = (\hat{p}_1, ..., \hat{p}_n)$ is the probability vector indexed by the estimate $\hat{\theta}$ of $\theta$
        * Formal: $\hat{p}_i = \hat{f}(x_i|\hat{\theta})$
    * $\hat{f}$ is the chosen parametrization of the data distribution
    * Distribution of $\hat{\theta}$:
        * Prior distribution: $g(\hat{\theta})$
        * Posterior distribution: $g(\hat{\theta}|\textbf{x})$
    * $L(\theta, \hat{\theta})$ is the loss function
        * Further assumption: minimizing $E[L(\theta, \hat{\theta})|\textbf{x}]$ is equivalent to maximizing $g(\hat{\theta}|\textbf{x})$
* Observations:
    * Compute $g(\hat{\theta}|\textbf{x})$:
        * Straightforward: $g(\hat{\theta}|\textbf{x}) \propto \hat{f}_n(\textbf{x}|\hat{\theta}) g(\hat{\theta})$
        * Sequential: $g(\hat{\theta}|\textbf{x}_{1:i}) \propto \hat{f}(x_i|\hat{\theta}) g(\hat{\theta}|\textbf{x}_{1:i-1})$
    * Conditional probability of $\textbf{x}$ given $\hat{\theta}$
        * $\hat{f}_n(\textbf{x}|\hat{\theta}) g(\hat{\theta}) = g(\hat{\theta}) \prod_i \hat{f}(x_i|\hat{\theta})^{n_i}$ where $n_i$ is the number of observations of type $i$ in the observed data
        * $\log \hat{f}_n(\textbf{x}|\hat{\theta}) g(\hat{\theta}) = \log g(\hat{\theta}) + \sum_i n_i \log \hat{f}(x_i|\hat{\theta})$
        * As $n \to \infty$, $\log \hat{f}_n(\textbf{x}|\hat{\theta}) g(\hat{\theta}) \to \sum_i n_i \log \hat{f}(x_i|\hat{\theta})$
    * From above, as $n \to \infty$, both Bayes estimator and MLE want to minimize $-\sum_i n_i \log \hat{f}(x_i|\hat{\theta})$
* Conclusion:
    * Bayes estimator and MLE: both converge to $\arg \min_{\hat{\theta}} D(p\|\hat{p})$ in probability 
    * Effects of $\hat{f}$ and $\hat{\theta}$: the same as MLE

# Discussion
**Cross entropy loss and MLE**: 
* Assumptions:
    * $\hat{f}$ is the parametric model
    * $\hat{\theta}$ is the parameters of $\hat{f}$, which are to be optimized
* Conclusion: minimizing cross entropy loss is equivalent to maximizing the likelihodd function
    * Explain: as $n \to \infty$, the cross entropy loss converges to $- n \sum_i p_i \log \hat{f}(x_i|\hat{\theta})$

**Mean squared error**: minimizing mean squared error is equivalent to maximizing $P(y|x, \hat{\theta})$ under the assumption that $P(y|x, \hat{\theta})$ is a Gaussian