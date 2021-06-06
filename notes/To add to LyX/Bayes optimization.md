---
title: Bayes optimization
tags: To add to LyX
---

**Bayes optimization**. A sequential design strategy for global optimization of black-box functions
* *Applications*. Optimize expensive-to-evaluate functions, i.e.

    $$\max_{x\in A} f(x)$$
    
    where $A$ is a set of points whose membership can be easily evaluated, and $f(x)$ is difficult to evaluate
    
* *Strategy*. Treat $f$ as a random function and place a prior over it
    * *Definitions*.
        * *Prior over $f$*. Capture beliefs about the behavior of the function
        * *Data*. The evaluations of $f$ on multiple values of $x$
    * *Idea*.
        1. Start with a prior of $f$ over $x \in A$
        2. Collect data by evaluating $f$ at multiple values of $x$
        3. Update to prior to yield a posterior distribution of $f$ over $x \in A$
        4. Use the posterior distribution to construct an acquisition function, which determines where to evaluate the function next
    * *Methods to define prior / posterior distribution over $f$*.
        * *Kriging*. Use Gaussian processes
        * *Parzen-tree estimator*. Construct two distributions for high and low points, then find the location maximizing the expected improvement
* *Exotic Bayesian optimization problems*. Bayesian optimization problems where $\{f(x):x\in A\}$ are not easy to evaluate
    * *Example*. 
        * When there is noise
        * When the evaluations are being done in parallel
        * When the quality of evaluations relies upon a trade-off between difficulty and accuracy
        * When there is some presence of random environmental conditions
        * When the evaluation involves derivatives

**Simulated annealing**. A probabilistic technique for approximating the global optimum of a given functio