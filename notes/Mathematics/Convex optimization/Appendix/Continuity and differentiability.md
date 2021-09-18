<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Continuous function](#continuous-function)
  - [Definition](#definition)
  - [Properties](#properties)
- [Continuity (expansions)](#continuity-expansions)
- [Differentiable function](#differentiable-function)
<!-- /TOC -->

# Continuous function
## Definition
**Limit-based definition**: $f$ is continuous at $c \in \textbf{dom } f$ if $\lim{x \to c} = f(c)$

**Weierstrass and Jordan definitions (epsilon–delta)**:
* Assumptions:
  * $f: D \to R$
* Conclusion:
  * $f$ is continuous at $x_0 \in D$ if for all $\epsilon > 0$, there exists some $\delta > 0$ that
  
  $\forall x \in (x_0 - \delta, x_0 + \delta)$ $|f(x_0) - f(x)| < \epsilon$

## Properties
**Intermediate value theorem**:
* Assumptions:
  * $f$ is continuous on $[a, b]$
  * $k \in [f(a), f(b)]$
* Conclusion:
  * There exists some $c \in [a, b]$ that $f(c) = k$

**Relation to differentiability and integrability**:
* Differentiability: differentiability implies continuity but the converse doesn't hold
  * Example: $f(x) = |x|$ is differentiable but not continuous
* Integrability: continuity implies integrability but the converse doesn't hold
  * Example: step functions

**Directional continuity and semi-continuity**:
* Right-continuous function: $f$ is right-continuous if: for any $\epsilon > 0$, there exists some $\delta > 0$ that for all $x \in (c, c + \delta)$,

$\hspace{1.0cm} |f(x) - f(c)| < \epsilon$
* Left-continuous function: similar to right-continuous function but for $x \in (c - \delta, c)$
* Directional continuity: extended version of semi-continuity in multidimensional space

* Oscillation (mathematics):
	* Assumptions:
		* $f: \cal{D} \to \textbf{R}$ is a function
	* Conclusion:
		* The oscillation of $f$ on an interval $I \in \textbf{dom } f$: $\omega_f (I) = \sup_{x \in I} f(x) - \inf_{x \in I} f(x)$
		* The oscillation of $f$ at a point $x_0$: $\omega_f(x_0) = \lim_{\epsilon \to 0} \omega_f(x_0 - \epsilon, x_0 + \epsilon)$
* Classification of discontinuities:
	* Removable discontinuity: when $L = \lim_{x \to x_0^-} f(x) = \lim_{x \to x_0^+} f(x) \neq f(x_0)$
	* Jump discontinuity: when $L = \lim_{x \to x_0^-} f(x) \neq \lim_{x \to x_0^+} f(x)$
	* Essential discontinuity: 
		* When $\lim_{x \to x_0^-} f(x)$ or $\lim_{x \to x_0^+} f(x)$ is infinite
		* (or) when $\lim_{x \to x_0^-} f(x)$ or $\lim_{x \to x_0^+} f(x)$ doesn't exists (i.e. undefined)
			* Example: $\lim_{x \to 0} \sin \frac{1}{x}$

# Continuity (expansions)
**Uniform continuity**:
* Assumptions:
  * $f: X \to Y$ is a function
* Conclusion:
  * $f$ is uniformly continuous if for every positive $\epsilon$, there exists a positive $\delta$ that:
    * For every $x, y \in X, Y$ with $|x - y| < \delta$
    
    $\hspace{1.0cm} \rightarrow |f(x) - f(y)| < \epsilon$
* Uniform continuity vs continuity at every point:
  * Uniform continuity: the value of $\delta$ depends only on $\epsilon$ and not on the point in the domain

**Absolute continuity**:
* Assumptions:
  * $I$ is an interval in $\textbf{R}$
  * $f: I \to \textbf{R}$ is a function
* Conclusion:
  * $f$ is absolutely continuous on $I$ if for every positive $\epsilon$, there is a positive $\delta$ that:
    * Whenever a finite sequence of pairwise disjoint sub-interval $(x_k, y_k)$ of $I$ with $x_k, y_k \in I$ satisfies $\sum_k (y_k - x_k) < \delta$
    
    $\hspace{1.0cm} \rightarrow \sum_k |f(y_k) - f(x_k)| < \epsilon$
  * Equivalent definitions:
    * $f$ has a derivative $f'$ almost everywhere and $f(x) = f(a) + \int_a^x f'(t) dt$ $\forall x \in [a, b]$
    * There exists an integrable function $g$ on $[a, b]$ that $f(x) = f(a) + \int_a^x g(t) dt$ $\forall x \in [a, b]$
      >**NOTE**: in this case, $g = f'$ almost everywhere

**Relationship between types of continuities**:
* Absolute continuity $\subseteq$ uniformly continuity $\subseteq$ continuity
* Continuously differentiable $\subseteq$ absolutely continuous $\subseteq$ bounded variation $\subseteq$ differentiable almost everywhere

# Differentiable function
**Differentiability of real functions of one variable**:
* Assumptions:
  * $f: U \subset \textbf{R} \to \textbf{R}$, defined on an open set $U$
* Conclusion:
  * $f$ is differentiable at $a \in U$ if any of the following equivalent conditions is satisfied:
    * $f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}$ exists
      * Another interpretation: $\lim_{h \to 0^+} \frac{f(a + h) - f(a)}{h} = \lim_{h \to 0^-} \frac{f(a + h) - f(a)}{h} = L$ where $-\infty < L < \infty$
      * Notes:
        * $\lim_{h \to 0^+} \frac{f(a + h) - f(a)}{h}$ denotes the rate of change of $f$ when moving from $a$ to some local point $b < a$
        * $\lim_{h \to 0^+} \frac{f(a + h) - f(a)}{h}$ denotes the rate of change of $f$ when moving from $a$ to some local point $b > a$
        
        $\hspace{1.0cm} \implies f$ is differentiable at $a$ if the rate of change of $f$ from $a$ in any direction converges to some limit $-\infty < L < \infty$
    * $\exists L \in \textbf{R}$ $\lim_{h \to 0} \frac{f(a + h) - f(a)}{h} = L$
    * $\exists g: U \subset \textbf{R} \to \textbf{R}$ $f(a + h) = f(a) + f'(a) h + g(h)$ and $\lim_{h \to 0} \frac{g(h)}{h} = 0$