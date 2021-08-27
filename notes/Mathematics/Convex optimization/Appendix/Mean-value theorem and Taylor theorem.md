<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Extreme value theorem](#extreme-value-theorem)
- [Rolle theorem](#rolle-theorem)
- [Mean-value theorem](#mean-value-theorem)
  - [Mean-value theorem for real variables](#mean-value-theorem-for-real-variables)
  - [General mean-value theorem](#general-mean-value-theorem)
- [Taylor's theorem in one real variable](#taylors-theorem-in-one-real-variable)
- [BONUS](#bonus)
<!-- /TOC -->

# Extreme value theorem
**Extreme value theorem**:
* Assumptions:
  * $f$ is a continuous real-valued function defined on $[a, b]$
* Conclusion:
  * There exist $c, d \in [a, b]$ that $f(c) \geq f(x) \geq f(d)$ $\forall x \in [a, b]$
* Another interpretation: $f$ must attain a maximum and a minimum in $[a, b]$, each at least once

**Boundedness theorem (weak version of extreme value theorem)**:
* Assumptions:
  * $f$ is a continuous real-valued function defined on $[a, b]$
* Conclusion:
  * There exist $m, M \in \textbf{R}$ that $m < f(x) < M$ $\forall x \in [a, b]$
* Another interpretation: $f$ is bounded on $[a, b]$

# Rolle theorem
**Rolle theorem**:
* Assumptions:
  * $f$ is a continuous real-valued function defined on $[a, b]$
  * $f$ is differentiable on $(a, b)$
  * $f(a) = f(b)$
* Conclusion:
  * There exists at least one $c \in (a, b)$ that $f'(c) = 0$

>**NOTE**: this is the special case of mean-value theorem (see below)

# Mean-value theorem
## Mean-value theorem for real variables
**Lagrange mean-value theorem (or mean-value theorem)**:
* Assumptions:
  * $f$ is a continuous function on $[a, b]$
  * $f$ is differentiable on $(a, b)$
* Conclusion:
  * There exists a point $c \in (a, b)$ that $f'(c) = \frac{f(b) - f(a)}{b - a}$
* Intuition: there's at least one point at which the tangent line to the arc is parallel to the secant through its endpoints

**Cauchy's mean value theorem (or extended mean value theorem)**:
* Assumptions:
  * $f, g$ are both continuous on $[a, b]$
  * $f, g$ are differentiable on $(a, b)$
* Conclusion:
  * There exists some $c \in (a, b)$ that, if $g(a) \neq g(b)$ and $g'(c) \neq 0$
  
  $\hspace{1.0cm} \frac{f'(c)}{g'(c)} = \frac{f(b) - f(a)}{g(b) - g(a)}$
* Intuition: similar to Lagrange mean-value theorem but the $x$-axis is now the $g(x)$-axis (i.e. the extension of Lagrange's mean-value theorem to any continuous curve in $Oxy$ space)

## General mean-value theorem
**Mean-value theorem for vector variables**:
* Assumptions:
  * $G \subseteq \textbf{R}^n$ is a open convex set of $\textbf{R}^n$
  * $f: G \to \textbf{R}$ is a differentiable function
  * $g(t) = f((1 - t) x + t y)$ where $x, y \in G$
* Conclusion:
  * Original form: there exists $c \in (0, 1)$ that $g'(c) = g(1) - g(0)$
  * Alternative form: there exists $c \in (0, 1)$ that $f(y) - f(x) = \nabla f((1 - c) x + c y) \cdot (y - x)$

**Mean-value theorem for definite integrals**:
* First mean-value theorem:
  * Assumptions:
    * $f: [a, b] \to \textbf{R}$ is a continuous function
  * Conclusion:
    * There exists $c \in (a, b)$ that $f(c) = \frac{1}{b - a} \int_a^b f(x) dx$
  * Intuition: there must exists some $c \in (a, b)$ that the area of the ordinate set of $f$ along $[a, b]$ equals to the rectangle (based on the $x$-axis) with height $f(c)$ and width $b - a$
* Second mean-value theorem:
  * Assumptions:
    * $G: [a, b] \to \textbf{R}$ is a monotonic function
    * $\phi: [a, b] \to \textbf{R}$ is an integrable function
    * $G(a^+)$ stands for $\lim_{x \to a^+} G(x)$
  * Conclusion:
    * There exists $x \in (a, b)$ that
    
    $\hspace{1.0cm} \int_a^b G(t) \phi(t) dt = G(a^+) \int_a^x \phi(t) dt + G(b^-) \int_x^b \phi(t) dt$
  * Intuition:
    * We can treat $I = \int_a^b G(t) \phi(t) dt$ as the sum of areas of rectangles with height $G(t)$ and width $\phi(t) dt$
    * $G(a^+) \int_a^b \phi(t) dt \geq I \geq G(b^-) \int_a^b \phi(t) dt$ (in case of non-increasing $G$) and $I$ is a continuous function of $t$
    
    $\hspace{1.0cm} \rightarrow$ There always exists $x \in (a, b)$ so that $\int_a^b G(t) \phi(t) dt = G(a^+) \int_a^x \phi(t) dt + G(b^-) \int_x^b \phi(t) dt$

# Taylor's theorem in one real variable
**Derivation**: the core idea is $f^{(n-1)}(x) \approx f^{(n-1)}(a) + \int_a^x f^{(n)}(x) dx$
* $f(x) \approx f(a) + \int_a^x f'(x_1) d x_1$ 

$\hspace{1.6cm} \approx f(a) + \int_a^x f'(a) dx_1 + \int_a^x \int_a^{x_1} f''(x_2) dx_2 dx_1 + ...$

$\hspace{1.6cm} \approx f(a) + \int_a^x f'(a) dx_1 + \int_a^x \int_a^{x_1} f''(a) dx_2 dx_1 + \int_a^x \int_a^{x_1} \int_a^{x_2} f'''(x_3) dx_3 dx_2 dx_1$

$\hspace{1.6cm} ...$

$\hspace{1.6cm} \approx f(a) + f'(a) (x - a) + \frac{f''(a)}{2!} (x - a)^2 + \frac{f'''(a)}{3!} (x - a)^3 + ...$

**Taylor theorem**:
* Assumptions:
  * $k \geq 1$ is an integer
  * $f: \textbf{R} \to \textbf{R}$ is $k$ times differentiable at the point $a \in \textbf{R}$
* Conclusion:
  * There exists a remainder function $R_k$ that
    
  $\hspace{1.0cm} f(x) = \sum_{i = 0}^k \frac{f^{(i)}(a)}{i!} (x - a)^i + R_k$
* Interpretation: the error $R_k$ in an approximation by a $k$-th order Taylor polynomial tends to zero faster than any non-zero $k$-th degree polynomial as $x \to a$

>**NOTE**: the theorem doesn't tell us how large the error is in any concrete neighborhood of the center of expansion

* Explain: use partial integral
    * $f(x) = f(a) + \int_a^x f'(t) dt$
    * $\int_a^x f'(t) dt = (f'(t) t)|_a^x - \int_a^x t f''(t) dt$
    * $f'(x) x - f'(a) a - \int_a^x t f''(t) dt = f'(a) (x - a) + x [f'(x) - f'(a)] - \int_a^x t f''(t) dt$

    $\hspace{5.4cm} = f'(a)(x - a) + \int_a^x (x - t) f''(t) dt$

    $\hspace{5.4cm} = f'(a) (x - a) + [f''(t) \frac{(x - t)^2}{2}]|_a^x - \int_a^x \frac{(x - t)^2}{2} f'''(t) dt$

    $\hspace{5.4cm} = f'(a) (x - a) + \frac{f''(a)}{2!} (x - a)^2 - \int_a^x \frac{(x - t)^2}{2} f'''(t) dt$

**Application**: 
* Estimate the error in using a polynomial $P_k(x)$ of degree $k$ to estimate $f(x)$ on a given interval $(a - r, a + r)$
* Find the smallest degree $k$ for which the polynomial $P_k(x)$ approximates $f(x)$ to within a given error on a given interval $(a - r, a + r)$
* Find the largest interval $(a - r, a + r)$ on which $P_k(x)$ approximates $f(x)$ to within a given error

**Forms of the remainder $R_k$**:
* Peano form: $R_k = h_k(x)(x - a)^k$ where $\lim_{x \to a} h_k(x) = 0$
* Mean-value form: 
  * Lagrange form: $R_k(x) = \frac{f^{(k+1)}(\xi_L)}{(k+1)!} (x - a)^{k+1}$
  * Cauchy form: $R_k(x) = \frac{f^{(k+1)}(\xi_C)}{(k+1)!} (x - \xi_C)^k (x - a)$
* Integral form of the remainder: $R_k(x) = \int_a^x \frac{f^{(k+1)}(t)}{k!} (x - t)^k dt$

**Prove**:
* General form of $R_k$:
  * Let $F(t) = \sum_{i = 0}^k \frac{f^{(i)}(t)}{i!} (x - t)^i$
    * $\frac{\partial \frac{f^{(i)}(t)}{i!} (x - t)^i}{\partial t} = \frac{f^{(i+1)}(t)}{i!} (x - t)^i - \frac{f^{(i)}(t)}{(i - 1)!} (x - t)^{i-1}$
      * If $i \geq 1$, $- \frac{f^{(i)}(t)}{(i - 1)!} (x - t)^{i-1}$ will be canceled by $\frac{f^{(i)}(t)}{(i - 1)!} (x - t)^{i-1}$ in $\frac{\partial \frac{f^{(i-1)}(t)}{(i-1)!} (x - t)^{i-1}}{\partial t}$
    * From above, $F'(t) = \frac{f^{(k+1)}(t)}{k!} (x - t)^k$
  * According to mean-value theorem, $F(x) - F(a) = (G(x) - G(a)) \frac{F'(\xi)}{G'(\xi)}$ where $\xi \in (a, x)$
    * $F(x) = f(x)$ and $F(a) = \sum_{i = 0}^k \frac{f^{(i)}(a)}{i!} (x - a)^i$
    
    $\hspace{1.0cm} \rightarrow R_k = (G(x) - G(a)) \frac{F'(\xi)}{G'(\xi)}$ is the remainder in the Taylor theorem
* Explicit form of $R_k$:
  * Lagrange form: choose $G(t) = t - a$
  * Cauchy form: choose $G(t) = (t - a)^{k+1}$
  * Integral form: choose $G(t) = \int_a^t \frac{f^{(k+1)}(s)}{k!} (x - s)^k ds$

---

# BONUS
* Secant of a curve: a line that intersects the curve in at least two (distinct) points
* Usual stochastic order: 
  * Definition: $A$ is less than $B$ in the "usual stochastic order" if

  $\hspace{1.0cm} \text{Pr}(A > x) \leq \text{Pr}(B > x)$ $\forall x \in (-\infty, \infty)$
  * Notation: $A \preceq B$ or $A \leq_\text{st} B$