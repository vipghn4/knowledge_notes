**Perplexity**: measure how well a probability distribution or probability model predicts a sample
* Interpretation: a low perplexity indicates the probability distribution is good at predicting the sample
* Definitions:
	* Perplexity of a probability distribution: $D^{H(p)}$ where $D$ is the base of the logarithm used to compute the entropy $H(p)$
		* Perplexity of a random variable $X$: the perplexity of the distribution over its possible values $x$
	* Perplexity of a probability model: $D^H(p, q)$ where $D$ is the base of the logarithm used to compute the cross entropy $H(p, q)$
* Why language modeling people like perplexity instead of just entropy:
	* Due to the exponent, improvements in perplexity is more substantial
	* Before people started using perplexity, the complexity of a language model was reported using a simplistic branching factor measurement that's more similar to perplexity than it is to entropy

**Definition of Markov chain**:
* Formal definition: $X_1, ..., X_n$ forms a Markov chain if $\text{Pr}(X_n|X_{n-1}, ..., X_1) = \text{Pr}(X_n|X_{n-1})$
* Informal definition: the knowledge of $X_{n-1}$ gives us the same information as the knowledge of the entire chain $X_1, ..., X_{n-2}$ to move on to $X_n$ conditionally (the term "conditionally" is really important since it means we want to determine $X_n$ not in absolute but given previous values of the chain)

$\hspace{1.0cm} \rightarrow$ Given $X_{n-1}$, we have nothing to do with $X_{n-2}, ..., X_1$ (i.e. $X_n$ is independent of those states given $X_{n-1}$)

---

# NEW WORD
* Substantial (n): đáng kể

**Entropy of functions of a random variable**:
* $H[g(X)] \leq H(X)$
    * Prove: $H(X) = H[g(X)] - H[g(X)|X] + H[X|g(X)] = H[g(X)] + H[X|g(X)] \geq H[g(X)]$
* If $H(Y|X) = 0$ then $Y$ is a function of $X$
    * Explain: for all $x$ where $p(x) > 0$, there's only one possible $y$ with $p(x, y) > 0$

**New perspectives on information entropy**:
* Assumptions:
    * $X$ is a random variable with entropy $H(X)$
    * $E$ is an experiment bringing to us $n_e$ bits of information about $X$
        * Formal: $H(X|E) = H(X) - n_e$ or $I(X; E) = n_e$
* Conclusion: to completely determine $X$, we need $\frac{H(X)}{n_e}$ times of carrying out $E$

**Entropy of sampling with replacement**: 
* Assumptions:
    * $X$ is a random variable with distribution $p$
    * $p = \{p_1, ..., p_n\}$
    * $B$ is a box containing $a_i$ items of type $i$
* Task: sample a sequence $X^n = \{X_i\}_{i=1}^n$ from $B$ with replacement and compute $H(X^n)$
* Conclusion: $H(X^n) = \sum_{i=1}^n H(X_i)$ where $H(X_i) = \log(\sum_{i=1}^n a_i) - \sum_{i=1}^n \frac{a_i}{\sum_{j=1}^n a_j} \log a_i$

**A entropy-based metric for random variables**: $\rho(X, Y) = H(X|Y) + H(Y|X)$
* Prove: direct prove
    * $\rho(x, y) \geq 0$
    * $\rho(x, y) = \rho(y, x)$
    * $\rho(x, y) = 0$ if $x = y$
    * $\rho(x, y) + \rho(y, z) \geq \rho(x, z)$
        * Prove: direct prove 
            * $H(X|Y) + H(Y|X) + H(Y|Z) + H(Z|Y)$
            
            $\hspace{0.4cm} = H(X) + H(Y) - 2 I(X; Y) + H(Y) + H(Z) - 2 I(Y; Z)$

            $\hspace{0.4cm} = H(X) + H(Z) - 2 I(X; Z) + 2 H(Y) + 2 I(X; Z) - 2 I(X; Y) - 2 I(Y; Z)$

            $\hspace{0.4cm} = [H(X|Z) + H(Z|X)] + H(Y|X) + H(Y|Z) + 2 I(X; Z)$

            $\hspace{0.4cm} \geq H(X|Z) + H(Z|X)$
* Zero-valued metric: $X = Y$ (i.e. $\rho(X, Y) = 0$) if there's a one-to-one function $f: X \to Y$

**Addition of independent variables adds uncertainty**:
* Assumptions:
    * $X$ and $Y$ are random variables
    * $Z = X + Y$
* Conclusion: if $X$ and $Y$ are independent then 
    * $H(Z) \geq H(Y)$
    * $H(Z) \geq H(X)$