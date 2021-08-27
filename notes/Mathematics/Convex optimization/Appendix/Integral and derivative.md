<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Integral](#integral)
  - [Terminology and notation](#terminology-and-notation)
  - [Formal definitions](#formal-definitions)
  - [Fundamental theorem of calculus](#fundamental-theorem-of-calculus)
- [Anti-derivative](#anti-derivative)
- [Discussion](#discussion)
  - [Basic formula](#basic-formula)
  - [Techniques](#techniques)
- [BONUS](#bonus)
- [NEW WORD](#new-word)
<!-- /TOC -->

# Integral
## Terminology and notation
**Standard**:
* The integral w.r.t $x$ of $f$ on $[a, b]$: $\int_a^b f(x) dx$
  * $\int$ represents integration
  * $dx$ is the differential of $x$ (i.e. the variable of integration is $x$)
  * $f$ is the integrand
  * $a, b$ are the limits of the integral

**Types of integral**:
* Definite integral: integrals whose limits are specified
  * Notation: $\int_a^b f(x) dx$
* Indefinite integral: integrals whose limits aren't specified
  * Notation: $\int f(x) dx$
  * Meaning: represent a class of functions (the anti-derivative) whose derivative is the integrand

**Meaning of $dx$**:
* Historical meaning: $dx$ represents an infinitesimally small piece of $x$ to be multiplied by the integrand $f$ and summed up in an infinite sense
* Introductory calculus: $dx$ is a part of the symbol for integration (i.e. the delimiter on the right side of the expression being integrated)
* More sophisticated context: $dx$ has its own significance, depending on the particular area of mathematics being discussed

## Formal definitions
**Riemann integral**:
* Assumptions:
  * $[a, b]$ is a closed interval of the real line
  * $a = x_0 \leq t_1 \leq x_1 \leq t_2 \leq x_2 \leq ... \leq t_n \leq x_n = b$ is a tagged partition of $[a, b]$
    * Explain:
      * $[a, b]$ is divided into sub-intervals $[x_{i-1}, x_i]$ indexed by $i$
      * $[x_{i-1}, x_i]$ is tagged by $t_i$
  * $\Delta_i = x_i - x_{i-1}$
* Conclusion:
  * Riemann sum of $f$ w.r.t the tagged partition above: $\sum_{i = 1}^n f(t_i) \Delta_i$
  * The mesh of the tagged partition above: $\max_{i = 1, ..., n} \Delta_i$
  * The Riemann integral of $f$ over $[a, b]$ is equal to $S$ if:
    * For any $\epsilon > 0$, there exists $\delta > 0$ that for any tagged partition $[a, b]$ with mesh less than $\delta$
    
    $\hspace{1.0cm} |S - \sum_{i = 1}^n f(t_i) \Delta_i| < \epsilon$

**Lebesgue integral**: the familiar integral $\int_a^b f(x) dx$

## Fundamental theorem of calculus
**First fundamental theorem of calculus**:
* Assumptions:
  * $f$ is a continuous real-valued function on $[a, b]$
  * $F(x) = \int_a^x f(t) dt$ $\forall x \in [a, b]$
* Conclusion:
  * $F$ is continuous on $[a, b]$, differentiable on $(a, b)$
  * $F'(x) = f(x)$ $\forall x \in (a, b)$

**Second fundamental theorem of calculus**
* Assumptions:
  * $f$ is a real-valued function defined on $[a, b]$
  * $F$ is the anti-derivative of $f$ on $[a, b]$
    * Formal: $f(x) = F'(x)$ $\forall x \in [a, b]$
* Conclusion:
  * If $f$ is integrable on $[a, b]$ then $\int_a^b f(x) dx = F(b) - F(a)$

# Anti-derivative
**Other names**: primitive function, primitive integral or indefinite integral

**Informal definition**: anti-derivative of $f$ is a differentiable function $F$ whose derivative equals to $f$

**Opposite operation of indefinite integration (or anti-differentiation)**: differentiation

# Discussion
## Basic formula
**Derivatives**:
* Univariate:
  * $(uv)' = u'v + v'u$
    * Explain: $\frac{u(x+h) v(x+h) - u(x) v(x)}{h} = \frac{[u(x+h) v(x+h) - u(x+h) v(x)] + [u(x+h) v(x) - u(x) v(x)]}{h} = u'(x) v(x) + v'(x) u(x)$
  * $(\frac{u}{v})' = \frac{u'v - v'u}{v^2}$
* Multivariate:
  * $f'(x, y) = \frac{\partial f}{\partial x} + \frac{\partial f}{\partial y}$
    * Explain: $f(x+h, y+h) - f(x, y) = [f(x+h, y+h) - f(x+h, y)] + [f(x+h, y) - f(x, y)]$

## Techniques
**Partial integral**: $\int u dv = u v - \int v du$
* Explain: $\int (u dv + v du) = \int d(uv) = uv$

---

# BONUS
* Assumptions:
  * $f: [a, b] \to \textbf{R}$ is a bounded function
  * $P = (x_0, ..., x_n)$ is a partition of $[a, b]$
    * Explain: $a = x_0 < x_1 < ... < x_n = b$
  * $M_i = \sup_{x \in [x_{i-1}, x_i]} f(x)$
  * $m_i = \inf_{x \in [x_{i-1}, x_i]} f(x)$
* Darboux sum:
  * Upper Darboux sum of $f$ w.r.t $P$: $U_{f, P} = \sum_{i=1}^n (x_i - x_{i-1}) M_i$
  * Lower Darboux sum of $f$ w.r.t $P$: $L_{f, P} = \sum_{i=1}^n (x_i - x_{i-1}) m_i$
* Darboux integral:
  * Upper Darboux integral: $U_f = \inf \{U_{f, P}|P$ is a partition of $[a, b]\}$
  * Lower Darboux integral: $L_f = \sup \{L_{f, P}|P$ is a partition of $[a, b]\}$
* $L^1$ function in some space $X$: $\{f|\int_X |f| d\mu < \infty\}$

# NEW WORD
* Delimiter (n): dấu phân cách