<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Laplacian operator](#laplacian-operator)
  - [Divergence of a vector field](#divergence-of-a-vector-field)
    - [Vector calculus in brief](#vector-calculus-in-brief)
    - [Divergence of a vector field](#divergence-of-a-vector-field-1)
  - [Laplace operator](#laplace-operator)
  - [Laplace equation](#laplace-equation)
  - [Dirichlet energy](#dirichlet-energy)
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

## Laplace equation
**Laplace equation and harmonic function**. The solution of the equation $\Delta f = 0$ is a function $f$ where $f(x)$ equals to the average of its neighbor, for every $x$ in the domain of $f$
* *Harmonic function*. A twice continuously differentiable function $f:U\to\mathbb{R}$, where $U$ is an open subset of $\mathbb{R}^n$, which satifies Laplace's equation

    $$\sum_{i=1}^n \frac{\partial^2 f}{\partial x_i^2} = 0$$

    or, in other notation, $\Delta f = 0$ and $\nabla^2 f = 0$
    * *Intuition*. The income of a person is approximately equal to the average income of his friends
* *"Harmonic" term*. Originate from a point on a taut string, which is undergoing harmonic motion
    * *Explain*. 
        * The solution to the differential equation for this type of motion can be written in terms of sines and cosines, functions which are thus referred to as harmonics
        * Fourier analysis involves expanding functions on the unit circles in terms of a series of these harmonics
        * These functions satisfy Laplace's equation, and over time "harmonic" was used to refer to all functions satisfying Laplace's equation
* *Remarks*.
    * *Harmonic function as null space of the Laplace operator $\Delta$*. The set of harmonic functions on a given open set $U$ can be seen as the null space of the Laplace operator

        $\to$ The set of harmonic functions is a vector space over $\mathbf{R}$ due to the linearity of derivative operator
    * *Harmonic function and partial derivatives*. If $f$ is a harmonic function on $U$, then all partial derivatives of $f$ are also harmonic functions on $U$

        $\to$ The Laplace operator and the partial derivative operator will commute on this class of functions

>**NOTE**. Laplace opeartor is, in fact, the accumulated difference between a point $x$ and its neighboring points

**Spectral graph theory**.
* *Spectral graph theory*. Spectral graph theory is a discrete analogue of spectral geometry, with the Laplacian on graph being a discrete analouge of the Laplace operator on a Riemannian manifold
* *Usages of the Laplacian*.
    * *Heat equation*. $\frac{\partial u}{\partial t} = \Delta u$, i.e. how heat propagates on the graph / manifold

        $\to$ The heat is average filtered over time
        * *Formula*. $\frac{\partial u}{\partial t} = \sum_{i=1}^n \frac{\partial^2 u}{\partial x_i^2}$
    * *Wave equation*. $\frac{\partial^2 u}{\partial t^2} = \Delta u$, i.e. how waves propagate on the graph / manifold

        $\to$ The mass is accelerated by the average of its neighbors over time
        * *Derivation for 1D case*. $u$ measures the distance from the equilibrium of the mass situated at $x$

            <div style="text-align:center">
                <img src="https://i.imgur.com/Mk4ZjHF.png">
                <figcaption>Illustration 1</figcaption>
            </div>

            <div style="text-align:center">
                <img src="https://i.imgur.com/BMyB0Kq.png">
                <figcaption>Illustration 2</figcaption>
            </div>

            * *Hook's law*. The force $F$ required to extend or compress a spring by some distance $x$ scales linearly w.r.t the distance
                * *Formal*. $F=kx$ where $k$ is a positive real number, charactersitic of the spring
            * *Scenario*. Consider an array of little weights of mass $m$ interconnected with massless springs of length $h$ with a spring constant $k$
                * Let $u(x)$ measures the distance from the equilibrium of the mass situated at $x$, i.e.

                    $$u(x) = x_\text{rest} - x$$
                * Let $h$ be the distance at rest between any two masses
            * *Observations*.
                * If a mass has moved to the left, then it will feel a restoring force to the right due to two sources, i.e. the compressed string on its left, and the extended string on its right

                    $\to$ $F_\text{Hooke} = F_{x+2h} - F_x$
                * By Newton's second law of motion, $F_\text{Hooke} = F_\text{Newton}$
            * *The force exerted on the mass $m$ at location $x+h$*.

                $$\begin{aligned}
                F_\text{Newton}&=m\cdot a(t)=m\cdot \frac{\partial^2}{\partial t^2} u(x+h, t)\\
                F_\text{Hooke}&=F_{x+2h}-F_x=k [u(x+2h,t) - u(x+h,t)] - k[u(x+h,t) - u(x,t)]
                \end{aligned}$$
            
            * *Equation of motion for the weight at $x+h$*. $F_\text{Newton}=F_\text{Hooke}$, i.e.

                $$\frac{\partial^2}{\partial t^2} u(x+h, t) = \frac{k}{m}[u(x+2h,t) - u(x+h,t) - u(x+h,t) - u(x,t)]$$
            * *Generalization*. We can generalize this wave euqation to $n$-dimensional wave equation
    * *Image segmentation*. Nearby pixels having low Laplacian corresponds to a cluster within an image
* *Solutions to heat equation and wave equation*. Controlled by the eigenvalues of the Laplacian, i.e.
    * *Heat equation*. The eigenvalues of the Laplacian control the rate, at which a given heat distribution decays to a stationary distribution
    * *Wave equation*. The eigenvalues of the Laplacian control the rate, at which standing wave solutions oscillate

        $\to$ This gives some intuition as to why the eigenvalues should be related to the connectivity of the graph
* *Conclusion*. The eigenvalues of the Laplacian describe some important physical properties of the graph / manifold
* *Reference*. https://math.stackexchange.com/questions/308952/motivation-for-spectral-graph-theory

## Dirichlet energy
**Dirichlet energy**. A measure of how variable a function is
* *Formal*.
    * *Assumptions*.
        * $\Omega\subseteq\mathbb{R}^n$ is an open set
        * $u:\Omega\to\mathbb{R}$ is a function
        * $\nabla u:\Omega\to\mathbb{R}^n$ is the gradient vector field of $u$
    * *Dirichlet energy of $u$*.

        $$E(u)=\frac{1}{2}\int_\Omega \|\nabla u(x)\|^2 dx$$
* *Dirichlet energy and Laplace operator*. By solving the Laplace's equation $-\Delta u(x) = 0$ for all $x\in\Omega$, subject to proper boundary conditions
    
    $\to$ We are solving the variational problem of finding $u$ satisfying the boundary conditions and has minimal Dirichlet energy
    * *Harmonic functions*. A twice differentiable function satisfying Laplace's equation, i.e. $\Delta u=0$
* *Applications*. Used in image processing, computer graphics, geometry processing, and manifold learning
    * *Interpretation of Dirichlet eneryg*. Basically, over some region $\Omega$, $E(u)$ measures how much $u$ changes over $\Omega$
    * *Dirichlet energy and variational calculus*. Variational calculus is something like a generalization of the standard calculus approach to find maxima and minima
        * *Explain*. For a function $f$, we look for extrema by finding points where $\partial_x f=0$, but what if we want the extrema of a functional, i.e. a function of functions

            $\to$ We need to take the derivative of a functional w.r.t a function, i.e. first variation, and find a function so that we are at a min/max of the functional

**Dirichlet energy in image processing**. 
* *Image segmentation*. A region segment should have very low gradient, i.e. low DE

    $\to$ This is part of the basis of the famous Mumford-Shah functional
    * *Idea*. An image is modeled as a piecewise-smooth function. The function penalizes
        * The distance between the model and the input image
        * The lack of smoothness of the model within the sub-regions
        * The length of the boundaries of the sub-regions
    * *Mumford-Shah functional*. Consider an image $I$ over domain $D$, and a model $J$ with boundary $b$

        $$E_\text{MS}(J,b)=\gamma \int_D |I(p) - J(p)|^2 dp + \alpha \int_{D\setminus b} \|\nabla J(p)\|_2^2 dp + \beta \int_b ds$$
* *Image smoothing and denoising*. Minimizing the DE can be used to penalize noisy image regions
* *Deep learning*. DE is used in deep learning loss functions without even being named

**Functional derivative (or variational derivative)**. Relate a change in a functional, i.e. functions acting on functions, to a change in a function, or which the functional depends
* *Functional expression in variational calculus*. Usually in terms of an integral of functions, their arguments, and their derivatives
    * *Definition*. In an integral $L$ of a functional, if a function $f$ is varied by adding to it another function $\delta f$, which is arbitrarily small, and the resulting integrand is expanded in powers of $\delta f$
        
        $\to$ Functional derivative is the coefficient of $\delta f$ in the first order term
    * *Example*. Consider the functional

        $$J(f)=\int_a^b L(x,f(x),f'(x))dx$$

        where $f'(x)=df/dx$
        * If $f$ is varied by adding to it a function $\delta f$, the resulting integrand $L(x,f+\delta f,f'+\delta f')$ is expanded in powers of $\delta f$
            
            $\to$ The change in the value of $J$ to the first order in $\delta f$ can be written as

            $$\begin{aligned}
            \delta J&=\int_a^b \bigg(\frac{\partial L}{\partial f} \delta f(x) + \frac{\partial L}{\partial f'} \frac{d}{dx}\delta f(x)\bigg) dx
            \end{aligned}$$

# Appendix
## Concepts
**Tensor field**. Combine the requirements of richer geometry, i.e. an ellipsoid varying from point to point

## References
* [1] https://csustan.csustan.edu/~tom/Clustering/GraphLaplacian-tutorial.pdf
* [2] https://en.wikipedia.org/wiki/Laplacian_matrix
* [3] https://en.wikipedia.org/wiki/Eigenfunction
* [4] https://en.wikipedia.org/wiki/Laplace_operator
* [5] https://web.mit.edu/sahughes/www/8.022/lec04.pdf