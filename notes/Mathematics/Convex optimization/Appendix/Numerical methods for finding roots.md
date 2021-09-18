<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [The bisection method (the binary search method)](#the-bisection-method-the-binary-search-method)
- [Fixed point iteration](#fixed-point-iteration)
- [Ridder's method](#ridders-method)
<!-- /TOC -->

# The bisection method (the binary search method)
**Task**: solve $f(x) = 0$ for $x$

**Algorithm**:

```
def bisection(f, a, b, n)
  # f is the objective function
  # a, b are initial points where f(a)*f(b) < 0
  # n is the number of iterations
  for i in range(n):
    m = (a + b)/2
    
    # if a root lies within [a, m] (i.e. a and m bracket a root)
    if f(a)*f(m) < 0:
      b = m
    # else, the root must lie within [m, b] (i.e. m and b bracket a root)
    else:
      a = m
  return m

```

>**NOTE**: when $f(a) f(b) < 0$, $a$ and $b$ are said to bracket a root (due to intermediate value theorem)

**Intuition**: the same idea as binary search (i.e. given an array of negative elements followed by positive ones, find the elements with value $0$)
* Idea: repeatedly shorten the width of the interval $(a, b)$, which brackets a root

**Complexity**: $n = \lceil \log_2 \frac{b - a}{\epsilon} - 1 \rceil$ where $\epsilon$ is our tolerance on the solution proposed by the algorithm

**Advantages and disadvantages**:
* Advantages: simple and robust
* Disadvantages: relatively slow

**Application**: used to obtain a rough approximation to a solution, which is then used as a starting point for more rapidly converging methods

**False position**: a variation of bisection method
* Idea: instead of choosing $m = \frac{a + b}{2}$

$\hspace{1.0cm} \rightarrow$ We draw a line through $(a, f(a))$ and $(b, f(b))$ and and see where is crosses the axis
* Formal: $m$ is the solution of $y = \frac{f(b) - f(a)}{b - a} (m - a) + f(a)$ at $y = 0$
  * $m = \frac{a f(b) - b f(a)}{f(b) - f(a)}$

# Fixed point iteration
**Fixed point of a function $g(x)$**: a value $p$ that $g(p) = p$

**Properties of fixed points**: 
* Some fixed point $p$ attracts nearby points towards it
  * Formal: the sequence $(x_n)$ where $x_i = g(x_i)$ $\forall i > 1$ and $x_1 = c$ converges to $p$
  
  >**NOTE**: the term "nearby point" must be emphasized

* Some fixed point $p$ repels nearby points (i.e. it's very hard to converge to $p$)

**Determine whether a fixed point $p$ is attracting or repelling**:
* If $|g'(p)| < 1$ then the fixed point is attracting
* If $|g'(p)| > 1$ then the fixed point is repelling
* If $|g'(p)| = 1$ then a more sophisticated analysis is needed to determine the point's behavior

>**NOTE**: the closer $|g'(p)|$ is to $0$, the faster the iterates will converge

**Using fixed points to solve equations**:
* Fixed point iteration: the process where we compute $g(x_0), g(g(x_0)), $ etc
  * Purpose: find an attracting fixed point of $f$
* Idea: re-write the equation as a fixed point problem

>**NOTE**: the initial value does matter

# Ridder's method
**Idea**: a variation of bisection / false position

**Advantages**:
* Easy to implement
* Work fairly well

**Idea**:
* Initialization: two initial points $a$, $b$ that $f(a) f(b) < 0$
* Iterations:
  * Compute $m = (a + b)/2$
  * Compute $z = m + \text{sign}(f(a) - f(b)) \frac{(m - a) f(m)}{\sqrt{f(m)^2 - f(a) f(b)}}$
  * If $f(a) f(z) > 0$ then set $a = z$, and $b = z$ otherwise
* Termination: when the value of $f$ is as close to $0$ as needed

**Practical performance**:
* Converge with quadratic order
* Slower than Newton's method
* More reliable than Newton's method