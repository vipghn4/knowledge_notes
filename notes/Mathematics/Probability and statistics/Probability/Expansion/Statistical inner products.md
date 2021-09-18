<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
  - [Inner product](#inner-product)
  - [Statistical inner product](#statistical-inner-product)
  - [Statistical quantities in inner product space](#statistical-quantities-in-inner-product-space)
<!-- /TOC -->

## Inner product
**Inner product**:
* Assumptions:
    * $V$ is a vector space over the field $F$
* Conclusion:
    * Inner product $\langle \cdot, \cdot \rangle: V \times V \to F$: a map satisfying
        * Conjugate symmetry: $\langle x, y \rangle = \langle y, x \rangle$
        * Linearity in first argument:
            * $\langle a x, y \rangle = a \langle x, y \rangle$
            * $\langle x + y, z \rangle = \langle x, z \rangle + \langle y, z \rangle$
        * Positive-definite: $\langle x, x \rangle > 0$ $\forall x \in V / \{0\}$
* Usage: generalize Euclidean spaces (i.e. the inner product is the dot product, or scalar product) to vector space of any dimension

**Examples**:
* Real numbers: $\langle x, y \rangle = x y$
* Euclidean space: $\langle x, y \rangle = x^T y$
* Complex coordinate space: $\langle x, y \rangle = x^T M y = y^T M^T x$
    * Explain: $x^T M y = x^T z$ where $z = M y$
* Hilbert space: $\langle f, g \rangle = \int_a^b f(t) g^*(t) dt$ where $g^*(t)$ means the conjugate of $g$
* Random variables: $\langle X, Y \rangle = E(X Y)$
    * See below
* Real matrices: $\langle A, B \rangle = \textbf{tr }(A B^T)$
    * Explain: $\textbf{tr }(A B^T) = \sum_{ij} A_{ij} B_{ij}$

## Statistical inner product
**Expectation of product as inner product**: $E(X, Y)$
* Inner product:
    * Interpretation: $E(X, Y) = \textbf{x}^T \textbf{f}(X, Y) \textbf{y}$
        * $\textbf{x} = (x_1, ..., x_{N_x})$ is the vector of possible values of $X$
        * $\textbf{y} = (y_1, ..., y_{N_y})$ is the vector of possible values of $Y$
        * $\textbf{f}(X, Y) \in \textbf{R}^{N_x \times N_y}$ is the p.m.f matrix with $\textbf{f}_{ij} = f(x_i, y_j)$
    * Conclusion: $E(X, Y)$ can be seen as an inner product in complex coordinate space (see above)
* Norm: $\|X\| = \sigma_X = \sqrt{E(X^2)}$

## Statistical quantities in inner product space
**Expectation of product of two independent random variables**: if $X$ and $Y$ are independent, $\textbf{f}(X, Y) = \textbf{f}_X \textbf{f}_Y^T$

$\hspace{1.0cm} \rightarrow E(X, Y) = (\textbf{f}_X^T \textbf{x})^T (\textbf{f}_Y^T \textbf{y}) = E(X) E(Y)$

**Variance and standard deviation**:
* Definition: 
    * Variance: $\text{Var }(X) = E(X^2) - E(X)^2$
        * Explain: $E(X)$ and $X - E(X)$ is orthogonal w.r.t the inner product $E(X, Y)$
        
        $\hspace{1.0cm} \rightarrow \|E(X)\|^2 + \|X - E(X)\|^2 = \|X\|^2$
    * Standard deviation: $\sigma_X = \|X - E(X)\|$
* Properties of variance:
    * Variance of sum: $\text{Var }(X + Y) = \text{Var }(X) + 2 \text{Cov }(X, Y) + \text{Var }(Y)$
        * Extension to Euclidean space: $\|X + Y\|^2 = \|X\|^2 + 2 \langle X, Y \rangle + \|Y\|^2$
    * Law of total variance: $\text{Var }(Y) = E[\text{Var }(Y|X)] + \text{Var }[E(Y|X)]$
        * Explain: $Y - E(Y|X)$ (unexplained variance) and $E(Y|X) - E(Y)$ (explained variance) are orthogonal

**Covariance and correlation**:
* Definition:
    * Covariance: $\text{Cov }(X, Y) = \langle \hat{X}, \hat{Y} \rangle$ where $\hat{X} = X - E(X)$ and $\hat{Y} = Y - E(Y)$
    * Correlation: $\rho(X, Y) = \frac{\langle \hat{X}, \hat{Y} \rangle}{\|\hat{X}\| \|\hat{Y}\|}$
* Properties of covariance:
    * Range of correlation: $[-1, 1]$
    * Maximum correlation: when $Y = a X + b$ where $a > 0$