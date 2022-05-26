<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Expansion](#expansion)
  - [Examples of Markov chain](#examples-of-markov-chain)
- [Appendix](#appendix)
  - [Concepts](#concepts)
<!-- /TOC -->

# Expansion
## Examples of Markov chain
**Ehrenfest chain**. This chain originated in physics as a model for two cubical volumes of air connected by a small hole
* *Mathematical model*. Consider two urns, in which there are $N$ balls
    
    $\to$ We pick one of the $N$ balls at random and move it to the other urn
* *Assumptions*.
    * $X_n$ is the number of balls in the left urn after the $n$-th draw
* *Markov property of $X_n$* The only relevant information for guessing $X_{n+1}$ from the observed $X_0,\dots,x_n$ is $X_n$, i.e.

    $$P(X_{n+1}=i+1|X_n=i,\dots,X_0=i_0)=(N-i)/N$$

* *State transition matrix*. 
    
    $$p(i,j)=\begin{cases}(N-i)/N & j=i+1\\ i/N & j=i-1\\ 0 & \text{otherwise}\end{cases}$$

* *Prevention of convergence of $p^n$*. Consider an Ehrenfest chain with an add number of balls in the left urn
    * *Observation*. No matter whether we add or subtract one, the result will be an even number

        $\to$ The similar thing happens when the number is even
    * *Consequence*. It is impossible to be back where we started, after an odd number of steps

        $\to$ This prevents the convergence of $p^n$

**Galton-Watson branching process**. These processes arose from Francis Galton’s statistical investigation of the extinction of family names
* *Scenario*. Consider a population, in which each individual in the $n$-th generation independently gives birth
    
    $\to$ They produces $k$ children, who are members of generation $n + 1$, with probability $p_k$
    
    >**NOTE**. In Galton’s application only male children count, since only they carry on the family name

* *Assumptions*.
    * $X_n$ is the number of individuals in generation $n$
    * $Y_1,Y_2,\dots$ are independent random variables with $P(Y_m=k)=p_k$

        $\to$ $Y_i$ is the number of children produced by individual $i$
* *State transition matrix*. 
    
    $$p(i,j)=\begin{cases}P(\sum_{k=1}^i Y_k=j) & i>0\land j>0\\ 1 & i=j=0\\ 0 & \text{otherwise}\end{cases}$$

* *Question of interest*. What is the probability that the line of a man becomes extinct?, i.e. the branching process becomes absorbed at 0?

**Wright-Fisher model**. Consider a population of $N/2$ diploid individuals, or of $N$ haploid individuals

$\to$ We consider a fixed population of $N$ genes that can be one of two types, i.e. $A$ or $a$
* *Constraints*. The population at time $n + 1$ is obtained by drawing with replacement from the population at time $n$
    * Generations are non-overlapping, i.e. all individuals reproduce and die simultaneously
    * New individuals are formed by random sampling with replacement of gametes produced by the parents
* *Assumptions*.
    * $X_n$ is the number of A alleles at time $n$
* *State transition matrix of $X_n$*. Consider $N$ independent trials with probability of producing $A$ is $i/N$

    $$p(i,j)=\binom{N}{j} (\frac{i}{N})^j (1-\frac{i}{N})^{N-j}$$

* *Questions of interest*.
    * Starting from $i$ of the $A$ alleles, and $N-i$ of the $a$ alleles
    
        $\to$ Find the probability that the population fixates in the all $A$ state
    * Does the genetic composition settle down to an equilibrium distribution as time $t\to\infty$

# Appendix
## Concepts
**Chromosomes**. A long DNA molecule with part or all of the genetic material of an organism

$\to$ Chromosomes are linear structures with genes located at specific sites, i.e. loci, along them
* *Diploid and haploid*.
    * *Diploid individuals*. Have two copies of each of their chromosomes
    * *Haploid individuals*. Have one copy of each of their chromosomes