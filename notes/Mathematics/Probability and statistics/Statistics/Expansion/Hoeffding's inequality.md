<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Hoeffding's inequality](#hoeffdings-inequality)
  - [Hoeffding's inequality](#hoeffdings-inequality-1)
  - [Finite hypothesis spaces](#finite-hypothesis-spaces)
  - [Structural risk minimization](#structural-risk-minimization)
  - [More on finite hypothesis spaces](#more-on-finite-hypothesis-spaces)
  - [Infinite spaces and VC dimension](#infinite-spaces-and-vc-dimension)
  - [Discussion](#discussion)
- [BONUS](#bonus)
<!-- /TOC -->

# Hoeffding's inequality
**Reference**: https://people.cs.umass.edu/~domke/courses/sml2010/10theory.pdf

## Hoeffding's inequality
**Hoeffding's inequality**: the most important (maybe) inequality in learning theory

**Formal**:
* Hoeffding's lemma: 
    * Formal: $E\{\exp[\lambda (Z - E[Z])]\} \leq \exp(\frac{\lambda^2 (b - a)^2}{8})$ $\forall \lambda \in \textbf{R}$ 
        * $Z \in [a, b]$ is a bounded random variable
    * Explain: 
* Hoeffding's inequality:
    * Assumptions:
        * $Z_1, ..., Z_n$ are i.i.d bounded variables
        * $Z_i \in [a, b]$ $\forall i$
    * Conclusion: for any $t \geq 0$,
        * $P(\frac{1}{n} \sum_i [Z_i - E(Z_i)] \geq t) \leq \exp(-\frac{2 n t^2}{(b - a)^2})$
        * $P(\frac{1}{n} \sum_i [Z_i - E(Z_i)] \leq -t) \leq \exp(-\frac{2 n t^2}{(b - a)^2})$
    * Explain: 
* Hoeffding's inequality for Bernoulli distributions:
    * Assumptions:
        * $X_1, ..., X_n \sim \text{Bernoulli}(p)$
    * Conclusion: for any $\epsilon > 0$, $P(|\bar{X}_n - p| > \epsilon) \leq 2 e^{- 2 n \epsilon^2}$
    * Usage: simply produce a confidence interval for a binomial parameter $p$

**Importances**: Hoeffding's inequality doesn't depend on any properties of the distribution

**Applications**: 
* Bound the probability that sums of bounded random variables are too large or too small
* Quantify how "usually" and "close" $Z_i$'s to their expectations
* Provide the cost of some desired accuracy $t$ and confidence $2 \exp(-\frac{2 n t^2}{(b - a)^2})$, in terms of sample size $n$
    * Accuracy is expensive
    * Confidence is cheap

## Finite hypothesis spaces
**Problem of interest**: bound the binary classification error rates of classifiers
* Assumptions:
    * ${\cal{G}}$ is a finite set of possible classifiers

    >**NOTE**: the assumption that ${\cal{G}}$ is finite is a very strong assumption!

    * $g$ is some classifier
    * $R_\text{true}(g)$ is the true error rate
    * $R_n(g)$ is the observed error rate on $n$ samples
    * $\delta = 2 e^{-2 n \epsilon^2}$
* Conclusion:
    * With probability of at least $1 - \delta$ that $|R_\text{true}(g) - R_n(g)| \leq \epsilon = \sqrt{\frac{1}{2n} \log \frac{2}{\delta}}$
    * If we want $|R_\text{true}(g) - R_n(g)| \leq \epsilon$ with probability at least $1 - \delta$

    $\hspace{1.0cm} \rightarrow$ We should pick $n \geq \frac{1}{2 \epsilon^2} \log \frac{2}{\delta}$

**Incorrect, wrong, broken algorithm**:
* Experiment:
    * Procedure:
        * Input a set of classifiers ${\cal{G}}$
        * Draw $n \geq \frac{1}{2 \epsilon^2} \log \frac{2}{\delta}$ samples
        * Output $g^* = \arg \min_{g \in {\cal{G}}} R_n(g)$
    * Wrong conclusion: $|R_n(g) - R_\text{true}(g)| \leq \epsilon$ with high probability for all $g$

    $\hspace{1.0cm} \rightarrow$ The output $g^*$ should be close to the best class
    * Right conclusion: for any given $g$, there aren't too many bad training sets, for which $|R_n(g) - R_\text{true}(g)| > \epsilon$

    >**NOTE**: different classifiers can have different bad training sets

* Conclusion: with probability $1 - \delta$, for all $g \in {\cal{G}}$ simultaneously, $|R_\text{true}(g) - R_n(g)| \leq \sqrt{\frac{1}{2n} \log \frac{2 |{\cal{G}}|}{\delta}}$
    * Explain: $P(|R_\text{true}(g) - R_n(g)| > \epsilon) \leq \frac{\delta}{|{\cal{G}}|}$ for each $g \in {\cal{G}}$

## Structural risk minimization
**Bias-variance trade-off**: as ${\cal{G}}$ gets bigger, we could fit the true function better but with a greater risk of overfitting
* Bias: the goodness of $R_\text{true}(g)$ (i.e. the goodness of the chosen model ${\cal{G}}$)
    * Bias decreasing: as ${\cal{G}}$ gets bigger, $\min_{g \in {\cal{G}}} R_\text{true}(g)$ will be non-increasing (i.e. decrease in bias)
* Variance: the difference between $R_n(g)$ and $R_\text{true}(g)$
    * Variance increasing: as ${\cal{G}}$ gets bigger, $\sqrt{\frac{1}{2n} \log \frac{2 |{\cal{G}}|}{\delta}}$ is creasing (i.e. increase in variance)

**Idea of structural risk minimization**:
* Assumptions:
    * ${\cal{G}}_1 \subset {\cal{G}}_2 \subset ...$ is a sequence of models
    * $g^*_i = \arg \min_{g \in {\cal{G}}_i} R_n(g^*_i)$
* Task: choose ${\cal{G}}_i$ to trade-off between bias and variance
    * Formal: should we output $g^*_1, g^*_2, ...$
* Idea: $R_\text{true}(g^*_i) \leq R_n(g^*_i) + \sqrt{\frac{1}{2n} \log \frac{2 |{\cal{G}}_i|}{\delta}}$

$\hspace{1.0cm} \rightarrow$ We minimize the bound of $R_\text{true}(g^*_i)$ instead of it

**Structural risk minimization using a Hoeffding bound**:
* Compute $g^*_i = \arg \min_{g \in {\cal{G}}_i} R_n(g)$ $\forall i$
* Pick $i = \arg \min_i [ R_n(g^*_i) + \sqrt{\frac{1}{2n} \log \frac{2 |{\cal{G}}_i|}{\delta}} ]$
* Output $g^*_i$

**Discussion**: in practice, the bound $R_\text{true}(g^*_i) \leq R_n(g^*_i) + \sqrt{\frac{1}{2n} \log \frac{2 |{\cal{G}}_i|}{\delta}}$ is very loose

$\hspace{1.0cm} \rightarrow$ SRM maybe based on firmer theoretical foundations than cross-validation, but it may not work better

## More on finite hypothesis spaces
**Problem of interest**:
* Assumptions:
    * $g^* = \arg \min_{g \in {\cal{G}}} R_\text{true}(g)$
* Task: bound the probability that the empirical risk minimization algorithm picks $g^*$

**Theorem**: with probability at least $1 - \delta$ that $R_\text{true}[\arg \min_{g \in {\cal{G}}} R_n(g)] \leq \min_{g \in {\cal{G}}} R_\text{true}(g) + 2 \sqrt{\frac{1}{2n} \log \frac{2 |{\cal{G}}|}{\delta}}$
* Interpretation: take the function $g^*_e$ minimizing $R_n(g)$

$\hspace{1.0cm} \rightarrow$ With high probability that $R_\text{true}(g^*_e)$ won't be too much worse than $R_\text{true}(g^*)$

## Infinite spaces and VC dimension
**Big question of interest**: given ${\cal{G}}$, choose $n$ to fit ${\cal{G}}$ reliably
* Difficulties:
    * ${\cal{G}}$ can be infinite
    * Digital computers represent numbers only to a fixed precision
* Observations:
    * If we have $P$ parameters and our computer uses $32$ bits to represent a float

    $\hspace{1.0cm} \rightarrow |{\cal{G}}| = 2^{32 P}$
    * From above, $n \geq \frac{1}{2 \epsilon} \log \frac{2 \cdot 2^{32 P}}{\delta}$ is required

    $\hspace{1.0cm} \rightarrow n$ grows linearly in $P$

**Theorem**: 
* Assumptions:
    * $\text{VC}[{\cal{G}}]$ is the VC-dimension of ${\cal{G}}$ (i.e. set of sets)
* Conclusion: with probability $1 - \delta$, for all $g \in {\cal{G}}$ simultaneously, 

$\hspace{1.0cm} \rightarrow R_\text{true}(g) \leq R_n(g) + \sqrt{\frac{\text{VC}[{\cal{G}}]}{n} (\log \frac{n}{\text{VC}[{\cal{G}}]} + \log 2e) + \frac{1}{n} \log \frac{4}{\delta}}$

**Structural risk minimization with VC dimension**:
* Compute $g^*_i = \arg \min_{g \in {\cal{G}}_i} R_n(g)$
* Pick $i = \arg \min_i  R_n(g^*_i) + \sqrt{\frac{\text{VC}[{\cal{G}}_i]}{n} (\log \frac{n}{\text{VC}[{\cal{G}}_i]} + \log 2e) + \frac{1}{n} \log \frac{4}{\delta}}$
* Output $g^*_i$

## Discussion
* Fundamental weakness of the above bounds is their looseness
    * Explain: the bound on $|R_\text{true}(g) - R_n(g)|$ is often hundreds of times higher than the true one
* An open research area is tightening the bounds above
* The model selected by structural risk minimization is sometimes quite good, despite the looseness of the bound

---

# BONUS
* Shattering: ${\cal{G}}$ shatters $S = \{x_1, ..., x_d\}$ if points in $S$ can be classified in all possible ways by ${\cal{G}}$
    * Formal: $\forall y_i \in \{-1, +1\}$, $\exists g \in {\cal{G}}: y_i = \text{sign} g(x_i)$
* VC dimension of ${\cal{G}}$: $|S|$ where $|S|$ is the largest set which can be shattered by ${\cal{G}}$
    * Find VC-dimension:
        * Step 1: find a set of size $d$ which can be shattered
        * Step 2: conclude that the VC-dimension is at least $d$