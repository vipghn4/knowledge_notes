<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Definitions](#definitions)
- [BONUS](#bonus)
<!-- /TOC -->

# Definitions
**Idea**: the exponential function arises whenever a quantity grows or decays at a rate proportional to its current value

**Definition via differential equations**: $y' = y$
* Initial condition: $y(0) = 1$

**Limit definition**: $e^x = \lim_{n \to \infty} (1 + \frac{x}{n})^n$
* Derivation:
  * $y(x) = y'(x) = \frac{y(x+h) - y(x)}{h}$ where $h \to 0$
  
  $\hspace{1.0cm} \rightarrow \frac{y(h) - y(0)}{h} = 1 \leftrightarrow y(h) - y(0) = h$
  
  $\hspace{4.1cm} \leftrightarrow y(h) = y(0) + h = (1 + h)$
  * $y(2h) = y(h) + y'(h) h = (1 + h) + (1 + h) h = (1 + h)^2$
  * By induction, given $y(kh) = (1 + h)^k$, 
  
  $\hspace{1.0cm} \rightarrow$ We can prove that $y((k+1)h) = (1 + h)^{k+1}$
  * From above, let $x = n h$ where $|n| \to \infty$ and $h \to 0$ be a finite constant
  
  $\hspace{1.0cm} \rightarrow e^x = y(n h) = \lim_{n \to \infty} (1 + h)^n = \lim_{n \to \infty} (1 + \frac{x}{n})^n$

**Series definition**: $e^x = \sum_{k=0}^\infty \frac{x^k}{k!}$
* Derivation:
  * $e^x = \lim_{n \to \infty} (1 + \frac{x}{n})^n = \sum_{k=0}^n {n \choose k} \frac{1}{n^k} x^k$
  * $\lim_{n \to \infty} {n \choose k} \frac{1}{n^k} = \lim_{n \to \infty} \frac{n!}{k! (n-k)! n^k} = \frac{1}{k!}$
  * From above, $e^x \approx \sum_{k=0}^\infty \frac{x^k}{k!}$
* Other derivation: take the Taylor approximation of $e^x$ around $x = 0$

---

# BONUS
* Constant $e$: $e = e^0 = \sum_{k=0}^\infty \frac{1}{k!}$
* **VERY IMPORTANT**: $e^{m n} = (e^m)^n$ only applies to $m, n \in \textbf{R}$