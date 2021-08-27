<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Right-angled triangle definitions](#right-angled-triangle-definitions)
- [Rise, run and slope of line segment definition](#rise-run-and-slope-of-line-segment-definition)
- [Definition via differential equations](#definition-via-differential-equations)
- [Series definition](#series-definition)
- [Properties](#properties)
- [NEW WORD](#new-word)
<!-- /TOC -->

# Introduction
**Other names**: 
  * Circular functions
  * Angle functions
  * Goniometric functions

**Informal definition**: functions of an angle, which relate the angles of a triangle to the length of its side

# Right-angled triangle definitions
**Assumptions**:
* $ABC$ is a right triangle
* $h = AB$ is the hypotenuse
* $a = BC$ is the opposite side of angle $A$
* $b = AC$ is the adjacent side of angle $A$

**Sine, cosine and tangent**:
* Sine: $\sin A = \frac{a}{h}$
  * "Sine": come from "sinus" (Latin), which means "bay" in English
  
  $\hspace{1.0cm} \rightarrow$ The opposide side is the side of the triangle, on which $A$ opens
* Cosine (complement-sine): $\cos A = \frac{b}{h}$
  * "Complement": 
    * $\cos \theta = \sin (\frac{\pi}{2} - \theta)$
    * $\sin \theta = \cos (\frac{\pi}{2} - \theta)$
* Tangent: $\tan A = \frac{a}{b} = \frac{\sin A}{\cos A}$
  * "Tangent": $\tan A$ can be represented as the slope of a line segment tangent to some circle
* Cotan (complement-tangent): $\cot A = \frac{b}{a} = \frac{\cos A}{\sin A} = \frac{1}{\tan A}$
  * "Complement": 
    * $\cot \theta = \tan (\frac{\pi}{2} - \theta)$
    * $\tan \theta = \cot (\frac{\pi}{2} - \theta)$
* Remember: sin đi học (đối huyền), cos không hư (kề huyền), tan đoàn kết (đối kề), cotan kết đoàn (kề đối)

**Secant, cosecant**:
* Secant: $\sec A = \frac{1}{\cos A} = \frac{h}{b}$
  * "Secant": come from "secare" (Latin), which means cut in English
  
  $\hspace{1.0cm} \rightarrow$ Secant represents the secant line that cuts the circle
* Cosecant (complement secant): $\csc A = \frac{1}{\sin A} = \frac{h}{a}$

**Pythagorean identity**: $\cos^2 \theta + \sin^2 \theta = 1$

# Rise, run and slope of line segment definition
* Idea: $\text{slope} = \frac{\text{rise}}{\text{run}}$
* Sine ~ rise: Sine takes the angle of the line segment and tells its vertical rise when the length of the line is $1$
* Cos ~ run: Cosine takes the angle of the line segment and tells its horizontal run when the length of the line is $1$
* Tangent ~ slope: Tangent takes the angle of the line segment and tells its slope (i.e. the vertical rise when the line segment's horizontal run is $1$)

# Definition via differential equations
**Sine**: $y'' = -y$ 
  * Initial conditions: $y'(0) = 1$ and $y(0) = 0$
  * Solve:
    * Guess the form of $y$: $y = e^{ax}$ where $a \in \textbf{C}$
    * $y'' + y = 0 \leftrightarrow a^2 e^{ax} + e^{ax} = 0$
    
    $\hspace{3.2cm} \leftrightarrow a = \pm i$
    * From above, the general form of $y$ is $y = c_1 e^{ix} + c_2 e^{-ix}$
    * $\begin{cases} y(0) = 0 \\ y'(0) = 1 \end{cases} \leftrightarrow \begin{cases} c_1 + c_2 = 0 \\ c_1 - c_2 = 1/i \end{cases}$
    
    $\hspace{3.5cm} \leftrightarrow \begin{cases} c_1 = \frac{1}{2i} \\ c_2 = \frac{-1}{2i} \end{cases}$
    * From above, $y = \frac{e^{ix} - e^{-ix}}{2i}$

**Cosine**: $y'' = -y$ 
  * Initial conditions: $y'(0) = 0$ and $y(0) = 1$
  * Solve: similar to above
    * $y = \frac{e^{ix} + e^{-ix}}{2}$

# Series definition
**Relationship to exponential function and complex number**
* Assumptions:
  * $x$ is a real number
* Conclusion:
  * $\cos x = \text{Re}(e^{ix})$
    * Intuition: unit circle in complex plane
  * $\sin x = \text{Im}(e^{ix})$
    * Intuition: unit circle in complex plane
  * Euler formula: $e^{ix} = \cos x + i \sin x$
    * Prove: see the definition of sine and cosine function via differential equations
* Corollary of Euler's formula:
  * $\sin x = \frac{e^{ix} - e^{-ix}}{2i}$
  * $\cos x = \frac{e^{ix} + e^{-ix}}{2}$

**Series definition of trigonometric functions**:
* Sine: $\sin x = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + ...$

$\hspace{1.9cm} = \sum_{n=0}^\infty (-1)^n \frac{x^{2n+1}}{(2n+1)!}$
* Cosine: $\cos x = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + ...$

$\hspace{2.4cm} = \sum_{n=0}^\infty (-1)^n \frac{x^{2n}}{(2n)!}$
* Explain: based on Euler's formula
  * $e^{ix} = \sum_{k=0}^\infty \frac{(ix)^k}{k!} = 1 + ix - \frac{x^2}{2!} - \frac{i x^3}{3!} + \frac{x^4}{4!} + \frac{i x^5}{5!} - \frac{x^6}{6!} ...$
  * $e^{-ix} = \sum_{k=0}^\infty \frac{(-ix)^k}{k!} = 1 - ix - \frac{x^2}{2!} + \frac{i x^3}{3!} + \frac{x^4}{4!} - \frac{i x^5}{5!} - \frac{x^6}{6!} + ...$
  * $\sin x = \frac{1}{2i}(e^{ix} - e^{-ix}) = \frac{1}{2i}(2ix - 2 \frac{ix^3}{3!} + 2 \frac{ix^5}{5!} - ...) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - ...$
  * $\cos x = \frac{1}{2}(e^{ix} + e^{-ix}) = \frac{1}{2}(2 - 2 \frac{x^2}{2!} + 2 \frac{x^4}{4!} - ...) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - ...$

# Properties
**Law of sines**: $\frac{\sin A}{a} = \frac{\sin B}{b} = \frac{\sin C}{c} = \frac{1}{h}$ where $h$ is the hypotenuse of $\Delta ABC$
  * $a, b, c$ are the opposite sides of $A, B, C$ respectively

**Law of cosines**: $c^2 = a^2 + b^2 - 2ab \cos C$ (or equivalently $\cos C = \frac{a^2 + b^2 - c^2}{2ab}$)

**Connection to inner product**: $\cos \text{angle}(x, y) = \frac{\langle x, y \rangle}{\|x\| \|y\|}$

---

# NEW WORD
* Right angle (n): góc vuông
* Hypotenuse (n): cạnh huyền
* Opposite side (n): cạnh đối
* Adjacent side (n): cạnh kề