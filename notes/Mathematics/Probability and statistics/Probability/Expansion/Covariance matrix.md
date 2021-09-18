<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Covariance matrix](#covariance-matrix)
- [Discussion](#discussion)
<!-- /TOC -->

# Covariance matrix
**Other names**: auto-covariance matrix, dispersion matrix, variance matrix or variance-covariance matrix

**Defnition**:
* Covariance matrix: $\text{cov}(\textbf{X}) = E[(\textbf{X} - E[\textbf{X}]) (\textbf{X} - E[\textbf{X}])^T]$ or $\text{cov}(\textbf{X})_{ij} = \text{cov}(\textbf{X}_i, \textbf{X}_j)$
  * Another notation: $\textbf{K}_{\textbf{X} \textbf{X}}$ 
* Cross-corvariance matrix: $\text{cov}(\textbf{X}, \textbf{Y}) = E[(\textbf{X} - E[\textbf{X}]) (\textbf{Y} - E[\textbf{Y}])^T]$ or $\text{cov}(\textbf{X})_{ij} = \text{cov}(\textbf{X}_i, \textbf{Y}_j)$
  * Another notation: $\textbf{K}_{\textbf{X} \textbf{Y}}$


**Covariance matrix of linear function**. 
* *Assumption*.
    * $x \in \mathbf{R}^n$ is a random vector with covariance $\Sigma_x$
    * $y = A x \in \mathbf{R}^m$ is another random vector where $A$ is a given parameter
        * $\Sigma_y$ is the covariance matrix of $y$
* *Observations*.
    * Assume that $A = a^T$ for some $a\in\mathbf{R}^n$

        $\to$ $\text{Var }(a^T x) = a^T \Sigma_x a$
    * We also have that $\text{Cov }(a_1^T x, a_2^T x) = a_1^T \Sigma_x a_2$
* *Conclusion*. $\text{Cov }(Ax)=A \Sigma_x A^T$
* *Corollary*. $\text{Cov }(Ax + b)=A\Sigma_x A^T + \Sigma_b$ for any random vector $b$ with covariance $\Sigma_b$, which is statistically independent of $x$

**Covariance matrix as a linear operator**: 
* Assumptions:
    * $\textbf{X}$ is a random vector with covariance $\text{cov}(\textbf{X})$
    * $\textbf{c}$ and $\textbf{d}$ are two vectors
* Conclusion:
    * $\textbf{c}^T \text{cov}(\textbf{X}) = \text{cov}(\textbf{c}^T \textbf{X}, \textbf{X})$
    * $\text{cov}(\textbf{X}) \textbf{c} = \text{cov}(\textbf{X}, \textbf{c}^T \textbf{X})$
* Consequence: $\textbf{d}^T \text{cov}(\textbf{X}) \textbf{c} = \text{cov}(\textbf{d}^T \textbf{X}, \textbf{c}^T \textbf{X})$

**Properties**:
* Assumptions:
    * $X = (X_1, ..., X_n)$ is a random vector from distribution $P$
    * $Y = (Y_1, ..., Y_n)$ is a random vector from distribution $P$
    * $\textbf{S}$ is the covariance matrix of $P$
    * $\mu$ is the mean of $P$
* Properties:
    * $\text{Var}(\sum_i X_i) = \sum_{i, j} \text{Cov}(X_i, X_j)$
    * $x^T \textbf{S} x$ gives the variance of $x$, in the sense that $x^T \textbf{S} x = \text{Var}(\sum_i x_i X_i)$
        * Explain:
            * $x = \sum_i x_i e_i$ where $e_i$ is the $i$-th column of the identity matrix
            * From above, $x^T \textbf{S} x = \sum_{i, j} x_i x_j (e_i^T \textbf{S} e_j)$ 
            
            $\hspace{3.3cm} = \sum_{i, j} x_i x_j \text{Cov}(X_i, X_j)$ 
            
            $\hspace{3.3cm} = \sum_{i, j} \text{Cov}(x_i X_i, x_j X_j)$
            
            $\hspace{3.3cm} = \text{Var}(\sum_i x_i X_i)$
            
  * $\textbf{S}$ characterizes a hyperellipsoid which can be used to approximate data distribution shape
    * Explain:
        * Consider the SVD of $\textbf{S} = \textbf{P} \textbf{D} \textbf{P}^T$
            * Due to symmetry, $\textbf{P} \textbf{D} \textbf{P}^T$ is also the diagonalization of $\textbf{S}$
        * Consider $\sigma_i$ and $v_i$ as eigenvalues and eigenvectors of $\textbf{S}$
        * $x^T \textbf{S} x$ gives the variance of $x$ (as stated above)

        $\hspace{1.0cm} \rightarrow v_i^T \textbf{S} v_i = \sigma_i \|v_i\|_2^2$
        * From above, the distribution of the data can be approximated as a hyperellipsoid $E: \sum_i \frac{x_i}{\sigma_i} = 1$ w.r.t the basis formed by the columns of $\textbf{P}$

# Discussion
**From covariance matrix to PCA**:
* Idea: reduce the dimension of data so that we can keep as much variance as possible
* Method:
    * Assumptions:
        * $\textbf{X} = \begin{bmatrix} \textbf{x}_1 && \cdots && \textbf{x}_n \end{bmatrix}$ is the matrix of data
        * $\bar{\textbf{x}}_n = \frac{1}{n} \sum_i \textbf{x}_i$ is the sample mean
    * Procedure:
        * Step 1: normalize the data by the formula
        
        $\hspace{3.0cm} \hat{\textbf{x}}_i = \textbf{x}_i - \bar{\textbf{x}}_n$
        * Step 2: compute the sample covariance matrix of the normalized data
        
        $\hspace{3.0cm} \textbf{S} = \frac{1}{n} \sum_i \hat{\textbf{x}}_i \hat{\textbf{x}}_i^T$ (or in vectorized form $\textbf{S} = \frac{1}{n} \hat{\textbf{X}} \hat{\textbf{X}}^T$)
        * Step 3: compute the SVD $\textbf{S} = \textbf{P} \textbf{D} \textbf{P}^T$ where diagonal entries of $\textbf{D}$ are sorted in decreasing order
        * Step 4: take the first $k$ columns of $\textbf{P}$ (i.e. corresponding to the $k$ largest eigenvalues of $\textbf{S}$) to form a basis
        * Step 5: for any new example $\textbf{x}$, write $\textbf{x}$ as $\sum_{i = 1}^k c_i \textbf{P}_{:,i}$ then take $\textbf{c} = (c_1, ..., c_k)$ as the reduced version of $\textbf{x}$
* Intuition: project the data distribution, which is approximated by an hyperellipsoid, onto another basis which preserves as much variance as possible

**From covariance matrix to Mahalanobis distance**:
* Derivation:
    * Consider the SVD $\textbf{S} = \textbf{P} \textbf{D} \textbf{D}^T$
    * Consider $x$ w.r.t the basis formed by the columns of $\textbf{P}$
        * Formal: $x = \sum_i c_i \textbf{P}_{:,i} = \textbf{P} \textbf{c}$
    * $x^T \textbf{S}^{-1} x = \textbf{c}^T \textbf{D}^{-1} \textbf{c} = \|\textbf{D}^{-1/2} \textbf{c}\|_2^2$

    $\hspace{1.0cm} \rightarrow x^T \textbf{S}^{-1} x$ is another measure of relative distance from the distribution characterized by $\textbf{S}$ and $x$
* Intuition:
    * Step 1: we plot $x$ w.r.t to the basis formed by the columns of $\textbf{P}$ (i.e. its coordinate would be $\textbf{c}$)
    * Step 2: scale down $c_i$ by $\sigma_i$ (i.e. the variance of the data in the direction of $\textbf{P}_{:, i}$)
    * Step 3: compute $\|\textbf{c}\|$ after scaling

**Singularity of covariance matrix**: 
* Assumptions:
    * $\hat{\textbf{x}}_i = \textbf{x}_i - \bar{\textbf{x}}_n$
    * $\textbf{S} = \frac{1}{n} \sum_i \hat{\textbf{x}}_i \hat{\textbf{x}}_i^T$ 
        * Vectorized form: $\textbf{S} = \frac{1}{n} \hat{\textbf{X}} \hat{\textbf{X}}^T$
* Conclusion: if the sample size $m$ is smaller than $n$

$\hspace{1.0cm} \rightarrow$ The sample covariance $\textbf{S}$ is singular
* Explain: see the Matrix rank note