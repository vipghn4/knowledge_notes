# On spectral clustering - Analysis and an algorithm
## Introduction
**Problem of interest**. Clustering points in $\mathbb{R}^n$
* *A standard approach*. Based on generative models, in which algorithms, e.g. EM, are used to learn a mixture density
    * *Drawbacks*.
        * To use parametric density estimators, harsh simplifying assumptions usually need to be made, e.g. the density of each cluster is Gaussian
            * *Example*. K-means clustering assumes that each cluster forms a Gaussian
        * The log likelihood can have many local minima, thus multiple restarts are required to find a good solution using iterative algorithms
* *A promising alternative*. Use spectral methods for clustering
    * *Idea*. Use the top eigenvectors of a matrix derived from the distance between points
    * *Usage*. Successfully used in many applications, e..g computer vision and VLSI design
    * *Problem*. 
        * Different authors still disagree on exactly which eigenvectors to use and how to derive clusters from them
        * The analysis of these algorithms has tended to focus on simplified algorithms, which only use one eigenvector at a time

**Spectral graph partitioning**. A line of analysis makes the link to spectral graph partitioning, in which the second eigenvector of a graph's Laplacian is used to define a semi-optimal cut
* *Idea*. The eigenvector is seen as a solving a relaxation of an NP-hard discrete graph partitioning problem

    $\to$ It can be shown that cuts based on the second eigenvector give a guaranteed approximation to the optimal cut
    * *Discrete graph partitioning problem*.
    * *Optimality of the second eigenvector of the Laplacian*.
* *Generalization to clustering*. This analysis can be extended to clustering by building a weighted graph, in which nodes correspond to data points and edges are related to the distance between them
    * *Idea*. Since the majority of analyses in spectral graph partitioning appear to deal with partitioning the graph into exactly two parts

        $\to$ These methods are typically applied recursively to find $k$ clusters
    * *Experimental observation*. Experimentally, it has been observed that using more eigenvectors and directly computing a $k$-way partitioning is better

## Algorithm
**Algorithm**.
* *Assumptions*. $S = \{s_1,\dots,s_n\} \in \mathbb{R}^l$ is a set of points we want to cluster into $k$ subsets
* *Algorithm*.
    1. Form the affinity matrix $A\in\mathbb{R}^{n\times n}$ defined by

        $$A_{ij} = \begin{cases}\exp(-\|s_i - s_j\|^2 / 2\sigma^2) & i \neq j \\ 0 & \text{otherwise}\end{cases}$$
    
    2. Define $D$ to be the diagonal matrix, whose $(i,i)$-element is the sum of $A$'s $i$-th row, then reconstruct the matrix $L = D^{-1/2} A D^{-1/2}$
    3. Find $x_1,\dots,x_k$, the $k$ largest eigenvectors of $L$ (chosen to be orthogonal to each other in case of repeated eigenvalues)

        $\to$ Form the matrix $X = \begin{bmatrix}x_1 & \cdots & x_k\end{bmatrix} \in \mathbb{R}^{n\times k}$ by stacking the eigenvectors in columns
    4. Form the matrix $Y$ from $X$ by renormalizing each of $X$'s rows to have unit length, i.e. $Y_{ij} = X_{ij} / \sqrt{\sum_j X_{ij}^2}$
    5. Treating each row of $Y$ as a point in $\mathbb{R}^k$, cluster them into $k$ clusters via K-means or any other algorithm, which attempts to minimize distortion
    6. Assign the original point $s_i$ to cluster $j$ if and only if row $i$ of the matrix $Y$ was assigned to cluster $j$
 * *Scaling parameter*. $\sigma^2$ controls how rapidly $A_{ij}$ falls off with the distance between $s_i$ and $s_j$

**Why not running K-means clustering directly to the data**.
* K-means running running directly to the data finds unsatisfactory clustering
* Once we map the points to $Y$'s rows, they form tight clusters, from which our method obtains the good clustering

## Analysis of algorithm
### Informal discussion - The ideal case
**Ideal case**. To understand the algorithm, it is instructive to consider its behavior in the ideal case, in which all points in different clusters are infinitely far apart
* *Assumptions*.
    * $k=3$ is chosen
    * There are three clusters $S_1,S_2,S_3$ of sizes $n_1,n_2,n_3$, i.e.

        $$S=S_1\cup S_2 \cup S_3,\quad n=n_1 + n_2 + n_3$$
    * To simplify our exposition, assume points in $S=\{s_1,\dots,s_n\}$ are ordered according to which cluster they are in
    * Clusters are moved infinitely far apart, i.e. 

        $$\hat{A}_{ij}=\begin{cases}0 & x_i,x_j \text{ are in different clusters} \\ A_{ij} & \text{otherwise}\end{cases}$$
    * $\hat{L},\hat{D},\hat{X},\hat{Y}$ are defined in the previous algorithm, starting with $\hat{A}$ instead of $A$
        * $\hat{A}$ and $\hat{L}$ are block-diagonal, i.e.

            $$\hat{A} = \begin{bmatrix}
            A^{(11)} & 0 & 0 \\ 0 & A^{(22)} & 0 \\ 0 & 0 & A^{(33)}
            \end{bmatrix};\quad\hat{L} = \begin{bmatrix}
            \hat{L}^{(11)} & 0 & 0 \\ 0 & \hat{L}^{(22)} & 0 \\ 0 & 0 & \hat{L}^{(33)}
            \end{bmatrix}$$
        
        * $\hat{L}^{(ii)} = (\hat{D}^{(ii)})^{-1/2} A^{(ii)} (\hat{D}^{(ii)})^{-1/2}$
    * $\hat{d}^{(i)} \in \mathbb{R}^{n_i}$ is the vector containing $\hat{D}^{(ii)}$'s diagonal elements
    * $\hat{d}\in\mathbb{R}^n$ is the vector containing $\hat{D}$'s diagonal elements
* *Notations*. $j\in S_i$ means $s_j \in S_i$
* *Intra-cluster affinities for cluster $i$*. $\hat{A}^{(ii)} = A^{(ii)} \in \mathbb{R}^{n_i\times n_i}$

**Construction of $\hat{X}$**.
* *Finding the first $k=3$ eigenvectors of $\hat{L}$*. Since $\hat{L}$ is block diagonal
    
    $\to$ Its eigenvalues and eigenvectors are the union of the eigenvalues and eigenvectors of its blocks, with the latter padded appropriately with zeros
    * *Eigenvalues of $\hat{L}$*.
        * $\hat{L}^{(ii)}$ has a strictly positive principal eigenvector $x_1^{(i)} \in \mathbb{R}^{n_i}$ with eigenvalue $1$
        * Since $A_{jk}^{(ii)} > 0$ for $j\neq k$, the next eigenvalue is strictly less than $1$
* *Construction of $\hat{X}$*. Stacking $\hat{L}$'s eigenvectors in columns will yield $\hat{X}$, i.e.

    $$\hat{X}=\begin{bmatrix}
    x_1^{(1)} & \vec{0} & \vec{0}\\
    \vec{0} & x_1^{(2)} & \vec{0}\\
    \vec{0} & \vec{0} & x_1^{(3)}
    \end{bmatrix}\in\mathbb{R}^{n\times 3}$$

# References
* [1] On spectral clustering - Analysis and an algorithm - Andrew Y. Ng, Michael I. Jordan