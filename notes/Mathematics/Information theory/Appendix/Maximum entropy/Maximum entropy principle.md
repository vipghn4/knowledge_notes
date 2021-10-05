<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Maximum entropy principle](#maximum-entropy-principle)
- [BONUS](#bonus)
<!-- /TOC -->

# Maximum entropy principle
**Maximum entropy principle**: the probability distribution which best represents the current state of knowledge is the one with largest entropy (in the context of precisely stated prior data)
* Another interpretation: 
    * Step 1: take precisely stated prior data (or testable information) about a probability distribution
    * Step 2: consider the set of all trial probability distributions that would encode the prior data
    * Step 3: according to this principle
    
    $\hspace{1.0cm} \rightarrow$ The distribution with maximal information entropy is the best choice

**Testable information**:
* Testable information: a statement about a probability distribution whose truth or falsity is well-defined
    * Example:
        * The expectation of the variable os $2.87$
        * $p_2 + p_3 > 0.6$ where $p_2, p_3$ are probabilities of events
    * Testable information and maximum entropy principle: maximum entropy principle is useful explicitly only when applied to testable information
* Maximum entropy procedure (given testable information): seeking the probability distribution which maximizes information entropy (s.t. the constraints of the information)
    * Find the optimal distribution: use Lagrange multiplies (typically)

**Application**:
* Prior probabilities: maximum entropy principle is used to obtain prior distribution for Bayesian inference
    * Claim: the maximum entropy distribution represented the least informative distribution
* Posterior probabilities: maximum entropy principle is a sufficient updating rule for radical probabilism
* Probability density estimation (one of the main applications): provide a sparse mixture model as the optimal density estimator
    * Similarity to SVM: both require the solution to a quadratic programming
    * Advantage: maximum entropy principle can incorporate prior information in the density estimation

**Justifications for the principle of maximum entropy**:
* Idea: information entropy can be seen as a numerical measure describing how uninformative a particular probability distribution is
    * Explain: as the intuition of information entropy suggests
* Observations: 
    * By choosing to use the distribution with maximum entropy allowed by our information
    
    $\hspace{1.0cm} \rightarrow$ We're choosing the most uninformative distribution possible
    * By choosing a distribution with lower entropy
    
    $\hspace{1.0cm} \rightarrow$ We're assuming information we don't have
* Conclusion: the maximum entropy distribution is the only reasonable distribution

---

# BONUS
* Compatibility (n): khả năng tương thích