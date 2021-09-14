<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Bessel's correction](#bessels-correction)
  - [Definition](#definition)
  - [Corrected sample variance as an estimator of the population variance](#corrected-sample-variance-as-an-estimator-of-the-population-variance)
  - [Discussion](#discussion)
- [BONUS](#bonus)
<!-- /TOC -->

# Bessel's correction 
## Definition
**Idea**: use $n - 1$ instead of $n$ in the formula for the sample variance and sample standard deviation
* Explain: we multiply the uncorrect sample variance by $\frac{n}{n - 1}$

**Definition**:
* Assumptions:
    * $n$ is the number of observations in a sample
    * $\bar{x} = \frac{1}{n} \sum_{i = 1}^n x_i$ is the sample mean
    * $s_n^2 = \frac{1}{n} \sum_i (x_i - \bar{x})^2$ is the sample variance
    * $s_n = \sqrt{\frac{1}{n} \sum_i (x_i - \bar{x})^2}$ is the sample standard deviation (w.r.t uncorrected sample variance)
* Conclusion:
    * Unbiased sample variance computed by Bessel: $s^2 = \frac{1}{n - 1} \sum_i (x_i - \bar{x})^2 = \frac{n}{n - 1} s_n^2$
    * Sample standard deviation (w.r.t corrected sample variance): $s = \sqrt{\frac{1}{n - 1} \sum_i (x_i - \bar{x})^2}$

**Usage**: used as the usual estimator for the variance

## Corrected sample variance as an estimator of the population variance
**Source of bias**:
* Consider $s_c = \frac{1}{n} \sum_i (X_i - c)^2$
    * The $s_c$ is minimized by $c = \bar{X}$ while $s_\mu$ is an unbiased estimator of $\sigma^2$
* From above, $E[ s_\bar{X} ] < \sigma^2$

$\hspace{1.0cm} \rightarrow$ This is the source of bias

**An unbiased estimator of variance**:
* Assumptions:
    * $\{X_i\}_{i = 1}^n$ is a random sample from some distribution
    * $\bar{X} = \frac{1}{n} \sum_i X_i$ is the sample mean
    * $\sigma^2$ is the true variance of the distribution
* Observations:
    * Consider $E[\sum_i (X_i - \bar{X})^2]$, without loss of generality, we shift the data by $- \mu$ to obtain a zero-mean distribution
        * $E[\sum_i ((X_i - \mu) - (\bar{X} - \mu))^2] = E[\sum_i (X_i - \mu)^2 - n (\bar{X} - \mu)^2]$

        $\hspace{5.0cm} = n \sigma^2 - n \text{Var }[\bar{X}]$

        $\hspace{5.0cm} = (n - 1) \sigma^2$
    * From above, an unbiased estimator of $\sigma^2$ is $\frac{1}{n - 1} \sum_i (X_i - \bar{X})^2$
* Conclusion: the corrected sample variance is an unbiased estimator of the population variance

**Why we still use uncorrected sample variance**:
* $s_n^2$ is the maximum-likelihood estimator of $\sigma^2$
* $s_n^2$ has lower mean squared error than $s^2$

## Discussion
**Advantages and disadvantages**:
* Advantages: 
    * Correct the bias in the estimation of population variance
    * Partially correct the bias in the estimation of the population standard deviation
        * Explain: $E[ \sqrt{ \frac{1}{n} (x_i - \bar{x})^2 } ] < E[ \sqrt{ \frac{1}{n - 1} (x_i - \bar{x})^2 } ] < \sigma$
* Disadvantages:
    * Often increase the M.S.E in the estimations of variance and standard deviation (e.g. Gaussian distribution)

**Criticisms on Bessel's correction**:
* It doesn't yield an unbiased estimator of standard deviation
    * Explain:
        * $\sqrt{ E[ \frac{1}{n - 1} \sum_i (x_i - \bar{x})^2 ] } > E[ \sqrt{ \frac{1}{n - 1} \sum_i (x_i - \bar{x})^2 } ]$
            * Explain: due to the strict concavity of square root
        * $\sqrt{ E[ \frac{1}{n - 1} \sum_i (x_i - \bar{x})^2 ] } = \sigma$

        $\hspace{1.0cm} \rightarrow \sigma > E[ \sqrt{ \frac{1}{n - 1} \sum_i (x_i - \bar{x})^2 } ]$
        * From above, $\sqrt{ \frac{1}{n - 1} \sum_i (x_i - \bar{x})^2 }$ is an biased estimator of $\sigma$
* The correct estimator often has higher M.S.E than the uncorrected estimator

>**NOTE**: there's no population distribution for which the corrected one has the minimum M.S.E
* Explain: a different scale factor can always be chosen to minimize M.S.E

* Only necessary when the population mean is unknown (and estimated as the sample mean)
    * Explain: when the population mean is known
    
    $\hspace{1.0cm} \rightarrow E[ \sum_i (X_i - \mu)^2 ] = n E[(X - \mu)^2] = n \text{Var } [X]$
    * Consequence: when the sample size is small enough so that the law of large numbers holds
    
    $\hspace{1.0cm} \rightarrow$ We don't need Bessel's correction

---

# BONUS
* Another unbiased estimator of variance:
    * Assumptions:
        * $x_1, x_2$ are two random variable from the same distribution
            * Formal: $x_i \sim P$ for all $i$
        * $\text{Var }[x_1] = \sigma^2$
    * Conclusion:
        * An unbiased estimator of $\sigma^2$: $\frac{1}{2} (x_1 - x_2)^2$
            * Explain: $E[\frac{1}{2} (x_1 - x_2)^2] = \sigma^2$