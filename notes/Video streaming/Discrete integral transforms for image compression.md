---
title: Discrete integral transforms for image compression
tags: Video streaming
---

# Table of Contents
[toc]

# Discrete integral transforms for image compression
## Integral transforms
**Integral transformation**. Also known as integral transform
* *Assumptions*.
    * $f(t)$ is a function to be mapped
    * $F(s)$ is the resulting function of the mapping
    * $K(s,t)$ is the kernel
* *Integral transformation*. A mapping from $f(t)$ to $F(s)$ using the formula of the form

    $$F(s)=\int_a^b K(s,t) f(t) dt$$

* *Applications*.
    * *Signal processing*. Image encoding
    * *Partial differential equation*. Convert a DE to an algebraic equation, which is much easier to solve
* *Choosing the appropriate integral transforms*. Determined by the boundary conditions

## Fourier sine and cosine transform
**Fourier sine and cosine transform**. Forms of the Fourier integral transform, which do not use complex numbers
* *Usage*. Originally used by Joseph Fourier and are still preferred in some applications, e.g. signal processing or statistics
* *Formulas*. Let $t$ represents time, and $\nu$ represents frequency, then
    * *Sine transform*. $\hat{f}^s(\nu) = {\cal{F}}_s(f)(\nu) = \int_{-\infty}^{\infty} f(t) \sin(2\pi\nu t) dt$

        $\to$ $\hat{f}^s(\nu)$ is an odd function of frequency, i.e. $\hat{f}^s(-\nu) = -\hat{f}^s(\nu)$
    * *Cosine transform*. $\hat{f}^c(\nu) = {\cal{F}}_c(f)(\nu) = \int_{-\infty}^{\infty} f(t) \cos(2\pi\nu t) dt$

        $\to$ $\hat{f}^c(\nu)$ is an even function of frequency,i.e. $\hat{f}^c(-\nu)=-\hat{f}^c(\nu)$
* *Relation with complex exponentials*.

    $$\begin{aligned}
    \hat{f}(\nu)&={\cal{F}}(f)(\nu)\\
    &=\int_{-\infty}^\infty f(t) e^{-2\pi i\nu t} dt\\
    &={\cal{F}}_c(f)(\nu)-i {\cal{F}}_s(f)(\nu)
    \end{aligned}$$

**Inversion transform**.
* *Fourier inversion transform (recall)*. $f(t)=\int_{-\infty}^{\infty} \hat{f}(\nu) e^{2\pi i t\nu} d\nu$
* *Inversion transform*.
    * *Formula*. When $f$ is a real-valued function of a real variable, then

        $$\begin{aligned}
        f(t)&=\int_{-\infty}^\infty \hat{f}^c(\nu) \cos(2\pi \nu t) d\nu + \int_{-\infty}^\infty \hat{f}^s(\nu) \sin(2\pi\nu t) d\nu\\
        &=\int_{-\infty}^\infty \int_{-\infty}^\infty f(x)\cos(2\pi\nu(x-t))dxd\nu
        \end{aligned}$$
    * *Derivation*. 

        $$\begin{aligned}
        f(t)&=\int_{-\infty}^\infty \hat{f}(\nu) e^{2\pi it\nu} d\nu\\
        &=\int_{-\infty}^\infty \int_{-\infty}^\infty f(x)e^{2\pi i\nu (t-x)}dxd\nu\\
        &=\int_{-\infty}^\infty \int_{-\infty}^\infty f(x) \cos (2\pi\nu (x-t))dxd\nu - i\int_{-\infty}^\infty \int_{-\infty}^\infty f(x) \sin (2\pi\nu (x-t))dxd\nu\\
        &=\int_{-\infty}^\infty \int_{-\infty}^\infty f(x) \cos (2\pi\nu (x-t))dxd\nu
        \end{aligned}$$
    * *Inversion transform of even functions*. If $f$ is an even function, then we obtain the cosine inversion transform from the inversion formula

        $\to$ Cosine transform implies an even extension of the original function
    * *Inversion transform of odd functions*. If $f$ is an odd function, then we obtain the sine inversion transform from the inversion formula

        $\to$ Sine transform implies an odd extension of the original function

**Another definition of Fourier cosine transform**.
* *Assumption*.
    * $x(t)$ is a signal defined on $t\geq 0$ only
    * $y(t)=\begin{cases} x(t) & t\geq 0 \\ x(-t) & t\leq 0\end{cases}$ is an even extension of $x(t)$
* *Formula*.
    * *Cosine transform*. $Y_c(\omega)=\sqrt{\frac{2}{\pi}} \int_0^\infty y(t) \cos(\omega t)dt$
    * *Inverse cosine transform*. $y(t)=\sqrt{\frac{2}{\pi}} \int_0^\infty Y_c(\omega) \cos(\omega t)d\omega$

>**NOTE**. $\sqrt{\frac{2}{\pi}}$ is used to insure the symmetry between the cosine transform and its inverse, just like conventions to insure symmetry of Fourier transforms

>**NOTE**. Similar variation exists for Fourier sine transform

**Fourier transforms as implicit extension of original function**.
* *Fourier transform*. Imply a periodic extension of the original function
* *Fourier sine transform*. Imply an odd extension of the original function
* *Fourier cosine transform*. Imply an even extension of the original function

**Variations**.
* *Sine transform*. $\hat{f}^s(\nu) = {\cal{F}}_s(f)(\nu) = \sqrt{\frac{2}{\pi}} \int_{0}^{\infty} f(t) \sin(2\pi\nu t) dt$
* *Cosine transform*. $\hat{f}^c(\nu) = {\cal{F}}_c(f)(\nu) = \sqrt{\frac{2}{\pi}} \int_{0}^{\infty} f(t) \cos(2\pi\nu t) dt$

## Discrete sine and cosine transform
**Discrete Fourier transform (recall)**. 

$$\begin{aligned}
X_k &= \sum_{n=0}^{N-1} x_n e^{-\frac{i2\pi kn}{N}}\\
&=\sum_{n=0}^{N-1} x_n \bigg[ \cos\frac{2\pi kn}{N} - i \sin\frac{2\pi kn}{N} \bigg]
\end{aligned}$$

**DST and DCT matrices**. The DST (or DCT) is a linear, invertible function ${\cal{F}}:\mathbf{R}^N\to\mathbf{R}^N$

$\to$ DST (or DCT) is equivalent to an $N\times N$ matrix
* *Orthogonality of DCT matrix*. If the DCT matrix is orthonormal

    $\to$ We can easily inverse the DCT transform using the transposed DCT matrix

**DST-I and DCT-I**.
* *DST*. $X_k=\sum_{n=0}^{N-1} x_n \sin \frac{\pi (n+1)(k+1)}{N+1}$ for $k=0,\dots,N-1$
    * *Orthogonality of DST-I matrix*. DST-I matrix is orthogonal, up to a scale factor
    * *Correspondence to DFT*. DST-I is exactly equivalent to a DFT of real sequence, which is odd around zero-th and middle points, scaled by $1/2$
    * *Boundary conditions*.
        * $x_n$ is odd around $n=-1$ and odd around $n=N$
        * $X_n$ is odd around $n=-1$ and odd around $n=N$
* *DCT*. $X_k=\frac{1}{2}(x_0 + (-1)^k x_{N-1}) +\sum_{n=1}^{N-2} x_n \cos\frac{\pi nk}{N-1}$ for $k=0,\dots,N-1$
    * *Orthogonality of DCT-I matrix*. Some authors multiply $x_0$ and $X_{N-1}$ by $\sqrt{2}$
        * *Purpose*. Make the DCT-I matrix orthogonal, if one further multiplies by an overall scale factor of $\sqrt{\frac{2}{N-1}}$
        * *Drawbacks*. Break the direct correspondence with a real-even DFT
    * *Correspondence to DFT*. DCT-I is exactly equivalent to DFT of $2N-2$ real numbers with even symmetry
    
        >**NOTE**. DCT-I is not defined for $N < 2$
    
    * *Boundary conditions*.
        * *x_n* is even around $n=0$ and even around $n=N-1$
        * *X_n* is even around $n=0$ and even around $n=N-1$

**DST-II and DCT-II**.
* *DST*. $X_k = \sum_{n=0}^{N-1} x_n \sin \frac{\pi (n+1/2) (k+1)}{N}$ for $k=0,\dots,N-1$
    * *Orthogonality of DST-II matrix*. Some authors multiply $X_{N-1}$ by $\frac{1}{\sqrt{2}}$ 

        $\to$ This results in DST-III
        * *Purpose*. Make the DST-II matrix orthogonal, up to a scale factor
        * *Drawback*. Breaks the correspondence with a real-odd DFT of half-shifted input 
    * *Boundary conditions*.
        * $x_n$ is odd around $n=-1/2$ and odd around $n=N-1/2$
        * $X_k$ is odd around $k=-1$ and even around $k=N-1$
* *DCT*. $X_k=\sum_{n=0}^{N-1} x_n \cos \frac{\pi (n+1/2) k}{N}$ for $k=0,\dots,N-1$
    * *Orthogonality of DCT-II matrix*. Some authors multiply $X_0$ by $\frac{1}{\sqrt{2}}$ and multiply the resulting matrix by an overall scale factor of $\sqrt{\frac{2}{N}}$
    
        $\to$ This results in DCT-III
        * *Purpose*. Make the DCT-II matrix orthogonal
        * *Drawbacks*. Break the direct correspondence with a real-even DFT of half-shifted input
    * *Boundary conditions*.
        * $x_n$ is even around $n=-1/2$ and even around $n=N-1/2$
        * $X_k$ is even around $k=0$ and odd around $k=N$

**DST-III and DCT-III**. 
* *DST*. $X_k=\frac{(-1)^k}{2}x_{N-1} + \sum_{n=0}^{N-2} x_n\sin\frac{\pi(n+1)(k+1/2)}{N}$ for $k=0,\dots,N-1$
* *DCT*. $X_k=\frac{1}{2}x_0+\sum_{n=1}^{N-1} x_n \cos \frac{\pi n (k+1/2)}{M}$ for $k=0,\dots,N-1$

**DST-IV and DCT-IV**.
* *DST*. $X_k=\sum_{n=0}^{N-1} x_n \sin \frac{\pi (n+1/2) (k+1/2)}{N}$ for $k=0,\dots,N-1$
* *DCT*. $X_k=\sum_{n=0}^{N-1} x_n \cos\frac{\pi (n+1/2) (k+1/2)}{n}$ for $k=0,\dots,N-1$

## Data compression with integral transform
**Problems with DCT**.
* *Problems*.
    * One has to specify whether the function is even or odd at both the left and right boundaries of the domain, i.e. the min $n$ and max $n$ boundaries
    * One has to specify around what point the function is even or odd
* *Consequences*. The choices above lead to all the standard variations of DCTs and also DSTs
* *Boundary conditions*. Strongly affect the applications of the transform and lead to uniquely useful properties for various DCT types

**Discrete cosine transform for data compression**.
* *Applications*.
    * *Digital image compression*. JPEG, HEIF, etc.
    * *Digital video*. MPEG, H26x, etc.
    * *Digital audio*. MP3, AAC, etc.
    * *Digital television*. SDTV, HDTV, VOD, etc.
    * *Digital radio*. ACC+, DAB+, etc.
    * *Speech coding*. AAC-LD, Siren, Opus, et.c
* *Boundary conditions and data compression*. To transform a sequence, we need first extend the sequence according to the boundary conditions of the underlying transform

    $\to$ Discontinuities may occur between boundary points between cycles of extension 
    * *Discontinuity implies lower convergence rate*. Discontinuities in a function reduce the convergence rate of the Fourier series

        $\to$ More sinusoids are required to represent the function with a given accuracy
        * *Consequence*. The smoother a function is, the fewer terms in its DFT or DCT are required to represent accurately, and the more it can be compressed
    * *DFT for data compression*. The implicit periodicity of the DFT means that discontinuities usually occur at the boundaries
        * *Explain*. Any random segment of a signal is unlikely to have the same value at both the left and right boundaries
    * *DST for data compression*. The odd left boundary condition implies a discontinuity for any function which does not happen to be zero at that boundary
    * *DCT for data compression*. A DCT where both boundaries are even always yields a continuous extensions at the boundaries

        $\to$ DCTs generally perform better for signal compression than DFTs and DSTs
* *Why DCT rather than DFT*. DCTs are equivalent to DFTs of roughly twice the length, operating on real data with even symmetry
    * *Explain*. DFT needs coefficients for sine functions also

## Amplitude distribution of the DCT coefficients
**Amplitude distribution of the DCT coefficients**.

<div style="text-align:center">
    <img src="/media/GZzhCls.png">
    <figcaption>Historgram for 8x8 DCT coefficient amplitudes measured for an image</figcaption>
</div>

* *AC coefficients distribution*. Laplacian pdf with zero mean and scale $b=\frac{1}{\sqrt{2}\sigma_y}$, i.e.

    $$p(y)=\frac{1}{\sqrt{2}\sigma_y} e^{\frac{-\sqrt{2}|y|}{\sigma_y}}$$
* *DC coefficients distribution*. Similar to the original image histogram

**Infinite Gaussian mixture modeling for AC coefficients**.
* *Assumptions*. For a given block variance, AC coefficient pdfs are Gaussian
* *Observations*.
    * Gaussian mixture with exponential variance distribution yields a Laplacian pdf, i.e.
        * Let $\phi(x;\mu,\sigma)$ be the pdf of Gaussian with mean $\mu$ and variance $\sigma^2$, and $f_\text{exp}(x;\lambda)$ be the pdf of exponential distribution with rate $\lambda$

        $$\begin{aligned}
        f(y)&=\int_0^\infty \phi(y;0,v)\cdot f_\text{exp}(v;1/\sigma_y^2)dv\\
        &=\int_0^\infty \frac{1}{\sqrt{2\pi v}} e^{-y^2/2v} \cdot \frac{1}{\sigma_y^2} e^{-v/\sigma_y^2}dv\\
        &=\frac{1}{\sqrt{2}\sigma_y} e^{\frac{-\sqrt{2}|y|}{\sigma_y}}
        \end{aligned}$$

    * Gaussian mixture with half-Gaussian variance, i.e. $\sigma_y/2$, yields pdf very close to Laplacian
* *Conclusion*. Each AC coefficient has Laplace distribution as given above

## Derivation of DCT from KLT
**History of DCT**. KLT was indeed the optimal transform on the basis of MSE criterion but there was no efficient algorithm at the time to compute it

$\to$ Nasir Ahmed focused on determining whether it would be possible to come up with a good approximation to the KLT, which could be computed efficiently
* *Potential idea*. Chebyshev interpolation, i.e. Ahmed studied a cosine transform using Chebyshev polynomials of the form

    $$\begin{aligned}
    T_0(m)&=\frac{1}{\sqrt{N}} & m=1,2,\dots,N\\
    T_k(m)&=\sqrt{\frac{2}{N}} \cos \frac{(2m-1)k\pi}{2N} & k=1,2,\dots,N
    \end{aligned}$$

* *Observation*. 
    * For a range of values of the correlation coefficients $\rho$ in the covariance matrix

        $\to$ The cosine functions above closely resembled KLT basis functions
    * The range of values for $\rho$ mentioned above is relevant to image data pertaining to a variety of applications
* *First criterion*. Rate distortion criterion

    $\to$ DCT's performance is compared very closely with that of the KLT

**Derivation of DCT**.
* *First-order Markov process*.
    * *Markov process of interest*. $\{x_t\}$ is a wide-sense stationary random sequence, defined on $T=\{1,\dots,N\}$ for some $N$ with the following properties

        $$\begin{aligned}
        E(x_t)=0,\quad E(x_t^2) = 1,\quad E(x_t x_s) = r_{|t-s|}
        \end{aligned}$$

        where $r_{|t-s|}\in(-1,1)$ is the correlation coefficient
    * *Covariance matrix of $X=(x_1,\dots,x_N)$*. $\Sigma_x=E(X X^T) \in \mathbf{R}^{N\times N}$

        $\to$ $\Sigma_x$ is a symmetric positive definite matrix having a Toeplitz form
    * *Covariance matrix of interest*. If $r_{|t-s|}=\rho^{|t-s|}$ for some $|\rho|<1$ then

        $$\Sigma_x = \begin{bmatrix}
        1 & \rho & \rho^2 & \cdots & \rho^{N-1}\\
        \rho & 1 & \rho & \cdots & \rho^{N-2}\\
        \vdots & \vdots & \vdots & \ddots & \vdots\\
        \rho^{N-1} & \rho^{N-2} & \rho^{N-3} & \cdots & 1\\
        \end{bmatrix},\quad |\rho| < 1$$
* *Karhunen-Loeve expansion of first-order Markov processes for $N$ even*.
    * *Assumption*.
        * $\{\omega_k\}$ is the positive roots of the transcendental equation

            $$\tan (N\omega_k) = \frac{(1-\rho^2) \sin \omega_k}{\cos \omega_k - 2\rho + \rho^2 \cos \omega_k}$$
    * *Theorem*. KLE Can be expressed in closed form as
    
        $$x(m)=\sum_{k=0}^{N-1} a(k) K_x(k) \sin \bigg[ \omega_k \big( m - \frac{N-1}{2} \big) + (k+1) \frac{\pi}{2}\bigg],\quad 0\leq m,k \leq N-1g$$

        where $K_x(k)$ is the $k$th KLT coefficient
        
        * *Orthogonal KLT basis functions*. $b(m,k)=\sin \bigg[ \omega_k \big( m - \frac{N-1}{2} \big) + (k+1) \frac{\pi}{2}\bigg]$
        * *Normalization factors*. $a(k)=\sqrt{\frac{2}{N+\lambda_k}}$ for $k\in[0,N-1]$ where

            $$\lambda_k = \frac{1-\rho^2}{1-2\rho \cos \omega_k + \rho^2},\quad 0\leq k\leq N-1$$

            is the $k$th eigenvalue of $\Sigma_x$
    * *Proof*.
* *Derivation of DCT*. We will derive the fact that KLT approaches DCT in the limiting case when $\rho \to 1$

* *Consequence*. Most signals of interest in practice are likely to be locally correlated, and can therefore be modeled by a first-order Markov process

    $\to$ We can always expect the results of the DCT transform to be close to KLT

**Fast computation of DCT-II**. 
* *Theorem*. All the $M$ DCT-II coefficients can be computed using a $2M$-point fast Fourier trasnform (FFT)
    * *Proof*.
* *Consequences*. 
    * Since DCT-II and IDCT-II are of the same form

        $\to$ FFT can be used to compute both DCT-II and IDCT-II
    * If a DST were defined, then we can use FFT to compute DST also

# Appendix
## Concetps
**Convention with $\frac{1}{\sqrt{2\pi}}$**. $\hat{f}(\nu) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^\infty f(x) e^{i\omega x} dx$
* *Explain*. 
    * Compared to $\hat{f}(\nu) = \int_{-\infty}^\infty f(x) e^{i\omega x} dx$

        $\to$ $\frac{1}{\sqrt{2\pi}}$ factor is there to insure symmetry between the Fourier transform and its inverse
    * Without the $\frac{1}{\sqrt{2\pi}}$ factor, the inverse would need a factor of $\frac{1}{2\pi}$ to compensate

**Odd and even symmetry complex-valued functions**.
* *Even symmetry*. A complex-valued function of real argument $f:\mathbf{R}\to\mathbf{C}$ is even symmetric if

    $$\forall x\in \mathbf{R},f(x)=\bar{f(-x)}$$
* *Odd symmetry*. A complex-valued function of real argument $f:\mathbf{R}\to\mathbf{C}$ is odd symmetric if

    $$\forall x\in \mathbf{R},f(x)=-\bar{f(-x)}$$

**Odd and even complex-valued finite length sequences**.
* *Even symmetry*. A $N$-point sequence is even symmetric if

    $$\forall n\in \{1,\dots,N-1\},f(n) = f(N-n)$$
    * *Explain*. Even function around $n=N/2$
* *Odd symmetry*. A $N$-point sequence is odd symmetric if

    $$\forall n\in \{1,\dots,N-1\},f(n) = -f(N-n)$$
    * *Explain*. Odd function around $n=N/2$

**Run-level coding**. Coding a run-length of zeros followed by a non-zero level

$\to$ The length of the run is sent, instead of sending all the zero values individually
* *Example procedure*.
    1. After zig-zag scanning, the sequence of DCT coefficients to be transmitted looks like

        $$\text{12 34 87 16 0 0 54 0 0 0 0 0 0 12 0 0 3 0 0 0 }\dots$$
    2. The DC coefficient, i.e. $12$, is sent via separate Huffman table
    3. After run-level parsing, the remaining coefficients and associated runs of zeros are

        $$\text{34 | 87 | 16 | 0 0 54 | 0 0 0 0 0 0 12 | 0 0 3 | 0 0 0 }\dots$$
    
    4. The sequence is then coded as

        $$(0,34),(0,87),(0,16),(2,54),(6, 12), (2, 3), \dots$$

**Uniform deadzone quantizer**. Transform coefficients falling below a threshold are discarded

$\to$ Positions of non-zero transform coefficients are transmitted in addition to their amplitude values
* *Efficient encoding of the position of nonzero transform coefficients*. Use zig-zag scan and run-level coding

**JPEG compression procedure**.
<div style="text-align:center">
    <img src="/media/vunmviL.png">
    <figcaption>JPEG compression procedure</figcaption>
</div>

**Laplace distribution pdf**. $p(x)=\frac{1}{2b} \exp\frac{-|x\mu|}{b}$
* *Parameters*.
    * *Location parameter*. $\mu$
    * *Scale parameter*. $b > 0$

**Toeplitz matrix (diagonal-constant matrix)**. A matrix, in which each descending diagonal from left to right is constant

**Strict sense (SSS) and wide sense stationary random processes**.
* *Assumptions*.
    * $X(t)$ is a random process
* *SSS*. $X(t)$ is SSS if all its finite-order distribution are time invariant
    * *Formal*. The joint cdfs of $(X(t_1),\dots,X(t_k))$ and $(X(t_1+\tau),\dots,X(t_k+\tau))$ are the same for all $k$, all $t_1,\dots,t_k$, and all time shifts $\tau$

        $\to$ The distribution of any two samples $X(t_1)$ and $X(t_2)$ depends only on $\tau=t_2 - t_1$
    * *Examples*. i.i.d processes, random walk, Poisson processes
* *WSS*. $X(t)$ is WSS if its mean and autocorrelation functions are time invariant
    * *Formal*.
        * $E[X(t)]=\mu$, independent of $t$
        * $R_X(t_1,t_2)$ is a function only of the time difference $t_2 - t_1$
        * $E[X(t)^2] < \infty$ (technical condition)
    * *Consequence*. Since $R_X(t_1,t_2) = R_X(t_2,t_1)$, $R_X(t_1,t_2)$ is a function only of $|t_2-t_1|$

**Autocorrelation function**. The similarity between obesrvations, as a function of time lag between time
* Search more...

**Karhunen-Loeve expansion**.

**Chebyshev interpolation**