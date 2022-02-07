<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Definition](#definition)
- [Motivation](#motivation)
- [Convergence](#convergence)
- [Properties](#properties)
- [Fourier transform formulas under different normalizations](#fourier-transform-formulas-under-different-normalizations)
- [Applications](#applications)
<!-- /TOC -->

# Introduction
**Other names**: frequency domain representation

**Frequency domain and time domain**:
* Frequency domain: the domain of the Fourier transform
* Time domain: the domain of the original function

**Fourier transform (FT)**:  decompose a function of time (a signal) into the frequencies that make it up
* Fourier transform as a function of frequency: the Fourier transform of a function of time is itself a complex-valued function of frequency, whose:
	* The absolute value: represent the amount of that frequency present in the original function
	* Complex argument: represent the phase offset of the basic sinusoid in that frequency

# Definition
**Fourier transform**:
* Assumption:
	* $f: \textbf{R} \to \textbf{C}$ is a integrable function
* Conclusion:
	* The Fourier transform of $f$: $\hat{f}(\xi) = \int_{-\infty}^\infty f(x) e^{-2\pi i x \xi} dx$
	* The reason for negative sign convention in $e^{-2\pi i x \xi}$: 
		* Electrical engineering: it's common to use $f(x) = e^{2\pi i \xi_0 x}$ to represent a signal with zero initial phase and frequency $\xi_0$
		* The reason for $e^{-2\pi i x \xi}$: $e^{2\pi i \xi_0 x} e^{-2\pi i x \xi} = 1$ (i.e. frequency zero) when $\xi = \xi_0$
		
		$\hspace{1.0cm} \rightarrow \hat{f}(\xi)$ becomes a Dirac delta function at $\xi = \xi_0$
	* Time variable and frequency variable:
		* Time variable: $x$ (s)
		* Frequency variable: $\xi$ (Hz)
	* The inverse transform: $f(x) = \int_{-\infty}^\infty \hat{f}(\xi) e^{2\pi i x \xi} d \xi$

**Intuition (of Fourier transform)**:
* Intuition 1:
    * $\hat{f}(\epsilon) = \int_{-\infty}^\infty f(x) e^{-2\pi i x \epsilon} dx$ is the inner product of $f(x)$ and $e^{-2 \pi i x \epsilon}$
    
    $\hspace{1.0cm} \rightarrow$ When the two vectors are in the same direction, the inner product is large
    * From above, $\hat{f}(\epsilon)$ tells us how much $f$ is in $e^{-2 \pi i x \epsilon}$
* Intuition 2:
    * Fourier transform:
        * In linear algebra, $x^T y = \cos(x, y) \|x\|_2 \|y\|_2$
        
        $\hspace{1.0cm} \rightarrow$ If $y$ is the unit vector, $x^T y$ is the length of $\text{proj}_y x$
        * In Fourier transform, we can see intuition 1 for equivalence
    * Inverse Fourier transform:
        * Given a set of orthogonal basis $\{u_i\}_i$
        
        $\hspace{1.0cm} \rightarrow x = \sum_i \text{proj}_{u_i} x = \sum_i (x^T u_i) u_i$
        * In Fourier transform, 
            * $u_\epsilon$ is equivalent to $e^{2 \pi i \epsilon x}$
            * $x^T u_\epsilon$ is equivalent to $\hat{f}(\epsilon)$

**Fourier integral pair (or Fourier transform pair)**: $f$ and $\hat{f}$

**Fourier inversion theorem**: $f$ can be reconstructed from $\hat{f}$
* Explain: see Fourier series note

**Fourier spectrum of $f$**: $F(2\pi \xi) = \hat{f}(\xi) = \int_{-\infty}^\infty f(x) e^{-2\pi i x \xi} dx$
* Magnitude spectrum of $f$ in the frequency domain: $|F(2\pi \xi)| = \sqrt{\text{Re}(F(2\pi \xi))^2 + \text{Im}(F(2\pi \xi))^2}$
* Phase spectrum of $f$ in the frequency domain: $\phi(2\pi \xi) = \arctan \frac{\text{Im}(F(2\pi \xi))}{\text{Re}(F(2\pi \xi))}$

# Motivation
**Fourier transform via Fourier series**: the Fourier transform is an extension of the Fourier series, when the period of some periodical function $f$ approaches infinity
* Explain:
	* Fourier transform: $c_n = \frac{1}{T} \int_{-T/2}^{T/2} f(x) e^{-2\pi i (\frac{n}{T}) x} dx = \frac{1}{T} \hat{f}(\frac{n}{T})$
	* Inverse Fourier transform:
		* $f(x) = \sum_{n=-\infty}^\infty c_n e^{2\pi i (\frac{n}{T}) x} = \sum_{n=-\infty}^\infty \hat{f}(\xi_n) e^{2\pi i \xi_n x} \Delta \xi$
			* $\Delta \xi = \xi_n - \xi_{n-1} = \frac{n}{T} - \frac{n-1}{T} = \frac{1}{T}$
		* From above, $\lim_{T \to \infty} f(x) = \int_{-\infty}^\infty \hat{f} e^{2\pi i \xi x} d\xi$

**Usage of Fouier transform**: simplify many of the formulas involved

# Convergence
**Condition for existence of Fourier and inverse Fourier transforms**: $f(x)$ must be an energy signal
* Formal: $\int_{-\infty}^\infty |f(x)|^2 dx < \infty$

>**NOTE**: $|f(x)|^2$ means $f(x) f^*(x)$ where $f^*$ is the complex conjugate of $f$

**Condition for convergence**: Dirichlet conditions for continuous functions (since Fourier transform, in fact, is the inverse of Fourier series representation)
* $\int_{-\infty}^\infty |f(x)| dx < \infty$
* $f(x)$ must have a finite number of extrema
* $f(x)$ must have a finite number of discontinuities

# Properties
**Linearity**: $h(x) = a f(x) + b g(x)$ implies $\hat{h}(\xi) = a \hat{f}(\xi) + \hat{g}(\xi)$
* Intuition: linearly combining $f$ and $g$ is equivalent to linearly combining their corresponding components

**Time shift**: $h(x) = f(x - x_0)$ implies $\hat{h}(\xi) = e^{-2\pi i x_0 \xi} \hat{f}(\xi)$
* Intuition: shifting $f$ by $-x_0$ in time domain is equivalent to shifting its components by $-x_0$ in time domain

**Frequency shift**: $h(x) = e^{2\pi i x \xi_0} f(x)$ implies $\hat{h}(\xi) = f(\xi - \xi_0)$
* Intuition: increasing the frequency of $f$ by $\xi_0$ is equivalent to shifting its frequency domain by $\xi_0$

**Time scaling**: $h(x) = f(ax)$ implies $\hat{h}(\xi) = \frac{1}{|a|} \hat{f}(\xi / a)$ where $a \neq 0$
* Intuition: scaling down the time axis of $f$ by $1/a$ (i.e. scale down the period of $f$ by $1/a$) is equivalent to 
  * Scaling up its frequency axis, in frequency domain, by $a$
  * Then scaling down the time axis of its components by $1/a$ (since the period of $f$ is scaled down by $1/a$)

**Differentiation**: $h(x) = \frac{\partial f}{\partial x}$ implies $\hat{h}(\xi) = 2\pi i \xi \hat{f}(\xi)$
* Intuition: differentiating $f$ along time domain is equivalent to differentiating each of its components along their time domain

>**NOTE**: this makes the major use of Fourier transform (i.e. solve ordinary differential equations)

**Integration**: $h(x) = \int_{-\infty}^x f(t) dt$ implies $\hat{h}(\xi) = \frac{\hat{f}(\xi)}{2\pi i \xi}$
* Intuition: integrating $f$ along time domain is equivalent to integrating each of its components along their time domain

**Convolution**: $h(x) = f(x) * g(x)$ implies $\hat{h}(x) = \hat{f}(\xi) \hat{g}(\xi)$
* Explain: 

$\hspace{1.0cm} \int (\int f(t) g(x - t) dt) e^{-2\pi i \xi x} dx = \int \int f(t) e^{-2\pi i \xi t} g(x - t) e^{-2\pi i \xi (x - t)} dt d(x - t)$

$\hspace{6.5cm} = \int f(t)  e^{-2\pi i \xi t} dt \cdot \int g(x - t) e^{-2\pi i \xi (x - t)} d(x - t)$

$\hspace{6.5cm} = \hat{f}(\xi) \hat{g}(\xi)$

>**NOTE**: this makes the importance of convolution

**Modulation**: $h(x) = f(x) g(x)$ implies $\hat{h}(x) = \hat{f}(\xi) * \hat{g}(\xi)$

**Parseval's formula**: $\int_{-\infty}^\infty |f(x)|^2 dx = \int_{-\infty}^\infty |\hat{f}(\xi)|^2 d\xi$
* Explain: the same as Parseval's formula for Fourier series

**Symmetry**:
* The energy spectrum of $f(x)$ is an even function
	* Formal: $|\hat{f}(\xi)|^2 = |\hat{f}(\xi)|^2$
* If $f$ is real-valued then $\hat{f}(\xi) = \hat{f}^*(-\xi)$
* If $f$ is real-valued and even then $\hat{f}(\xi)$ is also even
	* Formal: $\hat{f}(\xi) = \hat{f}(-\xi)$
* If $f$ is real-valued and odd then $\hat{f}(\xi)$ is also odd
	* Formal: $\hat{f}(\xi) = -\hat{f}(-\xi)$

# Fourier transform formulas under different normalizations
**General formula**: ${\mathcal{F}} f(s) = \frac{1}{A} \int_{-\infty}^\infty e^{i B s t} f(t) dt$

**Different forms of Fourier transforms**:
* Form 1: $A = \sqrt{2 \pi}$ and $B = \pm 1$
* Form 2: $A = 1$ and $B = \pm 2 \pi$
* Form 3: $A = 1$ and $B = \pm 1$

**Basic principles to live with Fourier transforms**:
* ${\mathcal{F}} {\mathcal{F}} f$
* $({\mathcal{F}} f)'$
* ${\mathcal{F}}(f * g)$

# Applications
**Solve partial differential equation**: the most important use of the Fourier transform
* History: many of the equations of the mathematical physics of the 19th century can be treated this way
* Fourier's problem: $\frac{\partial^2 y(x, t)}{\partial^2 x} = \frac{\partial^2 y(x, t)}{\partial^2 t}$
  * Boundary problem: there are infinitely many solutions for this, thus the problem isn't to find a solution
  
  $\hspace{1.0cm} \rightarrow$ Instead, we find a solution which satisfies the boundary conditions $y(x, 0) = f(x), \frac{\partial y(x, 0)}{\partial t} = g(x)$, given $f$ and $g$
  * Idea: it's easier to find the Fourier transform $\hat{y}$ of the solution than to find the solution directly
    * Explain: the Fourier transform takes differentiation into multiplication
    
    $\hspace{1.0cm} \rightarrow$ A partial differential equation applied to the original function is transformed into multiplication by polynomial functions of the dual variables applied to the transformed function
* Fourier's method: see Wikipedia - Fourier transform for examples
  * Choose a set of elementary solutions, parametrized by $\xi$
  
  $\hspace{1.0cm} \rightarrow$ The general solution would be a continuous linear combination, in the form of an integral over $\xi$
  * Express the boundary conditions in terms of these integrals and set them equal to $f$ and $g$
  * Exploit Fourier inversion by applying the Fourier transform to both sides
  
  $\hspace{1.0cm} \rightarrow$ We obtain expressions for the coefficients of the elementary solutions, in terms of $f$ and $g$

**Signal processing**: used for the spectral analysis of time-series