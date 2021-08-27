<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Laplacian operator](#laplacian-operator)
  - [Divergence of a vector field](#divergence-of-a-vector-field)
    - [Vector calculus in brief](#vector-calculus-in-brief)
    - [Divergence of a vector field](#divergence-of-a-vector-field-1)
  - [Laplace operator](#laplace-operator)
  - [Laplace equation](#laplace-equation)
- [Appendix](#appendix)
  - [Concepts](#concepts)
  - [References](#references)
<!-- /TOC -->

# Laplacian operator
## Divergence of a vector field
### Vector calculus in brief
**Gradient**. Convert the electric potential to the electric field, i.e.

$$\vec{E}=-\nabla\phi$$

**Divergence**. Relate the electric field to the charge density

$$\text{div} \vec{E} = 4\pi\rho$$

where charge density $\rho$ is the amount of electric charge per unit volume
* *Explain*. 

### Divergence of a vector field
**Divergence of a vector field $F(x)$ at $x_0$**. Represent the volume density of the outward flux of a vector field, from an infinitesimal volume around a given point
* *Example*. Consider air as it is heated or cooled
    * The velocity of the air at each point defines a vector field
    * While air is heated in a region, it expands in all directions
        
        $\to$ The vector field points outward from that region
    * The divergence of the velocity field in the region would thus have a positive value
* *Assumptions*.
    * $F$ is a vector field
    * $V$ is a closed volume enclosing some point $x_0$ with volume $|V|$
    * $S(V)$ is the boundary of $V$
    * $\hat{n}$ is the outward unit normal to $S(V)$
* *Divergence of a vector field $F(x)$ at $x_0$*. 
    
    $$\text{div} F|_{x_0} = \lim_{V\to 0} \frac{1}{|V|} \oiint_{S(V)} F \cdot \hat{n} dS$$

    where $V\to 0$ means $V$ shrinks to zero
* *Solenoidal*. A vector field with zero divergence, i.e. any closed surface has no net flux across it

**Physical interpretation**.
* *Divergence of a vector field*. The extent, to which the vector field flux behaves like a source at a given point

    $\to$ This is a local measure of the outgoingness of the source, i.e. the extent to which there are more of the field vectors exiting an infinitesimal region of space than entering it
* *Sign of divergence*. 
    * *Positive*. For points, at which the flux is outgoing, i.e. source points of the field
    * *Negative*. For points, at which the flux is directed inward, i.e. sink points of the field
    * *Zero*. For points, at which there is zero flux through an enclosing surface

**Definition in coordinates**.
* *Cartesian coordinates*. $F = F_x i + F_y j + F_z k$

    $$\nabla \cdot F = \frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}$$

* *Cylindrical coordinates*. $F = F_r e_r + F_\theta e_\theta + F_z e_z$

    $$\nabla \cdot F = \frac{1}{r} \frac{\partial}{\partial r} (r F_r) + \frac{1}{r} \frac{\partial F_\theta}{\partial \theta} + \frac{\partial F_z}{\partial z}$$
    * *Idea*. Derived from Cartesian coordinates divergence

## Laplace operator
**Laplacian operator (from [4])**. A second-order differential operator in the $n$-d Euclidean space
* *Background*.
    * *Vector differential operator $\nabla$*. Given that $e_i$ is the unit vector correpsonding to axis $x_i$, then

        $$\nabla = \sum_{i=1}^n \frac{\partial}{\partial x_i} e_i$$
    
    * *Gradient of the scalar field*. The result of applying vector differential operator to scalar field, i.e.

        $$\nabla f = \sum_{i=1}^n \frac{\partial f}{\partial x_i} e_i$$
    
    * *Divergence of the vector $F$*. The scalar product of vector differential operator with $F$

        $$\begin{aligned}
        \text{div} F(x,y,z) &= \nabla \cdot F\\
        &= \frac{\partial F_1}{\partial x} + \frac{\partial F_2}{\partial x} + \frac{\partial F_3}{\partial x}
        \end{aligned}$$

* *Definition*. $\Delta f = \nabla^2 f = \nabla \cdot \nabla f$ where 
    * $\nabla f = \big( \frac{\partial f}{\partial x_1},\dots,\frac{\partial f}{\partial x_n} \big)$
    * $\nabla \cdot$ is the divergence of gradient $\nabla f$
* *Theorem*. $\Delta f = \sum_{i=1}^n \frac{\partial^2 f}{\partial x_i^2}$
    * *Intuition*.
* *Motivation*.
    * *Laplacian as average*. 
        * *Assumptions*.
            * $f:\mathbf{R}^n \to \mathbf{R}$ is a twice continuously differentiable function
            * A point $p\in\mathbf{R}^n$ and a real number $h>0$
            * $\bar{f}_B(p,h)$ is the average of $f$ over the ball with radius $h$ around $p$
            * $\bar{f}_S(p,h)$ is the average of $f$ over the sphere with radius $h$ around $p$
        * *Conclusion*. 
            * $\bar{f}_B(p,h) = f(p) + \frac{\Delta f(p)}{2(n+2)} h^2 + o(h^2)$ as $h\to 0$
            * $\bar{f}_S(p,h) = f(p) + \frac{\Delta f(p)}{2n} h^2 + o(h^2)$ as $h\to 0$

## Laplace equation

# Appendix
## Concepts
**Tensor field**. Combine the requirements of richer geometry, i.e. an ellipsoid varying from point to point

## References
* [1] https://csustan.csustan.edu/~tom/Clustering/GraphLaplacian-tutorial.pdf
* [2] https://en.wikipedia.org/wiki/Laplacian_matrix
* [3] https://en.wikipedia.org/wiki/Eigenfunction
* [4] https://en.wikipedia.org/wiki/Laplace_operator