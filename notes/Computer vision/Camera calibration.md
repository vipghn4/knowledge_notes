---
title: Camera calibration
tags: Computer vision
---

# Table of Contents
[toc]

## Definitions
**Camera resectioning**. Determine which incoming light is associated with each pixel on the resulting image

>**NOTE**. In an ideal pinhole camera, a simple projection matrix is enough to do this

>**NOTE**. With more complex camera systems, errors resulting from misaligned lenses and deformations in their structures can result in more complex distortions in the final image

* *Usage*. Application of stereo vision, where the camera projection matrices of two cameras are used to calculate the 3D world coordinates of a point viewed by both cameras

**Camera projection matrix**. Derived from the intrinsic and extrinsic parameters of the camera, and is often represented by the series of transformation
* *Usage*. Associate points in a camera's image space with locations in 3D world space

**Homogeneous coordinates**. Coordinates having an additional last component, which is initially, by convention, a $1$
* *2D homogeneous coordinates*. $\begin{bmatrix}u & v & 1\end{bmatrix}^T$
* *3D homogeneous coordinates*. $\begin{bmatrix}x_w & y_w & z_w & 1\end{bmatrix}^T$

## Camera models
**Camera system**. A system which can record an image of an object or scene in the 3D world

### Pinhole cameras

<div style="text-align:center">
    <img src="/media/K7zctHP.png">
    <figcaption>Pinhole camera model</figcaption>
</div>

**Description**. A barrier is placed with a small aperture between the 3D object and a photographic film or sensor
* *Image (or retinal plane)*. The film
* *Pinhole (or center of the camera) $O$*. The aperture
* *Focal length $f$*. The distance between the image plane and the pinhole $O$
* *Virtual image (or virtual plane)*. The retina plane, in case it is placed between $O$ and the 3D object, at a distance $f$ from $O$

**Image and virtual image**. The projection of the object in image plane and the image of the object in the virtual image plane are identical, up to scale (similarity) transformation

<div style="text-align:center">
    <img src="/media/YhZFxFU.png">
    <figcaption>Image plane and virtual image plane</figcaption>
</div>

**Formulation of image**. The following formulation is called the pinhole model

<div style="text-align:center">
    <img src="/media/BY6ZctF.png">
    <figcaption>Formal construction of pinhole camera model</figcaption>
</div>

* *Assumptions*. $P=(x,y,z)$ is a point on some 3D object visible to the pinhole camera
* *Image formation*. $P$ is mapped or projected onto the image plane $\Pi'$

    $\to$ This results in point $P'=(x',y')$

    * *Formal*. $P'=(x',y')=(f\frac{x}{z}, f\frac{y}{z})$

    >**NOTE**. The pinhole itself can be projected onto the image plane, giving a new point $C'$

* *Camera reference system (or camera coordinate system)*. A coordinate system $(i,j,k)$ centered at the pinhole $O$ such that the axis $k$ is perpendicular to the image plane and points toward it
    * *Optical axis*. The line defined by $C'$ and $O$

**Real world scenarios**. In the formulation above, we assume that the aperture is a single point

$\to$ In most real world scenarios, we cannot assume the aperture can be infinitely small
* *Aperture size*. As the aperture size increases, the number of light rays passing through the barrier increases

    $\to$ Each point on the film may be affected by light rays from multiple points in 3D space, blurring the image
* *Fundamental problem of pinhole formulation*. Can we develop cameras which take crisp and bright images?

### Cameras and lens
**Idea**. Solve the conflict between crispness and brightness using lenses

<div style="text-align:center">
    <img src="/media/0wuf9Mm.png">
    <figcaption>A setup of a simple lens model</figcaption>
</div>

* *Lens*. Devices which can focus or disperse light
* *Ideal lens*. If we replace the pinhole with a lens, which is both properly placed and sized

    $\to$ All rays of light which are emitted by some point $P$ are refracted by the lens so that they converge to a single point $P'$

**Lens focus**. This desired property does not hold for all 3D points, but only for some specific point $P$

$\to$ Lenses have a specific distance, for which objects are in focus

* *Depth of field*. The effective range, at which cameras can take clear photos

**Focal point**. Camera lenses focus all light rays traveling parallel to the optical axis to one point, known as the focal point

<div style="text-align:center">
    <img src="/media/Iu0zLsq.png">
    <figcaption>Lenses focus light rays parallel to the optical axis into the focal point</figcaption>
</div>

* *Focal length $f$*. The distance between the focal point and the center of the lens

>**NOTE**. Light rays passing through the center of the lens are not deviated

**Formulation of image**. The following formulation is called the paraxial refraction model, i.e. the formulation below takes advantage of the paraxial, or thin-lens, assumption

<div style="text-align:center">
    <img src="/media/CYPqe9w.png">
    <figcaption>Lens projection model</figcaption>
</div>

* *Assumptions*. 
    * $P=(x,y,z)$ is a point on some 3D object visible to the pinhole camera
    * $z'=f$ (in pinhole model) and $z'=f+z_0$ (in camera lens model)
* *Image formation*. $P$ is mapped or projected onto the image plane $\Pi'$

    $\to$ This results in point $P'=(x',y')$

    * *Formal*. $P'=(x',y')=(z'\frac{x}{z}, z'\frac{y}{z})$
* *Thin-lens assumption*. For the angle $\theta$ which incoming light rays make with the optical axis of the lens

    $\to$ The paraxial assumption substitutes $\theta$ for any place $\sin\theta$ is used
    * *Motivation*. $\lim_{\theta\to 0} \frac{\sin 0}{\theta} = 1$

**Aberrations with thin-lens assumption**.
* *Radial distortion*. Cause the image magnification to decrease or increase, as a function of the distance to the optical axis

## Projection matrix
>**NOTE**. The projection model is derived from pinhole model, but also hold for paraxial refraction model

**Projection matrix**. Denoted as $M$

$$z_c \begin{bmatrix}u \\ v \\ 1\end{bmatrix} = K \begin{bmatrix}R  & T\end{bmatrix} \begin{bmatrix}x_w \\ y_w \\ z_w \\ 1\end{bmatrix} = M \begin{bmatrix}x_w \\ y_w \\ z_w \\ 1\end{bmatrix}$$

where $M = K \begin{bmatrix}R  & T\end{bmatrix}$

**Intrinsic parameters**. $K=\begin{bmatrix}\alpha_x & \gamma & u_0 & 0\\0 & \alpha_y & v_0 & 0\\0 & 0 & 1 & 0\end{bmatrix}$
* *Usage*. Derive pixel coordinates from camera coordinates
* *Notations*.
    * *Focal length*. 
        * *Focal length in terms of pixels*. $\alpha_x = f \cdot m_x$ and $\alpha_y = f \cdot m_y$
        * *Focal length in terms of distance*. $f$
        * *Width and height of a pixel on the projection plane*. $m_x$, $m_y$
    * *Skew coefficient between $x$ and $y$ axes*. $\gamma$ (often $0$)
    * *Principle point*. $(u_0, v_0)$ (ideally the center of the image)
* *Derivation*.

    <div style="text-align:center">
        <img src="/media/pKDlbaa.png">
    </div>

    <div style="text-align:center">
        <img src="/media/aYEoaGN.png">
    </div>

    * *Assumptions*.
        * $f$ is focal length
        * $\alpha, \beta$ are focal lengths, in terms of pixels without skewness
        * $\theta$ is the skew angle (if skewed horizontally)
    * *Observations*.
        * The horizontal focal length with skewness is given as $\frac{\beta}{\sin\theta} y_c$
        * The vertical focal length is given as $\alpha x_c - \alpha \cdot \cot \theta y_c$
        * The pre-scale pixel coordinates are given as

            $$z_c u=\alpha x_c -\alpha\cdot\cot\theta y_c + u_0 z_c,\quad z_c v=\frac{\beta}{\sin\theta} y_c + v_0 z_c$$
        
        * The final pixel coordinates are then

            $$u=\alpha \frac{x_c}{z_c} -\alpha\cdot\cot\theta \frac{y_c}{z_c} + u_0,\quad v=\frac{\beta}{\sin\theta} \frac{y_c}{z_c} + v_0$$

* *Non-linear intrinsic parameters*. Parameters such as lens distortion

    >**NOTE**. These parameters cannot be included in the linear camera model described by the intrinsic parameter matrix

    * *Estimation of non-linear intrinsic parameters*. Use non-linear optimization techniques

**Extrinsic parameters**. $\begin{bmatrix}R_{3\times 3} & T_{3\times 1}\\0_{1\times 3} & 1\end{bmatrix}_{4\times 4}$
* *Usage*. Derive camera coordinates from world coordinates

**Feugeras's theorem**.
* *Statement*. Let 

    $$M=K\begin{bmatrix}R & T\end{bmatrix} = \begin{bmatrix}KR & KT\end{bmatrix}=\begin{bmatrix}A & b\end{bmatrix}$$

    where $A=\begin{bmatrix}\mathbf{a}_1 & \mathbf{a}_2 & \mathbf{a}_3\end{bmatrix}$ then

    * A necessary and sufficient condition for $M$ to be a perspective projection matrix is 
    
        $$\det A \neq 0$$
    
    * A necessary and sufficient condition for $M$ to be a zero-skew perspective projection matrix is

        $$\det A \neq 0,\quad (\mathbf{a}_1\times \mathbf{a}_3) \cdot (\mathbf{a}_2 \times \mathbf{a}_3) = 0$$
    
    * A necessary and sufficient condition for $M$ to be a perspective projection matrix with zero skew and unit aspect-ratio is

        $$\det A \neq 0,\quad \begin{cases}(\mathbf{a}_1\times \mathbf{a}_3) \cdot (\mathbf{a}_2 \times \mathbf{a}_3)=0\\\|\mathbf{a}_1\times \mathbf{a}_3\|_2^2 = \|\mathbf{a}_2\times \mathbf{a}_3\|_2^2\end{cases}$$
* *Intuition*. $\mathbf{a}_1,\mathbf{a}_2,\mathbf{a}_3$ are unit vectors in world coordinates after converted into pixel coordinates

**Weak perspective projection**. Points are projected onto the image plane by the following steps
1. Project points to a reference plane using orthogonal projection
2. Project the points on reference plane to the image plane using a projective transform

## Camera calibration
**Camera calibration problem**. Given one or more images taken by a camera

$\to$ Estimate its intrinsic and extrinsic parameters
* *Assumptions*.
    * World coordinates with origin $O_w$ and unit vectors $i_w,j_w,k_w$

        $\to$ All of them are known
    * $n$ points $P_1,\dots,P_n$ with known positions in world coordinates
    * $n$ projections $p_1,\dots,p_n$ with known positions in pixel coordinates
* *Goal*. Compute intrinsic and extrinsic parameters

**Solution**. Refer to the reference

# Appendix
## References
* [Stanford's lecture](https://cvgl.stanford.edu/teaching/cs231a_winter1415/lecture/lecture3_camera_calibration_notes.pdf)
* [Standford's lecture](https://web.stanford.edu/class/cs231a/course_notes/01-camera-models.pdf