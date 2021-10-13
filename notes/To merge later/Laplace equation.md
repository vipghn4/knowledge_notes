
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