<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Definition](#definition)
- [Matrix norm induced by vector norms](#matrix-norm-induced-by-vector-norms)
- [Entry-wise matrix norms](#entry-wise-matrix-norms)
- [BONUS](#bonus)
<!-- /TOC -->

# Definition
**Assumptions**:
* $K$ is a field of either real or complex numbers

**Matrix norm**: a norm on $K^{m \times n}$
* Notation: $\|\cdot\|: K^{m \times n} \to \textbf{R}$
* Properties: for all scalars $\alpha \in K$ and for all matrices $A, B \in K^{m \times n}$, a norm must satisfy
  * $\|\alpha A\| = |\alpha| \|A\|$
  * $\|A + B\| \leq \|A\| + \|B\|$
  * $\|A\| \geq 0$
  * $\|A\| = 0$ if $\|A\| = 0_{m, n}$

**Sub-multiplicative norm**: $\|A B\|_q \leq \|A\|_p \|B\|_q$
* $A \in K^{m \times n}$
* $B \in K^{n \times k}$
* $\|\cdot\|_p, \|\cdot\|_q$ are norms induced from $K^n$ and $K^k$
* $p, q \geq 1$

**Consistent norms**: $\|\cdot\|$ on $K^{m \times n}$) is consistent with a $\|\cdot\|_a$ on $K^n$ and $\|\cdot\|_b$ on $K^m$ if $\|Ax\|_b \leq \|A\| \|x\|_a$ $\forall A \in K^{m \times n}, x \in K^n$
* Compatible norm: special case of consistent norms when $a = b$

>**NOTE**: in some books, matrix norm refers to only sub-multiplicative norm

# Matrix norm induced by vector norms
**Assumptions**:
* $\|\cdot\|$ is a vector norm defined on $K^d$
* $A$ is a $m \times n$ matrix (i.e. $A$ induces a linear operator from $K^n$ to $K^m$ w.r.t the standard basis)

**The corresponding induced norm (or operator norm) on $K^{m \times n}$**: $\|A\| = \sup \{\|Ax\|:x \in K^n, \|x\| = 1\} = \sup \{\frac{\|Ax\|}{\|x\|}:x \in K^n, x \neq 0\}$

**Matrix norm induced by $p$-norm for vectors**: $\|A\|_p = \sup_{x \neq 0} \frac{\|Ax\|_p}{\|x\|_p}$
* Special cases:
  * $\|A\|_1 = \max_{1 \leq j \leq n} \sum_{i = 1}^m |a_{ij}|$
  * $\|A\|_2 = \sigma_\max(A)$ where $\sigma_\max(A)$ is the largest singular value of $A$

# Entry-wise matrix norms
**Idea**: treat an $m \times n$ matrix as a vector of size $m n$

$\hspace{1.0cm} \rightarrow \|A\|_p = \|\text{vec }(A)\|_p = (\sum_{i=1}^m \sum_{j=1}^n |a_{ij}|^p)^{1/p}$

**L_{p, q} norms**: $\|A\|_{p, q} = (\sum_{j=1}^n (\sum_{i=1}^m |a_{ij}|^p)^{q/p})^{1/q}$

>**NOTE**: $p, q \geq 1$

**Frobenius norm (or Hilbert-Schmidt norm)**: 
* Formulas: 
  * $\|A\|_F = \|A\|_2$
  * $\|A\|_F = \sqrt{\sum_{i=1}^{\min(m, n)} \sigma_i^2(A)}$ where $\sigma_i(A)$ are singular values of $A$
* Motivation: Frobenius inner product
* Properties:
  * Sub-multiplicative
  * Invariant under rotations
    * Formal: $\|A\|_F^2 = \|A R\|_F^2 = \|R A\|_F^2$ for any rotation matrix $R$
  * $\|A^T A\|_F = \|A A^T\|_F \leq \|A\|_F^2$
  * $\|A + B\|_F^2 = \|A\|_F^2 + \|B\|_F^2 + 2 \langle A, B \rangle_F$
* Advantages over induced norm: easier to compute

$\hspace{1.0cm} \rightarrow$ Very useful for numerical linear algebra

**Max norm**: $\|A\|_\max = \max_{ij} |a_{ij}|$

---

# BONUS
* Field: a set, on which addition, subtraction, multiplication and division are defined
* Frobenius inner product: $\langle \textbf{A}, \textbf{B} \rangle_F = \sum_{i, j} \bar{A}_{ij} B_{ij}$
  * $A, B$ are $m \times n$ matrices
  * $\bar{A}_{ij}$ is the complex conjugate of $A_{ij}$