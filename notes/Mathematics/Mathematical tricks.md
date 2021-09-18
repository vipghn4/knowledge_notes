# Tricks
**Derivation trick**: assume that some approximation is right and find the parameters of the approximation
* Examples: Fourier series, Taylor series, power series, etc.

**Proof trick**: 
* Prove that $a = b$ by proving $a \leq b \land a \geq b$ is true
    * Variation: prove $f(x) = g(x)$ by proving $f(x) \in [g(x) - \epsilon, g(x) + \epsilon]$ where $\epsilon \to 0$
* Prove $f(x) \leq c$ by solving $f'(x) = 0$ and show that $\max_x f(x) \leq c$
* Jensen's inequality: if $f$ is convex then $f(\sum_i a_i x_i) \leq \sum_i a_i f(x_i)$ where $\sum_i a_i = 0$ and $a_i \geq 0$
    * Question: how to choose $f$, $x_i$, and $a_i$
    * Special cases: 
        * $f[E(X)] \geq E[f(X)]$
        * $a_1 = ... = a_n = \frac{1}{n}$
    * Applications:
        * Very useful for probability-related fields like Information theory, Probability and statistics, due to the wide usage of $\log(\cdot)$, a concave function, in these fields
        * Convex optimization - where this inequality comes from
* Prove something about $A x$: consider each element of $A x$ separately
    * Example: prove that eigenvalues of Markov transition matrix have magnitude at most $1$

**An application of linear difference equation**: $N(t) = \sum_{i=1}^{t-1} N(t - i)$ where $N(t)$ is a function of time
* Example: the number of customers arrived during $t$ hours

**Application of Information theory**: 
* Any quantity of the form $\log x_i$ or $\sum_i a_i \log x_i$, can be converted into self-information or cross-entropy to exploit Information theory's rules
* Axiom 3 of information entropy is a useful tool