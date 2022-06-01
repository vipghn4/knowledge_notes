<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Church-Turing thesis](#church-turing-thesis)
  - [The thesis and its history](#the-thesis-and-its-history)
    - [Making the informal concept of an effective method precise](#making-the-informal-concept-of-an-effective-method-precise)
- [Appendix](#appendix)
  - [Concepts](#concepts)
  - [References](#references)
<!-- /TOC -->

# Church-Turing thesis
**Brief**. There are various equivalent formulations of the Church-Turing thesis
* *Common formulation*. Every effective computation can be carried out by a Turing machine

>**NOTE**. The Church-Turing thesis is often misunderstood, particularly in recent writing in the philosophy of mind

## The thesis and its history
**The Church-Turing thesis**. Concern the concept of an effective or systematic or mechanical method in logic, mathematics and computer science
* *Effective (or systematic or mechanical) machine*. A method, or procedure, $M$ for achieving some desired result is effective if
    * $M$ is set out in terms of a finite number of exact instructions, where each instruction being expressed by means of a finite number of symbols
    * $M$ will, if carried out without error, produce the desired result in a finite number of steps
    * $M$ can, in practice or in principle, be carried out by a human being unaided by any machinery except paper and pencil
    * $M$ demands no insight, intuition, or ingenuity, on the part of the human being carrying out the method
* *Example*. The truth table test for tautologousness
    * *Explain*. A human being who works by rote could apply this test successfully to any formula of the propositional calculus, given sufficient time, tenacity, paper, and pencils

**Terminology**. Statements that "there is an effective method for achieving such-and-such a result" are commonly expressed by saying that "there is an effective method for obtaining the values of such-and-such a mathematical function"

### Making the informal concept of an effective method precise
**History of the concept of effective method**. The notion of an effective method is an informal one

$\to$ Attempts to characterize effectiveness lack rigor, for the key requirement that the method must demand no insight, intuition or ingenuity is left unexplicated
* *Alan Turing's 1936 paper*. Present a formally exact predicate, with which the informal predicate "can be done by means of an effective method" may be replaced
    
    >**NOTE**. Alonzo Church, working independently, did the same

**Key idea**. The replacement predicates that Turing and Church proposed were, on the face of it, very different from one another

$\to$ These predicates turned out to be equivalent
* *Idea*. Turing and Church, each picks out the same set $S$, of mathematical functions
    * *Church-Turing thesis*. The assertion that $S$ contains every function, whose values can be obtained by a method satisfying the conditions for effectiveness
* *Consequence*. Since it can also be shown that there are no functions in $S$ other than ones whose values can be obtained by a method satisfying the conditions for effectiveness
    
    $\to$ The thesis licences replacing the informal claim
    
    >There is an effective method for obtaining the values of function $f$
    
    by the formal claim
    
    >$f$ is a member of $S$
    
    or by any other formal claim equivalent to this one

**Formal concept proposed by Turing**. The computability by Turing machine
* *Turing's thesis*. A. M. Turing argued for the claim that whenever there is an effective method for obtaining the values of a mathematical function
    
    $\to$ The function can be computed by a Turing machine
    * *Original words by Turing in 1948*. L.C.M.s (logical computing machines: Turing’s expression for Turing machines) can do anything that could be described as "rule of thumb" or "purely mechanical"
* *Converse claim of Turing's thesis*. There are no functions in $S$ other than ones whose values can be obtained by an effective method
    * *Explain*. Since a Turing machine program is a specification of an effective method
        
        $\to$ Without exercising any insight, intuition, or ingenuity, a human being can work through the instructions in the program and carry out the required operations
* *Consequence*. If Turing’s thesis is correct
    
    $\to$ Talk about the existence and non-existence of effective methods can be replaced throughout mathematics, logic and computer science by talk about the existence or non-existence of Turing machine programs

**Proof**. There is currently no proof for this thesis

# Appendix
## Concepts
**Definition of universal machine by A. M. Turing**. A man provided with paper, pencil, and rubber, and subject to strict discipline, is in effect a universal machine

## References
* https://plato.stanford.edu/entries/church-turing/