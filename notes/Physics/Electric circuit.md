<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Electric circuit](#electric-circuit)
    - [Capacitor](#capacitor)
    - [Other components](#other-components)
- [Appendix](#appendix)
  - [Concepts](#concepts)
<!-- /TOC -->

# Electric circuit
**Electrical network**. An interconnection of electrical components, e.g. batteries, sensors, etc.
* *Electrical circuit*. A network consisting of a closed loop, giving a return path for the current
    * *Return path for the current*. The path followed by the current to return to the source
        * *Explain*. 
            * An electrical circuit is a path, through which electrons flow from a voltage or current source, where they enter the circuit

                $\to$ The point where the electrons leave an electrical circuit is called the return or ground
            * Since electrons always end up at the source when they complete the path of their circuit

                $\to$ We call that exit point "return"
        * *Why does the current return*. Without returning to the ground, the charge will build up at some place

            $\to$ There will be an excess of positive charge at a place and an excess of negative charge somewhere else
            * *Consequence*. This may cause potential differences which would make the current flow backward
        * *Kirchoff's law*. The current entering into a node must be equal to the current flowing out of it, i.e.

            $$I_\text{in} + I_\text{out}=0$$
    * *Reference*. https://www.protoexpress.com/blog/current-return-path-signal-integrity/
* *Linear circuit*. An electronic circuit obeying the superposition principle, i.e. 

    $$F(ax_1 bx_2) = aF(x_1) + bF(x_2)$$

    where $F(\cdot)$ is the output of the circuit, $x_1(t),x_2(t)$ are signals applied to the circuit

### Capacitor
**Polarizability**. Refer to the tendency of matter, when subjected to an electric field, to acquire an electric dipole moment in proportion to the applied field

$\to$ This is a property of all matter
* *Explain*. When subject to an electric field, the negatively charged electrons and positively charged atomic nuclei are subject to opposite forces and undergo charge separation
* *Mathematical definition*. The relative tendency of a charge distribution to be distorted from its normal shape by an external electric field
    * *Assumptions*.
        * $\mathbf{p}$ is the induced dipole moment of an atom to the electric field
        * $\mathbf{E}$ is the electric field producing the dipole moment
        * $\alpha$ is the polarizability in isotropic media
    * *Polarizability*
        
        $$\alpha=\mathbf{p}/\mathbf{E}$$

**Dielectric**. 

<div style="text-align:center">
    <img src="https://i.imgur.com/urG9daT.png">
    <figcaption>A polarized dielectric material</figcaption>
</div>

* *Dielectric*. An electrical insulator which can be polarized by an applied electric field
    * *Explain*. When a dielectric material is placed in an electric field 
        * Electric charges do not flow through the material since they do in an electrical conductor
            * *Explain*. Dielectric materials have no loosely bound, or free, electrons which may drift through the material
        * Electric charges shift slightly, instead, from their average equibrium positions, causing dielectric polarization
    * *Dielectric polarization*. Cause positive charges to be displaced in the direction of the field, and negative charges shift in the direction opposite to the field

        $\to$ This creates an internal electric field, which reduces the overall field within the dielectric itself
    * *Reorientation of molecules*. If a dielectric is composed of weakly bonded molecules

        $\to$ Those molecules are polarized, and reoriented so that their symmetry axes align to the field
* *Meaning of "dielectric"*. Materials with high polarizability
* *Reference*. https://en.wikipedia.org/wiki/Dielectric

**Capacitor**. A passive electronic component with two terminals, which stores electrical energy in an electric field

<div style="text-align:center">
    <img src="https://i.imgur.com/urG9daT.png">
    <figcaption>Charge separation in a parallel-plate capacitor</figcaption>
</div>

* *Theory of operation - Overview*. 
    * *Capacitor structure*. Consist of two conductors separated by a non-conductive region, which can be a vacuum, or a dielectric
    * *Functionality*. A charge on one conductor exerts a force on charge carriers within the other conductor, attracting opposite polarity charge and repelling like polarity charges

        $\to$ An opposite polarity charge will be induced on the surface of the other conductor
        * *Consequence*. The conductors hold equal and opposite charges on their facing surfaces, and the dielectric develops an electric field
    * *Ideal capacitor*. Characterized by a constant capacitance $C$, in farads

        $$C=Q/V$$

        where $Q$ is the positive or negative charge on each conductor, and $V$ is the voltage between them
        * *Interpretation*. Unit capacitance means that one coulomb of charge on each conductor causes a voltage of one volt across the device
        * *Conductor separation*. Since conductors are close together, the opposite charges on the conductors attract one another due to their electric fields

            $\to$ The capacitor can store more charge for a given voltage than when the conductors are separated, yielding a larger capacitance
    * *Practical devices*. $C=dQ / dV$
* *Energy stored in a capacitor*. To increase the charge and voltage on a capacitor

    $\to$ Work must be done by an external power source to move charge from the the negative to the positive plate against the opposing force of the electric field
    * *Energy to move a small increment of charge*.
        * *Assumption*.
            * $V$ is the voltage on the capacitor
            * $dW$ is the work required to move a small increment of charge $dq$ from the negative to positive plate
        * *Conclusion*. $dW=V dq$

            $\to$ The energy is stored in the increased electric field between the plates
    * *Total energy stored in a capacitor*.
        * *Assumptions*.
            * $Q$ is the charge stored in the capacitor
            * $V$ is the voltage in across the capacitor
            * $C$ is the capacitance 
        * *Conclusion*.
            
            $$W=\int_0^Q V(q) dq = \int_0^Q \frac{q}{C} dq = \frac{1}{2} \frac{Q^2}{C} = \frac{1}{2} VQ = \frac{1}{2} CV^2$$

* *Reference*. https://en.wikipedia.org/wiki/Capacitor#Theory_of_operation

**Capacitor charging**.

<div style="text-align:center">
    <img src="https://i.imgur.com/iDp0vCi.png">
    <figcaption>Charging circuit</figcaption>
</div>

* *Assumptions*.
    * The capacitor is fully discharged
    * The switch connected to the capacitor has just been moved to position A
    * The voltage across the 100uf capacitor is zero at this point
* *Capacitor charging*. A charging current $I$ begins to flow charging up the capacitor until the voltage across the plates is equal to the 12V supply voltage 
    
    $\to$ The charging current stops flowing and the capacitor is said to be “fully-charged”, i.e.
        
    $$V_C = V_S = 12V$$

**Applications of capacitor**. 
* *Energy storage*. A capacitor can store electric energy when it is connected to its charging circuit
    
    $\to$ When it is disconnected from its charging circuit, it can dissipate that stored energy, so it can be used like a temporary battery
ch    * *Consequence*. Capacitors are commonly used in electronic devices to maintain power supply while batteries are being changed
        
        $\to$ This prevents loss of information in volatile memory (DRAM)
* *Energy release*. When we disconnect the power, the capacitor keeps holding its charge until we connect it to a seond circuit containing an object, e.g. a flash bulb

    $\to$ Charge will flow from the capacitor, through the lamp, until there is nothing on the plates
* *Capacitors and batteries*.
    * A battery uses chemicals to store electrical energy and release it very slowly through a circuit, sometimes it can take several years
    * A capacitor releases its energy much more rapidly, often in seconds or less 
* *Other applications*. When taking a flash photograph, we need our camera to produce a huge burst of light in a fraction of a second
    * *Consequence*. A capacitor attached to the flash gun charges up for a few seconds using energy from the camera's batteries

        $\to$ Once the capacitor is fully charged, it can release all the energy in an instant through the xenon flash bulb

### Other components
**Analog-to-digital converter (ADC, A/D, or A-to-D)**. A system converting an analog signal into a digital signal, or convert an analog input voltage or current to a digital number representing the magnitude of the voltage or current

**Digital-to-analog converter (DAC)**. Perform the reverse function of ADC, i.e. convert a digital signal into an analog signal

**Amplifier**. 
* *Usage*. 
    * Whenever we have to transmit a voltage signal to a far distance, it is done via sending current signal

        $\to$ Due to the long distance, there would be lots of voltage drop and the signal strength will deteriorate
    * After reaching the destination, and appropriate resistance is provided to convert the signal to voltage drop

        $\to$ The voltage drop is then amplified to get a signal of measurable range
* *Consequence*. We always measure the voltage level of any signal at the destination end

# Appendix
## Concepts
**Short circuit**. An electrical circuit allowing a current to travel along an unintended path with no or very low resistance

$\to$ This results in an excessive current flowing through the circuit
* *Opposite*. Open circuit, i.e. an infinite resistance between two nodes
* *Examples*. When the positive and negative terminals of a battery are connected with a low-resistance conductor, e.g. a wire

    $\to$ With low resistance in the connection, a high current will flow, causing the delivery of a large amount of energy in a short period of time
    * *Consequence*. Rapid increase of temperature, potentially resulting in an explosion with the release of hydrogen gas and electrolyte, i.e. an acid or base, which can burn tissue can cause blindness or even death