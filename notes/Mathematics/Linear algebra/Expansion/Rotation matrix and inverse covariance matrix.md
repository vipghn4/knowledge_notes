**Rotation matrix and how a vector is rotated**. Consider a rotation matrix 

$$\mathbf{R} = \begin{bmatrix}r_1&\cdots&r_n\end{bmatrix} \in \mathbb{R}^{n\times n}$$
* *Rotation of identity matrix*. Let $\mathbf{I}=\begin{bmatrix}e_1&\cdots &e_n\end{bmatrix}\in\mathbb{R}^{n\times n}$ is the identity matrix, we have

    $$\begin{aligned}
    \mathbf{R}\cdot\mathbf{I} &= \mathbf{R}\\
    \mathbf{R}\cdot e_i &= e_i
    \end{aligned}$$

    $\to$ This indicates that $\mathbf{R}$ rotates $e_i$ so that the resulting vector is $r_i$
* *Rotation of arbitrary vector*. Consider a vector $x=(x_1,\dots,x_n)$, we have that

    $$\begin{aligned}
    \mathbf{R} \cdot x &=\sum_{i=1}^n \mathbf{R}\cdot e_i
    \end{aligned}$$

    $\to$ This means that $\mathbf{R}$ first rotates the basis $\beta_I=\{e_1,\dots,e_n\}$ to obtain the basis $\beta_R=\{r_1,\dots,r_n\}$, then compute the location of $x$, given its coordinates w.r.t the original basis $\beta_I$

**Covariance matrix**.
* *Variation along a dimension*. Consider again the product $x^T S x$ where $S$ is a covariance matrix of some multivariate distribution
    * *Assumptions*.
        * Since $S$ is symmetric, suppose its eigen decomposition is given as

            $$S=PDP^T$$
    * *Observations*. As given previously $x^T S x$ gives the variation of the distribution, over the dimension of $x$

        $\to$ How this is done under the hood?
    * *Conclusion*. We have that $x^T S x = (P^T x)^T D (P^T x)$, therefore, the procedure is
        1. $P^T$ rotates $x$ to obtain $P^T x$, which is aligned with variational dimensions of the distribution
        2. $D^{1/2}$ scales $P^T x$ along each dimension, by the standard deviation of that dimension
        3. $\|D^{1/2} P^T x\|_2^2$ is then computed, as the variation of the distribution along the dimension of $x$
* *Mahalanobis distance*. Consider the distance $x^T S^{-1} x$
    * *Observations*. We have that 
    
        $$\begin{aligned}
        x^T S^{-1} x&=x^T (P D P^T)^{-1} x\\ 
        &= x^T P^{-T} D^{-1} P^{-1} x\\
        &=x^T P D^{-1} P^T x\\
        &=(P^T x)^T D^{-1} (P^T x)
        \end{aligned}$$
    
    * *Conclusion*. The procedure here is
        1. $x$ is rotated by $P^T$ to obtain $P^T x$, which is aligned with variation dimensions of the distribution
        2. $P^T x$ is normalized by $D^{-1/2}$ along each dimension, i.e. by the standard deviation of that dimension
        3. $\|D^{-1/2} P^T x\|_2^2$ is computed, as the normalized variation of the distribution along the dimension of $x$