<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Graph neural network model](#graph-neural-network-model)
  - [Introduction](#introduction)
  - [Graph neural network model](#graph-neural-network-model-1)
    - [Model](#model)
    - [Computation of the state](#computation-of-the-state)
    - [Learning algorithm](#learning-algorithm)
    - [Transition and output function implementations](#transition-and-output-function-implementations)
    - [A comparison with random walks and RNNs](#a-comparison-with-random-walks-and-rnns)
  - [Computational complexity issues](#computational-complexity-issues)
    - [Complexity of instructions](#complexity-of-instructions)
    - [Time complexity of the GNN model](#time-complexity-of-the-gnn-model)
  - [Experimental results](#experimental-results)
- [Appendix](#appendix)
  - [Reference](#reference)
- [Semi-supervised classification with graph convolutional networks](#semi-supervised-classification-with-graph-convolutional-networks)
<!-- /TOC -->

# Graph neural network model
## Introduction
**Needs for graph neural networks**. Data can be naturally represented by graph structures in several application areas
* *Graph structures*. The simplest kinds include single nodes and sequences
    
    $\to$ In several applications, the information is organized in more complex graph structures such as trees, acyclic graphs, or cyclic graphs

**Structured data in machine learning**. Structured data is often associated with the goal of learning from examples a function, which maps a graph and one of its nodes to
a vector of reals $\tau(\mathbf{G},n)\in\mathbb{R}^m$
* *Applications to a graphical domain*. Generally be divided into two broad classes, i.e. graph-focused and node-focused applications
* *Graph-focused applications*. $\tau$ is independent of the node $n$ and implements a classifier or a regressor on a graph structured data set, e.g.
    * *Modeling*. A chemical compound can be modeled by a graph $\mathbf{G}$
        * The nodes of which stand for atoms, or chemical groups
        * The edges of which represent chemical bonds linking some of the atoms
    * *Task*. $\tau(\mathbf{G})$ is used to estimate the probability that the chemical compound causes a certain disease
* *Node-focused applications*. $\tau$ depends on the node, i.e. the classification or the regression depends on the properties of each node
    * *Example*. Object detection, i.e. it consists of finding whether an image contains a given object, and, if so, localizing its position
        
        $\to$ This problem can be solved by a function $\tau$ classifying the nodes of the region adjacency graph according to whether the corresponding region belongs to the object

**Approaches to cope with graph structured data**. Use a preprocessing phase, which maps the graph structured information to a simpler representation, e.g. vectors of reals
* *Idea*.
    1. The preprocessing step squashes the graph structured data into a vector of reals
    2. The preprocessed data is dealt with, using a list-based data processing technique
* *Drawback*. Important information, e.g. the topological dependency of information on each node, may be lost during the preprocessing stage
    
    $\to$ The final result may depend, in an unpredictable manner, on the details of the preprocessing algorithm
* *Improvements*. There have been various approaches attempting to preserve the graph structured nature of the data for as long as required before the processing phase
    * *Idea*. Encode the graph structured data using the topological relationships among the nodes of the graph
        
        $\to$ This helps incorporate graph structured information in the data processing step
    * *Examples*. Recursive neural networks and Markov chains
* *Proposed approach*. Extend these two improvements, i.e. it can deal directly with graph structured information

**Recursive neural networks**. Neural network models, whose input domain consists of directed acyclic graphs
* *Idea*. Estimate the parameters $w$ of a function $\psi_w$, which maps a graph to a vector of reals
    * *RNNs for node-focused applications*. The graph must undergo a preprocessing phase
    * *RNNs for cyclic graphs*. Using a preprocessing phase, it is possible to handle certain types of cyclic graphs
* *Usage*. Logical term classification, chemical compound classification, logo recognition, web page scoring, and face localization

**Support vector machines**. RNNs are also related to SVMs, which adopt special kernels to operate on graph structured data
* *Examples*. 
    * The diffusion kernel is based on heat diffusion equation
    * The kernels, which exploit the vectors produced by a graph random walker
    * The kernels constructed using a method of counting the number of common substructures of two trees
* *Comparison with RNNs*. Both encode the input graph into an internal representation
    * *RNNs*. The internal encoding is learned
    * *SVMs*. The internal encoding is designed by the user

**Markov chain models**. Can emulate processes, where the causal connections among events are represented by graphs
* *Examples*. Random walk theory, which addresses a particular class of Markov chain models, has been applied with success to the realization of web page ranking algorithms
    * *Idea*. Internet search engines use ranking algorithms to measure the relative importance of web pages, i.e. Page rank algorithm
        
        $\to$ Such measurements are generally exploited, along with other page features, by horizontal search engines, e.g. Google
* *Improvements*. Some attempts have been made to extend these models with learning capabilities 
    
    $\to$ A parametric model representing the behavior of the system can be estimated from a set of training examples extracted from a collection
    * *Idea*. Several other statistical methods have been proposed, assuming that the data set consists of patterns and relationships between patterns
    * *Examples*. Random fields, Bayesian networks, statistical relational learning, transductive learning, and semisupervised approaches for graph processing
    * *Consequence*. Those models are able to generalize the results to score all the web pages in the collection

**Graph neural network**. A supervised neural network model suitable for both graph and node-focused applications
* *Idea*. Unify the two existing models into a common framework, i.e. graph neural network (GNN)
* *GNNs versus RNNs and random walk models*. GNN is an extension of both recursive neural networks and random walk models, which retains their characteristics
    * *GNNs and RNNs*. GNNs extends RNNs since
        * It can process a more general class of graphs including cyclic, directed, and undirected graphs
        * It can deal with node-focused applications without any preprocessing steps
    * *GNNs and random walk theory*. GNNs extends random walk theory by the introduction of a learning algorithm and by enlarging the class of processes that can be modeled
* *Learning algorithm for GNNs*. In this paper, a learning algorithm will be introduced, which estimates the parameters of the GNN model on a set of given training examples
* *GNNs as universal approximators*. GNNs show a sort of universal approximation property and
    
    >**NOTE**. Under mild conditions, they can approximate most of the practically useful functions on graphs

**GNNs and information diffusion**. GNNs are based on an information diffusion mechanism
* *Graph processing*. A graph is processed by a set of units, each one corresponding to a node of the graph, which are linked according to the graph connectivity, i.e.
    1. The units update their states and exchange information until they reach a stable equilibrium
    2. The output of a GNN is then computed locally at each node on the base of the unit state
* *Constraints on the diffusion mechanism*. Imposed to ensure that a unique stable equilibrium always exists
* *Comparison with previous works*.
    * *Diffusion mechanism in previous works*. Such a realization mechanism was already used in cellular neural networks and Hopfield neural networks
        * *Idea*. In those neural network models
            * The connectivity is specified according to a predefined graph
            * The network connections are recurrent in nature
            * The neuron states are computed by relaxation to an equilibrium point
    * *Diffusion mechanism in GNNs*. 
        * GNNs can be used for the processing of more general classes of graphs, e.g. graphs containing undirected links
        * GNNs adopt a more general diffusion mechanism

## Graph neural network model
**Graph and labels**.
* *Graph representation*.
    * A graph $\mathbf{G}$ is a pair $(\mathbf{N}, \mathbf{E})$ of nodes and edges
    * $\text{ne}[n]$ is the neighbors of $n$, i.e. the nodes connected to $n$ by an arc
    * $\text{co}[n]$ is the set of arcs having $n$ as a vertex
* *Labels of nodes and edges*. Nodes and edges may have labels represented by real vectors
    * $\mathbf{l}_n\in\mathbb{R}^{l_N}$ is the label attached to node $n$
    * $\mathbf{l}_{(n_1,n_2)}\in\mathbb{R}^{l_E}$ is the label attached to edge $(n_1,n_2)$
    * $\mathbf{l}$ is the vector obtained by stacking all the labels of the graph
* *General notations*. If $\mathbf{y}$ is a vector containing data from a graph, and $S$ is a subset of nodes (or edges)

    $\to$ $\mathbf{y}_S$ is the vector obtained by selecting from $\mathbf{y}$ the components related to the nodes or edges in $S$

**Graph labels**. Usually include features of objects related to nodes, and features of the relationships between the objects
* *Multi-edge graphs*. When different kinds of edges coexist in the same dataset

    $\to$ We must distinguish them, e.g. by attaching a proper label to each edge

**Positional and nonpositional graphs**.
* *Nonpositional graphs*. The graphs described so far
* *Positional graphs*. A unique integer identifier is assigned to each neighbors of a node to indicate its logical position
    * *Formal definition*. For each node $n$ in a positional graph, there exists an injective function $\nu_n:\text{ne}[n]\to\{1,\dots,|N|\}$
        
        $\to$ $\nu_n$ assigns to each neighbor of a position
    
    >**NOTE**. The position of the neighbor can be implicitly used for storing useful information

**Domain of interest**. The domain considered in this paper is the set $\mathcal{D}$ of pairs of a graph and a node
* *Formal definition*. $\mathcal{D}=\mathcal{G}\times\mathcal{N}$ where 
    * $\mathcal{G}$ is a set of the graphs
    * $\mathcal{N}$ is a subset of their nodes
* *Learning framework*. A supervised learning framework
    * *Learning set*.

        $$\mathcal{L}=\{ (\mathbf{G}_i,n_{i,j},\mathbf{t}_{i,j}):\mathbf{G}_i=(\mathbf{N}_i,\mathbf{E}_i)\in\mathcal{G};n_{i,j}\in\mathbf{N}_i;\mathbf{t}_{i,j}\in\mathbb{R}^m, 1\leq i\leq p,1\leq j\leq q_i \}$$

        where
        * $n_{i,j}$ is the $j$th node in $\mathbf{N}_i\in\mathcal{N}$
        * $\mathbf{t}_{i,j}$ is the desired target associated to $n_{i,j}$
        * $p\leq|\mathcal{G}|$ is the number of graphs in $\mathcal{L}$
        * $q_i\leq|\mathbf{N}_i|$ is the number of supervised nodes in $\mathbf{G}_i$
    * *Learning set as a whole graph*. All graphs in $\mathcal{L}$ can be combined into a unique disconnected graph

        $\to$ $\mathcal{L}=(\mathbf{G},\mathcal{T})$ where $\mathbf{G}=(\mathbf{N}, \mathbf{E})$ is a graph and $\mathcal{T}$ is a set of pairs

        $$\{(n_i,\mathbf{t}_i):n_i\in N,\mathbf{t}_i\in\mathbb{R}^m,1\leq i\leq q\}$$
    
        * *Benefits*. The definition is compact, and it captures directly the nature of some problems, where the domain consists of only one graph

### Model
The intuitive idea underlining the proposed approach is that
nodes in a graph represent objects or concepts, and edges represent their relationships. Each concept is naturally defined by
its features and the related concepts. Thus, we can attach a state $\mathbf{x}_n\in\mathbb{R}^s$ to each node $n$ that is based on the information contained in the neighborhood of (see Fig. 2). The state contains a representation of the concept denoted by and can be
used to produce an output , i.e., a decision about the concept

Let be a parametric function, called local transition function, that expresses the dependence of a node on its neighborhood and let be the local output function that describes how
the output is produced. Then, and are defined as follows:
(1)
where , , , and are the label of , the labels
of its edges, the states, and the labels of the nodes in the neighborhood of , respectively.
Remark 1: Different notions of neighborhood can be adopted.
For example, one may wish to remove the labels , since
they include information that is implicitly contained in .
Moreover, the neighborhood could contain nodes that are two
or more links away from . In general, (1) could be simplified
in several different ways and several minimal models4 exist. In
the following, the discussion will mainly be based on the form
defined by (1), which is not minimal, but it is the one that more
closely represents our intuitive notion of neighborhood.
Remark 2: Equation (1) is customized for undirected graphs.
When dealing with directed graphs, the function can also accept as input a representation of the direction of the arcs. For example, may take as input a variable for each arc
such that , if is directed towards and , if
comes from . In the following, in order to keep the notations
compact, we maintain the customization of (1). However, unless explicitly stated, all the results proposed in this paper hold
4A model is said to be minimal if it has the smallest number of variables while
retaining the same computational power.
also for directed graphs and for graphs with mixed directed and
undirected links.
Remark 3: In general, the transition and the output functions
and their parameters may depend on the node . In fact, it is
plausible that different mechanisms (implementations) are used
to represent different kinds of objects. In this case, each kind of
nodes has its own transition function , output function
, and a set of parameters . Thus, (1) becomes
and .
However, for the sake of simplicity, our analysis will consider
(1) that describes a particular model where all the nodes share
the same implementation.
Let , , , and be the vectors constructed by stacking all
the states, all the outputs, all the labels, and all the node labels,
respectively. Then, (1) can be rewritten in a compact form as
(2)
where , the global transition function and , the global
output function are stacked versions of instances of and
, respectively.
We are interested in the case when are uniquely defined
and (2) defines a map , which takes a graph
as input and returns an output for each node. The Banach
fixed point theorem [53] provides a sufficient condition for the
existence and uniqueness of the solution of a system of equations. According to Banach’s theorem [53], (2) has a unique solution provided that is a contraction map with respect to the
state, i.e., there exists , , such that
holds for any , where denotes
a vectorial norm. Thus, for the moment, let us assume that
is a contraction map. Later, we will show that, in GNNs, this
property is enforced by an appropriate implementation of the
transition function.
Note that (1) makes it possible to process both positional and
nonpositional graphs. For positional graphs, must receive the
positions of the neighbors as additional inputs. In practice, this
can be easily achieved provided that information contained in
, , and is sorted according to neighbors’ positions and is properly padded with special null values in positions corresponding to nonexisting neighbors. For example,
, where is the maximal number of neighbors of a node; holds, if is the
th neighbor of ; and , for some predefined null state , if there is no th neighbor.
However, for nonpositional graphs, it is useful to replace
function of (1) with
(3)
where is a parametric function. This transition function,
which has been successfully used in recursive neural networks
[54], is not affected by the positions and the number of the children. In the following, (3) is referred to as the nonpositional
form, while (1) is called the positional form. In order to implement the GNN model, the following items must be provided:
1) a method to solve (1)
2) a learning algorithm to adapt and using examples
from the training data set5;
3) an implementation of and .
These aspects will be considered in turn in the following
sections.

### Computation of the state
Banach’s fixed point theorem [53] does not only ensure the
existence and the uniqueness of the solution of (1) but it also
suggests the following classic iterative scheme for computing
the state:
(4)
5In other words, the parameters  are estimated using examples contained in
the training data set.
where denotes the th iteration of . The dynamical system
(4) converges exponentially fast to the solution of (2) for any initial value . We can, therefore, think of as the state that
is updated by the transition function . In fact, (4) implements
the Jacobi iterative method for solving nonlinear equations [55].
Thus, the outputs and the states can be computed by iterating
(5)
Note that the computation described in (5) can be interpreted
as the representation of a network consisting of units, which
compute and . Such a network will be called an encoding
network, following an analog terminology used for the recursive
neural network model [17]. In order to build the encoding network, each node of the graph is replaced by a unit computing the
function (see Fig. 3). Each unit stores the current state
of node , and, when activated, it calculates the state
using the node label and the information stored in the neighborhood. The simultaneous and repeated activation of the units
produce the behavior described in (5). The output of node is
produced by another unit, which implements .
When and are implemented by feedforward neural networks, the encoding network turns out to be a recurrent neural
network where the connections between the neurons can be divided into internal and external connections. The internal connectivity is determined by the neural network architecture used
to implement the unit. The external connectivity depends on the
edges of the processed graph.

### Learning algorithm
Learning in GNNs consists of estimating the parameter
such that approximates the data in the learning data set
where is the number of supervised nodes in . For graph-focused tasks, one special node is used for the target (
holds), whereas for node-focused tasks, in principle, the supervision can be performed on every node. The learning task can
be posed as the minimization of a quadratic cost function
(6)
Remark 4: As common in neural network applications, the
cost function may include a penalty term to control other properties of the model. For example, the cost function may contain
a smoothing factor to penalize any abrupt changes of the outputs
and to improve the generalization performance.
The learning algorithm is based on a gradient-descent
strategy and is composed of the following steps.
a) The states are iteratively updated by (5) until at time
they approach the fixed point solution of (2): .
b) The gradient is computed.
c) The weights are updated according to the gradient computed in step b).
Concerning step a), note that the hypothesis that is a
contraction map ensures the convergence to the fixed point.
Step c) is carried out within the traditional framework of gradient descent. As shown in the following, step b) can be carried
out in a very efficient way by exploiting the diffusion process
that takes place in GNNs. Interestingly, this diffusion process
is very much related to the one which takes place in recurrent
neural networks, for which the gradient computation is based
on backpropagation-through-time algorithm [17], [56], [57]. In
this case, the encoding network is unfolded from time back to
an initial time . The unfolding produces the layered network
shown in Fig. 3. Each layer corresponds to a time instant and
contains a copy of all the units of the encoding network. The
units of two consecutive layers are connected following graph
connectivity. The last layer corresponding to time includes
also the units and computes the output of the network.
Backpropagation through time consists of carrying out the
traditional backpropagation step on the unfolded network to
compute the gradient of the cost function at time with respect
to (w.r.t.) all the instances of and . Then, is
obtained by summing the gradients of all instances. However,
backpropagation through time requires to store the states of
every instance of the units. When the graphs and are
large, the memory required may be considerable.6 On the
other hand, in our case, a more efficient approach is possible,
based on the Almeida–Pineda algorithm [58], [59]. Since (5)
has reached a stable point before the gradient computation,
we can assume that holds for any . Thus,
backpropagation through time can be carried out by storing
only . The following two theorems show that such an intuitive
approach has a formal justification. The former theorem proves
that function is differentiable.
Theorem 1 (Differentiability): Let and be the
global transition and the global output functions of a GNN,
respectively. If and are continuously differentiable w.r.t. and , then is continuously differentiable
w.r.t. .
Proof: Let a function be defined as
Such a function is continuously differentiable w.r.t. and , since it is the difference of
two continuously differentiable functions. Note that the
Jacobian matrix of w.r.t. fulfills
where denotes the -dimensional identity matrix and , is
the dimension of the state. Since is a contraction map,
there exists such that ,
which implies . Thus, the determinant of is not null and we can apply the
implicit function theorem (see [60]) to and point . As
a consequence, there exists a function , which is defined
and continuously differentiable in a neighborhood of , such
that and Since this
result holds for any , it is demonstrated that is continuously differentiable on the whole domain. Finally, note that
, where denotes the operator
that returns the components corresponding to node . Thus,
is the composition of differentiable functions and hence is
itself differentiable.
It is worth mentioning that this property does not hold for
general dynamical systems for which a slight change in the parameters can force the transition from one fixed point to another.
The fact that is differentiable in GNNs is due to the assumption that is a contraction map. The next theorem provides a
method for an efficient computation of the gradient.
Theorem 2 (Backpropagation): Let and be the transition and the output functions of a GNN, respectively, and assume that and are continuously differentiable w.r.t. and . Let be defined by
(7)

### Transition and output function implementations

### A comparison with random walks and RNNs

## Computational complexity issues

### Complexity of instructions

### Time complexity of the GNN model

## Experimental results

# Appendix
## Reference
* https://persagen.com/files/misc/scarselli2009graph.pdf

---

# Semi-supervised classification with graph convolutional networks
**Layer-wise propagation rule**.

$$H^{(l+1)}=\sigma(\tilde{D}^{-1/2} \tilde{A}\tilde{D}^{-1/2} H^{(l)} W^{(l)})$$

* *Interpretation*. Normalize $H^{(l)}$ using local structure of each node, i.e. node's neighbors and degree, then linearly transform the normalized representation of the nodes