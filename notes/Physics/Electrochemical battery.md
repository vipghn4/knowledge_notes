<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [The chemistry of a battery](#the-chemistry-of-a-battery)
  - [Metals and their properties](#metals-and-their-properties)
  - [How battery works in the first glance](#how-battery-works-in-the-first-glance)
- [Appendix](#appendix)
  - [Discussion](#discussion)
<!-- /TOC -->

# The chemistry of a battery
## Metals and their properties 
**Metal (definition from chemistry)**. An element which readily forms positive ions, i.e. cations, and has metallic bonds
* *Other description*. Metals are sometimes described as a lattice of positive ions surrounded by a cloud of delocalized electrons

    <div style="text-align:center">
        <img src="https://i.imgur.com/rNApuVt.png">
        <figcaption>Metallic bonding</figcaption>
    </div>

* *Metallic bond*. The sharing of many detached electrons between many positive ions, where the electrons act as a glue giving the substance a definite structure
    * *Explain*. Metals have low ionization energy, thus the valence electrons can be delocalized throughout the metals

        $\to$ These electrons are not associated with a particular nucleus of metal, they are free to move throughout the crystalline structure, forming a sea of electrons
    * *Attractive force*. The electrons and the positive ions in the metal have a strong attractive force between them, leading to high melting or boiling points
    * *Other consequences*. Metallic bonds causes many of the traits of metals, e.g. strength, malleability, ductility, luster, conduction of heat and electricity
        * *Stiffness of metal*. When the atoms give up their valence electrons, they form ions
            
            $\to$ These ions are held together by the electron cloud surrounding them, resulting in strength and stiffness
        * *Heat and electricity conduction*. Due to freely moving electrons
* *Most conductive metals*. Ag, Cu, Au, Al, Na, W, Cu, Zn, Fe
* *Reference*. https://www.cs.mcgill.ca/~rwest/wikispeedia/wpcd/wp/m/Metal.htm

## How battery works in the first glance
**Battery**. A device storing chemical energy, and convert it to electricity

$\to$ This is known as electrochemistry and the system underpining a battery is called an electrochemical cell
* *Electrochemical cell*. A battery is made up of multiple electrochemical cells

**Electrodes**. To produce a flow of electrons, we need to have somewhere for the electrons to flow from, and somewhere for the electrons to flow to

<div style="text-align:center">
    <img src="https://i.imgur.com/TwNvn6Y.png">
    <figcaption>Anode and cathode</figcaption>
</div>

<div style="text-align:center">
    <img src="https://i.imgur.com/xbTyBm9.png">
    <figcaption>Battery cell zoomed in</figcaption>
</div>

* *Cell's electrodes*. Electrons flow from one electrode, i.e. the anode or negative electrode, to another electrode, i.e. the cathode or positive electrode
    * *Volta's pile*. The anode was the zinc, from which electrons flowed through the wire, i.e. when connected, to the silver, which was the battery cathode

        $\to$ Lots of these cells are stacked to make the total pile and crank up the voltage
* *Electron production and consumption*. There are a couple of chemical reactions going on, i.e. they are reduction-oxidation reaction
    * *Anode*. The electrode reacts with the electrolyte in a reaction which produces electrons, which accumulate at the anode

        $\to$ The anode is oxidised, i.e. loss of electrons
    * *Cathode*. Another chemical reaction occurs simultaneously enabling the cathode to accept electrons

        $\to$ The cathode is reduced, i.e. gain of electrons
* *Materials for electrodes*. The ideal choice for an anode would be a material producing a reaction with a significantly lower, i.e. more negative, standard potential than the material we choose for our cathode

    $\to$ This is to get higher voltage
    * *Explain*. In electrochemical cells, electricity is generated due to the electric potential difference between two electrodes
    * *Consequence*. Electrons will be attracted to the cathode from the anode, with the anode not trying to fight very much
* *Conducting wire*. An easy pathway for the electron flow
* *Overall electrochemical potential*. The difference in standard potential between the electrodes kind of equates to the force, with which electrons will travel between the two electrodes

    $\to$ This determines the cell's voltage

**Increasing a battery's voltage**. Stack several cells together
* *Serial combination of cells*. When cells are stacked in series, it has an additive effect on the battery's voltage

    $\to$ The force, at which the electrons move through the battery, can be seen as the total force as it moves from the anode of the first cell, all the way through however many cells the battery contains, to the cathode of the final cell
* *Parallel combination of cells*. When cells are combined in parallel, in increases the battery's possible current, i.e. the total number of electrons flowing through the cells, not its voltage

**Electrolyte**. A liquid, gel, or a solib substance, which must be able to allow the movement of charged ions
* *Purpose*. Electrons have a negative charge, and we are sending the flow of electrons around through our circuit, thus we need a way to balance the charge movement
    
    $\to$ Electrolyte provides a medium, through which charge-balancing positive ions can flow
* *Explain*.
    * As the chemical reaction at the anode produces electrons, to maintain a neutral charge balance on the electrode
        
        $\to$ A matching amount of positively charged ions are also produced
    * These don’t go down the external wire (that’s for electrons only!) but are released into the electrolyte
    * At the same time, the cathode must also balance the negative charge of the electrons it receives
        
        $\to$ The reaction that occurs here must pull in positively charged ions from the electrolyte
        
        >**NOTE**. Alternatively, it may also release negative charged ions from the electrode into the electrolyte

**Semi-permeable barrier**. If all the ions released into the electrolyte were allowed to move completely freely through the electrolyte

$\to$ They would end up coating the surfaces of the electrodes and clog the whole system up
* *Solution*. Have some sort of barrier to prevent this from happening

<div style="text-align:center">
    <img src="https://i.imgur.com/QsHmBd8.png">
    <figcaption>Barrier</figcaption>
</div>

**Discharging**. When the battery is being used, we have a situation where there is a continuous flow of electrons (through the external circuit) and positively charged ions (through the electrolyte)

$\to$ If this continuous flow is halted, i.e. if the circuit is open, the charges will pile/build up and the chemical reactions driving the battery will stop

**Flat battery**. As the battery is used, and the reactions at both electrodes chug along, new chemical products are made

$\to$ These reaction products can create a kind of resistance that can prevent the reaction from continuing with the same efficiency
* *Consequence*. When this resistance becomes too great, the reaction slows down
    
    $\to$ The electron tug-of-war between the cathode and anode also loses its strength and the electrons stop flowing, and the battery slowly goes flat

**Recharging a battery**. When we connect an almost flat battery to an external electricity source, and send energy back in to the battery, it reverses the chemical reaction that occurred during discharge

$\to$ This sends the positive ions released from the anode into the electrolyte back to the anode, and the electrons that the cathode took in also back to the anode

<div style="text-align:center">
    <img src="https://i.imgur.com/KBH8WWw.png">
    <figcaption>Battery recharging</figcaption>
</div>

* *Consequence*. The return of both the positive ions and electrons back into the anode primes the system so it’s ready to run again: your battery is recharged

**Degradation of recharging battery**. The process isn’t perfect, however

$\to$ The replacement of the negative and positive ions from the electrolyte back on to the relevant electrode as the battery is recharged isn’t as neat or as nicely structured as the electrode was in the first place
* *Consequence*. Each charge cycle degrades the electrodes just a little bit more, meaning the battery loses performance over time
    
    $\to$ This is why even rechargeable batteries don’t keep on working forever
* *Battery charging and discharging speed*. Over the course of several charge and discharge cycles, the shape of the battery's crystals becomes less ordered
    
    $\to$ This is exacerbated when a battery is discharged/recharged at a high rate
    * *Consequence*. High-rate cycling leads to the crystal structure becoming more disordered, with a less efficient battery as a result.

**References**. https://www.science.org.au/curious/technology-future/batteries

# Appendix
## Discussion
**How water acts as an extremely aggressive solvent and the generation of voltage**. Water is an extremely aggressive solvent

<div style="text-align:center">
    <img src="https://i.imgur.com/kzTHCL0.png">
    <figcaption>Water solvent</figcaption>
</div>

* *Shape of water molecules*. An individual water molecule has a bent shape with a H-O-H bond angle of approximately 105 degrees

    $\to$ Water is thus polar thus having positive and negative partial charges on its ends
    * *Consequence*. 
        * The partial charges attract parts of polar molecules to dissolve them
        * Water does not dissolve nonpolar molecules
* *Functionality of water*. The water molecules will surround each metal ion and forcibly pry it loose from the solid surface, then attack the next, then the next

    $\to$ Like table salt, metals dissolve extremely rapidly
* *Problem with metal*. If we place metals in water, they should completely dissolve within minutes, but they don’t
    * *Metal dissolvation*. When the aggressive water molecules corrode a metal surface, they pull out each metal atom, but metal atom is positive charged

        $\to$ Whenever metal dissolves in water, the water is always transposting excess protons out of the solid metal
        * *Conclusion*. Metals are positive matter embedded in an electron cloud, and when metals dissolve in water, only positive particles are moving away from the metal surface into the water

            $\to$ The water becomes very strongly positive, and the metal strongly negative, and the capacitor dielectric between them is only a few atoms wide
    * *Why metal can sit under water for years without dissolving*. When water steals positive atoms from the solid metal
        * The water becomes a positive-charged conductor, which pushes backwards on the dissolving positive atoms

            $\to$ The positive atoms are prevented from leaving the metal
        * The metal is equally negative, pulling the positive metal atoms back into the metal surface
* *Generation of voltage*. Inside the surface layer between the metal and water, a voltage exists, and an immense electric field appears

    $\to$ Several volts over nanometers, many megavolts per meter
    * *Attraction and repulsion forces*. Any attraction and repulsion forces inside the layer are immense

        $\to$ Positive charges are repelled back into the meta, and the corrosion is halted
* *Overall process of corrosion*. 
    1. When metal first contacts water, the metal and water are uncharged and the corrosion happens easily, before the water becomes charged and the electric field appears
    2. Within milliseconds, the voltage rises to a high limit, and the attraction-repulsion forces form an electrical barrier halting further corrosion
* *How battery voltage is located*. The voltage comes from an extremely thin layer, i.e. the flat plane where the water is touching the flat metal surface of each battery plate
    * *Battery cell structure*. Each complete batery cell is always made from two totally separate components, i.e. two different metal surfaces in two different locations, each connected to the other by some conductive water
        * *Explain*. When the two plates are the same type of metal, the voltages must be equal and opposite

            $\to$ The voltages fight each other to a standstill, and the battery will not work
        * *Consequence*. If we use two different metal plates, each creates a different voltage w.r.t the water

            $\to$ The voltage between metal plates will not be zero
    * *Example*. If one metal creates 4V, and the other creates 7V, the battery output voltage will be 3V
    * *Flow of electricity*. When the battery is connected to a load, one plate dissolves and delivers energy, and the other un-dissolves and sucks in energy

        $\to$ Most of the chemical energy stored in a metal plate moves from the dissolving plate to the other

**Examples with $\ce{Zn,Cu,H_2SO_4}$**.

<div style="text-align:center">
    <img src="https://i.imgur.com/dsqiLYe.png">
    <figcaption>Illustration</figcaption>
</div>

* *Embed $\ce{Zn}$ and $\ce{Cu}$ (without connecting wire) into dilute $\ce{H_2SO_4}$*. $\ce{Zn + H_2SO_4 \to ZnSO_4 + H_2}$
    * *Phenomenon*. $\ce{Zn}$ is corroded and some gas appears
* *Embed $\ce{Zn}$ and $\ce{Cu}$ (with connecting wire) into dilute $\ce{H_2SO_4}$*.
    
    $$\ce{2Zn + H_2SO_4 \to Zn_2SO_4 + 2H^+ + 2e^-} \text{ (cathode)},\quad \ce{2H^+ + 2e^- \to H_2} \text{ (anode)}$$
    
    * *Phenomenon*. $\ce{Zn}$ is corroded but gas appears only at the $\ce{Cu}$ side
* *Additional information*. Ionization energy of $\ce{Zn}$ is 9.3942, while ionization energy of $\ce{Cu}$ is 7.7264

**Can ions exist independently of their oppositely charged pair**. In solution, oppositely charged ions are freely moving independently of ions of the opposite charge
* *Explain*.  A sodium ion and a chloride ion in water solution, for example, will spend a few nanoseconds in proximity, gazing at each other wistfully
    
    $\to$ Then the mass action of so many water molecules, each of which is attracted to the ions because of water’s dipole, will probably drag the erstwhile lovers apart
* *Conclusion*. The fact that ions can move freely within solution is similar to how water corrode metals

**Why electrons cannot go from anode to cathode directly via the electrolyte**. 