
# Introduction to magnetic field
## Fundamental
**Momentum**. $\mathbf{p} = m \mathbf{v}$
* *Interpretation*. A vector quantity, where the direction and magnitude is used to predict the resulting direction and speed of motion of objects after they collide

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

**Torque**. A rotational equivalent of lienar force
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

## Magnetic field
**Magnet**. A material or object producing a magnetic field, which is invisible but is responsible for the most notable property of a magnet, i.e. a force pulling on other ferrormagnetic materials and attracts or repels other magnets
* *Magnetic field*. The magnetic flux density $\mathbf{B}$ is a vector field, which is defined at a given point in space as having the following properties
    * *Direction*. Along the orientation of a compass needle
    * *Magnitude (strength)*. Proportional to how strongly the compass needle orients along the direction
* *Magnetic moment*. A vector characterizing the magnet's overall magnetic properties
    * *Example*. For a bar magnet, 
        * The direction of the magnetic moment points from the south to the north
        * The magnitude relates to how strong and how far these poles are
    * *Units of measurement*. Ampere times meters squared

**Magnetic moment**. The magnetic strength and orientation of a magnet or other object producing a magnetic field
* *Formal*. A vector relating the aligning torgue on the object from an externally applied magnetic field to the field vector itself

**Magnetic field**. A vector field describing the magnetic influence on moving electric charges, electric currents, and magnetic materials
* *Magnetic field strength and magnetic flux density*.
    * *Magnetic field strength $\mathbf{H}$*. Measured in the base units of ampere per meter
        * *Intuition*. $\todo$
    * *Magnetic flux density $\mathbf{B}$*. Measured in tesla, i.e. kilogram per square second per ampere
        * *Tesla meaning*. A particle carrying a charge of one coulomb, and moving perpendicularly through a magnetic field of one tesla, at a speed of one metre per second, experiences a force with magnitude one newton

            $$T=\frac{V\cdot s}{m^2}$$
        * *Intuition*. $\todo$
* *Magnetic field production*. Magnetic fields are produced by moving electric charges and the intrinsic magnetic moments of elementary particles with a fundamental quantum theory, their spin
    * *Elementary particle*. A subatomic particle, which is not composed of other particles