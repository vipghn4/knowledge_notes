<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Graph Laplacian](#graph-laplacian)
  - [Introduction](#introduction)
  - [Real-valued functions on graphs](#real-valued-functions-on-graphs)
  - [Connectivity](#connectivity)
  - [Laplacian of fundamental graphs](#laplacian-of-fundamental-graphs)
  - [Laplacian embedding - mapping a graph on a line](#laplacian-embedding---mapping-a-graph-on-a-line)
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
* *Theorem*.
    * $L$ is symmetric and positive-definite
    * $L$ has $n$ non-negative, real-valued eigen values $0=\lambda_1 \leq \dots \leq \lambda_n$
* *Proof*.

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
* *Consequence*. $\lambda_2 > 0$ if and only if $G$ is connected

**Laplacian of a graph with $K$ conneceted components**.
* *One connected component only, i.e. $K=1$*. A graph with one connected component has the constant vector $\mathbf{U}_1=\mathbf{1}_n$ as the only eigenvector of the Laplacian $L$ with eigenvalue $0$
* *More than one connected components, i.e. $K>1$*.

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

## Laplacian embedding - mapping a graph on a line
**Laplacian embedding**. Map a weighted graph onto a line so that connected nodes stay as close as possible
* *Problem*.

    $$\begin{aligned}
    \text{minimize}_{f} & \sum_{i,j=1}^n w_{i,j} (f(v_i) - f(v_j))^2 = f^T L f \\
    \text{subject to} & f^T f = 1 \\ & f^T 1 = 0
    \end{aligned}$$

* *Solution*. The eigenvector associated with the smallest nonzero eigenvalue of the eigenvalue problem

    $\to$ This is called the Fiedler vector

**Generalizations**. When $f$ maps vertices to vectors in $\mathbf{R}^m$

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