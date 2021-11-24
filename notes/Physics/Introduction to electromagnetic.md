<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction to electromagnetic](#introduction-to-electromagnetic)
  - [Fundamental](#fundamental)
    - [Energy](#energy)
    - [Work](#work)
  - [Electrical theory](#electrical-theory)
    - [Introduction](#introduction)
    - [Resistance, voltage, and electric current](#resistance-voltage-and-electric-current)
    - [Electric charge](#electric-charge)
<!-- /TOC -->

# Introduction to electromagnetic
## Fundamental
### Energy
**Energy**. The quantitative property, which must be transferred to a body or a physical system to perform work on the body, or to heat it
* *Conservation*. Energy can be converted in form, but not created or destroyed
* *Unit of measurement*. Joule (J)
    * *Meaning*. Energy transferred to an object by the work of moving it a distance of one metre against a force of one Newton, i.e. energy transferred to an object per unit work
* *Common forms of energy*.
    * *Kinetic energy*. Energy of a moving object
    * *Potential energy*. Stored by an object's positive in a force field, e.g. gravitational, electric, or magnetic
    * *Elastic energy*. Stored by stretching solid objects
    * *Chemical energy*. Released when a fuel burns
    * *Radiant energy*. Carried by light
    * *Thermal energy*. Due to an object's temperature

**Energy and mass**. 
* *Mass-energy equivalence*. $E=mc^2$
    * *Explain*. A small amount of rest mass corresponds to an enormous amount of energy, which is independent of the composition of the matter
        * Any object having mass when stationary, i.e. rest mass, also has an equivalent amount of energy, i.e. rest energy
        * Any additional energy of any form acquired by the object above that rest energy will increase the object's total mass, just as it increases its total energy
* *Rest mass*. The portion of the total mass of an object or system of objects, which is independent of the overall motion of the system

**Energy in classical mechanics**. Work, i.e. $W=\int_C \mathbf{F} \cdot d\mathbf{s}$ is a function of energy

**Power**. The amount of energy transferred or converted per unit time
* *Formula*. $P=\frac{dW}{dt}$
* *Unit of measurements*. Joule per second

### Work
**Work**. Work performed by a system is energy transferred by the system to its surroundings, by a mechanism, through which the system can spontaneously exert macroscopic forces on its surroundings
* *Formula*. $W = F s \cos\theta$ where $F$ is force, $s$ is displacement, and $\theta$ is the angle between the force and the displacement

    $\to$ Work is the energy transferred to or from an object via the application of a force along a displacement

**History**.
* *1824*. Work, i.e. weight lifted through a height, was originally defined in 1824 by Sadi Carnot in his paper, where he used the term "motive power" for work
    * *Quote*. We use here motive power to express the useful effect which a motor is capable of producing. This effect can always be likened to the elevation of a weight to a certain height. It has, as we know, as a measure, the product of weight multipled by the height, to which it is raised

        $\to$ $\text{Work}=\text{Height}\times \text{Weight}$
* *1845*. James Joule wrote a paper, in which he reported his best-known experiment, in which the mechanical power released through the action of a "weight falling through a height" was used to turn a paddle-wheel in an insulated barrel of water
    * *Explain*. The motion of the paddle wheel, through agitation and friction, heated the body of water, to increase its temperature

        $\to$ Both the temperature change of water, and the height of the fall of the weight, were recorded
    * *Consequence*. Joule determined the mechanical equivalent of heat

## Electrical theory
### Introduction
**Electric forces**. Responsible for almost every chemical reaction in our body
* *Basic rules for electric forces*. Electrons repel other electrons, but protons and electrons are attract each other
* *Definition of electric forces*. The force pushing apart two like charges, or pulling together two unlike charges

**Electric field**. If we have a single positively charged particle, a positively charged particle will be pushed away from it by the electric force
* *Electric field*. A force field around a charged object, which illustrates the direction the electric force would push an imaginary positively charged particle, if there was one there

    $\to$ It also shows us how hard a push the electric force would give
* *Purpose*. Used to determine how any other charged particles would move around the charged object
* *Example*. If we have two flat plates with a space in between, one is positively charge and one is negatively charged

    $\to$ The electric field between the plates is going to be strong, since the positively charged plate is pushing, while the negatively charged plate is pulling

**Electric potential energy**. The energy required to move a charge against an electric field

**Electric potential (voltage)**. The difference in potential energy per unit charge between two locations in an electric field
* *Explain*. 
    * When talking about electric field
        
        $\to$ We choose a location then ask what the electric force would do to an imaginary positively charged particle if we put one there
    * To find the electrical potential at a chosen spot
        
        $\to$ We ask how much the electrical potential energy of an imaginary positively charged particle would chage if we moved it there
    * The amount of charge we are pushing or pulling, and whether it is positive or negative, makes a difference to the electrical potential energy

        $\to$ Physicists use a single positive charge as our imaginary charge to test the electrical potential at any given point
* *Observation*. Consider a positively charged particle
    * Near the negative plate, and far from the positive plate, the electrical potential is very flow
    * Far from the negative plate, and near the positive plate, the electrical potential is very high

### Resistance, voltage, and electric current
**Electrical resistance of an object**. A measure of its opposition to the flow of the electric current

<div style="text-align:center">
    <img src="https://i.imgur.com/ZnjWds3.png">
    <figcaption>Conductor geometry</figcaption>
</div>

* *Current density*. The amount of charge per unit time flowing through a unit area of a chosen cross section
    * *Formula*. $J=\lim_{A\to 0} \frac{I_A}{A}=\frac{\partial I}{\partial A}|_{A=0}$
        * $I_A$ is the electric current flowing through a small surface $A$ centered at a given point $M$
        * $J$ is the electric current density at $M$
    * *Unit of measurements*.
        * $A$ is measured in $m^2$
        * $I_A$ is measured in ampere, i.e. $1A=1C/s$ where $C$ is the coulomb and $s$ is the number of seconds
    * *Current density vector and electric current velocity*. $\vec{J}=qn\vec{v}_a$
        * $n$ is the density of charge carriers
        * $q$ is the charge of one carrier
        * $\vec{v}_a$ is the average speed of their movement
    * *Consequence*. The electric current can be understood as the amount of charge per unit time flowing through a chosen cross section
* *Resistivity*. A fundamental property of a material measuring how strongly it resists electric current
    * *Formula*. Given a material, where the current and the electric field may vary or not in different part of the material, then
        
        $$\rho=E/J$$
        
        * $E$ is the magnitude of the electric field (inside the conductor)
        * $J$ is the magnitude of the current density (inside the conductor)
    * *Derivation of resistance from resistivity*. Resistivity is derived from the Ohm's law by removing the area and length factors of the resistor
        * Consider the resistivity for parallel current and electric field

            $$\rho=E/J$$
        * If the electric field is constant, it is given by the total voltage $V$ across the conductor, divided by the length $l$ of the conductor

            $$E=V/l$$

            since $V=\int_0^l E ds=lE$
        * If the current density is constant, then it is given as the total current divided by the cross section area

            $$J=I/A$$
        * Plugging in the three equations, we have that

            $$\rho=\frac{VA}{Il}$$
        * Using the Ohm's law, we have that $\rho=R\frac{A}{l}$
    * *Interpretation*.
        * $\rho$ is the resistance of a conductor with unit length and unit cross sectional area
        * In such conductor, $J$ is the electric current flowing through it
* *Resistance of an object*. $R=\rho \frac{l}{A}$
    * $l$ is the length of the conductor, measured in meters
    * $A$ is the cross-sectional area of the conductor, measured in square meters
    * $\rho$ is the electrical resistivity, i.e. electrical resistance, of the material, measured in $\Omega\cdot m$ (ohm-meters)
* *Resistive heating*. The process of power dissipation, by which the passage of an electric current through a conductor increases the internal energy of the conductor
    
    $\to$ This converts thermodynamic work into heat
    * *Joule's law*. By varying the current and the wire length, Joule discovered that

        $$P\propto I^2 R$$

**Voltage**. The difference between in electric potential between two points, which, in a static eletric field, is defined as the work required per unit of charge to move a test charge between two points

<div style="text-align:center">
    <img src="https://i.imgur.com/SUvwDJH.png">
    <figcaption>Voltage</figcaption>
</div>

* *Assumptions*.
    * The particle is moving with constant velocity, i.e. no acceleration thus total force applying to the particle is $\vec{F}=0$
    * $\vec{E}$ is the electric field 
* *Conclusion*. The voltage increases from point $x_A$ to some point $x_B$ is given by

    $$\begin{aligned}
    \Delta V_{AB}&=V(x_B) - V(x_A)\\
    &=-\int_{r_0}^{x_B} \vec{E}\cdot d\vec{l} - (-\int_{r_0}^{x_A} \vec{E} \cdot d\vec{l})\\
    &=-\int_{x_A}^{x_B} \vec{E} \cdot d\vec{l}
    \end{aligned}$$

    where $\int$ denotes the line integral
* *Interpretation*. The work done per unit charge, against the electric field, to move the charge from $A$ to $B$ without causing any acceleration

    $\to$ The more voltage, the stronger the force exerted on a charged particle to push or pull it according to the electric field
* *Unit of measurement*. Volt, i.e. $V=\frac{J}{C}$

**Electric current**. A stream of charged particles. e.g. electrons or ions, moving through an electrical conductor or space
* *Measurement*. Measured as the net rate of flow of electric charge through a surface, or into a control volume
* *Ohm's law*. The curent through a conductor between two points is proportional to the potential difference across the two points
    * *Assumptions*.
        * $I$ is the current through the conductor in units of amperes
        * $V$ is the potential difference measured across the conductor in units of volts
        * $R$ is the resistance of the conductor in units of ohms
    * *Conclusion*. The current through a conductor between two points is given as
    
        $$I=V/R$$
    
    * *History*. The Ohm's law is deduced from experiments
        * In January 1781, Henry Cavendisk experimented with Leyden jars and measured the current by noting how strong a shock he felt as he completed the circuit with his body

            $\to$ The "velocity" (current) varied directly as the "degree of electrification" (voltage)
        * Francis Ronalds delineated "intensity" (voltage) and "quantity" (current) for the dry pile

            $\to$ He found for a dry pile that the relationship between two parameters was not proportional under certain meteorological conditions
        * In 1825 and 1826, Ohm draw considerable inspiration from Fourier's work on heat conduction in the theoretical explanation of his towkr
            * *Simple modeling*. $x=\frac{a}{b+l}$
                * $x$ is the electric current measured form the galvanometer
                * $l$ is the length of the test conductor
                * $a$ depended on the tehrmocouple junction temperature
                * $b$ is a constant of the entire setup
            * *Modern modeling*. $I=\frac{\varepsilon}{r + R}$
                * $\varepsilon$ is the open-circuit emf of the thermocouple
                    * *Electromotive force (emf)*. The electrical action produced by a non-electrical source, by converting other forms of energy into electrical energy
                * $r$ is the internal resistance of the thermocouple
                * $R$ is the resistance of the test wire
* *Alternating and direct current*.
    * *Alternating current (AC) systems*. The movement of electric charge periodically reverses direction
    * *Direct current (DC) systems*. The movement of electric charge is in only one direction
* *Electric current flowing through a metal wire*. 
    * *Formula*. $I=Q/t$ where $Q$ is the electric charge transferred through the surface over a time $t$
* *Electric current direction*. the flow of positive charge

### Electric charge
**Electric charge**. 
* *Electron and proton*. The charge of an electron is negative, i.e. $-e$, while that of a proton is positive, i.e. $+e$
* *Repelling and attracting*. Charged parcticles whose charges have the same sign repel one another, and particles whose charges have different signs attract
* *Electric charge of a macroscopic object*. The sum of the electric charges of the particles making it up
    * *Atom*. Typically have equal numbers of protons and electrons
    * *Ion*. An atom, or group of atoms, which has lost one or more electrons, giving it a net positive charge
* *Unit of measurement*. Coulomb, i.e. denoted as $C$
    * *Interpretation*. The quantity of charge passing through the cross section of an electrical conductor carrying one ampere for one second
* *Role of charge in electric current*. Electric current is the flow of electric charge through an object, which produces no net loss or gain of electric charge
    * *Most common charge carriers*. Proton and electron
    * *Electric current constitution*. The movement of any of these charged particles constitutes an electric current
* *Conservation of electric charge*. The total electric charge of an isolated system remains constant regardless of charges within the system
    * *Charge-current continuity equation*.
        * *Assumptions*.
            * $\rho$ is the charge density within a volume of integration $V$
            * $J$ is the current density through the closed surface $S=\partial V$
            * $I$ is the net current
        * *Conclusion*. 

            $$-\frac{d}{dt}\int_V \rho dV=\oiint_{\partial V} \mathbf{J} \cdot d\mathbf{S} = I$$
        
        * *Consequence*. $I=-\frac{dq}{dt}$
    * *The charge transferred between time $t_i$ and $t_f$*.
        * *Assumptions*.
            * $I$ is the net outward current through a closed surface
            * $q$ is the electric charge contained within the volume defined by the surface
        * *Conclusion*. $q=\int_{t_i}^{t_f} I dt$

**Coulomb's law**. An experimental law of physics quantifying the amount of force between two stationary, electrically charged particles
* *Electric force (Coulomb force)*. The electric force between charged bodies at rest, i.e. they are not moving
* *Ampere force law*. The force of attraction or repulsion between two current-carrying wires

    <div style="text-align:center">
        <img src="https://i.imgur.com/MVmY340.png">
        <figcaption>Ampere force law</figcaption>
    </div>

    * *Explain*. Each wire generates a magnetic field, following the Biot-Savart law, and the other wire experiences a magnetic force as a consequence, follwoing the Lorentz force law

* *Law content*. 
    * *Assumptions*. 
        * $\mathbf{F}$ is the electrostatic force between two point charges $q_1$ and $q_2$
        * $r$ is the distance between $q_1$ and $q_2$
        * $k_e = \frac{1}{4\pi \epsilon_0}=8.988 \cdot 10^9 (N\cdot m^2 \cdot C^{-2})$ is the Coulomb's constant
        * $\epsilon_0$ is the electric constant
    * *Conclusion*. $|\mathbf{F}|=k_e \frac{|q_1 q_2|}{r^2}$
* *History of $\epsilon_0$*.
    * *Coulomb's experiments*. The force $F$ between two equal point-like amounts of electricity, situated a distance $r$ apart in free space, should be given as

        $$F=k_e \frac{Q^2}{r^2}$$

        where $Q$ is the quantity representing the amount of electricity present at each of the points, and $k_e$ is the Coulomb constant
        * *Values of $k_e$*. If one is starting with no constraints, then $k_e$ may be chosen arbitrarily

            $\to$ For each $k_e$, there is a different interpretation of $Q$
        * *Consequence*. To avoid confusion, each different interpretation of $Q$ has to be allocated a distinctive name and symbol
    * *Centermet-gram-second electrostatic of units*. When $k_e=1$, and a quantity called "Gaussian electric charge" $q_s$ is defined as

        $$F=\frac{q_s^2}{r^2}$$
    * *Rationalization*. A idea subsequently developed that it would be better, in situations of spherical geometry, to include a factor $4\pi$ in equations like Coulomb's law, i.e.

        $$F=k'_e \frac{q_s'^2}{4\pi r^2}$$

        where $4\pi r^2$ is the area of a sphere with radius $r$
    * *Rationalized meter-kilogram-second of units*. Treat the quantity representing amount of electricity as a fundamental quantity on its own right, denoted by $q$, i.e.

        $$F=\frac{1}{4\pi \epsilon_0} \frac{q^2}{r^2}$$

        In other words, $q_s=\frac{q}{\sqrt{4\pi\epsilon_0}}$
    * *Unit of measure of $\epsilon_0$*. We now wants force to be measured in newtons, distance in meters, and charge in coulomb, i.e. the charge accumulated when a current of 1 ampere flows for one second

        $\to$ $\epsilon_0$ should be allocated the unit $C^2 \cdot N^{-1} \cdot m^{-2}$
* *Value of $\epsilon_0$*.
    * *Vaccuum permeability*. The magnetic permeability in a classical vacuum
        * *The ampere-defined vacuum permeability*.
            * *Assumptions*.
                * Two thin, straight, stationary, parallel wires, a distance $r$ apart in free space
                * Each wire carries a current $I$ excerting a force on each other
            * *Conclusion*. $\frac{|\mathbf{F}_m|}{L}=\frac{\mu_0}{2\pi} \frac{|\mathbf{I}|^2}{\mathbf{r}}$
        * *Observation*. Given $\mathbf{r}=1$, $\mathbf{I}=1$, and $L=1$, then $\mathbf{F}_m$ can be measured

            $\to$ We can compute $\mu_0$ accordingly
    * *Value of $\epsilon_0$*. $\epsilon_0=\frac{1}{\mu_0 c^2}$ where $\mu_0$ is given above, and $c$ is the light speedin classical vacuum

**Electrostatics electrical fields from Coulomb's law**. To maek it easy to calculate the Coulomb force on any charge at position $\mathbf{x}_0$, we assume that $q_1=1$

$\to$ $\mathbf{E}(\mathbf{x}_0)=\frac{\mathbf{F}}{q_1}=k_e \frac{q_2}{r^2}\vec{r}$ where $\vec{r}$ is the unit vector representing the force direction
* *Interpretation*. $\mathbf{E}(\mathbf{x}_0)$ is the force made by a charged body with electric charge $q_2$ on a positively charged particle with charge $q_1=1$
* *Consequence*. $\mathbf{F}=q\mathbf{E}$