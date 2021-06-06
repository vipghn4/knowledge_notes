---
title: Orthogonal transforms
tags: Video streaming
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
* [Orthogonal transforms](#orthogonal-transforms)
  * [Orthogonal transform](#orthogonal-transform)
  * [Karhunen-Loeve transform (KLT)](#karhunen-loeve-transform-klt)
  * [Separable transform](#separable-transform)
* [Appendix](#appendix)
  * [Concepts](#concepts)
<!-- /TOC -->

# Orthogonal transforms
## Orthogonal transform
**History**. During the late 1960s and early 1970s, there was a great deal of research activity related to digital orthogonal transforms and their use for image data compression

$\to$ There were a large number of transforms being introduced with claims of better performance relative to other transforms
* *Benchmark method*.
    * *Qualitative method*. Comparisons were made on qualitative basis, by viewing a set of standard images, which had been subjected to data compression using transform coding techniques
    * *Quantitative method*. At the same time, a number of researchers were doing some excellent work on making comparisons on quantitative basis
        * *Explain*. The variance criterion and the rate distortion criterion were developed and used extensively as performance measures for evaluating image data compression

**Orthogonal transforms**.
* *Assumptions*.
    * $\mathbf{x}$ is a flattened image block of size $N\times N$
    * $\mathbf{A}$ is a $N^2\times N^2$ orthonormal transformation matrix
    * $\mathbf{y}$ is the flattened transformed image block of size $N\times N$
* *Orthogonal transforms*.
    * *Forward transform*. $\mathbf{y}=\mathbf{A}\mathbf{x}$
    * *Inverse transform*. $\mathbf{x}=\mathbf{A}^T \mathbf{y}$
* *Basis functions*. Columns of $\mathbf{A}$
* *Example*. DCT in JPEG compression

**Benefits of orthogonal transforms**. No need to find the inverse transformation matrix

$\to$ Just take $\mathbf{A}^T$

**Block transform for image compression**.
* *Data flow*.
    1. Divide the input image into transform blocks
    2. Perform orthogonal transforms on each block
    3. Quantize the coefficients using the transform coefficients as a unit
    4. Encode the quantized coefficients using an entropy encoder
* *Motivations*. Neighboring image pixels nearby each other in horizontal and vertical directions have high correlation with each other

    $\to$ We need to remove such correlations, i.e. remove information redundancy
    * *Idea*. Divide the image of size $K_1\times K_2$ into blocks of size $N_1\times N_2$
* *Benefits*. Reduce the computational complexity of orthogonal transform

**Energy conservation**. $\|\mathbf{y}\|^2 = \|\mathbf{x}\|^2$

<div style="text-align:center">
    <img src="/media/oxRfpU3.png">
    <figcaption>2D orthogonal transform</figcaption>
</div>

* *Energy distribution*. Energy is unevenly distributed among coefficients
* *Ideal case*. Most of the energy concentrate on as few components as possible

    $\to$ We can maximize the number of components to be removed (or compressed)
* *Consequences*. The idea of optimal orthogonal transform is like PCA for data compression
    * We want to decorrelate the entries of the output coefficients
        * *Explain*. To remove information redundancy between output entries
    * We want the energy to concentrate on as few dimensions as possible
        * *Explain*. We can remove low-energy entries of the output block

## Karhunen-Loeve transform (KLT)
**Optimal orthogonal transform**. Reduce the correlation, i.e. decorrelate, among the $N$ pixels in each block to the greatest extent
* *Measure of correlation between two pixels*. Use covariance between input pixels, or output pixels
* *Covariance matrix*. $\Sigma_y=\mathbf{A} \Sigma_x \mathbf{A}^T$

**KLT**. Exploit the same idea as PCA
* *Idea*. Since $\Sigma_x$ is a symmetric matrix

    $\to$ We can diagonalize it as $\Sigma_x = \mathbf{A}^T \Sigma_y \mathbf{A}$ and yield $\mathbf{y}$ with fully decorrelated entries
* *Requirements*.
    * $\Sigma_x$ has $N$ real numbered eigenvalues

        $\to$ There are also $N$ corresponding eigenvectors $\mathbf{a}_1,\dots,\mathbf{a}_N$ forming the matrix $\mathbf{A}$
    * $\forall i\in\{1,\dots,N\},\|\mathbf{a}_i\| = 1$ must be satisfied
* *Drawbacks*.
    * Depend on signal statistics
    * Not separable for image blocks

        $\to$ Individual image blocks cannot be coded efficiently
    * Transform matrix cannot be factored into sparse matrices
    * Large computational complexity
* *Idea for improvement*. Find structured transforms which can approximate KLT

    $\to$ This is the motivation of DCT

**KLT and MSE**. Suppose that we truncate the last coefficients of $\mathbf{y}$ and transmit only the first $p$ coefficients
* *MSE between original and reconstructed signals*.
    * *Assumptions*.
        *  $\mathbf{x}$ has zero mean, i.e. this can be explicitly implemented

            $\to$ $E(\mathbf{y})=A\cdot E(\mathbf{x})=\mathbf{0}$
    * *Conclusion*.

        $$\begin{aligned}
        E[\frac{1}{N} \sum_{i=1}^N (\mathbf{x}_i - \hat{\mathbf{x}}_i)^2]&=\frac{1}{N} E[(\mathbf{x}-\hat{\mathbf{x}})^T (\mathbf{x}-\hat{\mathbf{x}})]\\
        &=\frac{1}{N} E[(\mathbf{y}-\hat{\mathbf{y}})^T (\mathbf{y}-\hat{\mathbf{y}})]\\
        &=\frac{1}{N} \sum_{i=p+1}^N E(\mathbf{y}_i^2)\\
        &=\frac{1}{N} \sum_{i=p+1}^N \lambda_i
        \end{aligned}$$
* *Theorem*. KLT minimizes the MSE between the original signal and the reconstructed signal, i.e. $E[\frac{1}{N} \sum_{i=1}^N (\mathbf{x}_i - \hat{\mathbf{x}}_i)^2]$, given that only $p$ coefficients are kept for transmission
    * *Proof*. KLT is essentially PCA, which is a MSE minimizer
    * *Consequence*. KLT is the optimal transform w.r.t MSE
* *KLT as optimal transform*. KLT is optimal w.r.t the following performance measures
    * Variance distribution, i.e. estimated using MSE
    * Rate-distortion function

**Various improvements on orthonormal transforms**.
* Haar transform (1910)
* Walsh-Hadamard transform (1923)
* Slant transform (1971)
* Discrete cosine transform (DCT) (1974)

## Separable transform
**Separable transform**.
* *Assumptions*.
    * $\mathbf{y}$ is a $N\times N$ block of transform coefficients
    * $\mathbf{A}$ is orthonormal transform matrix of size $N\times N$
    * $\mathbf{x}$ is a $N\times N$ block of input signal
* *Separable transform*. A transform is separable if the transform of a $N\times N$ signal block can be expressed by

    $$\mathbf{y}=\mathbf{A}\mathbf{x}\mathbf{A}^T$$
* *Inverse transform*. $\mathbf{x}=\mathbf{A}^T \mathbf{y} \mathbf{A}$
* *Practical importance*. The transform requires 2 matrix multiplications of size $N\times N$, rather than one multiplication of a $1\times N^2$ vector with a $N^2\times N^2$ matrix

**Example**.

<div style="text-align:center">
    <img src="/media/tBoq6N5.png">
    <figcaption>Example of separable transform</figcaption>
</div>

# Appendix
## Concepts
**Rate-distortion theory**. Give an analytical expression for how much compression can be achieved using lossy compression methods
* *Distortion functions*. Measure the cost of representing a symbol $x$ by an approximated symbol $\hat{x}$
    * *Hamming distortion*. $d(x,\hat{x})=\begin{cases}0 & x = \hat{x}\\1 & x\neq \hat{x}\end{cases}$
    * *Squared-error distortion*. $d(x,\hat{x}) = \|x - \hat{x}\|_2^2$
* *Rate-distortion functions*.
    * *Assumptions*.
        * $Y$ is the communication channel output (compressed signal)
        * $X$ is the input (original signal)
        * $Q_{Y|X}(y|x)$ is a test channel, which is the conditional pdf of $Y$, for a given $X$
        * $I_Q(Y;X)$ is the mutual information between $Y$ and $X$
    * *Rate-distortion functions*. The functions relating the rate and distortion are found as the solution of the following minimization problem

        $$\text{minimize}_{Q_{Y|X}(y|x)} I_Q(Y;X) \text{ s.t. } D_Q \leq D^*$$
    * *Distortion between $X$ and $Y$ for a given $Q_{Y|X}(y|x)$*. $D_Q$ and $D^*$
        * *Formula*.

            $$\begin{aligned}
            D_Q&=\int_\infty^\infty \int_\infty^\infty P_{X,Y}(x,y) (x - y)^2 dx dy\\
            &=\int_\infty^\infty \int_\infty^\infty Q_{Y|X}(y|x) P_X(x) (x - y)^2 dx dy
            \end{aligned}$$

            where $D^*$ is a given distortio
