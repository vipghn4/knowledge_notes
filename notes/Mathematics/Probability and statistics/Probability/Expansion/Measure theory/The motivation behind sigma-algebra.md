<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [The motivation behind $\sigma$-algebras](#the-motivation-behind-sigma-algebras)
  - [Limitations of the classical measure approach](#limitations-of-the-classical-measure-approach)
    - [Proof of Banach-Tarski paradox](#proof-of-banach-tarski-paradox)
  - [$\sigma$-algebra](#sigma-algebra)
    - [Definition of $\sigma$-algebra](#definition-of-sigma-algebra)
    - [Derivation of $\sigma$-algebra](#derivation-of-sigma-algebra)
- [Appendix](#appendix)
  - [Concepts](#concepts)
  - [Discussions](#discussions)
  - [Reference](#reference)
<!-- /TOC -->

# The motivation behind $\sigma$-algebras
## Limitations of the classical measure approach 
**Classical mathematical approach to computing the measure of a body**. These approaches are justified by geometrical or physical intuition
* *Procedure*.
    1. Decompose the body into (finitely many) components
    2. Rearrange the components by rigid motions, e.g. translations or rotations

        $\to$ The measure is presumably unchanged after performing these operations
    3. Reassembling those components to form a simpler body, for which the measure is assumed to be known
    4.  For general curved figures often only lower and upper bounds could be determined by computing the measures of inscribed and circumscribed bodies, e.g. Archimedes’ computation of the area of the circle
        
        $\to$ To obtain the "true measure" we would need to pass to the limit

**Drawback of classical approach**. Once we try to define a measure using an analytical foundation

$\to$ The approach is no longer apparent how a measure should be defined
* *Explain*. The intuition of definining the measure of a body to be the sum of the measures of its components runs into an immediate problem
    * Typically a solid body consists of an uncountably infnite number of points, all of which have measure zero
        
        $\to$ The product $\infty\cdot 0$ is indeterminate
    * Sets with the same number of points need not have the same measure
        * *Example*. Consider intervals $[0, 1]$ and $[0, 2]$, using the bijection $x \to 2x$, we have that
            
            $\to$ They have the same cardinality, but $[0, 2]$ is twice as long as $[0, 1]$
        * *Consequence*. Theoretically, we can decompose $[0, 1]$ into disjoint components, i.e. points in this case
            
            $\to$ We then reassemble them to form the interval $[0, 2]$
    * The issue of the second point arises from the fact that the number of components is uncountably infinite
        
        $\to$ However, even if we restrict ourselves to finitely many components, one runs into trouble
        * *Explain*. Due to Banach-Tarski paradox

**Banach-Tarski paradox**. Given a solid ball $B\subseteq\mathbb{R}^3$, there exists a decomposition of $B$ into finite number $n$ of disjoint subsets

$\to$ These subsets then can be reassembled to different way to yield two identical copies of $B$

>**NOTE**. In fact, $n=5$ would suffice

### Proof of Banach-Tarski paradox
**Proof outline**. Similar to proof of nonmeasurability of Vitali set
1. Find a paradoxical decomposition of the free group in two generators
2. Find a group of rotations in 3D space isomorphic to the free group in two generators
3. Use the paradoxical decomposition of that group and the axiom of choice to produce a paradoxical decomposition of the hollow unit sphere
4. Extend this decomposition of the sphere to a decomposition of the solid unit ball

**A paradoxical decomposition of the free group with two generators**.
* *Free group $F_S$ over a given set $S$*. Consist of all words, which can be built from members of $S$
    * *Example*. Consider $S=\{A,B\}$, then

        $$F_S=\{A,B,AA,AB,BA,BB,\dots\}$$

    * *Group generator*. $A,B$ in the example above
* *Free group with two generators $a$ and $b$*. Consist of all finite strings, which can be formed from $a,a^{-1},b,b^{-1}$ so that
    * No $a$ appears directly next to $a^{-1}$
    * No $b$ appears directly next to $b^{-1}$
* *Group from free group*. The free group and the concatenation operation forms a group $F_2$ with identity element be the empty string $e$
* *Paradoxical decomposition of $F_2$*.
    * *Assumptions*.
        * $S(a)$ is the set of all non-forbidden strings starting with $a$
        * $S(a^{-1}),S(b),S(b^{-1})$ are defined similarly
    * *Observations*. 
        
        $$\begin{aligned}
        F_2&=\{e\}\cup S(a)\cup S(a^{-1})\cup S(b)\cup S(b^{-1})\\
        &= aS(a^{-1})\cup S(a)\\
        &= bS(b^{-1})\cup S(b)
        \end{aligned}$$

    * *Interpretation*. $F_2$ can be cut into pieces, plus $\{e\}$, and two of them shifted by multiplying with $a$ or $b$

        $\to$ They are reassembled as two pieces to make one copy of $F_2$, and the other two make another copy of $F_2$

**Expansion to group of rotations in 3D space**.
* *Group of rotations*.
    * *Assumptions*.
        * $\theta_A,\theta_B$ are irrational multiplies of $\pi$ 
        * $A$ is a rotation of $\theta_A$ radians about the $x$ axis
        * $B$ is a rotation of $\theta_B$ radians about the $z$ axis
    * *Conclusion*. $\mathbf{H}$ is the group of rotations generated by $A and $B$
* *Key observation*. Any sequence of rotations $\omega\in\mathbf{H}$, which is given by a non-trivial word in $A$ and $B$, satisfies $\omega\neq e$

    $\to$ $\mathbf{H}$ is a free group, isomorphic to $F_2$
    * *Explain*. 
        * Since $\theta_A$ and $\theta_B$ are irrational real numbers, there is no $k\in\mathbb{N}$ so that

            $$\exists z\in\mathbb{N},k\theta_A=2z\pi\lor k\theta_B=2z\pi$$
        
        * Hence, we can never rotate back to the original position
* *Paradoxical decomposition of $\mathbf{H}$*. $A$ and $B$ behave like $a$ and $b$ in $F_2$

    $\to$ There is a paradoxical decomposition of $\mathbf{H}$

**Paradoxical decomposition of the hollow unit sphere**.

<div style="text-align:center">
    <img src="https://i.imgur.com/hqlZsti.png">
    <figcaption>Paradoxical decomposition of the hollow unit sphere</figcaption>
</div>

* *Partitioning of unit sphere into orbits*. $\mathbf{H}$ partitions the unit sphere $S^2$ into orbits

    $\to$ Two points $x$ and $y$ belong to the same orbit if and only if

    $$\exists\omega\in\mathbf{H},\omega(x) = y\lor\omega(y)=x$$

* *Axiom of choice*. Used to pick exactly one point from every orbit into a set $M$

    $\to$ Every point in $S^2$ can be reached in exactly one way, by applying the proper rotation from $\mathbf{H}$ to the proper element from $M$
* *Paradoxical decomposition of $S^2$*. 
    * *Assumptions*.
        * $S(a)M=\{s(x):s\in S(a),x\in M\}$
        * $B=a^{-1}M\cup a^{-2}M\cup\dots$ is the set of circular paths directed by $a^{-1}$
    * *Conclusion*. The paradoxical $\mathbf{H}$ yields a paradoxical decomposition of $S^2$ into four pieces
        
        $$\begin{aligned}
        A_1&= S(a) M \cup M\cup B\\
        A_2&= S(a^{-1}) M \setminus B\\
        A_3&=S(b)M\\
        A_4&=S(b^{-1})M
        \end{aligned}$$

        where

        $$aA_2=A_2\cup A_3\cup A_4,\quad bA_4=A_1\cup A_2\cup A_4$$
    
    * *Explain*. Consider rotating $A_2$ and $A_4$ by $a$ and $b$ as given
        * *Reasons for $A_2=S(a^{-1})M\setminus B$*
            * If $A_2=S(a^{-1})M$ then $M\subseteq aA_2$ and $M\subseteq bA_4$, combined with $M\subseteq A_1$

                $\to$ We have triple $M$, which is excessive, since we only want double $S^2$
            * Hence, we need to remove $a^{-1}M$ from $A_2$ by moving it to $A_1$

                $\to$ $a^{-1}M$ exists in both $aA_2$ and $A_1$, which is excessive as well
            * Hence, we need to move $B$ from $A_2$ to $A_1$ to avoid unexpected replication
        * *Reasons for $A_1=S(a)M\cup M\cup B$*. We need two replications of $M$, hence $M\subseteq A_1$ must hold
    * *Consequence*. When $A_2$ and $A_4$ are rotated, we have double what what was had before, i.e. $A_1, A_1, A_2, A_2, A_3, A_3, A_4, A_4$

**Paradoxical decomposition of the solid ball**. By connecting every point on $S^2$ with a half-open segment to the origin

$\to$ The paradoxical decomposition of $S^2$ yields a paradoxical decomposition of the solid ball, minus the point at the ball's center

**Handling poles and center**. In the previous steps, fixed points, i.e. poles, and the ball center were omitted
* *Existence of poles*. Since the paradoxical decomposition of $F_2$ relies on shifting certain subsets

    $\to$ The fact that some points are fixed may cause trouble
* *Countability of poles*. Since any rotation in $S^2$, other than the null rotation, has exactly two fixed points, and since $\mathbf{H}$ is countable

    $\to$ There are countably many points of $S^2$, which are fixed by some rotation in $\mathbf{H}$
* *Analogy*. Consider a hotel with countably infinitely many rooms, where one room $n$ is empty

    $\to$ By taking every guest from room $n+1,n+2,\dots$ down one room, we have filled the space without creating a new one
* *Duplication of poles and center*. Treat the set of missing poles as vacanies dotting different lines on the duplicate sphere

    $\to$ Shifting the points on each line of latitude over, and infinity fills the vacanies

    >**NOTE**. The center point can be filled in a similar manner

* *Consequence*. Poles and center point are not duplicated

## $\sigma$-algebra
### Definition of $\sigma$-algebra
**Motivation**. $\sigma$-algebras are built to be the domain of measures
* *Problem*. Since we cannot make the domain of the measure to be the power set of the space in question
* *Naive solution*. Throw away the measure

    $\to$ We will not do this
* *Alternative solution*. Accept that our measure only works on some sets
    
    $\to$ We then consider this smaller collection of privileged subsets
* *Measurable sets*. These subsets will be called measurable sets
* *$\sigma$-algebra and measurable sets*. The collection of measurable sets form a $\sigma$-algebra

**$\sigma$-algebra**.
* *Assumptions*. $X$ is a set, whose superset is denoted as $\mathcal{P}(X)$
* *Conclusion*. The set system $\mathcal{A}\subseteq\mathcal{P}(X)$ is a $\sigma$-algebra, or $\sigma$-field, if it satisfies
    * $X\in\mathcal{A}$
    * Closed under complementation, i.e. $A\in\mathcal{A}\implies A^C\in\mathcal{A}$
    * Closed under countable unions, i.e. $A_1,A_2,\dots\in\mathcal{A}\implies\bigcap_{n=1}^\infty A_n\in\mathcal{A}$

### Derivation of $\sigma$-algebra
**Desired properties of a measure**. Consider $\mathcal{A}\subseteq\mathcal{P}(X)$, we want to define a measure $\mu:\mathcal{A}\to[0,\infty)\cup\{\infty\}$ with reasonable properties, e.g. translation and rotation invariance
* *Desiderata*. $\mathcal{A}$ should be as large as possible, since we want to properly assign measure to as many subsets as possible
* *Naive definition*. Choose $\mathcal{A}=\mathcal{P}(X)$
    
    $\to$ As mentioned, for some sets, there is no sensible notion for their measure
* *Alternative solution*. Convince ourselves that we should be able to measure nice enough sets, which we considered measurable

    $\to$ Weird sets should not have a measure

**Interpretation of $\sigma$-algebra's properties**.
* *Property 1*. $X\in\mathcal{A}$
    * *Explain*. We would like to know the measure of the entire space
* *Property 2*. If $A\in\mathcal{A}$ then $A^C\in\mathcal{A}$
    * *Explain*. If $A,X\in\mathcal{A}$, then we know $\mu(A)$ and $\mu(X)$

        $\to$ It is sensible to define $\mu(X\setminus A)=\mu(X)-\mu(A)$
    * *Interpretation in probability theory*. Our measure is a probability measure and the measure of a set $A$ denotes the probability that the outcome is in $A$
        
        $\to$ If we can ask whether the outcome is in $A$, we also want to be able to ask whether the outcome is not in $A$
* *Property 3*. $\mathcal{A}$ is closed under countable unions
    * *Explain*. The extension to countable unions is the most important structural element of a $\sigma$-algebra
        * If we have finitely many disjoint sets $A_i$, then we ought to be able to define

            $$\mu(\bigcup_{i=1}^n A_i)=\sum_{i=1}^n\mu(A_i)$$
        
        * Since we want to do analysis and take limits, we also want countable unions of measurable sets to be measurable
            * *Explain*. If we only allow finite unions
                
                $\to$ Our theory of measures will end up being incompatible with limiting operations
        
        >**NOTE**. This is what makes Lebesgue integral so useful, since we suddenly have a theory of integration playing well with limits

**Caratheodory's criterion of measurability**. We have yet to define measurability of a set

$\to$ Here, Caratheodory’s criterion of measurability comes in handy
* *Criterion of measurability*. A set $A\subseteq X$ is measurable if

    $$\forall B\subseteq X,\mu(B)=\mu(B\cap A)+\mu(B\setminus A)$$

    where $B$ needs not be measurable

    >**NOTE**. This is extremely important for proving theorems related to measurability

* *Interpretation for measurable $B$'s*. Consider a revision of the equality above, with $\mu(\cdot)$ being the Lebesgue outer measure

    $$\mu(B\cap A) = \mu(B) - \mu(B\setminus A)$$

    * *Case 1*. Consider when $B=X$, we have that
        * $\mu(B\cap A)$ defines the outer measure of $A$ and $\mu(B) - \mu(B\setminus A)$ defines the inner measure of $A$
        * Hence, the criterion states that $A$ is measurable if and only if its outer and inner agrees

            $\to$ This is similar to the definition of integrable functions
    * *Case 2*. Consider when $B\subset X$, then the interpretation is similar, but more strictly, since the equality must hold for all measurable $B\subseteq X$
* *Interpretation for nonmeasurable $B$'s*.
    * *Analogy*.
        * Treat $B$ as a rock with very jagged boundary, i.e. $B$ is not measurable, and $A$ as a knife
        * Treat the outer measure as a volume computed using shrink wrap
    * *Interpretation*.
        * When taking $B\cap A$ and $B\setminus A$, we think of using part of $A$'s boundary, which intersects $B$, to cut $B$

            $\to$ If $A$ is measurable, i.e. the cut is not too jagged, we will produce a very clean cut of $B$
        * Consider shrink wrapping $B\cap A$ and $B\setminus A$ individually
            * If the cut made by A is clean, then the shrink wrap fits the cut perfectly

                $\to$ No error is made for this part of the boundaries of $B\cap A$ and $B\setminus A$
            * For all other parts of $B\cap A$ and $B\setminus A$, i.e. the jagged parts

                $\to$ The errors made by the shrink wrap for $B\cap A$ and $B\setminus A$ precisely equal the errors made by the shrink wrap for $B$
    * *Conclusion*. $\mu(B)=\mu(B\cap A)+\mu(B\setminus A)$ holds whenever $A$ has a nice boundary, i.e. measurable
* *Reference*.
    * https://mathoverflow.net/questions/34007/demystifying-the-caratheodory-approach-to-measurability
    * https://jmanton.wordpress.com/2017/08/24/intuition-behind-caratheodorys-criterion-think-sharp-knife-and-shrink-wrap/

**$\sigma$-algebra and Caratheodory criterion of measurability**. Let $\mu:\mathcal{P}(X)\to[0,\infty)\cup\{\infty\}$ be a measure, then

$$\Sigma=\{A\subseteq X:A\text{ is measurable}\}$$

is a $\sigma$-algebra
* *Prove that $X\in\Sigma$*. This is obvious since

    $$\mu(B)=\mu(B\cap X)+\mu(B\setminus X)=\mu(B)+0=\mu(B)$$

* *Prove that $\Sigma$ is closed under complementation*. This is obvious since the roles of $A$ and $A^C$ in the Caratheodory criterion are interchangeable
* *Prove that $\Sigma$ is closed under countable unions*.
    * *Reference*. https://web.ma.utexas.edu/users/gordanz/notes/measures.pdf?fbclid=IwAR3lp1Vh3Le415aNQJcm2TnLgLBl91Y79h8AkSmZJ2Qsi218GifZZa3s_h8

# Appendix
## Concepts
**Group**. A set $G$ with a binary operation $\cdot$ on $G$ satisfying the group axioms
* *Group axioms*.
    * *Associativity*. $\forall a,b,c\in G,(a\cdot b)\cdot c=a\cdot (b\cdot c)$
    * *Identity element*. There exists an element $e\in G$ so that

        $$\forall a\in G, (e\cdot a = a)\land (a\cdot e=a)$$

        and such $e$ is unique
    * *Inverse element*. For each $a\in G$

        $$\exists b\in G,(a\cdot b=e) \land (b\cdot a=e)$$

* *Common interpretation*. Each element in a group is a function acting on the identity

    $\to$ The operation is a kind of function composition

**Limit of sets**. For a sequence of sets $A_1,A_2,\dots\subseteq X$, we define

$$\lim \inf_{n\to\infty} A_n=\bigcup_{n=1}^\infty \bigcap_{m=n}^\infty A_m,\quad\lim \sup_{n\to\infty} A_n=\bigcap_{n=1}^\infty \bigcup_{m=n}^\infty A_m$$

then $\lim_{n\to\infty}A_n$ exists if

$$\lim \inf_{n\to\infty} A_n=\lim \sup_{n\to\infty} A_n$$

* *Interpretation of limit in case of convergence*. Consider a sequence of polygons $A_1,A_2,\dots$ converging to a polygon $A$
    * *Interpretation of infimum limit*.
        * We have that for any $n\in\mathbb{N}$, let $\hat{A}_n=\bigcap_{m=n}^\infty A_m$
            
            $$\forall i\in\{n,n+1,\dots\},\hat{A}_n\subseteq A_i$$

            hence $\hat{A}_n$ is part of $A$ in some sense
        * We can interpret $\bigcup_{n=1}^\infty \hat{A}_n$ as collectively fill blank spaces in $A$, i.e.
            * If $\hat{A}_{n+1}$ covers some area $S_{n+1}\subseteq A$, which is then narrowed down to $S_n\subseteq S_{n+1}$ due to the intersection 
                
                $$\hat{A}_n=A_n\cap A_{n+1}$$
            
                then, by $\hat{A}_{n+1}\cup \hat{A}_n$, the covered area is extended from $S_n$ to $S_{n+1}\subseteq A$
            * As more $S_n$ gets combined, blank spaces in the polygon $A$ will be filled gradually
        * Hence, the limit infimum converges to the largest set of points which is covered by $A$, excluding $A$'s boundary
    * *Interpretation of supermum limit*.
        * We have that for any $n\in\mathbb{N}$, let $\hat{A}_n=\bigcup_{m=n}^\infty A_m$
            
            $$\forall i\in\{n,n+1,\dots\},\hat{A}_n\supseteq A_i$$

            hence $\hat{A}_n$ covers $A$ in some sense
        * We can interpret $\bigcap_{n=1}^\infty \hat{A}_n$ as collectively converge to the minimal open set which covers $A$'s closure, i.e.
            * If $\hat{A}_{n+1}$ covers some area $S_{n+1}\supseteq A$, which is then enlarged to $S_n\subseteq S_{n+1}$ due to the union 
                
                $$\hat{A}_n=A_n\cup A_{n+1}$$
            
                then, by $\hat{A}_{n+1}\cap \hat{A}_n$, the excessive area is narrowed down from $S_n$ to $S_{n+1}\supseteq A$
            * As more $S_n$ gets combined, the excessive area is narrowed down gradually
        * Hence, the limit infimum converges to the minimal set of points, which covers $A$, excluding $A$'s boundary
* *Interpretation of limit in case of divergence*. 
    * The infimum limit will converges to the largest set, which is covered by the intersection of limiting sets of $A_1,A_2,A_3,\dots$
    * The supermum limit will converges to the minimal set, which covers by the union of limit sets of $A_1,A_2,A_3,\dots$

## Discussions
**Special $\sigma$-algebra**.
* *Power set as $\sigma$-algebra*. For a given set $X$, its power set $\mathcal{P}(X)$ is a $\sigma$-algebra

**Measurability of all sets in $\sigma$-algebra**. The term "measurable" is defined only in relation to a given measure
* *Example*.
    * In the counting measure, all sets are measurable
    * In the Lebesgue measure, there are unmeasurable sets, assuming the axiom of choice
* *Correct statement*. There exists a measure, in which every set is measurable
    * *Explain*. Every member of a given $\sigma$-algebra is measurable for some measure
    * *Example*. Since all sets are measurable in the counting measure

        $\to$ This is true for all the sets in the given $\sigma$-algebra
* *Incorrect statement*. For a given arbitrary measure, the sets in every $\sigma$-algebra are measurable, since
    * *Explain*. Every set is member of the $\sigma$-algebra of all subsets

        $\to$ Any measure with unmeasurable sets is a counter-example
    * *Example*. The power set of any set form a $\sigma$-algebra, hence for any measure having some unmeasurable sets
        
        $\to$ There exists a $\sigma$-algebra, in which not all sets are measurable, i.e. the $\sigma$-algebra of all subsets
* *Reference*. https://math.stackexchange.com/questions/1554615/are-all-sets-in-sigma-algebra-measurable/3624590

**Closure under pairwise union does not imply closure under countable union**. Consider a family of sets $S(n)=[0,n]$
* This family is closed under pairwise union, i.e.

    $$S(n)\cup S(m)=S(\max\{n,m\})$$

* This family is not closed under countable union, i.e.

    $$\bigcup_{n=1}^\infty S(n)\to[0,\infty)$$

    which does not belong to the family

**Outer measure of limit of increasing sequence of sets**.
* *Assumptions*.
    * $\mu$ is an outer measure on a set $X$
    * $\langle S_n\rangle$ is an increasing sequence of $\mu$-measurable sets, i.e.

        $$\forall n=1,2,\dots,S_n=\bigcup_{i=1}^n A_i$$
    
    * $S_n\uparrow S$ as $n\to\infty$, i.e. $S=\bigcup_{i=1}^\infty A_i$
* *Conclusion*. For any subset $A\subseteq X$, we have

    $$\mu(A\cap S)=\lim_{n\to\infty} \mu(A\cap S_n)$$

* *Proof*.
    * Since $S_n\subseteq S$, we have that

        $$\mu(A\cap S)\geq \lim_{n\to\infty}\mu(A\cap S_n)$$
    
    * We have that $S=\bigcup_{i=0}^\infty (S_{i+1}\setminus S_i)$, where $S_0=\emptyset$, hence

        $$\begin{aligned}
        \mu(A\cap S)&\leq \sum_{i=0}^\infty \mu[A\cap (S_{i+1}\setminus S_i)]\\
        &=\sum_{i=0}^\infty\mu[(A\cap S_{i+1})\setminus(A\cap S_i)]\\
        &=\sum_{i=0}^\infty\big( \mu(A\cap S_{i+1}) - \mu(A\cap S_{i+1}\cap S_i) \big)\\
        &=\sum_{i=0}^\infty\big( \mu(A\cap S_{i+1}) - \mu(A\cap S_i) \big)\\
        &=\lim_{n\to\infty} \mu(A\cap S_n)
        \end{aligned}$$

**Outer measurable sets as $\sigma$-algebra**. The collection of measurable sets forms a $\sigma$-algebra, and measurable sets are element inside this $\sigma$-algebra
* *Assumptions*.
    * $\mu$ is an outer measure on a set $X$
    * $\mathcal{M}(\mu)$ is the set of all $\mu$-measurable subsets of $X$
* *Conclusion*. $\mathcal{M}(\mu)$ is a $\sigma$-algebra
* *Prove that $X\in\mathcal{M}(\mu)$*. This is obvious since

    $$\mu(B)=\mu(B\cap X)+\mu(B\setminus X)=\mu(B)+0=\mu(B)$$
* *Prove that $\mathcal{M}(\mu)$ is closed under complementation*. This is obvious since $A$ and $A^C$ are interchangable in Caratheodory's criterion
* *Prove that $\mathcal{M}(\mu)$ is closed under countable union*. Consider a sequence $\{S_i\}_{i\in\mathbb{N}}$ of $\mu$-measurable subsets of $X$, and $S=\bigcup_{n=1}^\infty S_n$

    $\to$ We want to prove that $S$ is $\mu$-measurable
    * Let $T_n=\bigcup_{i=1}^n S_i$, which is proven to be $\mu$-measurable via induction, we have that
        * The sequence $\langle T_n\rangle$ is increasing, and
        * $T_n\uparrow S$ as $n\to\infty$, where $\uparrow$ denotes the limit of an increasing sequence of sets
    * Let $A\subseteq X$ be any subset of $X$, we have that
        
        $$A=(A\cap S)\cup (A\setminus S)$$

        hence it suffices to prove that

        $$\forall A\subseteq X,\mu(A)\geq \mu(A\cap S) + \mu(A\setminus S)$$
    
    * We have that

        $$\begin{aligned}
        \mu(A)&=\mu(A\cap T_n) + \mu(A\setminus T_n)\\
        &\geq \mu(A\cap T_n) + \mu(A\setminus S)\\
        &=\mu(A\cap S) + \mu(A\setminus S)
        \end{aligned}$$

        * The second line is due to the fact that $T_n\subseteq S$
        * The third line is due to outer measure of limit of increasing sequence of sets

## Reference
* https://metaphor.ethz.ch/x/2021/fs/401-2284-00L/sc/notes_exclass01.pdf
* https://terrytao.files.wordpress.com/2012/12/gsm-126-tao5-measure-book.pdf