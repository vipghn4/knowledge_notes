<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Method of types](#method-of-types)
- [Law of large numbers](#law-of-large-numbers)
- [Universal source coding](#universal-source-coding)
- [Large deviation theory](#large-deviation-theory)
- [BONUS](#bonus)
- [Conditional limit theorem](#conditional-limit-theorem)
  - [Introduction](#introduction)
  - [Some insight into the geometry of $D(P\|Q)$](#some-insight-into-the-geometry-of-dpq)
  - [Conditional limit theorem](#conditional-limit-theorem-1)
- [Hypothesis testing](#hypothesis-testing)
<!-- /TOC -->

# Method of types
**AEP and method of types**: 
* AEP: consider a small subset of typical sequences (i.e. have "typical" sample entropy)
* Method of types: consider sequences that have the same empirical distribution

**Definitions**:
* Assumptions:
    * $X_1, ..., X_n$ is a sequence of $n$ symbols from an alphabet ${\cal{X}} = \{a_1, ..., a_{|{\cal{X}}|}\}$
        * $x^n$ and $\textbf{x}$ are used to denote a sequence $x_1, ..., x_n$
* Conclusion:
    * The type (or empirical distribution) $P_\textbf{x}$ of a sequence $x_1, ..., x_n$: the relative proportion of occurrences of  symbol of $\cal{X}$
        * Formal: $P_\textbf{x}(a) = N(a|\textbf{x}) / n$ $\forall a \in \cal{X}$ 
            * $N(a|\textbf{x})$ is the number of times $a$ occurs in $\textbf{x} \in \cal{X}$
    * The probability simplex in ${\cal{R}}^m$: the set of points $\textbf{x} = (x_1, ..., x_m)$ such that $x_i \geq 0$ and $\sum_{i = 1}^m x_i = 1$
    
    $\hspace{1.0cm} \rightarrow$ The probability simplex is an $(m - 1)$-dimensional manifold in $m$-dimensional space
    * The set of (possible) types ${\cal{P}}_n$ with denominator $n$
        * Example: if ${\cal{X}} = \{0, 1\}$
        
        $\hspace{1.0cm} \rightarrow {\cal{P}}_n = \{(\frac{0}{n}, \frac{n}{n}), ..., (\frac{n}{n}, \frac{0}{n})\}$
    * The type class (or composition class) of $P \in {\cal{P}}_n$: the set of sequences of length $n$ and type $P$
        * Formal: $T(P) = \{\textbf{x} \in {\cal{X}}^n|P_\textbf{x} = P\}$

**Upper bound on the size of $\cal{P}_n$**: 
* Statement: $|{\cal{P}}_n| \leq (n + 1)^{|{\cal{X}}|}$
  * Explain: there are $|\cal{X}|$ possible values and each of them can have frequency from $\frac{0}{n}$ to $\frac{n}{n}$
  
  >**NOTE**: we can exactly compute $|{\cal{P}}_n| \leq (n + 1)^{|{\cal{X}}|}$ but this bound is sufficiently good for our needs

* Consequence: 
  * The number of sequences is $|{\cal{X}}|^n$
  
  $\hspace{1.0cm} \rightarrow$ The minimum size of the largest type is $\frac{|{\cal{X}}|^n}{(n + 1)^{|{\cal{X}}|}}$
  
  * From above, at least one type has exponentially, in $n$, many sequences in its type class

>**NOTE**: in fact, the largest type class has essentially the same number of elements as the entire set of sequences, to first order in the exponent (i.e. $O(D^n) |\cal{X}|^n$)

**Theorem**:
* Assumptions:
  * $X_1, ..., X_n$ are drawn i.i.d according to a distribution $Q(x)$
  * $Q^n(x^n) = \prod_{i = 1}^n Q(x_i) = \prod_{i = 1}^n D^{- \log \frac{1}{Q(x_i)}}$
* Conclusion:
  * $Q^n(\textbf{x}) = D^{-n (H(P_\textbf{x}) + D(P_\textbf{x}\|Q))}$
* Explain:
  * $\prod_{i = 1}^n D^{- \log \frac{1}{Q(x_i)}} = D^{- \sum_i N(x_i|\textbf{x}) \log \frac{1}{Q(x_i)}} = D^{- n \sum_i P_\textbf{x}(x_i) \log \frac{1}{Q(x_i)}}$ 
  * $\sum_i P_\textbf{x}(x_i) \log \frac{1}{Q(x_i)}$ is the cross entropy of $Q$ and $P_\textbf{x}$ 

* Intuition 1:
    * Since $X_1, ..., X_n$ are i.i.d
    
    $\hspace{1.0cm} \rightarrow$ The information contained in $X_1, ..., X_n$ the sum of information contained in each $X_i$
    
    * The empirical distribution of $\textbf{x}$ is $P_\textbf{x}$ while the expected distribution (i.e. the distribution from which the sequence is drawn) is $Q$
    
    $\hspace{1.0cm} \rightarrow$ Due to AEP, the information contained in $\textbf{x}$ is approximately $n (H(P_\textbf{x}) + D(P_\textbf{x}\|Q))$
    * From above, $Q^n(\textbf{x}) \approx D^{- n (H(P_\textbf{x}) + D(P_\textbf{x}\|Q))}$

* Another interpretation of the intuition: 
    * As the sequence length approaches infinity
    
    $\hspace{1.0cm} \rightarrow$ The information contained in the sequence is approximately $n (H(P_\textbf{x}) + D(P_\textbf{x}\|Q))$
    * Since information and probability have a one-to-one relationship
    
    $\hspace{1.0cm} \rightarrow$ The probability of $\textbf{x}$ w.r.t $Q^n$ is approximately $D^{- n (H(P_\textbf{x}) + D(P_\textbf{x}\|Q))}$

>**NOTE**: all sequences with the same type have the same probability

* Corollary: if $\textbf{x}$ is in the type class of $Q$

$\hspace{1.0cm} \rightarrow Q^n(\textbf{x}) = D^{-n H(Q)}$

**Size of a type class $T(P)$**: for any type $P \in {\cal{P}}_n$, $\frac{1}{(n + 1)^{|{\cal{X}}|}} D^{n H(P)} \leq |T(P)| \leq D^{n H(P)}$
* Explain:
    * Since $|T(P)|$ is independent of the distribution from which $\textbf{x}$ is drawn
    
    $\hspace{1.0cm} \rightarrow$ We will bound $|T(P)|$ under the assumption that $X_1, ..., X_n$ are drawn from $P(x)$
        * Explain: we make this assumption since we can only derive a lower bound for $|T(P)|$ under this assumption
    * From above, $\frac{1}{(n + 1)^{|{\cal{X}}|}} \leq |T(P)| D^{-n H(P)} \leq 1$
        * $|T(P)| D^{-n H(P)}$ is the probability of $\textbf{x}$ w.r.t $P^n$
        * The upper bound is due to the constraint on a probability value
        * The lower bound is due to the assumption that $T(P)$ is the largest type class (i.e. $X_1, ..., X_n$ are drawn from $P(x)$)
* Extension: extend the assumption above (i.e. $X_1, ..., X_n$ are theoretically drawn some distribution $Q$)

$\hspace{1.0cm} \rightarrow |T(P)| \leq D^{n (H(P) + D(P\|Q))}$

**Probability of type class**: 
* Statement: for any $P \in {\cal{P}}_n$ and any distribution $Q$

$\hspace{1.0cm} \rightarrow$ The probability of the type class $T(P)$ under $Q^n$ is $D^{-n D(P\|Q)}$ to first order in the exponent
* Formal: $\frac{1}{(n + 1)^{|\cal{X}|}} D^{-n D(P\|Q)} \leq Q^n(T(P)) \leq D^{-n D(P\|Q)}$
* Explain: $Q^n(T(P)) = \sum_{\textbf{x} \in T(P)} Q^n(\textbf{x}) = |T(P)| Q^n(\textbf{x})$ for any $\textbf{x} \in T(P)$

**Idea of methods of type**: calculate the behavior of long sequences based on the properties of the type of the sequence

**Summary**:
* There is a polynomial number of types
    * Formal: $|{\cal{P}}| \leq (n + 1)^{|{\cal{X}}|}$
* The probability of type $P$ under $Q$: $Q^n(\textbf{x}) = D^{-n (H(P_\textbf{x}) + D(P_\textbf{x}\|Q))}$
* There are exponontial number of sequences of each type
    * Formal: $\frac{1}{(n + 1)^{|{\cal{X}}|}} D^{n H(P)} \leq |T(P)| \leq D^{n H(P)}$
* The approximate probability of $T(P)$ under $Q$: $\frac{1}{(n + 1)^{|{\cal{X}}|}} D^{- n D(P\|Q)} \leq Q^n(T(P)) \leq D^{- n D(P\|Q)}$

# Law of large numbers
**Original form**: $\bar{X}_n \to \mu$ as $n \to \infty$ where $\bar{X}_n = \frac{1}{n} \sum_i X_i$

**Typical set of sequences of the distribution $Q^n$**: $T^\epsilon_Q = \{x^n|D(P_{x^n}\|Q) \leq \epsilon\}$
* Typicality: means the typicality in empirical distribution
* Intuition: the set of $x^n$ whose empirical KL divergence from $Q^n$ is no larger than some pre-defined constant $\epsilon$
* An upper bound on probability of non-typical $x^n$: $Q^n(T^\epsilon_Q) \geq 1 - (n + 1)^{|{\cal{X}}|} D^{-n \epsilon}$
    * Explain: $\text{Pr}(D(P_{x^n}\|P) > \epsilon) \leq (n + 1)^{|{\cal{X}}|} D^{-n \epsilon}$ since
        * $D^{- n \epsilon}$ is the (approximately) maximum probability of a sequence outside of $T^\epsilon_Q$
        * $(n + 1)^{|{\cal{X}}|}$ is the maximum number of sequences of the whole sequence space
        
        $\hspace{1.0cm} \rightarrow$ This can be used as an upper bound on the number of sequences not in $T^\epsilon_Q$
    * Consequence: $\text{Pr}(x^n \in T^\epsilon_Q) \to 1$ as $n \to \infty$

**Strongly typical set**: the set of sequences in ${\cal{X}}^n$ which truly reflects the distribution $P$ (i.e. sample frequencies are close to the true values)
* Formal: $A^{*(n)}_\epsilon = \{\textbf{x} \in {\cal{X}}^n:\begin{cases} |\frac{1}{n} N(a|\textbf{x}) - P(a)| < \frac{\epsilon}{|{\cal{X}}|} && P(a) > 0 \\ N(a|\textbf{x}) = 0 && P(a) = 0\end{cases}\}$
* Probability of the strongly typical set: converges to $1$ as $n \to \infty$

# Universal source coding
**Motivation**:
* Downside of Huffman code: sensitive to the assumed distribution
    * Explain: Huffman coding compresses an i.i.d source with a known distribution $p(x)$ to its entropy limit $H(X)$
    
    $\hspace{1.0cm} \rightarrow$ If the code is designed for some incorrect distribution $q(x)$, a penalty of $D(p\|q)$ is incurred
* Question: 
    * What compression can be achieved if the true distribution $p(x)$ is unknown
    * Is there a universal code of rate $R$ that suffices to describe every i.i.d source with entropy $H(X) < R$
* Observations:
    * There are $D^{n H(P)}$ sequences of type $P$ but only a polynomial number of types with denomiator $n$
    
    $\hspace{1.0cm} \rightarrow$ An enumeration of all sequences $x^n$ with type $P_{x^n}$ such that $H(P_{x^n}) < R$ will require roughly $nR$ bits
    * From above, by describing all such sequences, we're prepared to describe any sequence that is likely to arise from any distribution $Q$ having entropy $H(Q) < R$

**Fixed-rate block code**:
* Assumptions:
    * $X_1, ..., X_n$ is a source with a unknown distribution $Q$
* Conclusion:
    * A fixed-rate block code of rate $R$ for $X_1, ..., X_n$ consists of:
        * The encoder: $f_n: {\cal{X}}^n \to \{1, ..., D^{nR}\}$
        * The decoder: $\phi_n: \{1, ..., D^{nR}\} \to {\cal{X}}^n$
    * The rate of the code: $R$
    * The probability of error for the code w.r.t $Q$: $P^{(n)}_e = Q^n(S)$ where $S = \{X^n:\phi_n(f_n(X^n)) \neq X^n\}$
* Another interpretation of fixed-rate block code: the code where every input sequence is mapped to a symbol taken from a fixed-size alphabet

**Universal fixed-rate block code**: a rate $R$ block code for a source is universal if:
* $f_n$ and $\phi_n$ don't depend on $Q$
* $P^{(n)}_e \to 0$ as $n \to \infty$ if $R > H(Q)$

**Theorem**: 
* Statement: there exists a sequence of $(D^{nR}, n)$ universal source codes that $P^{(n)}_e \to 0$ for every source $Q$ that $H(Q) < R$
* Explain: we prove the theorem by introducing a sequence of $(D^{nR}, n)$ universal source code satisfying the theorem
    * Proposed coding scheme:
        * Assumptions:
            * $R$ is the fixed code rate
            * $R_n = R - |{\cal{X}}| \frac{\log (n+1)}{n}$ (i.e. $D^{n R_n} = \frac{1}{(n + 1)^{|{\cal{X}}|}} D^{nR}$)
            * $A = \{\textbf{x} \in {\cal{X}}^n:H(P_\textbf{x}) \leq R_n\}$
            * The encoding function is $f_n(\textbf{x}) = \begin{cases} \text{index of } \textbf{x} \text{ in } A && \textbf{x} \in A \\ 0 && \text{otherwise} \end{cases}$
            * The decoding function is $\phi_n$ which maps each index onto the corresponding element of $A$
        * Observations:
            * $|A| \leq D^{nR}$
                * Explain: $|A| = \sum_{H(P) \leq R_n} |T(P)|$
                
                $\hspace{2.1cm} \leq \sum_{H(P) \leq R_n} D^{n R_n}$
                
                $\hspace{2.1cm} \leq (n + 1)^{|{\cal{X}}|} D^{n R_n}$
                
                $\hspace{2.1cm} = D^{nR}$
            * From above, all elements of $A$ are recovered correctly and all the remaining sequences result in an error
    * Universality of the proposed coding scheme:
        * Assumptions:
            * $X_1, ..., X_n$ are sampled i.i.d $\sim Q$
            * $H(Q) < R$
        * Decoding error probability: $P^{(n)}_e = 1 - Q^n(A) = (n + 1)^{\cal{X}} D^{\min_{P \notin A} D^{-n D(P\|Q))}}$
        
        $\hspace{1.0cm} \rightarrow P^{(n)}_e \to 0$ as $n \to \infty$
* Intuition: for any source $Q$ that $H(Q) < R$, the information contained in the sequence $X_1, ..., X_n$ is approximately $n H(Q)$

$\hspace{1.0cm} \rightarrow$ We can use $D^{n R}$ symbols to represent the sequence $X_1, ..., X_n$ with arbitrarily low probability of error

**Why use Huffman codes**: universal codes need a longer block length to obtain the same performance as a code designed specially for the probability distribution

$\hspace{1.0cm} \rightarrow$ We pay the penalty for this increase in block length by the increased complexity of the encoder and decoder
* Conclusion: a distribution specific code is best if one knows the distribution of the source

# Large deviation theory
**Motivating problem**: estimate the probability of a set of non-typical types
* Example: what is the probability that $\bar{X}_n = \frac{1}{n} \sum_i X_i > \frac{3}{4}$ given $X_1, ..., X_n \sim \text{Bernoulli}(\frac{1}{3})$
    * Solution: $\bar{X}_n = \frac{3}{4}$ means $P_\textbf{x} = (\frac{1}{4}, \frac{3}{4})$
    
    $\hspace{1.0cm} \rightarrow$ The probability of this large deviation should be $\approx D^{-n D[(\frac{3}{4}, \frac{1}{4})\|(\frac{1}{3}, \frac{2}{3})]}$

**Assumptions**:
* $E$ is a subset of the set of p.m.f's
* $Q^n(E)$ denotes $Q^n(E \cap {\cal{P}}_n) = \sum_{\textbf{x}:P_\textbf{x} \in E \cap {\cal{P}}_n} Q^n(\textbf{x})$

**Observations**:
* If $E$ contains a relative entropy (i.e. KL divergence) neighborhood of $Q$

$\hspace{1.0cm} \rightarrow Q^n(E) \to 1$
* If $E$ doesn't contain $Q$ or a neighborhood of $Q$

$\hspace{1.0cm} \rightarrow Q^n(E) \to 0$

**Sanov's theorem**:
* Assumptions:
    * $X_1, ..., X_n$ are i.i.d $\sim Q(x)$
    * $P^* = \arg \min_{P \in E} D(P\|Q)$ is the distribution in $E$ that's closest to $Q$ (in relative entropy)
* Conclusion:
    * $Q^n(E) = Q^n(E \cap {\cal{P}}_n) \leq (n + 1)^{|{\cal{X}}|} D^{-n D(P^*\|Q)}$
        * Explain:
            * $D^{-n D(P^*\|Q)}$ is the maximum probability of all sequences whose empirical distribution is in $E$
            * $(n + 1)^{|{\cal{X}}|}$ is the maximum number of sequences of the whole space
            
            $\hspace{1.0cm} \rightarrow$ This can be used as an upper bound on the number of sequences in $E$
    * If $E$ is the closure of its interior (i.e. $E$ is a regular closed set)
    
    $\hspace{1.0cm} \rightarrow \frac{1}{n} \log Q^n(E) \to - D(P^*\|Q)$
        * Explain:
            * The requirement on $E$ to be a regular closed set
                * This requirement ensures that $E$'s interior isn't empty
                * As $n$ grows larger, ${\cal{P}}$ can describe more precisely distributions in $E$ 
                
                $\hspace{1.0cm} \rightarrow E \cap {\cal{P}}_n$ becomes non-empty
            * $Q^n(E) \leq (n + 1)^{|{\cal{X}}|} D^{-n D(P^*\|Q)}$ (as proven above)
            
            $\hspace{1.0cm} \rightarrow \frac{1}{n} \log Q^n(E) \leq |{\cal{X}}| \frac{\log(n + 1)}{n} - D(P^*\|Q)$
            * $Q^n(E) \geq \frac{1}{(n + 1)^{|\cal{X}|}} D^{-n D(P^*\|Q)}$
                * Explain: $Q^n(E) \geq Q^n(T(P_n))\geq \frac{1}{(n + 1)^{|\cal{X}|}} D^{-n D(P^*\|Q)}$
                * Consequence: $\frac{1}{n} \log Q^n(E) \geq - |{\cal{X}}| \frac{\log(n + 1)}{n} - D(P^*\|Q)$
            * Both the lower bound and upper bound of $\frac{1}{n} \log Q^n(E)$ tend to $- D(P^*\|Q)$ as $n \to \infty$
            
            $\hspace{1.0cm} \rightarrow \frac{1}{n} \log Q^n(E) \to - D(P^*\|Q)$
        * Extension: the expression can be written as $Q^n(E) \to D^{-n D(P^*\|Q)}$ as $n \to \infty$
            * Explain: the contribution to $Q^n(E)$ of $(n + 1)^{|{\cal{X}}|}$ is vanished relative to $D^{-n D(P^*\|Q)}$
            * Another interpretation: the probability of a set of types under a distribution $Q$ is determined essentially by the probability of the closest element of the set to $Q$

---

# BONUS
* The notation $a_n≐b_n$ means,
$\lim_{n \to \infty} \frac{1}{n} \log \frac{a_n}{b_n}=0$.
That is, $a_n$ and $b_n$ agree to first order in the exponent
  * Another interpretation: $a_n \leq O(D^n) b_n$ where $D$ is the base of the logarithm
* Writing a probability distribution:
  * Statistics style: $p(x)$
  * Information theory style: $D^{- \log \frac{1}{p(x)}} = D^{-I_X(x)}$
  
  $\hspace{1.0cm} \rightarrow$ Writing probability in information theory style helps converting multiplication into addition (similar to what logarithm does to multiplication)
* The mapping from probability to information (measured by entropy or cross-entropy) is a one-to-one mapping
* Closure of a set: the closure of a set $S$ is the set $S$ together with all of its limit points
* Regular closed set: a set which has no “skinny holes” (holes without interior)

>**NOTE**: a regular closed set cannot have empty interior
* Explain: closure of an empty set is an empty set

$\hspace{1.0cm} \rightarrow$ The underlying set is empty, which is both open and closed which isn't regular closed

# Conditional limit theorem
## Introduction
**Assumptions**:
* $E$ is a set of probability distributions
* $P^* = \arg \min_{P \in E} D(P\|Q)$

**The goal of this section**: show that the total probability of other types which are far from $P^*$ is negligible
* Consequence (conditional limit theorem): the type observed is close to $P^*$ with very high probability

## Some insight into the geometry of $D(P\|Q)$
**Distribution space as a convex set**: a probability distribution space over $N$ values can be represented by a convex polygon with $N$ vertices in a $N$-dimensional space
* Vertices of the polygon: each vertex $V_i$ is a one-hot vector indicating the value it's responsible for (i.e. the unit vector of the dimension corresponding to the value it represents)
* Points within the polygon: each point within the polygon can be represented as a weighted sum of the polygon's vertices (i.e. $P = \sum_i p_i V_i = \textbf{p}^T \textbf{V}$) 

$\hspace{1.0cm} \rightarrow P_i = p_i$ represents the probability that the $i$-th value is chosen under the distribution indicated by that point
* Polygon shape: the polygon can be seen as a hyperplane in the $N$-dimensional space where the angle between the hyperplane and any hyperplane of the form $V_i = 0$ is $\frac{\pi}{4}$

**Pythagorean theorem**:
* Assumptions:
    * ${\cal{P}}$ is the set of all distributions
    * $E \subset {\cal{P}}$ is a closed convex set
    * $Q \notin E$ is a distribution
    * $P^* \in E$ is the distribution which achieves the minimum distance to $Q$
        * Formal: $D(P^*\|Q) = \min_{P \in E} D(P\|Q)$
* Conclusion:
    * $D(P\|Q) \geq D(P\|P^*) + D(P^*\|Q)$ for all $P \in E$
* Consequence: if there's some $P_n \in E$ that $D(P_n\|Q) \to D(P^*\|Q)$

$\hspace{1.0cm} \rightarrow D(P_n\|P^*) \to 0$

**${\cal{L}}_1$ distance between two distributions**: $\|P_1 - P_2\|_1 = \sum_{a \in {\cal{X}}} |P_1(a) - P_2(a)|$
* Intuition: the intuition of probability distribution as a convex set above
* Consequence:
    * Assumptions:
        * $A = \{x|P_1(x) > P_2(x)\}$
    * Conclusion:
        * $\|P_1 - P_2\|_1 = 2[P_1(A) - P_2(A)]$
            * Intuition (use KDE plot):
                * Since $\sum_x P_1(x) = \sum_x P_2(x)$
                
                $\hspace{1.0cm} \rightarrow |P_1(A) - P_2(A)|$ must equal to $|P_2(A^c) - P_1(A^c)|$ (i.e. the total difference $\sum_x (P_1(x) - P_2(x))$ must be zero)
                * From above, $\|P_1 - P_2\|_1 = (P_1(A) - P_2(A)) + (P_2(A^c) - P_1(A^c)) = 2 (P_1(A) - P_2(A))$
            * Intuition (use convex set):
                * Since $P_1$ and $P_2$ both belongs to the convex set indicated in the intuition of distribution
                
                $\hspace{1.0cm} \rightarrow$ If $P_1$ is larger than $P_2$ w.r.t some dimensions, the difference must be complemented by other dimensions
                * From above, $|P_1(A) - P_2(A)|$ must equal to $|P_2(A^c) - P_1(A^c)|$
        * $\max_{B \subseteq {\cal{X}}} |P_1(B) - P_2(B)| = P_1(A) - P_2(A) = \frac{\|P_1 - P_2\|_1}{2}$
            * Intuition (use convex set): $A$ is the largest set that $P_1(x) - P_2(x)$ has the same sign (i.e. positive sign, or negative if we're considering $A^c$) for all $x \in A$
            
            $\hspace{1.0cm} \rightarrow P_1(A) - P_2(A)$ is the largest distance (in terms of $L_1$ distance) we can be away from the hyperplane representing the probability distribution space
            * Explain:
                * $|P_1(B) - P_2(B)| = |\sum_{x \in B} (P_1(x) - P_2(x))|$
                
                $\hspace{1.0cm} \rightarrow |P_1(B) - P_2(B)|$ is maximized if and only if $P_1(x) - P_2(x)$ has the same sign for all $x \in B$
                * From above, $B$ can be either $A$ or $A^c$
                * $|P_1(A) - P_2(A)| = |P_2(A^c) - P_1(A^c)| = \frac{\|P_1 - P_2\|_1}{2}$
                
                $\hspace{1.0cm} \rightarrow \max_{B \subseteq {\cal{X}}} |P_1(B) - P_2(B)| = P_1(A) - P_2(A) = \frac{\|P_1 - P_2\|_1}{2}$

**Variational distance between $P_1$ and $P_2$**: $\max_{B \subseteq {\cal{X}}} |P_1(B) - P_2(B)|$

>**NOTE**: $P(B) = \sum_{X \in B} P(X)$

* Intuition: see the intuition of probability distribution space as a convex set
* Other names: 
    * Total variation distance
    * Statistical distance
* Interpretation: the largest possible difference between the probabilities that $P$ and $Q$ can assign to the same event
* Usage:  a distance measure for probability distribution

**Lemma**: $D(P_1\|P_2) \geq \frac{1}{2 \ln 2} \|P_1 - P_2\|_1^2$

## Conditional limit theorem
**Essential idea**: the probability of a type under $Q$ depends exponentially on the distance of the type to $Q$

$\hspace{1.0cm} \rightarrow$ Types that are farther away are exponentially less likely to occur

**Conditional limit theorem**:
* Assumptions:
    * ${\cal{P}}$ is the set of all distributions
    * $E$ is a closed convex subset of ${\cal{P}}$
    * $Q \notin E$ is a distribution
    * $X_1, ..., X_n$ are discrete random variables drawn i.i.d $\sim Q$
    * $P^* \in E$ is the distribution which achieves the minimum distance to $Q$
        * Formal: $D(P^*\|Q) = \min_{P \in E} D(P\|Q)$
* Conclusion:
    * $\text{Pr}(X_1 = a|P_{X^n} \in E) \to P^*(a)$ (in probability) as $n \to \infty$

# Hypothesis testing
**Hypothesis testing problem**: decide between two alternative explanations for the data observed
* General formulation:
    * $X_1, ..., X_n$ are i.i.d $\sim Q(x)$
    * $H_1: Q = P_1$ and $H_2: Q = P_2$ are hypotheses to test
* Decision function: $g(x_1, ..., x_n) = \begin{cases} 1 && H_1 \text{is accepted} \\ 2 && H_2 \text{is accepted} \end{cases}$ is the decision function
* Error probabilities:
    * Assumptions:
        * $A = \{x^n|g(x_1, ..., x_n) = 1\}$
    * Conclusion:
        * $\alpha = \text{Pr}(g(X_1, ..., X_n) = 2|H_1 \text{is true}) = P_1^n(A^c)$
        * $\beta = \text{Pr}(g(X_1, ..., X_n) = 1|H_2 \text{is true}) = P_2^n(A)$
* Task: minimize both $\alpha$ and $\beta$
    * Problem: there's a trade-off
    * Solution: minimize one of the probabilities of error s.t. a constraint on the other probability of error

**Neyman-Pearson lemma**:
* Assumptions: 
    * $X_1, ..., X_n$ are i.i.d $\sim Q(x)$
    * $H_1: Q = P_1$ and $H_2: Q = P_2$ are hypotheses to test
    * $A_n(T) = \{x^n|\frac{P_1(x_1, ..., x_n)}{P_2(x_1, ..., x_n)} \geq T\}$ where for some $T \geq 0$
    * $\alpha^* = P_1^n(A_n^c(T))$ and $\beta^* = P_2^n(A_n(T))$ are probabilities error corresponding to $A_n$
    * $B_n$ is any other decision with associated probabilities of error $\alpha$ and $\beta$
* Conclusion:
    * If $\alpha \leq \alpha^*$ then $\beta \geq \beta^*$
* Consequence: the optimal test for two hypotheses is of the form $\frac{P_1(x_1, ..., x_n)}{P_2(x_1, ..., x_n)} > T$

**Likelihood ratio**: $\frac{P_1(X_1, ..., X_n)}{P_2(X_1, ..., X_n)}$
* Log-likelihood ratio: $L(X_1, ..., X_n) = \log \frac{P_1(X_1, ..., X_n)}{P_2(X_1, ..., X_n)}$
    * Equivalent form of log-likelihood ratio test: $L(X_1, ..., X_n) = n D(P_{X^n}\|P_2) - n D(P_{X^n}\|P_1)$
    
    $\hspace{1.0cm} \rightarrow$ The likelihood ratio test is equivalent to $D(P_{X^n}\|P_2) - D(P_{X^n}\|P_1) > \frac{1}{n} \log T$