<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Graph Laplacian](#graph-laplacian)
  - [Introduction](#introduction)
  - [Real-valued functions on graphs](#real-valued-functions-on-graphs)
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

**Co-boundary mapping of the graph**. The mapping $T:f\to\nabla \cdot f$ where $f$ is a real-valued function on the graph, and $\nabla$ is the indicence matrix of the transformed graph
* *Formula*. $(\nabla f)(e_{i,j}) = f(v_j) - f(v_i)$
    * $e_{i,j}$ is the edge from $i$ to $j$
    * $v_i,v_j$ are vertices $i$ and $j$

**Laplacian matrix of a graph from co-boundary mapping**. 
* *Theorem*.
    * $L=\nabla^T \nabla$
    * $(L f)(v_i) = \sum_{v_i \sim v_j} (f(v_i) - f(v_j))$
* *Proof*.
* *Intuition*.

**Laplacian matrix of undirected weighted graph**.
* *Assumption*.
    * $\mathcal{G}$ is a graph where each edge $e_{i,j}$ is weighted by $w_{i,j} > 0$
* *Laplacian matrix of $\mathcal{G}$*. $(L f)(v_i) = \sum_{v_j \sim v_i} w_{i,j} (f(v_i) - f(v_j))$
    * *Quadratic form*. $f^T L f = \frac{1}{2} \sum_{e_{i,j}} w_{i,j} (f(v_i) - f(v_j))^2$

**Properties of Laplacian matrix of graph**.
* *Theorem*.
    * $L$ is symmetric and positive-definite
    * $L$ has $n$ non-negative, real-valued eigen values $0=\lambda_1 \leq \dots \leq \lambda_n$

**Generalizations of Laplacian matrix of graph**.
* *3D discrete surface (mesh)*. An undirected weighted graph where $w_{i,j} = \exp \frac{-\|v_i - v_j\|^2}{\sigma^2}$, i.e. Gaussian kernel

    $\to$ The geometric structure of a mesh is encoded in the weights

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