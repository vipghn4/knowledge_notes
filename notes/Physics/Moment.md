<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Moment](#moment)
  - [Fundamental](#fundamental)
  - [Moment](#moment-1)
  - [Physical moments](#physical-moments)
<!-- /TOC -->

# Moment
## Fundamental
**Curl**. A vector operator describing the infinitesimal circulation of a vector field in 3D Euclidean space
* *Mathematical representation*. 
    * *The curl at a point*. A vector whose length and direction denote the magnitude and axis of the maximum circulation
    * *The curl of a field*. The circulation density at each point of the field
* *Irrotational vector field*. A vector field, whose curl is zero
* *Generalization to higher dimensions*. Curl as formulated in vector calculus does not generalize simply to other dimensions
* *Mathematical formulation*. The curl of a vector field at a point is defined in terms of its projection onto various lines through the point
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

* *Interpretation*.
    * *Assumptions*.
        * A vector field describes the velocity field of a fluid flow
        * A small ball is located within the fluid or gas, with the centre being fixed at a certain point
    * *Conclusion*. If the ball has a rough surface, the fluid flowing past it will make it rotate
        * The rotation axis, oriented according to the right-hand rule, points in the direction of the curl
        * The angular speed of the rotation is half the magnitude of the curl at this point
* *Intuition of curl*.
    * *Solving for curl*. Since $\nabla\times \mathbf{F}\in\mathbb{R}^3$, we have that
        
        $$(\nabla\times \mathbf{F}) = \mathbf{I}_3\cdot (\nabla\times \mathbf{F}) = \begin{bmatrix}
        \lim_{A_x\to 0} \frac{1}{|A_x|} \oint_C \mathbf{F}\cdot d\mathbf{r}_x\\
        \lim_{A_y\to 0} \frac{1}{|A_y|} \oint_C \mathbf{F}\cdot d\mathbf{r}_y\\
        \lim_{A_z\to 0} \frac{1}{|A_z|} \oint_C \mathbf{F}\cdot d\mathbf{r}_z\end{bmatrix}$$
    
    * *Extreme cases*. Assume that the magnitudes of the vectors within the vector field $\mathbf{F}$ are fixed, and their orientations are allowed to change, then
        * *Maximum curl*. $\mathbf{F}$ reaches maximum curl at $p$ when 
            
            $$\forall p'\in N(p),\cos[\mathbf{F}(p'), d\mathbf{r}(p')]=1$$
            
            i.e. if $A$ has circular shape, then $\mathbf{F}$ will be circular as illustrated below

            <div style="text-align:center">
                <img src="https://i.imgur.com/kNZguH9.png" width="350">
                <figcaption>Vector field with maximum curl</figcaption>
            </div>

        * *Minimum curl*. $\mathbf{F}$ reaches minimum curl when $\oint_C \mathbf{F}(p) \cdot d\mathbf{r}(p)=0$, i.e.

            $$\forall p'\in N(p),\mathbf{F}(p')=\mathbf{c}$$

            for some constant vector $\mathbf{c}$

            <div style="text-align:center">
                <img src="https://i.imgur.com/lj2swUp.png" width="350">
                <figcaption>Vector field with minimum curl</figcaption>
            </div>
* *Stokes' theorem*.
    * *Assumptions*.
        * $\Sigma$ is a smooth oriented surface in $\mathbf{R}^3$ with boundary $\partial \Sigma$
        * $\mathbf{A} = (P(x,y,z), Q(x,y,z), R(x,y,z))$ is a vector field which has continuous first-order partial derivatives in a region containing $\Sigma$
    * *Conclusion*.

        $$\iint_\Sigma (\nabla\times \mathbf{A}) \cdot d\mathbf{a} = \oint_{\partial \Sigma} \mathbf{A} \cdot d\mathbf{l}$$

**Kinetic energy**. The energy an object possesses due to its motion, i.e. the work required to accelerate the object of a given mass from rest to its stated velocity

$\to$ Having gained this energy during its acceleration, the body maintains this energy unless its speed changes
* *Classical mechanics*. The kinetic energy of a non-rotating object of mass $m$ traveling at speed $v$ is $\frac{1}{2} mv^2$
    * *Unit of measurement*. Joule
* *Meaning of "kinetic"*. Motion in Greek
* *Derivation*. The work $W$ done by a force $F$ on an object over a distance $s$ parallel to $F$ is given as

    $$W = F\cdot s = ma \cdot \frac{at^2}{2} = m \frac{(at)^2}{2} = \frac{1}{2} mv^2$$
* *Kinetic energy of a rotating body*. If a rigid body $Q$ is rotating about any line through the center of mass, then it has rotational kinetic energy $E_r$

    $$E_r = \int_Q \frac{v^2 dm}{2} = \int_Q \frac{(r\omega)^2 dm}{2} = \frac{\omega^2}{2} \int_Q r^2 dm = \frac{1}{2} I \omega^2$$

    where $\omega$ is the body's angular velocity, and $I$ is the body's moment of inertia
* *Rotation in systems*. $E_k = E_t + E_r$ where
    * $E_k$ is the total kinetic energy
    * $E_t$ is the center-of-mass translational kinetic energy
    * $E_r$ is the rotational energy around the center of mass

**Potential energy**. The energy held by an object due to its position relative to other objects, stresses within itself, its electric charge, or other factors
* *Conservative force*. A force with the property that the total work done in moving a particle between two points is independent of the path taken

    $\to$ If a particle travels in a closed loop, the total work done by a conservative force is zero
    * *Examples*. Gravitational force, force in elastic spring, electrostatic force between two electric charges, and magnetic force between two magnetic poles
* *Motivation*. 
    * If the work done by a force on a body moving from A to B does not depend on the path between these points, i.e. the work is done by a conservative force

        $\to$ The work of this force measured from A assigns a scalar value to every other point in space and define a scalar potential field

## Moment
**Moment**. An expression involving the product of a distance and physical quantity, which accounts for how the physical quantity is located or arranged
* *Reference point* Moments are usually defined w.r.t a fixed reference point
* *Commonly used quantities*. Forces (work done), masses (momentum), electric charge distributions (electric dipole)
* *Formula*.
    * *Most basic form*. $\mu_n = r^n Q$
        * $Q$ is the physical quantity, e.g. force applied at a point
        * $r^n$ is the distance to reference point, raised to a power of $n$
    * *General formula*. $\mu_n = \int r^n \rho(r) dr$
        * $\rho$ is the distribution of the quantity being considered
    * *More complex formulas*. Take into account the angular relationships between the distance and the physical quantity
* *Naming conventions*.
    * *Monopole moment*. Moment with $n=0$
    * *Dipole moment*. Moment with $n=1$
    * *Quadrupole moment*. Moment with $n=2$
* *History*. The concept of physical moment is derived from the mathematical concept of moments
    * *Principle of moments*. Derived from Archimedes's discovery of the operating principle of the lever
        * *Idea*. In the lever, one applies a force, and the amount of force applied to the object, i.e. the moment of force, is given as

            $$M=rF$$

            where $F$ is the applied force, and $r$ is the distance from the applied force to object
    * *Meaning of "moment"*. The word moment was first used in mechanics in its the sense of "importance" or "consequence"

        $\to$ The moment of a force about an axis meant the importance of the force w.r.t its power to generate in matter rotation about the axis

## Physical moments
**Momentum**. A vector quantity, where the direction and magnitude is used to predict the resulting direction and speed of motion of objects after they collide
* *Other names*. Linear momentum, and translational momentum
* *Formula*. $\mathbf{p} = m \mathbf{v}$
    * *Single particle*. $p=mv$
    * *Many particles*. $p=\sum_i m_i v_i$
* *Conversation of momentum*. If a closed system is not affected by external forces, its total linear momentum does not change
* *Related quantities*.
    * *Center of mass*. A system of particles has a center of mass, i.e. a point determined by the weighted sum of their positions

        $$r_\text{cm}=\frac{\sum_i m_i r_i}{\sum_i m_i}$$

        * *Explain*. Center of mass is the unique point, where the weighted relative position of the distributed mass sums to zero, i.e.

            $$\sum_i m_i (r_i - r_\text{cm}) = 0$$
        
    * *Euler's first law*. Momentum of the system is given as
        
        $$p=m v_\text{cm}$$ 
        
        where $m$ is the total mass of the particles
        
        * *Explain*. If one or more of the particles is moving, the center of mass of the system will generally be moving as well
* *Application to elastic collisions*. A collision, in which no kinetic energy is transformed into heat or some other form of energy

    $$\begin{aligned}
    m_1 v_1 + m_2 v_2 &= m_1 v_1 + m_2 v_2\\
    \frac{1}{2} m_1 v_1^2 + \frac{1}{2} m_2 v_2^2 &= \frac{1}{2} m_1 v_1^2 + \frac{1}{2} m_2 v_2^2
    \end{aligned}$$

* *Generalization*.
    * *Lagrangian mechanics*.
        * *Lagrangian*. The difference between kinetic energy $T$ and potential energy $V$, i.e.

            $$\mathcal{L} = T - V$$

**Angular momentum**.
* *Moment of inertia*. Determine the torque required for a desired angular acceleration about a rotational axis, i.e. akin to how mass determines the force required for a desired acceleration 
    * *Formula*. $I=m r^2$
* *Angular momentum*. The rotational equivalent of linear momentum
    * *Formula*. $L = I \omega$
        * $\omega = \frac{\mathbf{r} \times \mathbf{v}}{r^2}$ is the orbital angular velocity
        * $\mathbf{r}$ is the position vector
        * $\mathbf{v}$ is the linear velocity of the particle relative to the origin
        * $m$ is the mass of the particle
* *Derivation*.
    * *Observations*.
        * The relation between physical velocity and angular velocity is given as $v=r\omega$

**Torque**. A rotational equivalent of linear        force
* *Other names*. Moment, moment of force, rotational force, or turning effect
* *Motivation*. Originated from the studies by Archimedes of the usage of levers
* *Ideas*. Just as a linear force is a push or a pull, 
    * *Option 1*. A torque can be though of as a twist to an object around a specified axis
    * *Option 2*. Torque is the product of the force magnitude and the perpendicular distance of the line of action of a force from the axis of rotation
* *3D case*. The torque is a pseudo-vector, which is given by the cross product of the position vector and the force vector
    * *Dependencies*. The magnitude of torque of a rigid body depends on
        * The force applied
        * The lever arm vector connecting the point, about which the torque is being measured, to the point of force application
        * The angle between the force and the lever arm vectors
    * *Formal*.
        * *Assumptions*.
            * $\mathbf{\tau}$ is the torque vector and $\tau$ is the magnitude of the torque
            * $\mathbf{r}$ is the position vector
            * $\mathbf{F}$ is the force vector
            * $\theta$ is the angle between the force vector and the lever arm vector
        * *Conclusion*.

            $$\mathbf{\tau} = \mathbf{r} \times \mathbf{F},\quad \tau=\|\mathbf{r}\| \|\mathbf{F}\| \sin\theta$$
* *Equivalence to linear force*. The work $W$ of a torque can be given as

    $$W=\int_{\theta_1}^{\theta_2} \tau d\theta =\int_{s_1}^{s_2} \mathbf{F} d\mathbf{s}$$

**Electric dipole moment**. A measure of the separation of positive and negative electrical charges within a system, i.e. a measure of the system's overal polarity
* *Unit of measurement*. Coulomb-meter
* *Elementary definition*. 
    * *Point changes*. Point particles with electric charge
    * *Electric dipole*. Two point charges, one with charnge $+q$ and the other with charge $-q$ separated by a distance $d$ constitute an electric dipole
        * *Electric dipole moment magnitude*. $p=qd$

            >**NOTE**. Some authors may split $d$ in half, and use $s=d/2$ since this quantity is the distance between either charge and the center of the dipole

        * *Electric dipole moment direction*. From negative charge to positive charge
        * *General mathematical definition*. $\mathbf{q} = q \mathbf{d}$ where $\mathbf{d}$ is the displacement vector pointing from the negative charge to the positive charge
    * *Ideal case*. When the two charge are infinitely charged and are infinitesimally separated
* *Energy and torque*. An object with an electric dipole moment is subject to a torque $\tau$ when placed in an external electric field
    * *Torque*. Tend to align the dipole with the field, i.e. a dipole aligned parallel to an electric field has lower potential energy than a dipole making some angle with it
    * *Formula*. Given the dipole moment $\mathbf{p}$ 
        * *Energy*. $U=-\mathbf{p}\cdot\mathbf{E}$
        * *Torque*. $\mathbf{\tau} = \mathbf{p}\times \mathbf{E}$
* *Dipole moment for a continuous distribution of charge confined to a volume $V$*. 
    * *Formal*. $\mathbf{p}(\mathbf{r}) = \int_V \rho(\mathbf{r}_0) (\mathbf{r}_0 - \mathbf{r}) d^3 \mathbf{r}_0$
        * $\mathbf{r}$ locates the point of observation
        * $d^3\mathbf{r}_0$ denotes an elementary volume in $V$
    * *Charge density an array of point charges*. $\rho(\mathbf{r}) = \sum_{i=1}^n q_i \delta(\mathbf{r}-\mathbf{r}_i)$ where $\delta(\cdot)$ is the Diract delta function
    * *Reduced formula*. $\mathbf{p}(\mathbf{r}) = \sum_{i=1}^n q_i (\mathbf{r}_i - \mathbf{r})$
* *Dipole moment density and polarization density*.
    * *Dipole moment density of an array of charges*. Contain both the location of the array and its dipole moment