<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Impossibility of distributed consensus with one faulty process](#impossibility-of-distributed-consensus-with-one-faulty-process)
  - [Introduction](#introduction)
  - [Consensus protocols](#consensus-protocols)
  - [Main result](#main-result)
- [Appendix](#appendix)
  - [References](#references)
<!-- /TOC -->

# Impossibility of distributed consensus with one faulty process
**Brief**. This is an example of application of DFAs in computer science

## Introduction
**Reaching agreement among remote processes**. One of the most fundamental problems in distributed computing

$\to$ This is at the core of many algorithms for distributed data processing, distributed file management, and faulttolerant distributed applications
* *Transaction commit problem*. A well-known form of the problem arising in distributed database systems
    * *Objective*. Have all the data manager processes, which have participated in the processing of a particular transaction, to agree on whether to install the transaction’s results in the database or to discard them
    * *Consequence*. All data managers must make the same decision to preserve the consistency of the database
* *Issues*. Real systems are subject to a number of possible faults, e.g. 
    * Orocess crashes, network partitioning, and lost, distorted, or duplicated messages, or
    * Byzantine types of failure, in which faulty processes might go completely haywire, perhaps even sending messages according to some malevolent plan
* *Consequence*. An agreement protocol, which is reliable as possible in the presence of such faults, is desired
    
    >**NOTE**. Any protocol can be overwhelmed by faults, which are too frequent or too severe
    >
    >$\to$ The best a protocol can do is to tolerant to a prescribed number of faulty processes

**Key points of the paper**. Show that no completely asynchronous consensus protocol can tolerate even a single unannounced process death
* *Assumptions*.
    * There is no Byzantine failure
    * The message system is reliable, i.e. it delivers all messages correctly and exactly once
    * Processing is completely asynchronous, i.e. we make no assumptions about 
        * The relative speeds of processes, or
        * The delay time in delivering a message
    * Processes do not have access to synchronized clocks
        
        $\to$ Algorithms based on time-outs, for example, cannot be used
    * The ability to detect the death of a process is not assumed
        
        $\to$ It is impossible for one process to tell whether another has died, or is running slowly
    * Some process eventually make a decision
        
        >**NOTE**. Any algorithm of interest would require that all nonfaulty processes make a decision

* *Requirements on consensus*. All nonfaulty processes that make a decision are required to choose the same value
* *Idea*. Even with these assumptions, the stopping of a single process at an inopportune time can cause any distributed commit protocol to fail to reach agreement
    
    $\to$ This problem has no robust solution without further assumptions about the computing environment, or still greater restrictions on the kind of failures, to be tolerated

>**NOTE**. Our impossibility result applies to even a very weak form of the consensus
problem


**Process modeling as a DFA**. Processes are modeled as automata, with possibly infinitely many states, that communicate by means of messages
* *Initial and final states*.
    * *Initial state*. Every process starts with an initial value in $\{0, 1\}$
    * *Final state*. A nonfaulty process decides on a value in $\{0, 1\}$ by entering an appropriate decision state
* *Process behavior in one atomic step*. A process can 
    * Attempt to receive a message
    * Perform local computation on the basis of whether or not a message was delivered to it, and if so, which one
    * Send an arbitrary but finite set of messages to other processes
        * *Atomic broadcast capability*. This is assumed, i.e. a process can send the same message in one step to all other processes
            
            $\to$ Such a broadcast is done with the knowledge that if any nonfaulty process receives the message, then all the nonfaulty processes will
* *Asynchronization of processes*. Every message is eventually delivered as long as the destination process makes infinitely many attempts to receive
    
    >**NOTE**. Messages can be delayed, arbitrarily long, and delivered out of order

* *Asynchronous commit protocols in current use*. Have a window of vulnerability
    
    $\to$ It follows from our impossibility result that every commit protocol has such a window, confirming a widely believed tenet in the folklore
    * *Window of vulnerability*. An interval of time during the execution of the algorithm, in which the delay or inaccessibility of a single process can cause the entire algorithm to wait indefinitely

## Consensus protocols
**Consensus protocol $P$**. An asynchronous system of $N\geq 2$ processes

**Process modeling as a DFA**.
* *Process structure*. Each process $p$ is like a Turing machine, with 
    * A one-bit input register $x_p$
    * An output register $y_p$ with values in $\{b, 0, 1\}$
    * An unbounded amount of internal storage
* *Internal state of process*. Consist of
    * The values in the input and output registers
    * The program counter and internal storage
* *State space*.
    * *Initial internal state*. Initial states prescribe fixed starting values for all but the input register
        * *Explain*. The output register starts with value $b$
    * *Decision states*. The states, in which the output register has value $0$ or $1$
* *State transition function*. $p$ acts deterministically according to a transition function
    * *Transition function and decision state*. The transition function cannot change the value of the output register once the process has reached a decision state
        
        $\to$ The output register is write-once
* *Deterministic of consensus protocol $P$*. The system $P$ is specified by 
    * The transition functions associated with each of the processes, and
    * The initial values of the input registers

**Process communication**. Processes communicate by sending each other messages
* *Message structure*. A pair $(p, m)$, where 
    * $p$ is the name of the destination process
    * $m$ is a message value from a fixed universe $M$
* *Message buffer*. A multiset of messages, which have been sent but not yet delivered, maintain by the message system
* *Message-related operations*. 
    * *$\text{send}(p, m)$*. Place $(p, m)$ in the message buffer
    * *$\text{receive}(p)$*. 
        * Delete some message $(p, m)$ from the buffer and returns $m$, i.e. $(p, m)$ is delivered, or 
        * Returns the special null marker $\emptyset$ and leaves the buffer unchanged
* *Nondeterministicity of the message system*. The message system acts nondeterministically
    * *Assumption*. If $\text{receive}(p)$ is performed infinitely many times
        
        $\to$ Every message $(p, m)$ in the message buffer is eventually delivered
    * *Explain*. The message system is allowed to return $\emptyset$ a finite number of times in response to $\text{receive}(p)$, even though a $(p, m)$ is in the buffer

**System configuration**.
* *Configuration of the system*. Consist of the internal state of each process,
and the contents of the message buffer
* *Initial configuration*. Each process starts at an initial state and the message buffer is empty
* *Configuration transition*. A step takes one configuration to another and consists of a primitive step by a single process $p$
    * *Phases of a step*. Consider a configuration $C$, then a step occurs in two phases
        1. $\text{receive}(p)$ is performed on the message buffer in $C$ to obtain a value $m \in M \cup\emptyset$
        2. Depending on $p$’s internal state in $C$ and on $m$, $p$ enters a new internal state and sends a finite set of messages to other processes
* *Event*. Since processes are deterministic, the step is completely determined by the pair $e = (p, m)$, i.e. an event
    * *Interpretation*. Event $(p,m)$ indicates the receipt of $m$ by $p$
    * *Resulting configuration of an event $e$*. $e(C)$, i.e. $e$ can be applied to $C$
    
    >**NOTE**. The event $(p, \emptyset)$ can always be applied to $C$, so it is always possible for a process to take another step

* *Schedule from $C$*. A finite or infinite sequence $\sigma$ of events, which can be applied, in turn, starting from $C$
    * *Run*. The associated sequence of steps of a schedule
* *Reachable and accessible configurations*
    * *Reachable configuration*. If $\sigma$ is finite, the resulting configuration $\sigma(C)$ is said to be reachable from $C$
    * *Accessible configuration*. A configuration reachable from some initial configuration

**Commutavitity of schedules**.
* *Assumptions*.
    * $C$ is a configuration
    * $\sigma_1,\sigma_2$ are schedules, where $\sigma_1(C)=C_1$ and $\sigma_2(C)=C_2$
* *Conclusion*. If the sets of processes taking steps in $\sigma_1$ and $\sigma_2$ are disjoint, then $\sigma_1(C_2)=\sigma_2(C_1)=C_3$

**Correctness of a consensus protocol**.
* *Decision value of a configuration*. $C$ has decision value $v$ is some process $p$ is in a decision state $y_p=v$

    >**NOTE**. Only nonfaulty processes can enters a decision state, as given previously

* *Faulty process*. $p$ is nonfaulty if it takes infinitely many steps, and is faulty otherwise
* *Admissible and deciding runs*.
    * *Admissible run*. A run is admissible if at most one process is faulty, and all messages sent to nonfaulty processes are eventually received
    * *Deciding run*. A run is deciding if some process reaches a decision state in that run
* *Admissible without deciding runs*. A run, which is admissible, i.e. only one processor failure and eventual delivery of every message, but is not a deciding run, i.e. no processor eventually decides
* *Partially correct consensus protocol*. $P$ is partially correct if
    * No accessible configuration has more than one decision value, and
        * *Explain*. Processes must produce the same output value
    * For each $v\in\{0,1\}$, some accessible configuration has decision value $v$
        * *Explain*. Every produced output must be valid
* *Totally correct consensus protocol*. $P$ is totally correct in spite of one fault if
    * $P$ is partially correct, and
    * Every admissible run is a deciding run
        * *Explain*. Every process must eventually provide output

## Main result
**Bivalent and univalent configurations**. Consider the set $V$ of decision values of configurations reachable from $C$
* $C$ is bivalent if $|V|=2$
* $C$ is univalent if $|V|=1$, i.e. 0-valent or 1-valent accordingly

**Adjacent configurations**. $C_1$ and $C_2$ are adjacent if they differ only in the initial value $x_p$ of a process $p$

**Lemma**. Consider $P$ is a consensus protocol, which is totally correct in spite of one fault, then $P$ has a bivalent initial configuration
* *Proof*. Proof by contradiction
    * Assuming that the lemma does not hold, then following from the definition of partially correct consensus protocol

        $\to$ $P$ must have both 0-valent and 1-valent configurations
    * Since any pair of initial configurations are connected by a set of adjacent configurations

        $\to$ There must be a 0-valent $C_0$ adjacent to a 1-valent $C_1$, where $C_0$ and $C_1$ differs at the internal state of some process $p$
    * Due to the definition of totally correct consensus protocol, assume that $p$ is faulty

        $\to$ Consider some admissble deciding run from $C_0$, where $p$ takes no steps, and let $\sigma$ be the associated schedule
    * $\sigma$ can be applied to $C_1$ also, and corresponding configurations in the two runs are identical, except for the faulty process $p$

        $\to$ Eventually, both runs reach the same decision value, by the definition of partially correct consensus protocol
    * Hence, if the decision value is 1, then $C_0$ is bivalent, otherwise $C_1$ is bivalent

        $\to$ This violates the initial assumption

**Lemma**.
* *Assumptions*.
    * $P$ is a consensus protocol, which is totally correct in spite of one fault
    * $C$ is a bivalent configuration of $P$
    * $e=(p,m)$ is an event applicable to $C$
    * $\mathcal{C}$ is the set of configurations reachable from $C$ without applying $e$
    * $\mathcal{D}=e(\mathcal{C})=\{e(E):E\in\mathcal{C}\land e\text{ is applicable to }E\}$
* *Conclusion*. $\mathcal{D}$ contains a bivalent configuration
* *Proof*. $\TODO$

**Theorem**. No consensus protocol $P$ is totally correct in spite of one fault

$\to$ Every partially correct protocol for the consensus problem has some admissible run, which is not a deciding run
* *Proof*. $\TODO$

# Appendix
## References
* https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf