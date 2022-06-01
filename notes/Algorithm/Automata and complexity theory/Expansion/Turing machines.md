<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [On computable numbers, with an application to the Entscheidungsproblem](#on-computable-numbers-with-an-application-to-the-entscheidungsproblem)
  - [Computing machine - Turing machine](#computing-machine---turing-machine)
  - [Definitions](#definitions)
  - [Examples of computing machines](#examples-of-computing-machines)
  - [Abbreviated tables](#abbreviated-tables)
  - [Enumeration of computable sequences](#enumeration-of-computable-sequences)
  - [The universal computing machine](#the-universal-computing-machine)
- [Appendix](#appendix)
  - [Concepts](#concepts)
  - [Stanford's lecture](#stanfords-lecture)
  - [References](#references)
<!-- /TOC -->

# On computable numbers, with an application to the Entscheidungsproblem
**Computable numbers**. Real numbers, whose expressions as a decimal are calculable by finite means
* *Computable objects*. It is almost equally easy to define and investigate computable functions of an integral variable, or a real or computable variable, computable predicates, etc.
* *Formal definition*. A number is computable if its decimal can be written down by a machine
* *Motivation*. Human memory is necessarily limited

## Computing machine - Turing machine
**Computing machine**. Consider comparing a man in the process of computing a real number to a machine, which is only capable of a finite number of conditions $q_1,\dots,q_R$
* *m-configurations*. The conditions $q_1,\dots,q_R$, i.e Turing state
    * *Interpretation*. An m-configuration can be seen as an instruction, which the machine is capable of
        * *Reference*. https://en.wikipedia.org/wiki/Turing_machine
        
        >**NOTE**. The machine m-configuration and its state of progress are strongly distinguished by Alan Turing (1936)

* *Memory tape*. The machine is supplied with a tape, i.e. the analogue of paper, running through it
    * *Tape structure*. The tape is divided into sections, i.e. squares, each capable of bearing a symbol
* *Tape scanning*.
    * *Scanned square*. At any moment, there is just one square $r$-th bearing the symbol $\sigma(r)$, which is in the machine
        * *Scanned square*. The square $r$-th
        * *Scanned symbol*. The symbol on the scanned square
    * *Scanning restriction*. The scanned symbol is the only one, of which the machine is directly aware

>**NOTE**. By altering its m-configuration, the machine can effectively remember some of the symbols, which it has scanned previously

* *Computation of real numbers*.
    * *Machine behavior*. At any moment, the behavior is determined by the m-configuration $q_n$ and the scanned symbol $\sigma(r)$
    * *Machine configuration*. $(q_n,\sigma(r))$, which determines the possible behavior of the machine, e.g.
        * In some configurations, in which the scanned square is blank, the machine writes down a new symbol on the scanned square
        * In other configurations, it erases the scanned symbol
        * In other configurations, it may change the square, which is being scanned, but only by shifting it one place to right or left
            * *Explain*. Moving the read/write heads one step to the left or right
        * In addition to these operations, the m-configuration may be changed
    * *Computation of real numbers*.
        * Some of the symbols written down will form the sequence of figures, which is the decimal of the real number being computed
        * The others are just rough notes to assist the memory, and these notes will be liable to erasure

## Definitions
**Automatic machines (a-machine)**. A machine is automatic if at each stage, the motion of the machine is completely determined by the configurations
* *Choice machine (c-machine)*. A machine, whose motion is only partially deteremined by the configuration, hence the use of the word "possible"
    * *Explain*. When the machine reaches one of the ambiguous configurations, it cannot go until some arbitrary choice has been made by an external operator

        $\to$ This is the case if we were using machines to deal with axiomatic systems

>**NOTE**. In this paper, Turing deals only with a-machine, hence often omit the prefix `a-`

**Computing machine**. 
* *Computing machine*. An a-machine, which prints two kinds of symbols, i.e.
    * *Figures*. The first kind, which consists entirely of `0` and `1`
    * *Symbols of the second kind*. The second kind, i.e. other symbols
* *Sequence computed by the machine*. If the machine is supplied with a blank tape, and set in motion, starting from the correct initial m-configuration

    $\to$ The subsequence of the symbols printed by it, which are of the first kind, is the sequence computed by the machine
    * *Number computed by the machine*. The real number, whose expression as a binary decimal is obtained by prefacing the computed sequence by a decimal point

        $\to$ The machine only computes the fractional part of any real number
* *Complete configuration*. At any stage of motion of the machine, the complete configuration at the stage is described by
    * The number of scanned square
    * The complete sequence of all symbols on the tape
    * The m-configuration of the machine

**Circular and circle-free machines**.
* *Circular machine*. A computing machine, which never writes down more than a finite number of symbols of the first kind
    * *Explain*. A machine is circular if
        * It reaches a configuration, from which there is no possible move, or
        * It goes on moving, and possibly printing symbols of the second kind only
* *Circle-free machine*. A computing machine which is not circular

**Computable sequences and numbers**.
* *Computable sequence*. A sequence, which can be computed by a circle-free machine
* *Computable number*. A number, which differs by an integer from the number computed by a circle-free machine

## Examples of computing machines
**Example 1**. Consider a machine, which can be constructed to compute the sequence `010101...`
* *m-configurations*. `b`, `c`, `f`, `e`
* *Printable symbols*. `0` and `1`
* *Basic moves*. 
    * $R$ means "machine moves so that it scans the square immediately on the right of the one it was scanning previously", so does $L$
    * $E$ means "the scanned symbol is erased"
    * $P$ means printing a symbol
* *Machine behavior*. Starting in the m-configuration `b` with a blank tape, the machine behaves as follows

    | m-config | symbol | operations | final m-config |
    | --- | --- | --- | --- |
    | `b` | None | $P0,R$ | `c` |
    | `c` | None | $R$ | `e` |
    | `e` | None | $P1,R$ | `f` |
    | `f` | None | $R$ | `b` |

    * *Explain*. When the second column is left blank, the behavior of the third and fourth columns applies for any symbol and for no symbol

**Example 2**. Consider a machine, which can be constructed a compute the sequence `001011011101111011111...`
* *m-configurations*. `o`, `q`, `p`, `f`, `b`
* *Printable symbols*. `e`, `x`, `0`, and `1`
* *Memory tape initial content*. 
    * The first three symbols on the tape be `ee0`, i.e. other figures follow on alternate squares
    * On the intermediate squares, nothing is printed but `x`, which serve to keep the place for us and are erased when we have finished with them
    * In the sequence of figures on alternate squares, there will be no blanks
* *Machine behavior*.

    | m-config | symbol | operations | final m-config |
    | --- | --- | --- | --- |
    | `b` | blank | $Pe,R,Pe,R,R0,R,R,P0,L,L$ | `o` |
    | `o` | `1` | $R,Px,L,L,L$ | `o` |
    | `o` | `0` | None | `q` |
    | `q` | `0` or `1` | $R,R$ | `q` |
    | `q` | None | $P1,L$ | `p` |
    | `p` | `x` | $E,R$ | `q` |
    | `p` | `e` | $R$ | `f` |
    | `p` | None | $L,L$ | `p` |
    | `f` | `0` or `1` | $R,R$ | `f` |
    | `f` | None | $P0,L,L$ | `o` |

* *Example*. The complete comfigurations below are described by writing down the sequence of symbols, which are on the tape, with the m-configuration written below the scanned symbol

    >**NOTE**. The successive complete configurations are separated by colons

    <div style="text-align:center">
        <img src="https://i.imgur.com/flKjDzb.png">
        <figcaption>Example of complete configurations</figcaption>
    </div>

* *String representation of machine behavior table*. `b : e e o 0   0 : e e q 0   0: ...`

    $\to$ This form is easy to follow, but only for theoretical purposes
* *Convention of writing figures only on alternate squares*. Very useful, as claimed by Alan Turing
    * *F-squares*. The sequence of alternate squares
        * *Symbol marking*. If a symbol $\beta$ is on an F-square $S$, and a symbol $\alpha$ is on the E-square next on the right of $S$

            $\to$ $S$ and $\beta$ are said to be marked with $\alpha$
    * $E-squares$. The other sequence, i.e. symbols in this sequence will be liable to erasure

        $\to$ Symbols on F-squares form a continuous sequence
        * *Number of E-squares between each pair of F-squares*. No need to be more than one
            * *Explain*. An apparent need of more E-squares can be satisfied by having a sufficiently rich variety of symbols capable of being printed on E-squares
    
    >**NOTE**. There are no blanks until the end is reached

## Abbreviated tables
**Brief**. There are certain types of process used by nearly all machines
* *Commonly used processes*.
    * Copying down sequences of symbols
    * Comparing sequences
    * Erasing all symbols of a given form

**Skeleton tables**. When such commonly used processes are concerned, we can abbreviate the tables of the m-configurations considerably using skeleton tables
    * *Idea*. From the m-coniguration $f(\mathcal{C}, \mathcal{B}, \alpha)$
        * The machine finds the symbol of form $a$, the m-configuration then becomes $\mathcal{C}$
        * If there is no $a$ then the m-configuration becomes $\mathcal{B}$
    * *m-configuration function (or m-function)*. The function $f(\mathcal{C}, \mathcal{B}, \alpha)$

        $\to$ This is the some of the first notion of functions, as in programming languages
        * *Expressions admissible for substitution in an m-function*. m-configurations and symbols of the machine
    * *Nested m-function*. We can use nested m-function, i.e. example 2 and 3 on skeleton tables in A. M. Turing's 1936 paper, to describe more sophisticated computing machines 
* *Enumeration of m-configurations*. We should give names to the m-configurations of the machine, mostly expressed in terms of m-functions

    $\to$ We then should give skeleton tables
* *Obtaining complete table for the m-configurations of the machine*. Obtained by repeated substitution in the skeleton tables

**Skeleton tables and programming language**. Skeleton tables and m-functions can be understood as one of the programming language of TMs

$\to$ The resulting machine behavior can be understood as computer software

## Enumeration of computable sequences
**Computable sequence $\gamma$**. Determined by a description of a machine which computes $\gamma$

>**NOTE**. Any computable sequence is capable of being described in terms of such a machine

* *Problem of interest*. Put the skeleton tables describing machine behavior into a standard form

    $\to$ We can use the method as given by A. M. Turing in his 1936 paper (page 240)
* *Standard description (SD) of a machine*. The serialized representation of a machine's skeleton table
* *Description number (DN) of a machine*. The integer obtained by replacing symbols in the SD by integers

    $\to$ The DN determines the SD and the structure of the machine uniquely
    * *Notation*. $\mathcal{M}(n)$ describes the machine, whose DN is $n$
    * *Correspondence between DNs and TMs*. The computable sequences and numbers are enumerable, i.e. 
        * To each computable sequence, there corresponds at least one description number
        * To no description number, does there correspond more than one computable sequence
* *Satisfactory number*. The DN of a circle-free machine

## The universal computing machine
**Brief**. It is possible to invent a machine, which can be used to compute any computable sequence
* *Explain*. If this machine $\mathcal{U}$ is supplied with a tape on the beginning of which is written the SD of some computing machine $\mathcal{M}$

    $\to$ $\mathcal{U}$ will compute the same sequence as $\mathcal{M}$

>**NOTE**. This section explains in outline the behavior of the machine

**Idea**.
* *Storing configurations of $\mathcal{M}$* Have a machine $\mathcal{M}'$ writing down on the F-squares the successive complete configurations of $\mathcal{M}$

    $\to$ If $\mathcal{M}$ can be constructed, then so can $\mathcal{M}'$
* *Manner of operation of $\mathcal{M}'$*. Can be made to depend on having the rules of operation of $\mathcal{M}$ written somewhere within itself

    $\to$ Each step could be carried out by referring to these rules
    * *Consequence*. If the rules can be taken out and exchanged
        
        $\to$ We have something very akin to the universal machine
* *Printing figures with $\mathcal{M}'$*. $\mathcal{M}'$ can print, between each successive pair of complete configurations, the figures which appear in the new configuration but not in the old

# Appendix
## Concepts
**Axiomatic system**. Any set of axioms, from which some or all axioms can be used in conjunction to logically derive theorems

**Importance of Turing' paper**. It influenced the architecture used by most of the current computers, the von Neumann architecture
* *Universal Turing Machine*. The most significant contribution of the paper
    * *Universal Turing Machine*. A regular Turing Machine with a special configuration that makes it unique
        
        $\to$ This machine has such a configuration that can replicate any other Turing Machine
    * *TM replication by universal TM*. 
        1. Write down the configuration of the TM we want to duplicate in the tape
        2. The UTM reads the tape and then keeps going depending on what it is reading
* *Programming language*. To write down the configuration in the tape, Alan Turing came up with a language to encode the configuration
    
    $\to$ With this language, we would be able to encode the tape of every machine
* *Consequence*. An UTM can do anything that the others can

    $\to$ This idea of storing the configuration in the tape is one of the main contributions to Computer Science
* *Conclusion*. Having a universal configuration that can adapt makes it possible for our computers to do many things
    * *Explain*. By storing the instructions, i.e. the software, in the tape, instead of having them implemented directly in the machine

**Computably enumerable set**. A set $S$ of natural numbers, where there is a partial computable function, whose domain is exactly $S$
* *Other definition*. A set $S$ is enumerable if there is a one-to-one mapping from $S$ to a finite subset of $\mathbb{N}$ 
* *Computable function*. A function is computable if its value can be obtained by an effective procedure
* *Partial computable function*. A partial function $f:\mathbb{N}^k\to \mathbb{N}$, where
    * If $f(\mathbf{x})$ is defined, then the program will terminate on $\mathbf{x}$ with $f(\mathbf{x})$ stored in the computer memory
    * If $f(\mathbf{x})$ is undefined, then the program never terminates on $\mathbf{x}$
* *Conutable and computably enumerable*. All subsets of the natural numbers are countable but not all of them are enumerable
    * *Proof*. There are uncountably many different subsets of $\mathbb{N}$ but only countably many Turing machines that could act as enumerators

## Stanford's lecture
**Turing machines (TMs) versus DFAs**.
* TMs can both write to and read from the tape
* The head can move left and right
* The input does not have to be read entirely, and the computation can continue further, even forever, after all input has been read
* Accept and reject takes immediate effect

**Formal definition of Turing machine**. A Turing machine is a 7-tuple $T=(Q,\Sigma,\Gamma,\delta,q_0,q_\text{accept},q_\text{reject})$, where
* $Q$ is a finite set of states
* $\Sigma$ is the input alphabet, where $\varepsilon\not\in\Sigma$
* $\Gamma$ is the tape alphabet, where $\varepsilon\in\Gamma$ and $\Sigma\subseteq\Gamma$
* $\delta:Q\times\Gamma\to Q\times\Gamma\times\{L,R\}$
* $q_0\in Q$ is the start state
* $q_\text{accept}\in Q$ is the accept state
* $q_\text{reject}\in Q$ is the reject state, and $q_\text{reject}\neq q_\text{accept}$

**Acceptance and rejection**.
* *Yielding configurations*. Let $C_1$ and $C_2$ be complete configurations of the TM $M$

    $\to$ $C_1$ yields $C_2$ if, after running $M$ in $C_1$ for one step, $M$ is then in configuration $C_2$
* *Acceptance of strings*. Consider a string $w\in\Sigma^*$ and a TM $M$, then $M$ accepts $w$ if there are complete configurations $C_0,\dots,C_k$ s.t.
    * $C_0=q_0 w$
    * $C_i$ yields $C_{i+1}$ for $i=0,\dots,k-1$
    * $C_k$ contains the accepting state $q_\text{accept}$
* *Recongition of languages*. $M$ recognizes a language $L$ if $M$ accepts all and only those strings in $L$

    $\to$ $L$ is recognizable or recursively enumerable if some TM recognizes $L$
* *Decision of a language*. A TM $M$ decides a language $L$ if $M$ accepts all strings in $L$, and rejects all strings not in $L$

    $\to$ $L$ is decidable or recursive if some TM decides $L$
* *Difference between recognition and decision*. Deciders always terminate, while recognizers can run forever without deciding

**Multi-tape Turing machine**. Consider a mutli-tape TM with $k$ tapes, then the state transition function is given as

$$\delta: Q\times\Gamma^k\to Q\times\Gamma^k\times\{L,R\}^k$$

* *Equivalence to single-tape TM*. Every multi-tape TM can be transformed into a single tape TM

**Nondeterministic TMs (NTMs)**. An NTM's next state is not completely determined by its action and the current symbol it sees
* *Formal definition*. The state transition function $\delta$ is now given as

    $$\delta\subseteq (Q\times\Sigma)\times (Q\times \Sigma\times\{L, R\})$$

* *Equivalence to DTMs*. Every NTM can be transformed into a single-tape TM, which recognizes the same language

**Universality of Turing machines**. 
* *Universality of Turing machines*. There is a universal Turing machine (UTM) $U$, with
    * *Inputs*. The code of an arbitrary TM $M$, and an input string $w$
    * *Outputs*. $U(M,w)$ accepts if $M(w)$ accepts
* *Proof*. Refer to A. M. Turing's 1936 paper for the construction of such an UTM

>**NOTE**. This is a fundamental property, i.e. TMs can run their own code

>**NOTE**. DFAs and NFAs do not have this property

## References
* https://plato.stanford.edu/entries/turing-machine/#DefiTuriMach
* https://www.astro.puc.cl/~rparra/tools/PAPERS/turing_1936.pdf
* http://theory.stanford.edu/~trevisan/cs154-12/turing-machines-1.pdf