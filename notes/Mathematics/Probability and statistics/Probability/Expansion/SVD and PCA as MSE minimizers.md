<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [SVD and PCA as MSE minimizers](#svd-and-pca-as-mse-minimizers)
  - [Singular value decomposition](#singular-value-decomposition)
  - [PCA as MSE minimizer](#pca-as-mse-minimizer)
<!-- /TOC -->

# SVD and PCA as MSE minimizers
## Singular value decomposition
**Singular value decomposition**. The best low rank approximation of a matrix

$\to$ This is the decomposition that all others try to beat
* *Formulation*.
    * *Assumptions*.
        * $A\in\mathbf{R}^{m\times n}$ where $m > n$ is a matrix
        * $U\in\mathbf{R}^{m\times m}$ is an orthogonal matrix
        * $\Sigma\in\mathbf{R}^{m\times n}$ is a diagonal matrix with entries $\sigma_1,\dots,\sigma_n$
        * $V\in\mathbf{R}^{n\times n}$ is another orthogonal matrix
    * *SVD*. $A=U \Sigma V^*$ where $V^*$ denotes the conjugate transpose of $V$
* *Thin SVD*. $A = U \Sigma V^*$ where $U\in\mathbf{R}^{m\times n}$ and $\Sigma \in \mathbf{R}^{n\times n}$

**Low rank approximation**.
* *Assumptions*.
    * $r=\min(m,n)$ is the rank of $A$
    * $U\in\mathbf{R}^{m\times r}$ is a matrix with orthogonal columns
    * $\Sigma\in\mathbf{R}^{r\times r}$ is a diagonal matrix
    * $V\in\mathbf{R}^{n\times r}$ is a matrix with orthogonal columns
* *SVD approximation of $A$*. $A = U\Sigma V^T=\sum_{i=1}^r \sigma_i u_i v_i^T$
* *Rank $k$ approximation*. $A_k=\sum_{i=1}^k \sigma_i u_i v_i^T$ where $k<r$
    * *Intuition*. $A_k$ is the projection of $A$ onto the space spanned by the top $k$ singular vectors of $A$
* *Drawbacks for SVD*. Expensive to compute if the dimension of $A$ is very large

**Eckart-Young theorem**.
* *Assumptions*.
    * $A_k$ is the rank-$k$ approximation of $A$ achieved by SVD-truncation
    * $r=\min(m,n)$ is the rank of $A$
* *Conclusion*. $A_k$ is the closest rank-$k$ matrix to $A$, i.e.

    $$\forall B\in\{B:\text{rank}(B)=k\},\|A-A_k\|_F\leq \|A-B\|_F$$
* *Proof*.

**Minimal error given by the SVD truncation**. $\|A-A_k\|_F=\sqrt{\sigma^2_{k+1}+\dots+\sigma_r^2}$
* *Proof*.
    * Let $\Sigma_k$ is a diagonal matrix obtained by keeping the first $k$ entries of $\Sigma$, We have that

        $$U^T(A-A_k)V=\Sigma - \Sigma_k$$
    * Since $U$ and $V$ are orthonormal matrices, we have that

        $$\begin{aligned}
        \|U^TAV\|_F^2&=\|U^T A\|^F_2\\
        &=\|A\|_F^2
        \end{aligned}$$
    * We have that

        $$\begin{aligned}
        \|A-A_k\|_F^2&=\|U^T(A-A_k)V\|_F^2\\
        &=\text{trace}(V^T(A-A_k)^TU U^T(A-A_k)V)\\
        &=\text{trace}((\Sigma-\Sigma_k)^T (\Sigma - \Sigma_k))\\
        &=\sum_{i=k+1}^r \sigma_i^2
        \end{aligned}$$

**SVD as best low rank approximation w.r.t spectral norm**. SVD also gives the best low rank approximation in spectral norm, i.e.

$$\|A-A_k\|_2=\min_{\text{rank}(B)=k}\|A-B\|_2=\sigma_{k+1}$$

## PCA as MSE minimizer
**PCA as MSE minimizer**.
* *Assumptions*.
    * $X = \begin{bmatrix}x_1 & \cdots & x_n\end{bmatrix}$ is the data matrix of size $r\times n$
        * $x_1,\dots,x_n$ are i.i.d
        * $x_i$ has zero mean, i.e. $E(x_i) = 0$
    * $\Sigma_X \in \mathbf{R}^{r\times r}$ is the covariance matrix of $x_i$ with SVD

        $$\Sigma_X = P\Sigma P^T$$
        
        where $P$ is an orthonormal matrix
    * $I_k\in\mathbf{R}^{r\times r}$ is a matrix obtained from identity matrix $I$ by keeping only $k$ non-zero diagonal entries
* *Compression and reconstruction*. 
    * *Compression*. $z=I_k P^T x$
    * *Reconstruction*. $\hat{x}=Pz=P I_k P^T x$
* *Reconstruction error of PCA*. 

    $$\forall M\in\mathbf{R}^{r\times r},E(\|x-MI_kM^Tx\|_2^2)\geq E(\|x-PI_kP^Tx\|_2^2)$$