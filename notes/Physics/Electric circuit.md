<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Electric circuit](#electric-circuit)
  - [Major components](#major-components)
    - [Capacitor](#capacitor)
    - [Resistor](#resistor)
    - [Transistor](#transistor)
    - [Other components](#other-components)
- [Appendix](#appendix)
  - [Concepts](#concepts)
  - [Discussion](#discussion)
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

## Major components
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

<div style="text-align:center">
    <img src="https://i.imgur.com/SYfOPca.png">
    <figcaption>Battery charges capactiro to applied voltage</figcaption>
</div>

* *Theory of operation - Overview*. 
    * *Capacitor structure*. Consist of two conductors separated by a non-conductive region, which can be a vacuum, or a dielectric
    * *Functionality*. A charge on one conductor exerts a force on charge carriers within the other conductor, attracting opposite polarity charge and repelling like polarity charges

        $\to$ An opposite polarity charge will be induced on the surface of the other conductor
        * *Consequence*. The conductors hold equal and opposite charges on their facing surfaces, and the dielectric develops an electric field
    * *Ideal capacitor*. Characterized by a constant capacitance $C$, in farads

        $$C=Q/V$$

        where $Q$ is the positive or negative charge on each conductor, and $V$ is the voltage between them
        * *Interpretation*. Unit capacitance means that one coulomb of charge on each conductor causes a voltage of one volt across the capacitor, i.e. the voltage between the two plates of the capacitor

            $\to$ Higher capacitance means that the capacitor can holds more charges before being fully charged
        * *Conductor separation*. Since conductors are close together, the opposite charges on the conductors attract one another due to their electric fields

            $\to$ The capacitor can store more charge for a given voltage than when the conductors are separated, yielding a larger capacitance
    * *Practical devices*. $C=dQ / dV$
* *Energy stored in a capacitor*. To increase the charge and voltage on a capacitor

    $\to$ Work must be done by an external power source to move charge from the negative to the positive plate against the opposing force of the electric field
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

**Capacitor discharging**. The action of neutralizing the charge in the capacitor by connecting a conductive path across the dielectric
* *Explain*. With the stored charge in the dielectric providing the potential difference, the negative plate repels electrons, which are attracted to the positive plate through the wire

    $\to$ This keeps going until the positive and negative charges are neutralized

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

### Resistor
**Resistor**. A passive two-terminal electrical component implementing electrical resistance as a circuit element
* *Usage*. Used in electronic circuits to reduce current flow, adjust signal levels, divide voltages, bias active elements, and terminate transmission lines
    * *High-power resistors*. Dissipate many watts of electrical power as heat, and are used as part of motor controls, power distribution systems, or as test loads for generators
    * *Fixed resistors*. Have resistances only changing slightly with temperature, time, or operating voltage
    * *Variable resistors*. Can be used to adjust circuit elements, or as sensing devices for heat, light, humidity, force, or chemical activity
* *Theory of operation*.
    * *Ohm's law in practice*. In practice, resistors deviate from the ideal behavior given by Ohm's law, e.g. they have inductance and capacitance affecting the relation between voltage and current in AC circuits
    * *Series and parallel resistors*.
        * *Serial resistors*. $R_\text{eq} = R_1 + R_2 + \dots + R_n$
            * *Explain*. Serial resistors means summation of resistors' lengths, i.e. if all resistors have the same area and resistivity

                $\to$ Their total length is the summation of individual lengths
        * *Parallel resistors*. $\frac{1}{R_\text{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \dots + \frac{1}{R_n}$
            * *Explain*. Parallel resistors means summation of resistors' areas, i.e. if all resistors have the same length and resistivity

                $\to$ Their total area is the summation of individual areas
    * *Power dissipation*. At any instant, the power $P$ (watts) consumed by a resistor of resistance $R$ (ohms) is given as

        $$P=I^2 R = I V = \frac{V^2}{R}$$

        where $V$ is the voltage across the circuit, $R$ is the resistance of the circuit, and $I$ is the current flowing through the circuit

        $\to$ This power is converted into heat, which must be dissipated by the resistor's package before its temperature rises excessively
        * *Explain*. Voltage in an electric circuit is measured against a ground point, whose voltage are supposed to be zero, and the voltage across all resistors are, in fact, the total voltage drop when plugging an power source to the circuit

            $\to$ The ground point is supposed to have a fixed voltage 0, and the input voltage is computed depending on the voltage drop across all resistors and the ground voltage 

### Transistor
**Semiconductor doping**. The introduction of impurities into a semiconductor crystal to the defined modification of conductivity
* *Materials for doping*. Boron (with 3 valence electrons), phosphorus (with 5 valence electrons)
    * *Elements with 3 valence electrons*. Used for p-type doping
    * *Elements with 5 valence electrons*. Used for n-type doping
* *n-doping*. The 5-valent dopant has an outer electron more than the sillicon atoms

    $\to$ Four outer electrons combine with ever one sillicon atom, while the fifth electron is free to move and serves as charge carrier

    <div style="text-align:center">
        <img src="https://i.imgur.com/86Il01c.png">
        <figcaption>The phosphorus atom donates its fifth valence electron</figcaption>
    </div>

    * *Electron donor*. The dopant, which emits an electron, i.e. the dopants are then positively charged by the loss of electrons and are built into the lattice
    * *n-type doped*. Doped semimetals whose conductivity is based on free electrons

        $\tp$ Free electrons are major charge carriers, while free mobile holes are minor charge carriers
        * *Explain*. Thermal energy may occasionally free an electron from the crystal lattice, leading to the appearance of holes
* *p-doping*. The 3-valent dopants can catch an additional outer electron, leaving a hole in the valence band of silicon atoms

    $\to$ Electrons in the valence band become mobile, and the holes move in the opposite direction to the movement of the electrons

    <div style="text-align:center">
        <img src="https://i.imgur.com/NSgXSQK.png">
        <figcaption>The free place on the boron atom is filled with an electron</figcaption>
    </div>

    * *Movement of holes*. 

        <div style="text-align:center">
            <img src="https://i.imgur.com/XvZ8ZdV.png">
            <figcaption>Movement of electron and hole</figcaption>
        </div>

        * In attempting to form four covalent bonds, the three electrons around the boron atom move around, trying to form four bonds, making the hole appear to move
        * The boron atom may borrow an electron from an adjacent silicon atom to form four covalent bonds, leaving the silicon atom deficient by one electron

            $\to$ The hole has moved to an adjacent silicon atom
    * *Energy band of hole*. Holes reside in valence band, a level below the conduction band
    * *Electron acceptor*. With the inclusion of an electron, the dopant, i.e. the acceptor, is negatively charged, and the dopant is fixed in the crystal lattice

        $\to$ Only the positive charges can move
    * *p-doped*. Due to positive holes, these semiconductors are called p-doped

        $\to$ Holes are the major charge carriers, and free electrons are the minor charge carriers
        * *Explain*. Thermal energy may occasionally free an electron from the crystal lattice, leading to the appearance of free electron
* *Electron flow in doped semiconductors*.

    <div style="text-align:center">
        <img src="https://i.imgur.com/SkWxG5K.png">
        <figcaption>Flow of electrons and holes</figcaption>
    </div>

    * *n-doped semiconductor*. Electron flow in an n-type semiconductor is similar to electrons moving in a metallic wire
    * *p-doped semiconductor*. Holes may move about the semiconductor bar, thus, given the positive battery terminal connected to the left end of the p-type bar

        $\to$ Electron flow is out of the negative battery terminal, through the the p-type bar, returning to the positive battery terminal
        * An electron leaving the positive end of the semiconductor bar for the positive battery terminal leaves a hole in the semiconductor, which may move to the right

            $\to$ Holes traverse the crystal lattice from left to right
        * At the negative end of the bar, an electron from the battery combines with a hole, neutralizing it

            $\to$ This makes room for another hole to move in at the positive end of the bar toward the right

* *Reference*. 
    * https://www.halbleiter.org/en/fundamentals/doping/
    * https://workforce.libretexts.org/Bookshelves/Electronics_Technology/Book%3A_Electric_Circuits_III_-_Semiconductors_(Kuphaldt)/02%3A_Solid-state_Device_Theory/2.05%3A_Electrons_and_%E2%80%9Choles%E2%80%99%E2%80%99

**Forward bias and reverse bias**. 

**Transistor**. A semiconductor device used to amplify or switch electrical signals and power

$\to$ This is one of the basic building block of modern electronics
* *Structure*. A transistor is composed of semiconductor material, usually with at least three terminals for connection to an electronic circuit

    $\to$ A voltage or current applied to one pair of transistor's terminals controls the current through another pair of terminals
* *Usage*. In advanced circuits, there are plenty of cases when the output from one stage of a circuit is very small and we need that tiny amount of current to switch on a much larger current
    
    $\to$ In that case, this transistor circuit is just what we need

**Simplified operation**.
* *Main functionality*. 
    * A transistor can use a small signal applied between one pair of its terminals to control a much larger signal at another pair of terminals

        $\to$ Transistor can produce a stronger output signal, a voltage or current, which is proportional to a weaker input signal, hence act as an amplifier
    * A transistor can be used to turn current on or off in a circuit as an electrically controlled switch, where the amount of current is determined by other circuit elements
* *Types of transistor*.
    * *Bipolar transistor*. Have terminals labeled base, collector, and emitter

        <div style="text-align:center">
            <img src="https://i.imgur.com/AN2lQTf.png">
            <figcaption>Bipolar transistor structure</figcaption>
        </div>

        * *Functionality*. A small current at the base terminal, i.e. flowing between the base and the emitter, can control or switch a much larger current between the collector and the emitter terminals
        * *Components*.
            * *Emitter*. Supply charge carriers to the collector via the base region
            * *Collector*. Collect most of all charge carriers emitted from the emitter
            * *Base*. Trigger and control the amount of current flows through the emitter to collector
    * *Field-effect transistor*. Terminals are labeled gate, source, and drain

        <div style="text-align:center">
            <img src="https://i.imgur.com/aVXMcc9.png">
            <figcaption>Field-effect transistor structure</figcaption>
        </div>

        * *Functionality*. A voltage at the gate can control a current between source and drain
* *Transistor as a switch*. Transistors are commonly used in digital circuits as electronic switches, which can be either in an "on" or "off" state, both for high-power applications and low-power applications
    * *Important parameters*. The current switched, the voltage handled, and the switching speed, characterized by the rise-and-fall times 
    * *Objectives*. Simulate, as near as possible, the ideal switch having the properties of an open circuit when off, the short circuit when on, and an instantaneous transition between the two states
        * *Idea*. Parameters are chosen so that
            * The "off" output is limited to leakage currents too small to affect connected circuitry
            * The resistance of the transistor in the "on" state is too small to affect circuitry
            * The transition between the two states is fast enough not to have an detrimental effect
* *Transistor as an amplified*. Transistor-based amplifiers are designed so that a small change in input voltage changes the small current through the base of the basistor, whose current amplification combined with the properties of the circuit means that small swings in input voltage produce large changes in output voltage

**How bipolar transistors work**.

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

**Diode**. A two-terminal electronic component conducting current primarily in one direction, i.e. asymmetric conductance with low (ideally zero) resistance in one direction and high (ideally infinite) resistance in the other
* *Types of dicode*.
    * *Termionic diode*. A vacuum tube with two electrodes, i.e. a heated cathode and a plate, in which electron
    * *Semiconductor diode*. A crystalline piece of semiconductor with a p-n function connected to two electrical terminals
* *Main functions*. Allow an electric current to pass in one direction, i.e. diode's forward direction, while blocking it in the opposite direction, i.e. the reverse direction
    * *Rectification*. The unidirectional behavior of the diode
    * *Usage*. Convert alternating current (AC) to direct current (DC)
* *Cut-in voltage*. Semiconductor diodes begin conducting electricity only if a certain threshold voltage, i.e. cut-in voltage, is present in the forward direction

    $\to$ This is the state, in which the diode is said to be forward-biased

# Appendix
## Concepts
**Short circuit**. An electrical circuit allowing a current to travel along an unintended path with no or very low resistance

$\to$ This results in an excessive current flowing through the circuit
* *Opposite*. Open circuit, i.e. an infinite resistance between two nodes
* *Examples*. When the positive and negative terminals of a battery are connected with a low-resistance conductor, e.g. a wire

    $\to$ With low resistance in the connection, a high current will flow, causing the delivery of a large amount of energy in a short period of time
    * *Consequence*. Rapid increase of temperature, potentially resulting in an explosion with the release of hydrogen gas and electrolyte, i.e. an acid or base, which can burn tissue can cause blindness or even death

**Electronic switch**. An electronic component or device, which can switch an electrical circuit, interrupting the current, or diverting it from one conductor to another

**Electric circuit symbols**.
* *Voltage symbol*. https://electronics.stackexchange.com/questions/162564/what-does-this-strange-symbol-refer-to

**Depletion region**. An insulating region within a conductive, doped semiconductor material, where mobile charge carries have been diffused away, or have been forced away by an electric field
* *Other names*. Depletion region, depletion layer, depletion zone, junction region, space charge region, or space charge layer

>**NOTE**. Understanding the depletion region is key to explaining modern semiconductor electronics, e.g. diodes, transistors, etc.

* *Formation of a p-n junction*. A depletion region forms instantaneously across a p-n junction, when the junction is in thermal equilibrium or in a steady state
    * *Explain*. Electrons and holes diffuse into regions with lower concentration of them, i.e. when N-doped and P-doped semiconductors are placed together to form a junction

        $\to$ Free electrons in the N-side conduction band migrate into the P-side conduction band, and holes in P-side valence band migrate into the N-side valence band
        * Following transfer, the diffused electrons contact with holes and are eliminated by recombination in the P-side, likewise, the diffused holes are recombined with free electrons in the N-side

            $\to$ The diffused electrons and holes are gone
        * In a N-side region near to the junction interface, free electrons in the conduction band are gone due to
            * The diffusion of electrons to the P-side, and
            * Recombination of electrons to holes that are diffused from the P-side
        * Holes in a P-side region near to the interface are also gone by a similar reason
    * *Consequence*. Majority charge carriers are depleted in the region around the junction interface
    * *Side effects*. The depletion region is charged, i.e. its N-side is positively charged and its P-side is negatively charged

        $\to$ This creates an electric field providing a force opposing the charge diffusion
        * *Consequence*. When the electric field is strong enough to cease further diffusion of holes and electrons, the region reaches equilibrium
    * *Built-in voltage (junction voltage or barrier voltage)*. Integration of the electric field across the depletion region
    * *Conclusion*. Charge transfer in semiconductor devices is from
        * The charge carrier drift by the electric field, and
        * The charge carrier diffusion due to the spatially varying carrier concentration
* *Mathematical formulation of p-n junction formation*.
    * *Assumptions*.
        * $\sigma$ is the electrical conductivity, i.e. $\sigma = J / E$ is the reverse of resistivity
        * $D_e,D_h$ are diffusion constants for electrons and holes respectively
        * $\mathbf{E}$ is the electric field
        * $e$ is the elementary charge, i.e. $1.6 \cdot 10^{-19}$ coulomb
        * $p$ is the hole density, i.e. number of holes per unit volume
        * $n$ is the electron density, i.e. the number of electrons per unit volume
    * *Net current density for holes*. In the P-side of the depletion region, where holes drift by the electric field, the net current density is given by
        
        $$\mathbf{J} = \sigma \mathbf{E} - e D_h \nabla p$$
    
    * *Net current density for electrons*. In the N-side of the depletion region, where electrons drift by the electric field, the net current density is given by

        $$\mathbf{J} = \sigma \mathbf{E} + e D_e \nabla n$$

    * *Equilibrium*. Electrons will flow until the density gradient builds up enough for the diffusion current to exactly balance the drift current, i.e.

        $$\sigma \mathbf{E} + e D_e \nabla n = 0$$

    * *References*. 
        * https://en.wikipedia.org/wiki/Diffusion_current
        * https://en.wikipedia.org/wiki/Fick%27s_laws_of_diffusion
* *Why depletion region does not occupy the whole semiconductor region*. The electrons already on the P side may "want" to continue diffusing deeper into the p-type material, further expanding the depletion region
    
    $\to$ However, this doesn't actually happen because semiconductor materials do not conduct minority carriers well at all
    * *Explain*. 
        * Once a hole gets filled by an electron, that electron falls from the conduction band down to the valence band and is effectively "annihilated" as far as charge conduction is concerned 
        * Since the electric field is basically zero in the p-type region outside the depletion region (the negatively and positively charged sides of the junction balance each other out)
            
            $\to$ There is no strong force pushing electrons away from the junction. Of course, the reverse applies to holes on the n-type side
* *Forward bias*. Narrow the depletion region and lower the baterrier to carrier injection by applying a positive voltage to the P-side w.r.t the N-side
    * *Explain*. Majority carriers get some energy from the bias field, enabling them to go into the region and neutralize opposite charges
        * The more bias the more neutralization (or screening of ions in the region) occurs
            
            $\to$ The carriers can be recombined to the ions but thermal energy immediately makes recombined carriers transition back
        * When bias is strong enough that the depletion region becomes very thin, the diffusion component of the current, through the junction interface, greatly increases and the drift component decreases
            
            $\to$ The net current flows from the P-side to the N-side
    * *Consequence*. The carrier density is large, i.e. it varies exponentially with the applied bias voltage, making the junction conductive and allowing a large forward current
* *Reverse bias*. The potential drop across the depletion region increases by applying a negative voltage to the P-side w.r.t the N-side
    * *Explain*. 
        * Majority carriers are pushed away from the junction, leaving behind more charged ions
        * The depletion region is widened and its field becomes stronger, which increases the drift component of current, through the junction interface, and decreases the diffusion component

            $\to$ The net current flows from the N-side to the P-side
    * *Consequence*. The carrier density, i.e. mostly minority carriers, is small and only a very small reverse saturation current flows

**p-n junction**. A boundary or interface between p-type and n-type semiconductor materials, inside a single crystal of semiconductor, which is created by doping
* *Usage*. Building blocks of semiconductor electronic devices, e.g. diodes, transistors, etc.

## Discussion
**Why dielectric is used in capactiors**. Dielectric material between the two plates developed an electric field opposed to the electric field of the power source, decreasing the voltage across the capactior

$\to$ Capacitance is increased

**Electric current in serial and parallel circuits**.
* *Serial circuits*. $I = I_1 = I_2 = \dots = I_n$
    * *Explain*. The high resistance of the resistor doesn’t block the passing charges, it slows them
        
        $\to$ These slower moving charges in turn repel the charges approaching the resistor and so the current in the whole circuit slows
* *Parallel circuits*. $I = I_1 + I_2 + \dots + I_n$
    * *Explain*. Due to the summation of conductivity
* *Reference*. 
    * https://www.reddit.com/r/AskPhysics/comments/lcccye/why_is_the_current_before_and_after_a_resistor/
    * https://en.wikipedia.org/wiki/Kirchhoff%27s_circuit_laws

**What is capacitance and inductance in resistors**

**What if the electric circuit does not have return path to the ground**.

**Why electrons cannot flow in an open circuit**.

**What is the definition of "voltage" inside an electric circuit**.

**Why voltage and electric current in serial and parallel circuits have their form**.

**What is AC and DC and how they are generated**