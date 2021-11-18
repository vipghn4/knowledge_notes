<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Other Laplacian matrices](#other-laplacian-matrices)
  - [Normalized graph Laplacian](#normalized-graph-laplacian)
  - [Random walk and adjacent matrix](#random-walk-and-adjacent-matrix)
  - [Summary](#summary)
- [Appendix](#appendix)
  - [Concepts](#concepts)
<!-- /TOC -->

# Other Laplacian matrices
## Normalized graph Laplacian
**Normalized adjacency matrix**. $\hat{\mathbf{A}}=\mathbf{D}^{-1/2} \mathbf{A} \mathbf{D}^{-1/2}$
* *Largest eigenvalue of $\mathbf{A}$*. Given $d_\text{min}$ and $d_\text{max}$ as the minimum and maximum degrees among graph vertices 
    
    $$d_\text{min}\leq \min_{\|\mathbf{x}\|_2=1} \mathbf{x}^T \mathbf{A} \mathbf{x} \leq \lambda_\text{min} \leq \lambda_\text{max} \leq \max_{\|\mathbf{x}\|_2=1} \mathbf{x}^T \mathbf{A} \mathbf{x}\leq d_\text{max}$$
    * *Proof*. For any $\mathbf{x}\neq \mathbf{0}$, suppose that $\mathcal{E}$ is the set of edges in the graph, and $\mathcal{V}$ is the set of vertices
        
        $$\begin{aligned}
        \frac{\mathbf{x}^T \mathbf{A} \mathbf{x}}{\mathbf{x}^T \mathbf{x}} &= \frac{\sum_{(i,j)\in\mathcal{E}} 2 x_i x_j}{\sum_{i\in\mathcal{V}} x_i^2}\\
        &\leq \frac{\sum_{(i,j)\in\mathcal{E}} (x_i^2 + x_j^2)}{\sum_{i\in\mathcal{V}} x_i^2}\\
        &= \frac{\sum_{i\in\mathcal{V}} d_i x_i^2}{\sum_{i\in\mathcal{V}} x_i^2}\\
        &\in [d_\text{min},d_\text{max}]
        \end{aligned}$$
* *Eigenvalues of $\hat{\mathbf{A}}$*. $\lambda\in[-1,1]$ for all eigenvalues $\lambda$ of $\hat{\mathbf{A}}$
    
    $\to$ Normalizing the adjacency matrix makes its largest eigenvalue unit
    * *Proof*.

        $$\begin{aligned}
        \frac{\mathbf{x}^T \hat{\mathbf{A}} \mathbf{x}}{\mathbf{x}^T \mathbf{x}} &= \frac{\sum_{(i,j)\in\mathcal{E}} \frac{2}{\sqrt{d_i d_j}} x_i x_j}{\sum_{i\in\mathcal{V}} x_i^2}\\
        &\leq \frac{\sum_{(i,j)\in\mathcal{E}} (\frac{1}{d_i} x_i^2 + \frac{1}{d_j} x_j^2)}{\sum_{i\in\mathcal{V}} x_i^2}\\
        &= \frac{\sum_{i\in\mathcal{V}} x_i^2}{\sum_{i\in\mathcal{V}} x_i^2}\\
        &= 1
        \end{aligned}$$

* *Eigenvalues of functions of $\hat{\mathbf{A}}$*.
    * $-\hat{\mathbf{A}}$ has spectrum negatives of $\hat{\mathbf{A}}$
    * $\mathbf{I}-\hat{\mathbf{A}}$ adds one to each eigenvalue of $-\hat{\mathbf{A}}$
* *Consequence*. The eigenvalues of the normalized graph Laplacian (below) is bounded within the interval $[0,2]$ with the lowest eigenvalue be zero

**Connectivity and the Fiedler vector of normalized graph Laplacian**. The second smallest eigenvalue of normalized graph Laplacian is zero if and only if $G$ is disconnected

**Reference**. https://cs.stanford.edu/~mpkim/notes/lec6.pdf

## Random walk and adjacent matrix
**Normalized adjacent matrix**. $\hat{\mathbf{A}} = \mathbf{D}^{-1} \mathbf{A}$, i.e. we normalize each row of $\mathbf{A}$ so that it sums to 1

$\to$ $\hat{\mathbf{A}}$ maps a vertex to the average of all its neighbors in the space

**Random walk and adjacent matrix**. If we start at a vertex $i$ of the graph and randomly select a neighbor uniformly, with equal probability, and move to that neighbor

$\to$ The row $\hat{\mathbf{A}}_i$ gives the induced probability distribution over these choices
* *Interpretation*. This is an example of a Markov chain on a finite state space with transition matrix $\hat{\mathbf{A}}$
* *Question*. 
    * What if we iterate this random walk for infinity, i.e. $\hat{\mathbf{A}}^m$ as $m\to\infty$?
    * Does it matter what the starting distribution $v$ is?

**Left eigenvalues of $\hat{\mathbf{A}}$**. 
* The largest one is exactly $1$ and the smallest one is at least $-1$, which is achieved if and only if the graph is bipartite
    * *Explain*. Since the eigenvalues are the same for both left and right eigenvectors, we can prove this statement via right eigenvalues
        * We can prove the first clause as below
            * Let $N(x)$ be the set of neighbor vertices of $x$, and $x_\text{max}$ be the maximum entry of $x$, then for all $x_i$

                $$\begin{aligned}
                (\hat{\mathbf{A}} \mathbf{x})_i &= E(\{x'_i:x'_i\in N(x_i)\})\\
                &\leq x^*
                \end{aligned}$$
            
            * Thus, the eigenvalues of $\hat{\mathbf{A}}$ cannot exceed $1$. The equality holds when $\mathbf{x}\propto\mathbf{1}$
        * We can prove the second clause as below
            * We easily can show that the eigenvalues of $\hat{\mathbf{A}}$ cannot be below $-1$
            * Suppose that $\lambda=-1$ is an eigenvalue of $\hat{\mathbf{A}}$, and let $i^*$ be the index of the entry with largest magnitude of a corresponding eigenvector $\mathbf{x}$, we have that

                $$(\hat{\mathbf{A}} \mathbf{x})_{i^*} = \sum_{i\in N(i^*)} A_{i^*i} x_i = - x_{i^*}$$

                * Suppose that $A_{i^* i^*} > 0$, then we have that

                    $$\sum_{i\in N(i^*) \setminus \{i^*\}} A_{i^*i} x_i = - (1 + A_{i^* i^*}) x_{i^*} > x_{i^*}$$

                    which is impossible, thus $A_{i^* i^*} = 0$ must hold
                * Now, we have that

                    $$\sum_{i\in N(i^*) \setminus \{i^*\}} A_{i^*i} x_i = - x_{i^*}$$

                    which only holds if and only if $x_i = -x_{i^*}$ for all $i\in N(i^*) \setminus \{i^*\}$
            
            * Suppose that the graph is connected, then recursively, we have that 
                * $\mathbf{x}$ is a vector, whose entries have the same magnitude, and connected vertices correspond to entries with opposite signs
                * For $\mathbf{x}$ to exist, the graph must be bipartite, i.e. $\mathbf{x}$ assign positive sign to a partite and negative sign to the other, and the graph must not contain self-loop
* The multiplicity of $1$ is equal to the number of connected components of the graph
    * *Intuition*. Similar to the relationship between regular Laplacian matrix and graph connectivity
    * *Explain*. Since the eigenvalues are the same for both left and right eigenvectors, we can prove this statement via right eigenvalues
        * It is easy to prove that, if the graph has $k$ connected components, then the multiplicity of $1$ is at least $k$
        * Now, suppose that there is only one connected component in the graph, then it is easy to prove that the only eigenvector corresponding to eigenvalue $1$ is $(1,1,\dots,1)^T$

**Convergence to stationary**. There is exactly one stationary distribution and the distribution of a random walk, over a long time horizon, converges to it
* *Theorem*. Suppose that every entry of the transition matrix $M$ is strictly positive, then its eigenvalues satisfy

    $$\lambda_1 = 1,\quad \forall i\in\{2,\dots,n\}, |\lambda_i| < 1$$
    * *Explain*. $M$ represents an adjacent matrix of a connected graph
* *Theorem*.
    * *Assumptions*.
        * $p^{0}$ is our starting distribution over the vertices
        * $p^{(t)}$ is the probability distribution after $t$ steps of repeatedly applying the transition matrix $M$, i.e.

            $$p^{(t)} = p^{(0)} M^t$$
        
        * Every entry of $M$ is strictly positive and $M$ is a diagonalizable matrix
        * $\sigma = 1 - \max_{i=2,\dots,n} |\lambda_i|$
    * *Conclusion*. There exists a constant $C$ such that, for all $t$, we have

        $$\|\pi - p^{(t)}\|_1 \leq C\cdot n\cdot e^{-t\sigma}$$
    * *Explain*.
        * Consider the left eigenvectors $\pi,v_2,\dots,v_n$ of $M$, since those vectors are linearly independent

            $\to$ $p^{(0)}$ can be written as a linear combination of those vectors, i.e. $p^{(0)} = \pi + \sum_{i=2}^n c_i v_i$
        * We have that

            $$p^{(0)} M^t = \pi + \sum_{i=2}^n \lambda_i^t c_i v_i \to \pi$$

            due to the previous theorem
        * Without loss of generality, assume that $\|v_i\|=1$ for all $v_i$. We also have that

            $$\begin{aligned}
            \|\pi-p^{(t)}\|_1 &= \|\sum_{i=2}^n \lambda_i^t c_i v_i\|_1\\
            &\leq\sum_{i=2}^n |\lambda^t| |c_i| & \text{since } \|v_i\|_1 = 1\\
            &\leq\sum_{i=2}^n |(1 - \lambda)^t| |c_i|\\
            &\leq C\cdot n\cdot (1 - \sigma)^t\\
            &\leq C \cdot n\cdot e^{-\sigma t} & \text{since } 1 - \sigma \leq e^\sigma
            \end{aligned}$$

    * *Consequence*. Even if the number of vertices of the graph is gigantic, e.g. $n=2^d$ for some $d$

        $\to$ We can get convergence very close to the stationary distribution in only $O(d/\sigma)$ steps of random walk

    >**NOTE**. The equality $1 - \sigma \leq e^\sigma$ is very important for proof of convergence related to probability

**PageRank**.
* *Key idea*. Let $G$ be the directed graph of hyperlinks on the web, where each vertex is a webpage with edges to every page it has links to
    * *Random walk*. Suppose a random walk of the normalized adjacency matrix $\hat{\mathbf{A}}$, then 
        * With probability $\alpha$, we jump to a new, completely uniformly random webpage
        * With probability $1-\alpha$, we follow a random link on the current page
    * *Modified transition matrix*. $M(i,j)=\frac{\alpha}{n} + (1 - \alpha) \hat{\mathbf{A}}(i,j)$
* *Observation*. For $\alpha > 0$, every entry is strictly positive and there is a unique stationary probability distribution $\pi$ of the random walk

    $\to$ This is the PageRank of the graph $G$
* *Page ranking*. For each page $i$, its rank or score is $\pi(i)$, with larger being better
    * *Property of $\pi$*. Following from the fact that $\pi M = \pi$

        $$\pi(j) = \sum_{i=1}^n \pi(i) M(i,j) = \frac{\alpha}{n} + (1-\alpha) \sum_{i:(i,j)\in G} \frac{\pi(i)}{\text{degree}(i)}$$
    * *Interpretation*. The asymptotic probability of being on page $j$ is the sum of two processes
        * With probability $\alpha$, no matter where we are, we jump randomly, in which case there is a $\frac{1}{n}$ chance of landing on page $j$
        * WIth probability $1-\alpha$, we are on page $i$ with probability $\pi(i)$, and we jump to page $j$ with probability $\frac{1}{\text{degree}(i)}$ is there is a link $(i,j)$
* *Problem*. Since the number of webpages is very large, we need to approximately sample from $\pi$

**Markov chain Monte Carlo**.
* *Idea*. We need to sample or estimate an integral from a challenging distribution over a very large space

    $\to$ We cannot write down the distribution, but we have some information about it
* *Theorem*.
    * *Assumptions*.
        * $p^{(0)}$ is any distribution and $p^{(t)} = p^{(0)} M^t$
        * $M$ is the transition matrix of a Markov chain
    * *Conclusion*. If $M$ is connected, i.e. state $i$ is reachable from any state $j$, then 
        * It has a unique stationary distribution $\pi$
        * As $t\to\infty$, the average $\frac{\sum_{i=0}^t p^{(i)}}{t}$ converges to $\pi$
* *Lemma*. For a Markov chain with transition matrix $M$, if strongly connected, if there exists a distribution $\pi$ such that

    $$\pi(i)M(i,j)=\pi(j)M(j,i)$$

    then $\pi$ is the unique stationary distribution

    >**NOTE**. This does not claim the stationary distribution always satisfies this relationship

**Reference**. https://www.bowaggoner.com/courses/2019/csci5454/docs/spectral.pdf

## Summary
**Other Laplacian matrices**.
* *Normalized graph Laplacian*. $\mathbf{L}_n = \mathbf{D}^{-1/2} \mathbf{L} \mathbf{D}^{-1/2} = \mathbf{I} - \hat{\mathbf{A}}$
    * *Explain*. Eigenvalues of $\mathbf{L}$ are normalized to $[0,2]$
* *Transition matrix (analogous to Markov chains)*. $\mathbf{L}_t = \mathbf{D}^{-1} \mathbf{A}$
    * *Explain*. $\mathbf{L} \cdot \mathbf{1} = \mathbf{1}$, i.e. $\mathbf{L}$ represents a transition matrix of a Markov chain
* *Random-walk graph Laplacian*. $\mathbf{L}_r = \mathbf{D}^{-1} \mathbf{L} = \mathbf{I} - \mathbf{L}_t$
* *Similarity between graph Laplacians*. 
    
    $$\mathbf{L}_r = \mathbf{D}^{-1/2} \mathbf{D}^{-1/2} \mathbf{L} \mathbf{D}^{-1/2} \mathbf{D}^{1/2} = \mathbf{D}^{-1/2} \mathbf{L}_n \mathbf{D}^{1/2}$$

**Eigenvalues and eigenvectors of $\mathbf{L}_n$ and $\mathbf{L}_r$**.

# Appendix
## Concepts
**Strongly connected graph**.
* Connected is usually associated with undirected graphs (two way edges), i.e. there is a path between every two nodes
* Strongly connected is usually associated with directed graphs (one way edges), i.e. there is a route between every two nodes
* Complete graphs are undirected graphs where there is an edge between every pair of nodes