<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Laplacian operator](#laplacian-operator)
  - [Divergence of a vector field](#divergence-of-a-vector-field)
    - [Vector calculus in brief](#vector-calculus-in-brief)
    - [Divergence of a vector field](#divergence-of-a-vector-field-1)
  - [Laplace operator](#laplace-operator)
- [Appendix](#appendix)
  - [Concepts](#concepts)
  - [References](#references)
<!-- /TOC -->

# Laplacian operator
## Divergence of a vector field
### Vector calculus in brief
**Gradient**. Convert the electric potential to the electric field, i.e.

<div style="text-align:center">
    <img src="https://i.imgur.com/Dvtytj1.png">
    <figcaption>Electrical potentrial and electric field</figcaption>
</div>

$$\vec{E}=-\nabla\phi$$
* *Intuition*. We can imagine the electric potential as the height of the location we are standing at in a electromagnetic field

    $\to$ Charged particles should flow from higher places to lower places

**Divergence theorem**. Suppose $V\subset \mathbb{R}^n$ is a compact set with a piecewise smooth boundary $S$, and $\mathbf{F}$ is a continuously differentiable vector field defined on a neighbor of $V$

$$\iiint_V (\nabla \cdot \mathbf{F}) dV = \oiint_S (\mathbf{F} \cdot \hat{\mathbf{n}}) dS$$

* *Informal derivation*. If $V$ is partitioned into separate parts, the flux out of the original volume is equal to the sum of the flux out of each component volume
    * *Explain*. New subvolumes have surfaces which are not part of $V$, but the flux between these surfaces just passes from one volume to another

        $\to$ The flux is canceled out when the flux of the subvolumes are summed

**Divergence**. Relate the electric field to the charge density

$$\text{div} \vec{E} = \rho/\epsilon_0$$

where charge density $\rho$ is the amount of electric charge per unit volume, and $\epsilon_0$ is given in the Coulomb's law
* *Explain*. Assume that the charge density is uniform within the flat sphere object
    
    $$\begin{aligned}
    \text{div}\vec{E}&=\lim_{V\to 0} \frac{1}{|V|} \oiint_{S(V)} \frac{q}{4\pi\epsilon_0 r^2} dS\\
    &\approx\frac{1}{\epsilon_0} q/|V|\\
    &=\rho/\epsilon_0
    \end{aligned}$$

>**NOTE**. This is called the Poisson equation, which relates the electric potential $\phi$ to the charge density $\rho$

**Gauss's law (Gauss' flux theorem)**. Relate the distribution of electric charge to the resulting electric field
* *Assumptions*.
    * $Q$ is the total charge enclosed within the volume $V$
    * $\Phi_E$ is the electric flux through a closed surface $S$ enclosing $V$
* *Conclusion*.

    $$\Phi_E=\frac{Q}{\epsilon_0}=\oiint_S \mathbf{E} \cdot d\mathbf{A}=\iiint_V (\nabla \cdot \mathbf{E}) dV$$

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

    * *Derivation*.
        * *Scenario*. 
            * Consider an infinitesimal cube with sides $\Delta x, \Delta y, \Delta z$ centered on $(x,y,z)$
            * Fill the cube with a vector field $\vec{F}$
            * We want to compute the flux of $\vec{F}$ over this cube
        * *Observations*.
            * Consider the flux over just the $z$ faces

                $$\begin{aligned}
                \Delta\Phi_z&=\int_{\text{top \& bottom}} \vec{F} d\vec{A}\\
                &\approx \Delta x\Delta y F_z(x,y,z+\Delta z/2) - \Delta x\Delta y F_z(x,y,z-\Delta z/2)
                \end{aligned}$$

                where $-F_z(x,y,z-\Delta z/2)$ reflects the fact that the underlying face is pointing down
            * We have that, by Taylor approximation

                $$\begin{aligned}
                \Delta\Phi_z&\approx \Delta x\Delta y [F(x,y,z) + \frac{\Delta z}{2}] - \Delta x\Delta y [F(x,y,z) - \frac{\Delta z}{2}]\\
                &\approx \Delta x \Delta y \Delta z \frac{\partial F_z}{z}
                \end{aligned}$$
            
            * Similarly, we have

                $$\Delta\Phi_x = \Delta x\Delta y\Delta z \frac{\partial F_x}{\partial x},\quad \Delta\Phi_y = \Delta x\Delta y\Delta z \frac{\partial F_y}{\partial y}$$
            
            * Therefore, we have that

                $$\begin{aligned}
                \text{div}\vec{F} &= \lim_{V\to 0} \frac{1}{|V|} \int \vec{F} \cdot d\vec{A}\\
                &=\lim_{\Delta x,\Delta y,\Delta z \to 0} \frac{\Delta x\Delta y\Delta z (\partial F_x/\partial x + \partial F_y / \partial y + \partial F_z / \partial z)}{\Delta x \Delta y \Delta z}\\
                &=\frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y} + \frac{\partial F_z}{\partial z}\\
                &=\vec{\nabla} \cdot \vec{F}
                \end{aligned}$$

* *Cylindrical coordinates*. $F = F_r e_r + F_\theta e_\theta + F_z e_z$

    $$\nabla \cdot F = \frac{1}{r} \frac{\partial}{\partial r} (r F_r) + \frac{1}{r} \frac{\partial F_\theta}{\partial \theta} + \frac{\partial F_z}{\partial z}$$
    * *Idea*. Derived from Cartesian coordinates divergence

## Laplace operator
**Laplacian operator (from [4])**. A second-order differential operator in the $n$-d Euclidean space, which describes the divergence of gradient of a function
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

* *Definition*. $\Delta f = \nabla^2 f = \nabla \cdot \nabla f= \sum_{i=1}^n \frac{\partial^2 f}{\partial x_i^2}$ where 
    * $\nabla f = \big( \frac{\partial f}{\partial x_1},\dots,\frac{\partial f}{\partial x_n} \big)$
    * $\nabla \cdot$ is the divergence of gradient $\nabla f$
* *Vector Laplacian in multivariate Catesian coordinates*. $\nabla^2 \mathbf{A} = (\nabla^2 A_x, \nabla^2 A_y, \nabla^2 A_z)$

**Laplacian as average**.
* *Ball and sphere*. Given a point $\bar{x}\in\mathbb{R}^d$ and a radius $h>0$, tnen we have the ball and sphere
    
    $$\begin{aligned}
    B&=B(\bar{x},h)&=\{x\in\mathbb{R}^d:|x-\bar{x}|<h\},\\
    S&=S(\bar{x},h)&=\{x\in\mathbb{R}^d:|x-\bar{x}|=h\}
    \end{aligned}$$

* *Assumptions*.
    * $f:\mathbf{R}^n \to \mathbf{R}$ is a twice continuously differentiable function
    * A point $p\in\mathbf{R}^n$ and a real number $h>0$
    * $\bar{f}_B(p,h)$ is the average of $f$ over the ball with radius $h$ around $p$
    * $\bar{f}_S(p,h)$ is the average of $f$ over the sphere with radius $h$ around $p$
* *Conclusion*. 
    * $\bar{f}_B(p,h) = f(p) + \frac{\Delta f(p)}{2(n+2)} h^2 + o(h^2)$ as $h\to 0$
    * $\bar{f}_S(p,h) = f(p) + \frac{\Delta f(p)}{2n} h^2 + o(h^2)$ as $h\to 0$
* *Intuitive explanation*. We have that

    $$\begin{aligned}
    f(p) +\frac{\Delta f(p)}{2n} h^2 &= f(p) + \frac{h^2}{2n} \lim_{h\to 0} \sum_{i=1}^n \frac{f(x_1,\dots,x_i+h,\dots,x_n) - 2 f(x_1,\dots,x_i,\dots,x_n) + f(x_1,\dots,x_i-h,\dots,x_n)}{h^2}\\
    &=\frac{1}{n} \sum_{i=1}^n \frac{f(x_1,\dots,x_i+h,\dots,x_n) + f(x_1,\dots,x_i-h,\dots,x_n)}{2}\\
    &\approx \bar{f}_S(p,h)
    \end{aligned}$$

    >**NOTE**. This is just a approximate explanation

# Appendix
## Concepts
**Tensor field**. Combine the requirements of richer geometry, i.e. an ellipsoid varying from point to point

## References
* [1] https://csustan.csustan.edu/~tom/Clustering/GraphLaplacian-tutorial.pdf
* [2] https://en.wikipedia.org/wiki/Laplacian_matrix
* [3] https://en.wikipedia.org/wiki/Eigenfunction
* [4] https://en.wikipedia.org/wiki/Laplace_operator
* [5] https://web.mit.edu/sahughes/www/8.022/lec04.pdf