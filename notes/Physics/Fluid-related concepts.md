<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
  - [Divergence of a vector field](#divergence-of-a-vector-field)
    - [Vector calculus in brief](#vector-calculus-in-brief)
    - [Divergence of a vector field](#divergence-of-a-vector-field-1)
  - [Flux of a vector field](#flux-of-a-vector-field)
  - [Curl of a vector field](#curl-of-a-vector-field)
<!-- /TOC -->

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

## Flux of a vector field
**Flux**. Describe any effect appearing to pass or travel, i.e. whether it actually moves or not, through a surface or substance
* *Terminology*. The word flux comes from Latin "fluxus", i.e. "flow" in English, which is introduced into differential calculus by Isaac Newton

**Flux as flow rate per unit area**. In transport phenomena, e.g. heat transfer, mass transfer, and fluid dynamics, flux is the rate of flow of a property per unit area
* *General mathematical definition*. There are 3 definitions in increasing order of complexity
    * *Assumptions*.
        * $j$ is the flux
        * $q$ is the physical quantity which flows
        * $t$ is the flowing time
        * $A$ is the area
    * *Flux as a single scalar*. Assume that the surface is flat, and the flow is constant everywhere w.r.t position, and perpendicular to the surface
        
        $$j=I/A,\quad I=\lim_{\Delta t\to 0} \frac{\Delta q}{\Delta t} = \frac{dq}{dt}$$
    * *Flux as a scalar field defined along a surface*. Assume that the surface is flat, but the flow is perpendicular to the surface 
        
        $$j(\mathbf{p}) = \frac{\partial I}{\partial A}(\mathbf{p}),\quad I(A,\mathbf{p}) = \frac{dq}{dt}(A,\mathbf{p})$$
    * *Flux as a vector field*. Assume that the surface is not flat
        
        $$\mathbf{j}(\mathbf{p})=\frac{\partial \mathbf{I}}{\partial A}(\mathbf{p}),\quad \mathbf{I}(A,\mathbf{p})=\arg\max_{\hat{\mathbf{n}}} \hat{\mathbf{n}}_\mathbf{p} \frac{dq}{dt}(A,\mathbf{p},\hat{\mathbf{n}})$$

        * *Explain*.
            * $q$ is a function of a point $\mathbf{p}$, an area $A$, and a direction $\hat{\mathbf{n}}$, and measures the flow through the disk of area $A$ perpendicular to $\hat{\mathbf{n}}$
            * $I$ picks the unit vector maximizing the flow around $\mathbf{p}$, since the true flow is maximized across the disk that is perpendicular to it

                $\to$ The unit vector uniquely maximizes the function when it points in the true direction of the flow
* *Common transport fluxes*. Momentum flux, heat flux, diffusion flux, volumetric flux, mass flux, radiative flux, energy flux, particle flux, etc.

**Vector area**.
* For finite planar surface area $S$ and unit normal $\hat{\mathbf{n}}$, the vector area $\mathbf{S}$ is defined as

    $$\mathbf{S}=\hat{\mathbf{n}} S$$
* For an orientable surface $S$ composed of a set $S_i$ of flat facet areas, the vector area is given by

    $$\mathbf{S}=\sum_i \hat{\mathbf{n}}_i S_i$$
* For bounded, oriented curved surfaces which are sufficiently well-behaved, we can split the surface into infinitesimal elements

    $$d\mathbf{S}=\hat{\mathbf{n}}dS$$

    Integrating gives the vector area for the surface

    $$\mathbf{S}=\int d\mathbf{S}$$

**Flux as a surface integral**.
* *General mathematical definition*.
    * *Assumptions*.
        * $\mathbf{F}$ is a vector field
        * $d\mathbf{A}$ is the vector area of the surface $A$, directed as the surface normal
        * $\mathbf{n}$ is the outward pointed unit normal vector to the surface
    * *Formulation*.

        $$\mathbf{\Phi}_F = \iint_A \mathbf{F}\cdot d\mathbf{A}=\iint_A \mathbf{F} \cdot \mathbf{n} dA$$
    
    * *Derivation*. The surface integral of flux $\mathbf{j}$, i.e. in the previous definition, over a surface $A$, gives the proper flowing per unit of time through the surface

        $$\frac{dq}{dt}=\iint_A \mathbf{j}\cdot\hat{\mathbf{n}}dA=\iint_A \mathbf{j}\cdot d\mathbf{A}$$

* *Common surface fluxes*. Electric flux, magnetic flux, poynting flux

## Curl of a vector field
**Curl**. A vector operator describing the infinitesimal circulation of a vector field in 3D Euclidean space
* *Mathematical representation*. 
    * *The curl at a point*. A vector whose length and direction denote the magnitude and axis of the maximum circulation
    * *The curl of a field*. The circulation density at each point of the field
* *Irrotational vector field*. A vector field, whose curl is zero
* *Generalization to higher dimensions*. Curl as formulated in vector calculus does not generalize simply to other dimensions

**Mathematical formulation**. The curl of a vector field at a point is defined in terms of its projection onto various lines through the point
* *Curl operator*. Map continuously differentiable functions $f:\mathbb{R}^3\to\mathbb{R}^3$ to continuous functions $g:\mathbb{R}^3\to\mathbb{R}^3$
* *The projection o the curl of $\mathbf{F}$ onto $\hat{\mathbf{n}}$*.
    * *Assumptions*.
        * $\mathbf{F}$ is a vector field
        * $\hat{\mathbf{n}}$ is an unit vector
    * *The projection o the curl of $\mathbf{F}$ onto $\hat{\mathbf{n}}$*. The limiting value of a closed line integral in a plane orthogonal to $\hat{\mathbf{n}}$, divided b y the area enclosed, as the path of the integration is contracted around the point
* *The curl defined at a point $p$*.
    * *Assumptions*.
        * $C$ is the boundary of the area $A$, upon which the line integral is calculated
            * $C$ is oriented via the right-hand rule
        * $|A|$ is the magnitude of $A$
        * $\hat{\mathbf{n}}$ is the normal of the infinitesimal surface bounded by $C$
    * *The curl defined at a point $p$*.
            
        $$(\nabla\times \mathbf{F})(p)\cdot \hat{\mathbf{n}} = \lim_{A\to 0} \frac{1}{|A|} \oint_C \mathbf{F}\cdot d\mathbf{r}$$

        >**NOTE**. This is somewhat similar to the definition of divergence, where $\mathbf{F}\cdot \hat{\mathbf{n}}$ is taken, rather than $\mathbf{F}\cdot d\mathbf{r}$ due to the difference in purposes

**Intuition of curl**.
* *Solving for curl*. Since $\nabla\times \mathbf{F}\in\mathbb{R}^3$, we have that
    
    $$(\nabla\times \mathbf{F}) = \mathbf{I}_3\cdot (\nabla\times \mathbf{F}) = \begin{bmatrix}
    \lim_{A_x\to 0} \frac{1}{|A_x|} \oint_C \mathbf{F}\cdot d\mathbf{r}_x\\
    \lim_{A_y\to 0} \frac{1}{|A_y|} \oint_C \mathbf{F}\cdot d\mathbf{r}_y\\
    \lim_{A_z\to 0} \frac{1}{|A_z|} \oint_C \mathbf{F}\cdot d\mathbf{r}_z\end{bmatrix}$$

* *Extreme cases*. Assume that the magnitudes of the vectors within the vector field $\mathbf{F}$ are fixed, and their orientations are allowed to change, then
    * *Maximum curl*. $\mathbf{F}$ reaches maximum curl when 
        
        $$\forall p\in\mathbb{R}^3,\cos[\mathbf{F}(p), d\mathbf{r}(p)]=1$$
        
        i.e. if $A$ has circular shape, then $\mathbf{F}$ will be circular as illustrated below

        <div style="text-align:center">
            <img src="https://i.imgur.com/kNZguH9.png" width="350">
            <figcaption>Vector field with maximum curl</figcaption>
        </div>

    * *Minimum curl*. $\mathbf{F}$ reaches maximum curl when $\oint_C \mathbf{F}(p) \cdot d\mathbf{r}(p)=0$, i.e.

        $$\forall p\in\mathbb{R}^3,\mathbf{F}(p)=\mathbf{c}$$

        for some constant vector $\mathbf{c}$

        <div style="text-align:center">
            <img src="https://i.imgur.com/lj2swUp.png" width="350">
            <figcaption>Vector field with minimum curl</figcaption>
        </div>

**Mathematical formulation of curl in orthogonal coordinates**.
* *Formulation of curl under Cartesian coordinates*.

    $$\begin{aligned}
    (\nabla\times \mathbf{F})_x&=\frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z}\\
    (\nabla\times \mathbf{F})_y&=\frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x}\\
    (\nabla\times \mathbf{F})_z&=\frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y}\big)
    \end{aligned}$$

    * *Intuition*. Approximate $(\nabla \times \mathbf{F})(p)$ using an infinitesimal cube centered at $p$
    * *Properties*. 
        * $\nabla \times \mathbf{F}$ is invariant under proper rotations of the coordinate axes
        * $\nabla \times \mathbf{F}$ inverts under reflection
* *Generalization to orthogonal coordinates*. Let $(u_1,u_2,u_3)$ be an orthogonal coordinates

    $$\begin{aligned}
    (\nabla\times \mathbf{F})_1&=\frac{1}{h_2 h_3} \big(\frac{\partial (h_3 F_3)}{\partial u_2} - \frac{\partial (h_2 F_2)}{\partial u_3}\big)\\
    (\nabla\times \mathbf{F})_2&=\frac{1}{h_3 h_1} \big(\frac{\partial (h_1 F_1)}{\partial u_3} - \frac{\partial (h_3 F_3)}{\partial u_1}\big)\\
    (\nabla\times \mathbf{F})_3&=\frac{1}{h_1 h_2} \big(\frac{\partial (h_2 F_2)}{\partial u_1} - \frac{\partial (h_1 F_1)}{\partial u_2}\big)
    \end{aligned}$$
* *Interpretation*.
    * *Assumptions*.
        * A vector field describes the velocity field of a fluid flow
        * A small ball is located within the fluid or gas, with the centre being fixed at a certain point
    * *Conclusion*. If the ball has a rough surface, the fluid flowing past it will make it rotate
        * The rotation axis, oriented according to the right-hand rule, points in the direction of the curl
        * The angular speed of the rotation is half the magnitude of the curl at this point

**Stokes' theorem**. The line integral of a vector field over a loop equals to the flux of its curl through the enclosed surface

<div style="text-align:center">
    <img src="https://i.imgur.com/7rCE9CB.png" width="350">
    <figcaption>Stoke theorem's illustration</figcaption>
</div>

* *Other names*. The fundamental theorem for curls, or curl theorem
* *Assumptions*.
    * $\Sigma$ is a smooth oriented surface in $\mathbf{R}^3$ with boundary $\partial \Sigma$
    * $\mathbf{A} = (P(x,y,z), Q(x,y,z), R(x,y,z))$ is a vector field which has continuous first-order partial derivatives in a region containing $\Sigma$
* *Conclusion*.

    $$\iint_\Sigma (\nabla\times \mathbf{A}) \cdot d\mathbf{a} = \oint_{\partial \Sigma} \mathbf{A} \cdot d\mathbf{l}$$

* *Explicit formula*.

    $$\iint_\Sigma \bigg[\big(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}\big) dy dz + \big(\frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}\big) dz dx + \big(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\big) dx dy\bigg]=\oint_{\partial\Sigma} (Pdx + Qdy + Rdz)$$