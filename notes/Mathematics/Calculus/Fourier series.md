<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Deferent and epicycle](#deferent-and-epicycle)
- [BONUS](#bonus)
- [NEW WORD](#new-word)
- [Base knowledge](#base-knowledge)
- [Fourier series](#fourier-series)
- [Convergence of Fourier series representation](#convergence-of-fourier-series-representation)
- [BONUS](#bonus-1)
- [NEW WORD](#new-word-1)
<!-- /TOC -->

# Deferent and epicycle
>**NOTE**: this section is taken under the assumption that the Earth is the center of the Solar system (i.e. assumed by ancient Greek)

**Introduction**:
* Epicycle and deferent:
  * Epicycle: in ancient Greek's opinion, the planets are assumed to move in a small circle called "epicycle"
  * Deferent: an epicycle moves along a larger circle called "deferent"
  * Direction of rotation: both circles rotate clockwise and are roughly parallel to the plane of the Sun's orbit
* Eccentric: although the Earth is the center of the universe, the deferent wasn't centered on the Earth but at a point slightly away from the Earth, called "eccentric"

**Epicycle**:
* Greek meaning: upon the circle (i.e. circle moving on another circle)
* Use: used by ancient Greek to:
  * Explain the variations in speed and direction of the apparent motion of the planets
  * Explain changes in the distance of the planets from the Earth

**Mathematical formalism**:
* Informal: any path - periodic or not, closed or open - can be represented with an infinite number of epicycles
* Formal:
  * Assumptions:
    * $z_0 = a_0 e^{i k_0 t}$ correspond to a deferent centered on the origin of the complex plane and revolving with radius $a_0$ and angular velocity $k_0 = \frac{2 \pi}{T}$
      * $t$ is time
      * $T$ is the period
  * Observations:
    * If $z_1$ is the path of an epicycle
    
    $\hspace{1.0cm} \rightarrow$ The deferent plus epicycle is represented as $z_2 = z_0 + z_1 = a_0 e^{i k_0 t} + a_1 e^{o k_1 t}$
  * Conclusion:
    * $z_N = \sum_{j = 0}^N a_j e^{i k_j t}$ represents the deferent plus $N$ epicycles
    * Periodicity of $z_N$:
      * $z_N$ is almost periodic
      * $z_N$ is periodic just when every pair of $k_j$ is rationally related (i.e. $k_j / k_i \in \textbf{R}$ $\forall (i, j)$)

---

# BONUS
* Apparent retrograde motion
  * Retrograde ("retro" = "backward" and "gradus" = "step"): an adjective used to describe the path of a planet as it travels through the night sky
    * Retrograde in apparent retrograde motion: the planets, as they appear from Earth, to stop briefly and reverse direction at certain times
  * Apparent motion:
    * Example: 
      * Standing on the Earth, looking up at the sky, the moon travels from east to west
    
      $\hspace{1.0cm} \rightarrow$ The motion of the moon from east to west is a westward apparent motion (from Earth)
      * In fact, the both Earth and the Moon rotates from west to east, but the Earth completes one rotation period before the Moon
      
      $\hspace{1.0cm} \rightarrow$ It looks like the Moon is traveling in the opposite direction (i.e. from east to west)
    * Apparent retrograde motion: the motion of a planet, when watching from some other planet
* Apparent distance of two point objects, as viewed from some other location: the angle of length between two directions originating from the observer and pointing toward the point objects

# NEW WORD
* Move against some direction: di chuyển theo hướng nào đó
* Orbit (n): quỹ đạo

# Base knowledge
**Orthogonal signals**: $f$ and $g$ are orthogonal if they are mutually independent
* Inner produce of signal space: 
  * Idea: $\langle \textbf{u}, \textbf{v} \rangle = \sum_i u_i v_i$
  * Non-periodic signals: $\langle x_1, x_2 \rangle = \int_{-\infty}^\infty x_1(t) x_2^*(t) dt$
    * $x_2^*(t)$ means the complex conjugate of $x_2(t)$
    * Intuition: we treat $x_1, x_2$ with periodical signals with infinity period
  * Periodic signals: $\langle x_1, x_2 \rangle = \int_{0}^T x_1(t) x_2^*(t) dt$
* Orthogonal signals: two signals are orthogonal if their inner product is zero
  * Formal: $\langle x_1, x_2 \rangle = 0$
* Properties:
	* $\sin(n_1 x) \cos(n_2 x) = \frac{1}{2} (\sin((n_1 + n_2) x) + \sin(n_1 - n_2) x)$
		* $\int_0^{2 \pi} \sin((n_1 - n_2) x) dx = 0$
		* $\int_0^{2 \pi} \sin((n_1 + n_2) x) dx = 0$
		
		$\hspace{1.0cm} \rightarrow \sin(n_1 x)$ and $\cos(n_2 x)$ are orthogonal for all $n_1, n_2$
		
		$\implies \sin(n_1 x)$ and $\cos(n_2 x)$ are orthogonal for all $n_1, n_2$
	* $\cos(n_1 x) \cos(n_2 x) = \frac{1}{2} (\cos((n_1 + n_2) x) + \cos(n_1 - n_2) x)$
		* If $n_1 = n_2$: $\cos(n_1 - n_2) x)$ equals to $1$ for all $x \in [0, 2\pi]$ and $(\cos((n_1 + n_2) x)$ integrates to $0$ over $x \in [0, 2\pi]$
		
		>**NOTE**: in the case where $n_1 = -n_2$, $\cos(n_1 x) \cos(-n_1 x) = \cos(n_1 x) \cos(n_1 x)$, which is the inner product of two signals with the same frequency $n_1$
		
		$\hspace{1.0cm} \rightarrow$ The result is the same as when $n_1 = n_2$
		
		* If $|n_1| \neq |n_2|$: both $\cos((n_1 + n_2) x)$ and $\cos(n_1 - n_2) x$ integrate to $0$ over $x \in [0, 2\pi]$
		
		$\implies \cos(n_1 x)$ and $\cos(n_2 x)$ are orthogonal when $|n_1| = |n_2|$
	* $\sin(n_1 x) \sin(n_2 x) = \frac{1}{2} (\cos((n_1 + n_2) x) - \cos(n_1 - n_2) x)$
		* If $n_1 = n_2$: $\cos(n_1 - n_2) x)$ equals to $1$ for all $x \in [0, 2\pi]$ $(\cos((n_1 + n_2) x)$ integrates to $0$ over $x \in [0, 2\pi]$
		
		>**NOTE**: in the case where $n_1 = -n_2$, $\sin(n_1 x) \sin(-n_1 x) = - \sin(n_1 x) \sin(n_1 x)$, which is the negative of the inner product of two signals with the same frequency $n_1$
		
		$\hspace{1.0cm} \rightarrow$ The result is the same as when $n_1 = n_2$
		
		* If $|n_1| \neq |n_2|$: both $\cos((n_1 + n_2) x)$ and $\cos(n_1 - n_2) x$ integrate to $0$ over $x \in [0, 2\pi]$
		
		$\implies \sin(n_1 x)$ and $\sin(n_2 x)$ are orthogonal when $|n_1| = |n_2|$
	* $e^{i n_1 x} (e^{i n_2 x})^*$:
		* The complex conjugate of $e^{i n_2 x}$: $\cos(n_2 x) - i \sin(n_2 x) = \cos(- n_2 x) + i \sin(- n_2 x) = e^{-i n_2 x}$
		
		$\hspace{1.0cm} \rightarrow e^{i n_1 x} (e^{i n_2 x})^* = e^{i n_1 x} e^{- i n_2 x} = e^{i (n_1 - n_2) x} = \cos((n_1 - n_2) x) + i \sin((n_1 - n_2) x)$
		* If $n_1 = n_2$:
			* $\cos((n_1 - n_2) x) = 1$ for all $x \in [0, 2\pi]$
			* $\sin((n_1 - n_2) x) = 0$ for all $x \in [0, 2\pi]$
		* If $n_1 \neq n_2$:
			* $\sin((n_1 - n_2) x)$ integrates to $0$ over $x \in [0, 2\pi]$
			* $\cos((n_1 - n_2) x)$ integrates to $0$ over $x \in [0, 2\pi]$
		
		$\implies e^{i n_1 x}$ and $e^{i n_2 x}$ are orthogonal when $|n_1| = |n_2|$
	* (Most important) if $x_1(t)$ and $x_2(t)$ are orthogonal and $y = x_1 + x_2$
		* If $y, x_1, x_2$ are power signals
		
		$\hspace{1.0cm} \rightarrow P_y = P_{x_1} + P_{x_2}$ where $P_x$ is the power of $x$
		* If $y, x_1, x_2$ are energy signals
		
		$\hspace{1.0cm} \rightarrow E_y = E_{x_1} + E_{x_2}$ where $E_x$ is the energy of $x$

# Fourier series
**Introduction**: a way to decompose any periodic function (or signal) into the weighted sum of a (possibly infinite)  set of simple sine waves

**History**:
* How was Fourier series was introduced: Joseph Fourier introduced the series for the purpose of solving the heat equation in a metal plate
  * Fourier's result: an arbitrary continuous function can be represented by a trigonometric series
  * Heat equation: a partial differential equation
    * Solution of the PDE: if the heat source behaved in a simple way (i.e. was a sine or cosine wave)
    
    $\hspace{1.0cm} \rightarrow$ Particular solutions of the PDE were known and called "eigensolutions"
    * Fourier's idea: model a complicated heat source as a linear combination of simple sine and cosine waves
      * Solution of the heat equation: a linear combination of corresponding eigensolutions
    * Fourier series: the linear combination of corresponding eigensolutions mentioned above
* The idea of decomposing a periodic function into the sum of simple oscillating functions: date back to the 3rd century, when ancient astronomers proposed an empiric model of planetary motions, based on deferents and epicycles (see above)

**Definition**:
* Assumptions:
  * $s(x)$ is a function of the real variable $x$
    * $s$ is integrable on interval $[x_0, x_0 + P]$ for real numbers $x_0$ and $P$
  * $s$ is periodic with period $P$ outside $[x_0, x_0 + P]$
* Conclusion:
  * Fourier series approximation of $s$: 
  
  $\hspace{1.0cm} s_N(x) = \frac{A_0}{2} + \sum_{n = 1}^N A_n \sin(\frac{2 \pi n x}{P} + \phi_n)$ where $N \geq 1$
  
  $\hspace{2.3cm} = a_0/2 + \sum_{n = 1}^N (a_n \cos(\frac{2 \pi n x}{P}) + b_n \sin(\frac{2 \pi n x}{P}))$ where $a_n = A_n \sin(\phi_n), b_n = A_n \cos(\phi_n)$
  
  $\hspace{2.3cm} = \sum_{n = -N}^N c_n e^{i \frac{2 \pi n x}{P}}$
  * Fourier coefficients: $a_n, b_n, c_n$
    * $a_n = \frac{2}{P} \int_{x_0}^{x_0 + P} s(x) \cos(\frac{2 \pi n x}{P}) dx$
    * $b_n = \frac{2}{P} \int_{x_0}^{x_0 + P} s(x) \sin(\frac{2 \pi n x}{P}) dx$
    * $c_n = \frac{1}{P} \int_{x_0}^{x_0 + P} s(x) e^{-i \frac{2 \pi n x}{P}} dx$
  * Fourier series representation of $s$: $s_N(x)$ where $N \to \infty$

**Intuition**: via Fourier's point of view
* Fourier's problem: solve the heat equation (i.e. a partial equation)
	* Informal problem:
		* Difficulty: up to Fourier's time, only heat equations corresponding to heat sources characterized by sine and cosine waves can be solved
		* Fourier's idea: how to find a way to decompose a function $s$, that characterizes a heat source, into sine and cosine waves
		
		$\hspace{1.0cm} \rightarrow$ So that Fourier can transform the problem of solving heat equations corresponding to general heat sources, which is hard, into problem of solving heat equations corresponding to heat sources characterized by sine and cosine waves, which is much easier
	* Formal problem:
		* Assumptions:
      * $s(x)$is a function of the real variable $x$
            * $s$ is integrable on interval $[x_0, x_0 + P]$ for real numbers $x_0$ and $P$
      * $s$ is periodic with period $P$ outside $[x_0, x_0 + P]$
      * $s$ can be approximated by $a_0/2 + \sum_{n = 1}^\infty a_n \cos(\frac{2\pi n x}{P}) + \sum_{n = 1}^\infty b_n \sin(\frac{2\pi n x}{P})$
		* Task:
			* Find the coefficients $a_0, a_1, ...$ and $b_1, b_2, ...$ that: $s(x) \approx a_0/2 + \sum_{n = 1}^\infty a_n \cos(\frac{2\pi n x}{P}) + \sum_{n = 1}^\infty b_n \sin(\frac{2\pi n x}{P})$
			
			>**NOTE**: writing $a_0/2$ or $a_0$ doesn't change the essence of this problem, $a_0/2$ is chosen for simplicity of further formulas
* Observations:
	* $\sin(x)$ and $\cos(x)$ are orthogonal signals
	* $\cos(x)$ and $\cos(y)$ are orthogonal signals for all $x \neq y$
	* From above, we can find $a_n$ and $b_n$ as following:
		* Find $a_k$: we multiply two sides by $\cos(\frac{2\pi k x}{P})$, which cancels out all $\cos(\frac{2\pi n x}{P})$ with $n \neq k$ and all $\sin(\frac{2\pi n x}{P})$
		
		$\hspace{1.0cm} \int_{x_0}^{x_0 + P} s(x) \cos(\frac{2\pi k x}{P}) dx \approx a_0/2 \int_{x_0}^{x_0 + P} \cos(\frac{2\pi k x}{P}) dx + \sum_{n = 1}^\infty a_n \int_{x_0}^{x_0 + P} \cos(\frac{2\pi n x}{P}) \cos(\frac{2\pi k x}{P}) dx + \sum_{n = 1}^\infty b_n \int_{x_0}^{x_0 + P} \sin(\frac{2\pi n x}{P}) \cos(\frac{2\pi k x}{P}) dx$
		
		$\hspace{1.0cm} \int_{x_0}^{x_0 + P} s(x) \cos(\frac{2\pi k x}{P}) dx \approx a_k \int_{x_0}^{x_0 + P} \cos(\frac{2\pi k x}{P})^2 dx$
		
		$\hspace{1.0cm}$ We got: $\int_{x_0}^{x_0 + P} \cos(\frac{2\pi k x}{P})^2 dx = \frac{1}{4} \sin(\frac{4\pi k (x_0 + P)}{P}) + \frac{x_0 + P}{2} - \frac{1}{4} \sin(\frac{4\pi k x_0}{P}) + \frac{x_0}{2} = \frac{P}{2}$
		
		$\hspace{2.0cm} \rightarrow \int_{x_0}^{x_0 + P} s(x) \cos(\frac{2\pi k x}{P}) dx \approx a_k \frac{P}{2}$
		
		$\implies a_k \approx \frac{2}{P} \int_{x_0}^{x_0 + P} s(x) \cos(\frac{2\pi k x}{P}) dx$
		* Find $b_k$: similar to finding $a_k$
		
		$\implies b_k \approx \frac{2}{P} \int_{x_0}^{x_0 + P} s(x) \sin(\frac{2\pi k x}{P}) dx$
* Fourier's series in complex form: $s(x) \approx \sum_{n = -\infty}^\infty c_n e^{i \frac{2\pi n x}{P}}$
	* Essence: the same as the original idea of Fourier (i.e. decompose a signal into sine and cosine signals)
		* Explain: due to Euler's formula: $e^{ix} = \cos(x) + i \sin(x)$
  
  * Observation: $e^{i \frac{2\pi k_1 x}{P}}$ and $e^{i \frac{2\pi k_2 x}{P}}$ are orthogonal for all $k_1 \neq k_2$
	* Find $c_k$: we multiply two sides by $e^{-i \frac{2\pi k x}{P}}$, which cancels out all $e^{i \frac{2\pi n x}{P}}$ with $n \neq k$ and convert $a_k e^{i \frac{2\pi k x}{P}}$ into $a_k$
	
	$\implies c_n = \frac{1}{P} \int_{x_0}^{x_0 + P} s(x) e^{-i \frac{2\pi n x}{P}} dx$

**Parseval formula**: 
* Assumptions: 
	* $s(x)$ is a function
		* $P$ is the fundamental period of $s(x)$
	* $s_\infty(x)$ is the Fourier series representation of $s(x)$
		* Formal: $s_\infty(x) = \sum_{n = -\infty}^\infty c_n e^{i \frac{2\pi n x}{P}}$
* Conclusion:
	* $\frac{1}{P} \int_0^P s(x) s^*(x) dx = \sum_{n = -\infty}^\infty c_n c_n^*$

* Explain: easy to prove
* Intuition:
	* $\frac{1}{P} \int_0^P c_n e^{i \frac{2\pi n x}{P}} (c_n e^{i \frac{2\pi n x}{P}})^* dx = \frac{1}{P} \int_0^P |c_n|^2 dx = |c_n|^2$ where $|c_n| = \sqrt{\text{Re}(c_n)^2 + \text{Im}(c_n)^2}$
	
	$\hspace{1.0cm} \rightarrow$ The power of the component $c_n e^{i \frac{2\pi n x}{P}}$ is $|c_n|^2$
	* From above, Parseval formula states that the power of a signal, in time domain, equals to the power of that signal, in frequency domain
* Geometric interpretation of Parseval's formula:
	* Consider $s_\infty(x)$ as a vector in some vector space
	* $s_\infty(x)$ is the sum of orthogonal vectors $c_n e^{i \frac{2\pi n x}{P}}$
	
	$\hspace{1.0cm} \rightarrow$ By Pythagora's theorem, $\|s_\infty(x)\|_2^2 = \sum_{n = -\infty}^\infty \|c_n e^{i \frac{2\pi n x}{P}}\|_2^2$

**Power spectrum of $s(x)$**: the plot of $|c_k|^2$ against the frequencies
* Usage: answer the question "how much power is contained in the frequency components of the signal"
* The power spectrum of a periodic signal is a function of discrete frequencies
* Properties:
  * Statement:
    * The power spectrum of a periodic signal $x(t)$ is an even function
      * Explain: $|c_k|^2 = |c_{-k}|^2$ where $|c_k| = \sqrt{\text{Re}(c_k)^2 + \text{Im}(c_k)^2}$
    * If $s(x)$ is real-valued and even

    $\hspace{1.0cm} \rightarrow c_k = c_{-k}$ $\forall k$
    * If $s(x)$ is real-valued and odd

    $\hspace{1.0cm} \rightarrow c_k = -c_{-k}$ $\forall k$

# Convergence of Fourier series representation

>**NOTE**: the fact that any periodic signal could be represented by a Fourier series isn't quite true

$\hspace{1.0cm} \rightarrow$ The true statement is that Fourier series can be used to represent an extremely large class of periodic signals

**Convergence analysis**:
* Assumptions:
  * $s(x)$ is a periodic function
  * $s_N(x) = \sum_{n = -N}^N c_n e^{i \frac{2\pi n x}{P}}$
  * $e_N(x) = s(x) - s_N(x)$ is the approximation error
  * $E_N = \int_{x_0}^{x_0 + P} |e_N(x)|^2 dx$ is a quantitative measure of the size of $e_N(x)$
    * $E_N$, in fact, is the energy in the error over one period
* Minimizing $E_N$: $c_n = \frac{1}{P} \int_{x_0}^{x_0 + P} s(x) e^{-i\frac{2\pi n x}{P}} dx$ is the particular choice for $c_n$ that minimizes $E_N$
* Observations:
  * In some cases, the integral $\int_{x_0}^{x_0 + P} s(x) e^{-i\frac{2\pi n x}{P}} dx$ may diverge
  
  $\hspace{1.0cm} \rightarrow c_n$ may be infinite
  * Even when $c_n$ is finite for all $n$, $s_N(x)$ may not converge to $s(x)$


**Dirichlet conditions**: 
* Usage:
	* Sufficient conditions for $s(x)$ to be equal to $s_N$ representation at each point where $s$ is continuous
	* The behavior of $s_N$ at points of discontinuity is determined (i.e. it's the midpoint of the values of the discontinuity)
* Conditions:
  * $s$ must be absolutely integrable over a period
    * Formal: $\int_{x_0}^{x_0 + P} |s(x)|$ is finite
    * Corollary: $c_n$ is finite for all $n$
  * $s$ is of bounded variation
    * Explain: $s$ must have a finite number of extrema in any given bounded interval
  * $s$ must have a finite number of discontinuities in any given bounded interval and each of these discontinuities is finite
    * Finite discontinuity: $f$ has a finite discontinuity at $x_0 \in \textbf{dom } f$ if both $\lim_{x \to x_0^-} f(x)$ and $\lim_{x \to x_0^+} f(x)$ exist
      * Intuition: the jump over the discontinuity is a finite jump

**Convergence of Fourier series representation in practice**: signals don't satisfy the Dirichlet conditions are generally pathological in nature

$\hspace{1.0cm} \rightarrow$ Such signal dont typically arise in practical contexts
* Corollary: the question of the convergence of Fourier series won't play a particular significant role from now on

---

# BONUS
* Square-integrable function: $f$ is square-integrable if $\int_{-\infty}^\infty |f(x)|^2 dx < \infty$
* Trigonometric series: $\frac{A_0}{2} + \sum_{n = 1}^\infty (A_n \cos nx + B_n \sin nx)$
  * Fourier series in terms of trigonometric series: Fourier series is a special case of trigonometric series, where
    * $A_n = \frac{1}{\pi} \int_0^{2 \pi} f(x) \cos nx dx$
    * $B_n = \frac{1}{\pi} \int_0^{2 \pi} f(x) \sin nx dx$
* Frequency domain and time domain:
	* Time-domain graph: show how a signal changes over time
	* Frequency-domain graph: show how much of the signal lies within each given frequency band over a range of frequency
* Fourier series and Fourier transform:
	* Usages:
		* Fourier series: used to represent a periodic function by a discrete sum of complex exponentials
		* Fourier transform: used to represent a general, non-periodic function by an integral of complex exponentials
	* Fourier transform via Fourier series: Fourier transform can be viewed as the limt of the Fourier series of a function, with period $P$ approaches infinity

# NEW WORD
* Oscillating (adj): dao động
* Pathological (adj): bệnh lý