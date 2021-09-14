<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Formal description of Bayesian inference](#formal-description-of-bayesian-inference)
  - [Mathematical properties](#mathematical-properties)
- [Frequentist inference](#frequentist-inference)
<!-- /TOC -->

## Introduction
**Bayesian inference**: a method of statistical inference using Bayes' theorem to update the probability for a hypothesis as more evidence becomes available
* Importance: particularly important in the dynamic analysis of a sequence of data

**Bayesian inference perspectives**: 
* Probability describes degree of belief, not limiting frequency
    * We can make probability statements about lots of things, not just data
* We can make probability statements about parameters, even when they are fixed constants
* We make inferences about $\theta$, by producing a probability distribution for $\theta$

$\hspace{1.0cm} \rightarrow$ Inferences can be extracted from this distribution

**Bayes' rule**: update prior probability to posterior probability
* Bayes' rule for updating: $P(H|E) = \frac{P(E|H)}{P(E)} P(H)$
    * Prior probability: $P(H)$
    * Posterior probability: $P(H|E)$
    * Impact of $E$ on $H$: $\frac{P(E|H)}{P(E)}$
* Alternatives to Bayesian updating: there are non-Bayesian updating rules

**Drawbacks of Bayesian inferences**:
* Inherently embrace a subjective notion of probability
* Provide no guarantees on long run performance

## Formal description of Bayesian inference
**Predictive inference**: predict the distribution of a new data point, instead of the point

**Terminologies**:
* Prior distribution $p(\theta|\alpha)$: the distribution of parameter(s) before observing data
    * $\alpha$ is the hyper-parameter of the probability model
    * $\theta$ is the parameter of the data distribution $p(x|\theta)$
* Sampling distribution $p(\textbf{X}|\theta)$: the distribution of the observed data conditional on $\theta$
    * Other name: likelihood (when treated as a function of $\theta$)
* Marginal likelihood $p(\textbf{X}|\alpha)$: the distribution of the observed data marginalized over $\alpha$
    * Formal: $p(\textbf{X}|\alpha) = \int p(\textbf{X}|\theta) p(\theta|\alpha) d\theta$
* Posterior distribution $p(\theta|\textbf{X}, \alpha)$: the distribution of $\theta$ after observing data
    * Formal: $p(\theta|\textbf{X}, \alpha) = \frac{p(\textbf{X}|\theta, \alpha)}{p(\textbf{X}|\alpha)} p(\theta|\alpha) \propto p(\textbf{X}|\theta, \alpha) p(\theta|\alpha)$

**Bayesian prediction**: predict the distribution of a new data poitn $\tilde{x}$
* Posterior predictive distribution: $p(\tilde{x}|\textbf{X}, \alpha) = \int p(\tilde{x}|\theta) p(\theta|\textbf{X}, \alpha) d\theta$
* Prior predictive distribution: $p(\tilde{x}|\alpha) = \int p(\tilde{x}|\theta) p(\theta|\alpha) d\theta$

**Inference with mixture probability model**: treat the belief distribution (i.e. distribution of $\theta$) as a whole
* Assumptions:
    * $\{E_n\}_n$ is a process which generates i.i.d events with unknown distribution
    * $\Omega$ is the event space, which is the current state of belief of the process
    * $M_m$ is a probability model characterizing $E_n$ by $P(E_n|M_m)$
        * $P(M_m)$ is the degree of belief in $M_m$
* Conclusion:
    * Initial prior probabilities: $\{P(M_m)\}$ where $\sum_m P(M_m) = 1$
    * Updating with single observation: $P(M|E) = \frac{P(E|M)}{\sum_m P(E|M_m) P(M_m)} P(M)$ $\forall M \in \{M_m\}$
    * Updating with multiple observations: replace $E$ (above) by $\textbf{E}$ where $P(\textbf{E}|M) = \prod_i P(E_i|M)$

**Comparison to frequentist prediction**:
* Frequentist prediction: 
    * Step 1: find an optimum estimate of $\theta$ by maximum likelihood (MLE) or maximum a posteriori estimation (MAP)
    * Step 2: plug the estimate of $\theta$ into the formula for the distribution of a data point
* Drawbacks of frequentist prediction: parameter uncertainty isn't included

## Mathematical properties
**Interpretation of factor**:
* $\frac{P(E|M)}{P(E)} > 1$: if the model were true, the evidence would be more likely than is predicted by the current state of belief
* $\frac{P(E|M)}{P(E)} = 1$: the evidence is independent of the model (i.e. if the model were true, the evidence would be exactly as likely as predicted by the curretn state of belief)

**Hard models are insentitive to counter-evidence**:
* $P(M) = 0$ implies $P(M|E) = 0$
* $P(M) = 1$ implies $P(M|E) = 1$

**Asymptotic behavior of posterior**: in the limit of infinite trials, the posterior converges to a Gaussian distribution independent of the initial prior under some conditions

**Estimates of parameters and predictions**: 
* Estimate $\theta$:
    * Approach 1: $\theta = \text{Median}(\theta|\textbf{X}, \alpha)$ 
    * Approach 2: $\theta = E[\theta|\textbf{X}, \alpha]$
    * Approach 3: $\{\theta_\text{MAP}\} \subset \arg \max_\theta p(\theta|\textbf{X}, \alpha)$
* Predict $\tilde{x}$: $p(\tilde{x}|\textbf{X}, \alpha) = \int p(\tilde{x}|\theta) p(\theta|\textbf{X}, \alpha) d\theta$

**Bayesian model comparison**: use Bayes factor to compare probability models
* Bayes factor: a likelihood ratio of the marginal likelihood of two competing hypotheses
    * Formal: $K = \frac{P(D|M_1)}{P(D|M_2)}$ where $D$ is the data, $M_1, M_2$ are the competing models

# Frequentist inference
**Frequentist inference**: draw conclusions from sample data by emphasizing the frequency or proportion of the data
* Frequentist-inference-based techniques: statistical hypothesis testing, confidence intervals

**Frequentist (or classical) inference perspectives**:
* Probability refers to limiting relative frequencies, which are object properties of the real world
* Parameters are fixed (usually unknown) constants
    * Explain: they aren't fluctuating, no probability statements can be made about parameters
* Statistical procedures should be designed to have well-defined long run frequency propoerties
    * Example: a $95\%$ confidence interval should trap $\theta$ with limiting frequency at least $95\%$