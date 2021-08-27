<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Floating point arithmetic](#floating-point-arithmetic)
- [BONUS](#bonus)
<!-- /TOC -->

# Floating point arithmetic
**Machine epsilon**: the difference between $1$ and the closest floating-point number larger than $1$

$\hspace{1.0cm} \rightarrow$ If $|x - y|$ is less than the machine epsilon then the computer may think $x = y$

**Round-off error**: the error when representing a floating-point number in computer, due to limited precision

**Floating-point problems**:
* Round-off errors can accumulate (or propagate)
  * Explain: the more operators are carried out, the more serious roundoff error
* Subtraction of very close numbers can cause serious problems for numerical methods
  * The golden rule of numerical analysis: don't subtract nearly equal numbers

**Using floating-point numbers in calculations**:
* Single-precision (i.e. float32 in NumPy):
  * Structure: $24$ bits for the mantissa and $8$ bits for the exponent
  * Representation limit:
    * Precision: $6$ digits of precision
    * Magnitude: from $10^{-128}$ upto $10^{127}$
  * Advantage: reduce space complexity twice and a little runtime complexity
* Quadruple-precision (i.e. float128 in NumPy):
  * Disadvantage: significant slowdown in computations
    * Explain: float128 are implemented in software, instead of hardware
* Double-precision (i.e. float64 in NumPy): used in most scientific calculations

---

# BONUS
* Stable numerical methods: numerical methods that aren't seriously affected by roundoff error