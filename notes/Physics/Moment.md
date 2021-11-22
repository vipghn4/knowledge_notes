<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Moment](#moment)
  - [Fundamental](#fundamental)
    - [Conservative force](#conservative-force)
    - [Energy](#energy)
    - [Moment](#moment-1)
    - [Geometrical products](#geometrical-products)
  - [Physical moments](#physical-moments)
    - [Mechanical moments](#mechanical-moments)
    - [Electrical moments](#electrical-moments)
<!-- /TOC -->

# Moment
## Fundamental
### Conservative force
**Conservative vector field**. A vector field which is the gradient of some function
* *Characteristics*. 
    * The line integral is path independent, i.e. the choice of any path between two points does not change the value of the line integral

        $\to$ Path independence of line integral is equivalent to the vector field being conservative
    * The vector field is irrotational, i.e. in 3D, it means that it has vanishing curl
* *Conservative vector field in mechanics*. They are vector fields representing forces of physical systems, in which energy is conserved
* *Mathematical definition*.
    * *Assumptions*.
        * $U$ is an open subset of $\mathbb{R}^n$
        * $\mathbf{v}:U\to\mathbb{R}^n$ is a vector field
    * *Conclusion*. $\mathbf{v}$ is conservative if and only if there exists a $C^1$ scalar field $\phi$ on $U$ such that

        $$\mathbf{v}=\nabla \phi$$
    * *Scalar potential for $\mathbf{v}$*. $\phi$
* *Fundamental theorem of vector calculus*. Any vector field can be expressed as the sum of a conservative vector field and a solenoidal field
    * *Solenoidal vector field*. A vector field $\mathbf{v}$ with zero divergence at all points in the field, i.e.

        $$\nabla\cdot \mathbf{v}=0$$

        * *Other names*. Incompressible vector field, or divergence-free vector field, or traverse vector field
* *Path independence*. $\oint_C \mathbf{v}\cdot d\mathbf{r}=0$ for every rectifiable simple closed path $C$ in $U$
* *Reference*. https://en.wikipedia.org/wiki/Conservative_vector_field

**Conservative force**. 
* *Conservative force*. A force with the property that the total work done in moving a particle between two points is independent of the path taken
    
    $\to$ Equivalently, if a particle travels in a closed loop, the total work done by a conservative force is zero
    * *Total work done*. The sum of the force acting along the path multiplied by the displacement
    * *Examples*. 
        * Force in elastic spring
        * Electrostatic force between two electric charges
        * Magnetic force between two magnetic poles
    * *Consequences*. A conservative force depends only on the position of the object
        * If a force is conservative, we can assign a numerical value for the potential at any point, and conversely
            * *Explain*. When an object moves from one location to another, the force changes the potential energy of the object, by an amount which does not depend on the path taken

                $\to$ This contributes to the mechanical energy and the overall conservation of energy
        * If a force is not conservative, then defining a scalar potential is not possible
            * *Explain*. Taking different paths would lead to conflicting potential differences between the start and end points
* *Mathematical formulation*.
    * *Formulation*. A force field $\mathbf{F}$ defined everywhere in space is conservative if it meets any of these equivalent conditions
        * The curl of $\mathbf{F}$ is the zero vector, i.e.

            $$\nabla\times\mathbf{F} = \mathbf{0}$$
        
        * There is zero net work $W$ done by the force when moving a particle through a trajectory starting and ending in the same place

            $$W=\oint_C \mathbf{F}\cdot d\mathbf{r}=\mathbf{0}$$
        
        * The force can be written as the negative gradient of a potential $\mathbf{\Phi}$

            $$\mathbf{F}=-\nabla\mathbf{\Phi}$$
* *Meaning of "conservative"*. When a conservative force exists, it converses mechanical energy

### Energy
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
* *Motivation*.  If the work done by a force on a body moving from A to B does not depend on the path between these points, i.e. the work is done by a conservative force

    $\to$ The work of this force measured from A assigns a scalar value to every other point in space and define a scalar potential field
    * *Consequence*. There is a function $U(\mathbf{x})$, i.e. a potential, can be evaluated at two points $\mathbf{x}_A,\mathbf{x}_B$ to obtain the work over any trajectory between these points

        $$W=\int_C\mathbf{F}\cdot d\mathbf{x}=U(\mathbf{x}_A) - U(\mathbf{x}_B)$$

        where $C$ is the trajectory taken from $A$ to $B$
    * *The potential energy associated with the applied force*. $U(\mathbf{x})$

**Relativity of potential energy**. Absolute energy values are based on an arbitrary zero value
* *Example*. A teacher raises a 5-Newton weight from the bench to a height of 1.5m, they then calculate the work done to lift it up to 1.5m

    $\to$ Assuming the weight has been raised before, what if it was raised from the floor, or from ground level outside if the room is not at ground level
* *Interpretation of negative potential energy*. An object with negative potential energy is in a location, where it would require work done on it, i.e. energy put in, to move the object to the zero energy point

### Moment
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

### Geometrical products
**Cross product**. Defined only in 3D space and denoted as $\mathbf{a}\times\mathbf{b}$
* *Cross product $\mathbf{a}\times\mathbf{b}$*. A vector $\mathbf{c}$ which is perpendicular to both $\mathbf{a}$ and $\mathbf{b}$, with a direction given by the right-hand rule, and a magnitude equal to the area of the parallelogram spanned by $\mathbf{a}$ and $\mathbf{b}$
    * *Assumptions*.
        * $\theta$ is the angle between $\mathbf{a}$ and $\mathbf{b}$ in the plane containing them
        * $\|\cdot\|$ denotes the magnitude operator
        * $\mathbf{n}$ is the unit vector perpendicular to the plane containing $\mathbf{a}$ and $\mathbf{b}$, in the direction given by the right-hand rule
    * *Formula*. $\mathbf{a}\times\mathbf{b}=\|\mathbf{a}\| \|\mathbf{b}\| \sin(\theta) \mathbf{n}$
* *Derivation*.
    * *Coordinate notation*. If $(\mathbf{i}, \mathbf{j}, \mathbf{k})$ is a oriented orthonormal basis, then the basis vectors satisfy the following equalities

        $$\mathbf{i}\times\mathbf{j}=\mathbf{k},\quad \mathbf{j}\times\mathbf{k}=\mathbf{i},\quad \mathbf{k}\times\mathbf{i}=\mathbf{j}$$

        * *Anticommutativity*. 

            $$\mathbf{j}\times\mathbf{i}=-\mathbf{k},\quad \mathbf{k}\times\mathbf{j}=-\mathbf{i},\quad \mathbf{i}\times\mathbf{k}=-\mathbf{j}$$

            * *Consequence*. $\mathbf{i}\times\mathbf{i} = \mathbf{0}$ for every vector $\mathbf{i}$
    * *Derivation of $\mathbf{a}\times\mathbf{b}$*. We can derive $\mathbf{a}\times\mathbf{b}$ by representing these vectors as

        $$\mathbf{a}=a_1\mathbf{i} + a_2\mathbf{j} + a_3\mathbf{k},\quad \mathbf{b}=b_1\mathbf{i} + b_2\mathbf{j} + b_3\mathbf{k}$$

**Scalar triple product**. The dot product of one of the vectors with the cross product of the other two
* *Formula*. $\mathbf{a}\cdot(\mathbf{b}\times\mathbf{c})$
    * *Geometric interpretation*. The signed volume of the parallelepiped defined by the given three vectors
* *Relation to exterior product*. The exterior product $\mathbf{a}\land \mathbf{b}\land \mathbf{c}$ is a trivector with magnitude equal to to scalar triple product, i.e.

    $$|\mathbf{a}\land \mathbf{b}\land \mathbf{c}| = |\mathbf{a}\cdot (\mathbf{b}\times \mathbf{c})|$$

## Physical moments
### Mechanical moments
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

**Lever**. A simple machine consisting of a beam or rigid rod pivoted at a fixed hinge, or fulcrum
* *Importance of lever*. First mathematically described by Archimedes, play a central role in generalizing linear forces and moments to their rotational versions
* *Meaning of "lever"*. From Old French word "levier", which means "to raise"
* *Force and levers*. The mechanical advantage of a lever can be determined by considering the balance of moments or torque $T$ about the fulcrum
    * *Assumptions*.
        * $F_1, F_2$ are the input forces to the lever
        * $a,b$ are the corresponding perpendicular distances between the forces and the fulcrum lying between the forces
    * *Torque*. $T_1=F_1 a$ and $T_2 = F_2 b$
    * *Balanced moments of torque*. $T_1 = T_2$
    * *Mechanical advantage of the lever*. The ratio of output force to input force

        $$\text{MA}=\frac{F_2}{F_1}=\frac{a}{b}$$
* *Law of the lever*. $\text{MA}=\frac{F_2}{F_1}=\frac{a}{b}$
    * *Explain*. As the lever rotates around the fulcrum, points further from this pivot move faster than points closer to the pivot

        $\to$ A force applied to a point further from the pivot must be less than the force located at a point closer in
        * *Explain*. Power is the product of force and velocity

**Torque**. A rotational equivalent of linear force

<div style="text-align:center">
    <img src="https://i.imgur.com/bBgy3M6.png" width="350">
    <figcaption>Torque illustration</figcaption>
</div>

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
        
        * *Intuition*. Consider an object unit distance apart from the rotation center, then $\mathbf{\tau}$ is an entity with direction and magnitude, just as the angular displacement but with different meanings
            * *Direction*. Represent the rotational direction, just as angular displacement
            * *Magnitude*. Represent the force applied to the object when applying a force $\mathbf{F} \sin\theta$ perpendicularly to a point which is $\|\mathbf{r}\|$ distance apart from the rotation center (just as the principle of lever)
* *Angular work - Equivalence to linear force*. The work $W$ of a torque can be given as

    $$W=\int_{\theta_1}^{\theta_2} \tau \cdot d\theta =\int_{s_1}^{s_2} \mathbf{F} \cdot d\mathbf{s}$$

    where $d\mathbf{s}=d\mathbf{\theta}\times\mathbf{r}$ is the infinitesimal linear displacement
    * *Rotation representation in 3D*.
        * *Axis-angle representation (rotation vector or Euler vector) of a rotation*. Parametrize a rotation in 3D Euclidean space by two quantities, i.e. a unit vector $\mathbf{e}$ indicating the direction of an axis of rotation, and an angle $\theta$ describing the magnitude of the rotation about the axis
            * *Formal*. $\mathbf{\theta}=\theta \mathbf{e}$
        * *Angular displacement in 3D*. 
            * *Angular displacement*. An entity, i.e. an axis-angle, with a direction and a magnitude
                * *Direction*. Specify the axis of rotation
                * *Magnitude*. Specify the rotation in radians about the axis, using the right-hand rule to determine direction
            * *Angular displacement as vectors*. Angular displacement is not a vector, since it does not obey the commutative law for addition
    * *Linear displacement from angular displacement*. $\mathbf{s}=\mathbf{\theta}\times\mathbf{r}$ is the linear displacement, where $d\theta$ is the angular displacement, and $\mathbf{r}$ is the radius vector
        * *Explain*. $\|\mathbf{s}\|=\theta \|\mathbf{r}\|$ and $\mathbf{s}$'s direction points to the direction of linear displacement
    * *Proof*.

        $$W=\int_{s_1}^{s_2} \mathbf{F} \cdot d\mathbf{s}=\int_{\theta_1}^{\theta_2} \mathbf{F}\cdot (d\mathbf{\theta}\times d\mathbf{r})=\int_{\theta_1}^{\theta_2} (\mathbf{F}\times\mathbf{r})\cdot d\mathbf{\theta}=\int_{\theta_1}^{\theta_2} \mathbf{\tau} \cdot d\mathbf{\theta}$$
* *Pseudovector*. Quantities such as toeque, angular displacement, and axis-angle representation are called pseudovectors, i.e. they are not actually vectors but have direction and magnitude

**Moment of inertia of a rigid body**. Determine the torque required for a desired angular acceleration about a rotational axis, i.e. akin to how mass determines the force required for a desired acceleration
* *Other names*. Mass moment of inertia, angular mass, second moment of mass, or rotational inertia
* *Scenario*. When a body is free to rotate around an axies, torque must be applied to change its angular momentum

    $\to$ The amount of torque required to cause any given angular acceleration is proportional to the moment of inertia of the body
    * *History*. Christian Huygens introduced this quantity in his study of the oscillation of a body hanging from a pivot
* *Formula*. $I=m r^2$ where $m$ is the body's mass and $r$ is the distance from the pivot point
    * *Explain*. Solve the equation $\mathbf{\tau}=I\alpha$ for $I$, given $\mathbf{\tau}=\mathbf{F}\times\mathbf{r}=m (d\mathbf{v}_\text{tangent} \times \mathbf{r})$ and $\alpha=(\mathbf{r}\times d\mathbf{v}_\text{tangent}) / r^2$
* *Relation to torque*. If the shape of the body does not change, then

    $$\mathbf{\tau}=I\alpha$$

    where $\mathbf{\tau}$ is the applied torque on the body, and $\alpha$ is the angular acceleration around the principal axis
    * *Angular acceleration*. A pseudovector representing the rate, at which the angular velocity of the object about the origin changes
        * *Formula in 2D for angular velocity*. $\omega=\frac{v_\text{tangent}}{r}$
        * *Formula in 3D for angular velocity*. $\mathbf{\omega}=\mathbf{r}\times\mathbf{v}_\text{tangent} / r^2$
    * *Intuition*. This formula is just as $F=ma$

**Angular momentum**. The rotational equivalent of linear momentum $\mathbf{p}=m\mathbf{v}$
* *Formula*. $\mathbf{L} = I \mathbf{\omega} = m (\mathbf{r}\times\mathbf{v})$
    * $\omega = \frac{\mathbf{r} \times \mathbf{v}}{r^2}$ is the orbital angular velocity
    * $\mathbf{r}$ is the position vector
    * $\mathbf{v}$ is the linear velocity of the particle relative to the origin
    * $m$ is the mass of the particle
* *Derivation*. 

    $$\mathbf{L}=\int \mathbf{\tau} dt = \int m [d\mathbf{v}(t) \times \mathbf{r}] dt = m (\mathbf{r}\times\mathbf{v})$$

* *Consequence*. Rotating a mass $mr$ with distance $(\mathbf{r}\times\mathbf{v}) / r$ apart from the origin is the same as rotating a mass $m$ with distance $\mathbf{r}\times\mathbf{v}$ apart from the origin

### Electrical moments
**Electric dipole moment**. A measure of the separation of positive and negative electrical charges within a system, i.e. a measure of the system's overal polarity
* *Unit of measurement*. Coulomb-meter
* *Elementary definition*. 
    * *Point charges*. Point particles with electric charge
    * *Electric dipole*. Two point charges, one with charnge $+q$ and the other with charge $-q$ separated by a distance $d$ constitute an electric dipole
        * *Electric dipole moment magnitude*. $p=qd$

            >**NOTE**. Some authors may split $d$ in half, and use $s=d/2$ since this quantity is the distance between either charge and the center of the dipole

        * *Electric dipole moment direction*. From negative charge to positive charge
* *General mathematical definition*. $\mathbf{q} = q \mathbf{d}$ where $\mathbf{d}$ is the displacement vector pointing from the negative charge to the positive charge
    * *Ideal case*. When the two charge are infinitely charged and are infinitesimally separated, but with a finite $\mathbf{p}$

**Energy and torque of electric dipole**. An object with an electric dipole moment is subject to a torque $\tau$ when placed in an external electric field

<div style="text-align:center">
    <img src="https://i.imgur.com/C128a0Z.png" width="350">
    <figcaption>Electric dipole moment and torque</figcaption>
</div>

* *Explain*. The torque tends to align the dipole with the field
    
    $\to$ A dipole aligned parallel to an electric field has lower potential energy than a dipole making some angle with it
* *Torque*. $\mathbf{\tau} = \frac{1}{2} \mathbf{p}\times \mathbf{E} + \frac{1}{2} \mathbf{p}\times \mathbf{E} = \mathbf{p}\times \mathbf{E}$
    * *Explain*. The torque is computed given that the lever arm for each charge is located at the center of the dipole

        <div style="text-align:center">
            <img src="https://i.imgur.com/OjHHrOI.png">
            <figcaption>Electric dipole moment and torque</figcaption>
        </div>
    
    * *References*. http://hyperphysics.phy-astr.gsu.edu/hbase/electric/diptor.html
* *Potential energy*. $U=-\mathbf{p}\cdot\mathbf{E}$
    * *Explain*. 

        <div style="text-align:center">
            <img src="https://i.imgur.com/22FF118.png">
            <figcaption>Low energy and high energy states</figcaption>
        </div>

        * To rotate the dipole from the low energy state against the field requires work
        * We have a potential energy function

            $$\begin{aligned}
            U&=\int_0^\theta \mathbf{\tau} d\theta'=\int_0^\theta (\mathbf{p}\times\mathbf{E})\cdot d\theta'\\
            &=\int_0^\theta \|\mathbf{E}\| \|\mathbf{p}\| \sin(\theta') \|d\theta'\|\\
            &=\|\mathbf{E}\| \|\mathbf{p}\| (1 - \cos\theta)
            \end{aligned}$$

            This is the potential energy of the dipole, provided one takes the potential energy to be zero when $\mathbf{p}$ and $\mathbf{E}$ are parallel, i.e. $U=0$ when $\theta=0$
        * In many applications, writers find it convenient to take $U=0$ at $\theta=90^o$, in such cases, the potential energy is given as

            $$U=\int_{\pi/2}^\theta \mathbf{\tau} d\theta'=-\|\mathbf{E}\| \|\mathbf{p}\| \cos\theta=-\mathbf{E}\cdot\mathbf{p}$$

* *Dipole moment for a continuous distribution of charge confined to a volume $V$*. 
    * *Formal*. $\mathbf{p}(\mathbf{r}) = \int_V \rho(\mathbf{r}_0) (\mathbf{r}_0 - \mathbf{r}) d^3 \mathbf{r}_0$
        * $\mathbf{r}$ locates the point of observation
        * $d^3\mathbf{r}_0$ denotes an elementary volume in $V$
    * *Charge density an array of point charges*. $\rho(\mathbf{r}) = \sum_{i=1}^n q_i \delta(\mathbf{r}-\mathbf{r}_i)$ where $\delta(\cdot)$ is the Diract delta function
    * *Reduced formula*. $\mathbf{p}(\mathbf{r}) = \sum_{i=1}^n q_i (\mathbf{r}_i - \mathbf{r})$
* *Dipole moment density and polarization density*.
    * *Dipole moment density of an array of charges*. Contain both the location of the array and its dipole moment

        $$\mathbf{p}=\sum_i q_i \mathbf{d}_i$$
    * *Polarization density*. $\mathbf{P} = \frac{d \mathbf{p}}{d V}$ where $\nabla \mathbf{p}$ is the dipole moment carried by a certain volume element $\nabla V$ in the material