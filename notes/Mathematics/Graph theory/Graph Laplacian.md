<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Graph Laplacian](#graph-laplacian)
  - [Introduction](#introduction)
  - [Real-valued functions on graphs](#real-valued-functions-on-graphs)
  - [Connectivity](#connectivity)
  - [Laplacian of fundamental graphs](#laplacian-of-fundamental-graphs)
  - [Laplacian embedding](#laplacian-embedding)
  - [Other Laplacian matrices](#other-laplacian-matrices)
  - [The graph partitioning problem](#the-graph-partitioning-problem)
- [Appendix](#appendix)
  - [Concepts](#concepts)
  - [References](#references)
<!-- /TOC -->

# Graph Laplacian
## Introduction
**Graph Laplacian**. A matrix representation of a graph (from [2])
* *Definition*. 
    * *Assumptions*. 
        * $G$ is a simple graph with $n$ vertices
        * $D$ is the degree matrix, i.e. a diagonal matrix with $D_{i,i}$ is the degree of vertex $i$
        * $A$ is the adjacency matrix of $G$, i.e. $A_{i,j}$ indicates whether vertices $i$ and $j$ are adjacent or not
    * *Laplacian matrix of $G$*. $L = D - A \in \mathbf{R}^{n\times n}$, i.e.

        $$L_{i,j}=\begin{cases}
        \text{deg}(v_i) & i = j\\
        -1 & i\neq j \land A_{i,j} = 1\\
        0 & \text{otherwise}
        \end{cases}$$

* *Usage*. 
    * Find many useful properties of a graph, e.g. the number of spanning trees
    * Act as a natural link between discrete representations, e.g. graphs, and continuous representations, e.g. vector spaces and manifolds
* *Most important application*. 
    * Spectral clustering, i.e. correspond to a computationally tractable solution to the graph partitioning problem
    * Spectral matching, i.e. solve for graph matching

**Spectral graph theory**. Study the properties of graphs via the eigenvalues and eigenvectors of a graph via its Laplacian

## Real-valued functions on graphs
**Real-valued function on graph**. Any function $f:{\mathcal{V}} \to\mathbf{R}$
* *Vector representation*. We can see that $f\in\mathbf{R}^n$ where $n=|{\mathcal{G}}|$
* *Notation*. $f = (f(v_1),\dots,f(v_n)) = (f(1),\dots,f(n))$

**Adjacent matrix as eigenfunctions**. The eigenvectors of the adjacency matrix $A$ can be seen as eigenfunctions w.r.t linear operator $A$
* *Adjacent matrix as operator*. If $g = A\cdot f$ then $g(i) = \sum_{A_{i,j} = 1} f(j)$
* *Adjacent matrix as a quadratic form*. $f^T A f = \sum_{A_{i,j} = 1} f(i) f(j)$

**Graph spectrum**. The set of graph eigenvalues of the adjacency matrix
* *Intuition*.

**Co-boundary mapping of the graph**. The mapping $T:f\to\nabla \cdot f$ where $f$ is a real-valued function on the graph, and $\nabla$ is the indicence matrix of the transformed graph
* *Incidence matrix of a graph $|\mathcal{E}|\times |\mathcal{V}|$*. A $m\times n$ matrix $\nabla$ defined as

    $$\nabla = \begin{cases}
    \nabla_{ev} = -1 & v\text{ is the initial vertex of } e\\
    \nabla_{ev} = 1 & v\text{ is the terminal vertex of } e\\
    \nabla_{ev} = 0 & v\text{ is not in } e\\
    \end{cases}$$
* *Co-boundary mapping of the graph*. $(\nabla f)(e_{i,j}) = f(v_j) - f(v_i)$
    * $e_{i,j}$ is the edge from $i$ to $j$
    * $v_i,v_j$ are vertices $i$ and $j$

**Laplacian matrix of a graph from co-boundary mapping**. 
* *Formal*.
    * $L=\nabla^T \nabla$
    * $(L f)(v_i) = \sum_{v_i \sim v_j} (f(v_i) - f(v_j))$
* *Theorem*. $L = D - A$ (easy to prove)
* *Intuition*.
    * Let $N(v)$ be the set of vertices having connection with vertex $v$ 
    * Consider the product of the Laplacian matrix $L$ and a function $f$ defined on $\mathcal{V}$

        $$\begin{aligned}
        L\cdot f&=\begin{bmatrix}
        |N(v_1)| f(v_1) - \sum_{u\in N(v_1)} f(u)\\
        \vdots\\
        |N(v_n)| f(v_n) - \sum_{u\in N(v_n)} f(u)\\
        \end{bmatrix}=\begin{bmatrix}
            \sum_{u\in N(v_1)} [f(v_1) - f(u)]\\
            \vdots\\
            \sum_{u\in N(v_n)} [f(v_n) - f(u)]\\
            \end{bmatrix}\\
        \end{aligned}$$
    
    * This is somewhat similar to the Laplacian of a function $f$ with $h_1=1$ and $h_2=-1$ and

        $$f'(x)=\frac{f(x+h_1) - f(x)}{h_1},\quad f''(x)=\frac{f'(x+h_2) - f'(x)}{h_2}$$
    
* *Consequences*. 
    * *Derivative of graph*. From the Laplacian of graph, we can define directional derivatives of graph at a node $v\in\mathcal{V}$ w.r.t a neighbor $u\in N(v)$ as

        $$\frac{\partial f}{\partial u}(v)=\frac{f(u)-f(v)}{h}$$

        where $h=1$ or $h=-1$ depending on the definition of the user
        * *Intuition of $h$*. Neighbor vertices within a graph is treated as having unit space between each other
    * *Generalization*. A Euclidean space can be seen as a infinite graph with infinitely many nodes, each of which has vertical and horizontal neighbors as in ordinary Euclidean space

        $\to$ In this case, graph Laplacian becomes ordinary Laplapce operator, with $h\to 0$
        * *Consequence*. Eigenvectors of the graph Laplacian now becomes eigenfunctions of Laplace operator

**Laplacian matrix of undirected weighted graph**.
* *Assumption*. $\mathcal{G}$ is a graph where each edge $e_{i,j}$ is weighted by $w_{i,j} > 0$
* *Laplacian matrix of $\mathcal{G}$*. $(L f)(v_i) = \sum_{v_j \sim v_i} w_{i,j} (f(v_i) - f(v_j))$
    * *Quadratic form*. $f^T L f = \frac{1}{2} \sum_{e_{i,j}} w_{i,j} (f(v_i) - f(v_j))^2$
* *Intuition*.
    * The degree matrix $D$ is given as

        $$D=\begin{bmatrix}
        \sum_{i=1}^n w_{1,i} & 0 & \cdots & 0\\
        \vdots & \vdots & \ddots & \vdots\\
        0 & 0 & \cdots & \sum_{i=1}^n w{n,i}
        \end{bmatrix}$$
    * The adjacenct matrix $A$ is given as

        $$A=\begin{bmatrix}
        w_{11} & \cdots & w_{1n}\\
        \vdots & \ddots & \vdots\\
        w_{n1} & \cdots & w_{nn} 
        \end{bmatrix}$$

**Properties of Laplacian matrix of graph**.
* *Theorem*. $L$ is symmetric and positive semi-definite
    * *Proof*.
        * For unweighted graphs

            $$\forall x,x^T L x = \sum_{(i,j)\in\mathcal{E}} (x_i - x_j)^2 \geq 0$$
        * For weighted graphs
            
            $$\forall x,x^T L x = \sum_{(i,j)\in\mathcal{E}} w_{i,j} (x_i - x_j)^2 \geq 0$$
* *Consequence*. $L$ has $n$ non-negative, real-valued eigen values $0=\lambda_1 \leq \dots \leq \lambda_n$
    * *Proof*. Since $L$ is positive semi-definite, it cannot have negative eigenvalue, and it also has eigenvalue $0$ corresponding to eigenvector $\mathbf{1}_n$

**Examples of Laplacian matrix of graph**.
* *3D discrete surface (mesh)*. An undirected weighted graph where $w_{i,j} = \exp \frac{-\|v_i - v_j\|^2}{\sigma^2}$, i.e. Gaussian kernel

    $\to$ The geometric structure of a mesh is encoded in the weights
* *Cloud of points graph representation*. 
    * *Option 1*. 3-nearest neighbor graph, i.e. the graph is guaranteed to be connected
    * *Option 2*. $\epsilon$-radius graph, i.e. the graph is not guaranteed to be connected

## Connectivity
**Zero eigenvalue of Laplacian matrix**. Given any constant vector $x$, then $L x = 0$, i.e $x$ is an eigenvector of eigenvalue $0$

**Connectivity and Laplacian matrix**.
* *Assumptions*. 
    * $G=(\mathcal{V}, \mathcal{E})$ be a graph
    * $0=\lambda_1\leq\lambda_2\leq\dots\leq\lambda_n$ are eigenvalues of the Laplacian matrix
* *Conclusion*. $\lambda_2 > 0$ if and only if $G$ is connected
* *Proof*.
    * If $G$ is disconnected, then by reindexing the vertices, $L$ can be written as a block matrix

        $$L=\begin{bmatrix}
        L_1 & 0 & \cdots & 0\\
        0 & L_2 & \cdots & 0\\
        \vdots & \vdots & \ddots & \vdots\\
        0 & 0 & \cdots & L_m
        \end{bmatrix}$$

        where $L_1,\dots,L_m$ are matrix blocks
    * It is proven that the solution of $Lx=0$ has the form

        $$x=[x_1;\dots;x_m]$$

        where $x_i$ is a solution of $L_i x = 0$ and $[\cdot;\cdot]$ denotes concatenation
    * Thus, if $G$ is disconnected, by setting $x_1\neq x_2\neq \cdots \neq x_m$

        $\to$ We have at least two eigenvectors corresponding to eigenvalue $\lambda = 0$
* *Generalization*. The number of zero eigenvalues is the number of connected components of the graph, with the corresponding eigenvectors

    $$\{\begin{bmatrix}1_{n_1} \\ 0 \\ \vdots \\ 0\end{bmatrix},\begin{bmatrix}0 \\ 1_{n_2} \\ \vdots \\ 0\end{bmatrix},\dots,\begin{bmatrix}0 \\ 0 \\ \vdots \\ 1_{n_m}\end{bmatrix}\}$$

    where $n_i$ is the number of vertices in the $i$-th connected component
    * *Consequence*. $(0,\dots,1_{n_i},\dots,0)$ is the indicator vector of the graph's $i$-th connected component
* *Consequence*. In general, it is pointless to consider unconnected graphs, because their spectra are just the union of the spectra of their components

**Fiedler vector of the graph Laplacian**. 
* *Fiedler value*. The first non-zero eigenvalue $\lambda_{k+1}$ where $k$ is the number of zero eigenvalues of the Laplacian
    * *Interpretation*. Represent the algebraic connectivity of a graph, i.e. the further from 0, the more connected
    * *Usage*. Extensively used for spectral bi-partitioning

    >**NOTE**. Fiedler value only makes sense for connected graph

* *Fiedler vector*. The eigenvector corresponding to the Fiedeler eigenvalue
* *Fiedler vector as optimization solution*.
    * *Smallest eigenvector finding as optimization*. Let $A$ be any symmetric matrix

        $\to$ Minimizing $\frac{x^T A x}{x^T x}$ over all nonzero $x$, i.e. $\|x\| = 1$ results in the smallest eignevalue, with $x$ being its eigenvector
    * *Fiedler vector finding*.
        * *Optimization problem*.

            $$\begin{aligned}
            \text{minimze } &\frac{x^T A x}{x^T x}\\
            \text{subject to } & \|x\|=1\\
            & x^T 1_n = 0
            \end{aligned}$$
            
            * *The second constraint*. Mean that the desired $x$ should be perpendicular to the first eigenvalue of $A$
                
                $\to$ We will yield the second smallest eigenvalue
        * *Consequence*. Finding the Fiedler vector means minimzing

            $$x^T L x = \sum_{(i,j)\in\mathcal{E}} (x_i - x_j)^2$$

            $\to$ We want to make the components on any two adjacent vertices as close as possible
        * *Interpretation of Fiedler vector*. The Fiedler vector paints the graph in a gradient going from positive to negative, so that
            * Each individual value $x$ does not mean much by itself
            * Clusters of neighbor vertices get similar values
            * Far-apart vertices often get different values
    * *Generalization*. To find the next eigenvector, we add additional constraints to our problem in the similar manner

        $\to$ This eigenvector should have similar properties, but be different from the previous eigenvectors, hence describing a different feature of the graph
        * *Example*. If our graph has three big and sparsely connected clusters
            * The Fiedler vector may assign positive values to one cluster and negative values to the other two
            * The next eigenvector may choose a different cluster to separate from the other two clusters
        * *Consequence*. The eigenvectors of the Laplacian distinguishes all the clusters

            $\to$ The eigenvector after that will have to find some inter-cluster separation
* *Multiplicity of Fiedler eigenvalue*. Always equal to 1
    * *Explain*.
* *References*. https://arxiv.org/pdf/2002.00283.pdf

**Eigenvectors of the Laplacian of connected graphs**.
* *Special eigenvectors*.
    * *Eigenvector 1*. $1_n$, i.e. $L 1_n = 0$
    * *Eigenvector 2*. The Fiedler vector with multiplicity 1
* *Relationships between eigenvectors*.
    * The eigenvectors form an orthonormal basis, i.e. due to symmetricity of $L$
    * For any eigenvector $u_i$ where $2\leq i\leq n$, $u_i^T 1_n = 0$

        $\to$ $\sum_{i=1}^n u_{ij} = 0$
    * Each component is bounded by $-1<u_{ij}<1$, i.e. so that $\|u_i\|=1$ 

## Laplacian of fundamental graphs
**Complete graph on $n$ vertices**. Consider a complete graph $K_n$ on $n$ vertices, which has edge set $\{(u,v):u\neq v\}$
* *Eigenvalues of the Laplacian of $K_n$*. The Laplacian of $K_n$ has eigenvalue $0$ with multiplicity $1$, and $n$ with multiplicity $n-1$

**Star graph on $n$ vertices**. Consider a star graph $S_n$ on $n$ vertices, which has edge set $\{(1,v):2\leq u\leq n\}$
* *Eigenvalues of graph with connected vertices*. Let $G=(\mathcal{V},\mathcal{E})$ be a graph, and $i,j$ are vertices of degree one, which are both connected to another vertex $k$, then the vector $v$

    $$v(u)=\begin{cases}
    1 & u=i\\
    -1 & u=j\\
    0 & \text{otherwise}
    \end{cases}$$

    is an eigenvector of the Laplacian of $G$ of eigenvalue $1$

* *Eigenvalues of the Laplacian of $S_n$*. The Laplacian $S_n$ has eigenvalue $0$ with multiplicity $1$, eigenvalue $1$ with multiplicity $n-2$, and eigenvalue $n$ with multiplicity $1$

**Path graph on $n$ vertices**. Consider a path graph $P_n$ on $n$ vertices, which has edge set $\{(u,u+1):1\leq u\leq n\}$

**Ring graph on $n$ vertices**. Consider a ring graph $R_n$ on $n$ vertices, which the edges of the path graph, plus the edge $(1,n)$
* *Eigenvalues of the Laplacian of $R_n$*. 
    * *Formal*. 
        * The Laplacian $R_n$ has eigenvectors

            $$x_k(u) = \sin(2\pi k u/n),\quad y_k(u)=\cos(2\pi k u/n)$$

            for $1\leq k\leq n/2$
        * When $n$ is even, $x_{n/2}$ is the all-zero vector, thus we only have $y_{n/2}$
        * Eigenvectors $x_k$ and $y_k$ have eigenvalue $2-2\cos(2\pi k/n)$

## Laplacian embedding
**Laplacian embedding on a line**. Map a weighted graph onto a line so that connected nodes stay as close as possible
* *Optimization problem*.

    $$\begin{aligned}
    \text{minimize}_{f} & \sum_{i,j=1}^n w_{i,j} (f(v_i) - f(v_j))^2 = f^T L f \\
    \text{subject to} & f^T f = 1 \\ & f^T 1 = 0
    \end{aligned}$$

* *Solution*. The eigenvector associated with the smallest nonzero eigenvalue of the eigenvalue problem

    $\to$ This is called the Fiedler vector
* *Interpretation*. Fiedler vector maps nodes of a graph onto a line

**Laplacian embedding on an Euclidean space**. When $f$ maps vertices to vectors in $\mathbf{R}^m$
* *Idea*, Embed the graph in a $k$-dimensional Euclidean space
    * *Explain*. The embedding is given by the $n\times k$ matrix $\mathbf{F} = \begin{bmatrix}\mathbf{f}_1 & \cdots & \mathbf{f}_k\end{bmatrix}$

        $\to$ The $i$-th row $\mathbf{f}^{(i)}$ of this matrix corresponds to the Euclidean coordinates of the $i$-th graph node $v_i$
* *Optimization problem*,

    $$\begin{aligned}
    \text{minimize } & \sum_{(i,j)\in\mathcal{E}} w_{ij} \|\mathbf{f}^{(i)} - \mathbf{f}^{(j)}\|^2\\
    \text{subject to } & \mathbf{F}^T \mathbf{F} = \mathbf{I}
    \end{aligned}$$

* *Solution*. The solution is provided by the matrix of eigenvectors corresponding to the $k$ lowest nonzero eigenvalues of the eigenvalue problem $Lf = \lambda f$

**Spectral embedding using the unnormalized Laplacian**.

<div style="text-align:center">
    <img src="https://i.imgur.com/WZ47urG.png">
    <figcaption>Mappings of graph on different eigenvectors</figcaption>
</div>

1. Compute the eigendecomposition of the Laplacian $L = D - A$
2. Select the $k$ smallest non-zero eigenvalues $\lambda_2 \leq \dots \leq \lambda_{k+1}$
    * *Eigengap*. $\lambda_{k+2} - \lambda_{k+1}$
3. Compute the corresponding eigenvectors and obtain the $n\times k$ matrix

    $$\mathbf{U} = \begin{bmatrix}\mathbf{u}_2 & \cdots & \mathbf{u}_{k+1}\end{bmatrix}$$

    * *Orthogonality of $\mathbf{U}$*. $\mathbf{U}^T \mathbf{U} = \mathbf{I}_k$
4. The column $i$, where $2\leq i\leq k+1$, of this matrix is a mapping of the graph on the eigenvector $\mathbf{u}_i$

**Euclidean L-embedding of the graph's vertices**.
* *Assumptions*.
  * $\mathbf{\Lambda}_k = \text{diag}(\lambda_2,\dots,\lambda_{k+1})$ is a diagonal matrix
  * $\mathbf{U} = \begin{bmatrix}\mathbf{u}_2 & \cdots & \mathbf{u}_{k+1}\end{bmatrix}$ is the matrix of the corresponding eigenvectors
* *L-embedding of the graph*. $\mathbf{X}=\mathbf{\Lambda}_k^{-1/2} \mathbf{U}^T = \begin{bmatrix}\mathbf{x}_1 & \cdots & \mathbf{x}_n\end{bmatrix}$

    $\to$ $\mathbf{x}_j = (\frac{\mathbf{u}_{2,j}}{\sqrt{\lambda_2}}, \dots, \frac{\mathbf{u}_{k+1,j}}{\sqrt{\lambda_{k+1}}})$
* *Commute-time distance (CTD) and PCA of a graph*. Important contepts allowing to reason statistically on a graph
    * *The commute-time distance (CTD)*. The average number of (weighted) edges that it takes, starting at vertex $v_i$, to randomly reach vertex $v_j$ for the first time and go back
        
        >**NOTE**. This is a well known quantity in Markov chains

        * *Formal*. $\text{CTD}^2(v_i, v_j) = \text{vol}(\mathcal{G}) \|\mathbf{x}_i - \mathbf{x}_j\|^2$
        * *CTD and the number of connections*. The CTD decreases as the number of connections between the two nodes increases
        * *CTD and connectivity structure of graph*. The CTD captures the connectivity structure of a small graph volume, rather than a single path between two vertices, e.g. the shortest-path geodesic distance
    * *The graph PCA*.
        * *Graph embedding mean*. 
            
            $$\bar{\mathbf{x}} = \frac{1}{n} \sum_{i=1}^n \mathbf{x}_j = \mathbf{\Lambda}_k^{-1/2} \begin{bmatrix} \sum_{j=1}^n \mathbf{u}_{2,j} \\ \vdots \\ \sum_{j=1}^n \mathbf{u}_{k+1,j}\end{bmatrix} = \mathbf{0}$$
        
        * *Graph covariance matrix*.

            $$\mathbf{S} = \frac{1}{n} \sum_{j=1}^n \mathbf{x}_j \mathbf{x}_j^T = \frac{1}{n} \mathbf{X} \mathbf{X}^T = \frac{1}{n} \mathbf{\Lambda}_k^{-1/2} \mathbf{U}^T \mathbf{U} \mathbf{\Lambda}_k^{-1/2}=\frac{1}{n} \mathbf{\Lambda}_k^{-1}$$
        
        * *Consequence*. The vectors $\mathbf{u}_2,\dots,\mathbf{u}_{k+1}$ are the directions of maximum variance of the graph embedding, with $\lambda_2^{-1} \geq \dots \geq \lambda_{k+1}^{-1}$

## Other Laplacian matrices
**Normalized adjacency matrix**. $\hat{\mathbf{A}}=\mathbf{D}^{-1/2} \mathbf{A} \mathbf{D}^{-1/2}$
* *Motivation*.
    * *Largest eigenvalue of $\mathbf{A}$*. Given $d_\text{min}$ and $d_\text{max}$ as the minimum and maximum degrees among graph vertices 
        
        $$d_\text{min}\leq \min_{\|\mathbf{x}\|_2=1} \mathbf{x}^T \mathbf{A} \mathbf{x} \leq \lambda_\text{min} \leq \lambda_\text{max} \leq \max_{\|\mathbf{x}\|_2=1} \mathbf{x}^T \mathbf{A} \mathbf{x}\leq d_\text{max}$$
    * *Proof*. For any $\mathbf{x}\neq \mathbf{0}$, suppose that $\mathcal{E}$ is the set of edges in the graph, and $\mathcal{V}$ is the set of vertices
        
        $$\begin{aligned}
        \frac{\mathbf{x}^T \mathbf{A} \mathbf{x}}{\mathbf{x}^T \mathbf{x}} &= \frac{\sum_{(i,j)\in\mathcal{E}} 2 x_i x_j}{\sum_{i\in\mathcal{V}} x_i^2}\\
        &\leq \frac{\sum_{(i,j)\in\mathcal{E}} (x_i^2 + x_j^2)}{\sum_{i\in\mathcal{V}} x_i^2}\\
        &= \frac{\sum_{i\in\mathcal{V}} d_i x_i^2}{\sum_{i\in\mathcal{V}} x_i^2}\\
        &\in [d_\text{min},d_\text{max}]
        \end{aligned}$$

**Other Laplacian matrices**.
* *Normalized graph Laplacian*. $\mathbf{L}_n = \mathbf{D}^{-1/2} \mathbf{L} \mathbf{D}^{-1/2} = \mathbf{I} - \hat{\mathbf{A}}$
* *Transition matrix (analogous to Markov chains)*. $\mathbf{L}_t = \mathbf{D}^{-1} \mathbf{A}$
* *Random-walk graph Laplacian*. $\mathbf{L}_r = \mathbf{D}^{-1} \mathbf{L} = \mathbf{I} - \mathbf{L}_t$
* *Similarity between graph Laplacians*. 
    
    $$\mathbf{L}_r = \mathbf{D}^{-1/2} \mathbf{D}^{-1/2} \mathbf{L} \mathbf{D}^{-1/2} \mathbf{D}^{1/2} = \mathbf{D}^{-1/2} \mathbf{L}_n \mathbf{D}^{1/2}$$

**Eigenvalues and eigenvectors of $\mathbf{L}_n$ and $\mathbf{L}_r$**.

**Spectral embedding using $\mathbf{L}_r$**.

**The normalized additive Laplacian**.

## The graph partitioning problem
**The graph partitioning problem**.
* *Graph-cut problem*. Partition the graph such that edges between groups have very low weight, and edges within a group have high weight, i.e.

    $$\text{cut}(A_1,\dots,A_k) = \frac{1}{2} \sum_{i=1}^k W(A_i,\bar{A}_i)$$

    where $W(A,B) = \sum_{i\in A, j\in B} w_{ij}$
* *Ratio cut*.

    $$\text{RatioCut}(A_1,\dots,A_k) = \frac{1}{2} \sum_{i=1}^k \frac{W(A_i,\bar{A}_i)}{|A_i|}$$
* *Normalized cut*.

    $$\text{NCut}(A_1,\dots,A_k) = \frac{1}{2} \sum_{i=1}^k \frac{W(A_i,\bar{A}_i)}{\text{vol}(A_i)}$$

**Spectral clustering**. Both ratio-cut and normalized-cut minimizations are NP-hard problems

$\to$ Spectral clustering is a way to solve relaxed versions of these problems
* *Idea*.
    * The smallest non-zero eigenvectors of the unnormalized Laplacian approximate the ratio-cut minimization criterion
    * The smallest non-zero eigenvectors of the random-walk Laplacian approximate the NCut criterion

**Spectral clustering using the random-walk Laplacian**.

**Example - Mesh segmentation using spectral clustering**.

<div style="text-align:center">
    <img src="https://i.imgur.com/EsATjHu.png">
    <figcaption>Mesh segmentation using spectral clustering</figcaption>
</div>

# Appendix
## Concepts
**Simple graph**. A graph that does not have more than one edge between any two vertices and no edge starts and ends at the same vertex

**Incidence matrix of a graph**. A square matrix whose entry $(i,j)$ indicates whether
* There is an edge from $i$ to $j$, i.e. $\nabla_{i,j}=-1$
* There is an edge from $j$ to $i$, i.e. $\nabla_{i,j}=1$
* There is not edge between $i$ and $j$, i.e. $\nabla_{i,j}=0$

## References
* [1] https://csustan.csustan.edu/~tom/Clustering/GraphLaplacian-tutorial.pdf
* [2] https://en.wikipedia.org/wiki/Laplacian_matrix
* [3] https://en.wikipedia.org/wiki/Eigenfunction
* [4] https://en.wikipedia.org/wiki/Laplace_operator
* [5] https://www.cs.yale.edu/homes/spielman/561/2009/lect02-09.pdf