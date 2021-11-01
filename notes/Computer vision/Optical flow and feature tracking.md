<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Optical flow and feature tracking](#optical-flow-and-feature-tracking)
  - [Optical flow](#optical-flow)
  - [Feature tracking](#feature-tracking)
  - [Applications](#applications)
<!-- /TOC -->

# Optical flow and feature tracking
**From images to videos**. A video is a sequence of frames captured over time

$\to$ Our image data is a function of space $(x,y)$ and time $t$

**Motion estimation techniques**.
* *Optical flow*. Recover image motion at each pixel, from spatio-temporal image brightness variation, i.e. optical flow

    <div style="text-align:center">
        <img src="https://i.imgur.com/Qo4uxjs.png">
        <figcaption>Optical flow</figcaption>
    </div>

* *Feature tracking*. Extract visual features, e.g. corners, textured areas, etc. and track them over multiple frames

    <div style="text-align:center">
        <img src="https://i.imgur.com/LkzH7S8.png">
        <figcaption>Feature tracking</figcaption>
    </div>

## Optical flow
**Optical flow**. The apparent motion of brightness patterns in the image

>**NOTE**. Apparent motion can be caused by lighting changes without any actual motion
>* *Example*. A uniform rotating sphere under fixed lightning versus a stationary sphere under moving illumination

* *Objective*. Recover image motion at each pixel from optical flow
* *Usage*. Used by robotics researchers in 
    * Object detection and tracking
    * Image dominant plane extraction
    * Movement detection
    * Robot navigation and visual odometry

**Estimating optical flow**. Given two subsequent frames, estimate the apparent motion field $(u(x,y),v(x,y))$ between them
* *Key assumptions*.
    * *Brightness constancy*. Projection of the same point looks the same in every frame
    * *Small motion*. Points do not move very far
    * *Spatial coherence*. Points move like their neighbors
* *Brightness constancy constraint*. $I(x,y,t-1)=I(x+u(x,y),y+v(x,y),t)$
    * *Taylor approximation*.$I(x+u,y+v,t) = I(x,y,t-1) + I_x u + I_y v + I_t$
        
        $\to$ $I(x+u,y+v,t) - I(x,y,t-1) = I_x u + I_y v + I_t$
        * *Consequence*. $I_x u + I_y v + I_t \approx 0$

            $\to$ $\nabla I \cdot (u,v)^T + I_t = 0$
    * *Question*. Can we use the equation $\nabla I \cdot (u,v)^T + I_t = 0$ to recover image motion $(u,v)$ at each pixel
        * *Problems*.
            * There is one equation and two unknowns $u,v$
            * The component of the flow perpendicular to the gradient, i.e. parallel to the edge, cannot be measured
        * *Solution*. If $(u,v)$ satisfies the equation, then $(u+u',v+v')$ does so if

            $$\nabla I \cdot (u',v')^T = 0$$

            where $(u',v')$ is perpendicular to the gradient
            
            * *Consequence*. $\nabla I \cdot (u+u',v+v') + I_t=0$

**Lucas-Kanade flow**.
* *Problem of interest*. How to get more equations for a pixel
* *Spatial coherence constraint*. Assume the pixel's neighbors have the same motion $(u,v)$
    * *Explain*. If we use a $n\times n$ window, we will have $n^2$ equations per pixel, i.e.

        $I_t(p_i) + \nabla I(p_i) \cdot (u,v)^T = 0$
    * *Vectorization form*.

        $$\begin{bmatrix}
        I_x(p_1) & I_y(p_1)\\
        \vdots & \vdots\\
        I_x(p_{n^2}) & I_y(p_{n^2})
        \end{bmatrix} \cdot \begin{bmatrix}u \\ v\end{bmatrix} = -\begin{bmatrix}
        I_t(p_1) \\ \vdots \\ I_t(p_{n^2})
        \end{bmatrix}$$
    
    * *Solving the linear system*. Use least-square method
* *Problem*. The linear system above is overconstrained
    * *Assumptions*.
        * $A=\begin{bmatrix}
        I_x(p_1) & I_y(p_1)\\
        \vdots & \vdots\\
        I_x(p_{n^2}) & I_y(p_{n^2})
        \end{bmatrix} \in \mathbb{R}^{n^2 \times 2}$
        * $d=\begin{bmatrix}u \\ v\end{bmatrix} \in \mathbb{R}^{2\times 1}$
        * $b=-\begin{bmatrix}I_t(p_1) \\ \vdots \\ I_t(p_{n^2})\end{bmatrix} \in \mathbb{R}^{n^2\times 1}$
    * *Conditions for solvability*.
        * $A^T A = \begin{bmatrix}\sum I_x I_x & \sum I_x I_y \\ \sum I_x I_y & \sum I_y I_y\end{bmatrix}$ is invertible
        * $A^T A$ should not be too small due to noise
            * *Explain*. Eigenvalues of $A^T A$ should not be too small
        * $A^T A$ should be well-conditioned
            * *Explain*. $\lambda_1 / \lambda_2$ should not be too large
    * *Intuition*. $A^T A$ is, in fact, the second moment matrix as in Harris corner detector

        $\to$ Eigenvectors and eigenvalues of $A^T A$ relate to edge direction and magnitude
        * Condition 1 means that $\det (A^T A)\neq 0$, i.e. $\lambda_1 \lambda_2 \neq 0$

            $\to$ The intensity of neighbor points must not be constant along any direction
        * Condition 2 means that the pixel should not lie within a flat region
        * Condition 3 means that the chosen point should not be an edge point
* *Good features to track*. Tracking Harris corners, or equivalent, guarantees small error sensitivity

**Revisiting small motion assumption**. For large motion, we can reduce the resolution of the image
* *Multi-resolution Lucas-Kanade algorithm*. After computing simple LK at highest level, at level $i$, we do the following steps
    1. Take flow $u_{i-1},v_{i-1}$ from level $i-1$
    2. Bilinear interpolate the flow to create $u^*_i,v^*_i$ matrices of twice resolution for level $i$
    3. Multiply $u_i^*,v_i^*$ by $2$
    4. Compute $f_t$ from a block displaced by $u_i^*(x,y),v_i^*(x,y)$
    5. Apply LK to get $u_i'(x,y),v_i'(x,y)$, i.e. the correction in flow
    6. Add corrections $u'_i,v_i'$, i.e.

        $$u_i = u_i^* + u'_i,\quad v_i=v_i^* + v_i'$$

**Iterative LK algorithm**.
1. Estimate velocity at each pixel by solving LK equations
2. Warp $I(t-1)$ towards $I(t)$ using the estimated flow field
3. Repeat until convergence

**Coarse-to-fine optical flow estimation**.

<div style="text-align:center">
    <img src="https://i.imgur.com/shUgvRf.png">
    <figcaption>Coarse-to-fine optical flow estimation</figcaption>
</div>

**Motion segmentation**. Break image sequence into layers, each of which has a coherent, i.e. affine, motion
* *Layer*. Each layer is defined by an alpha mask and an affine motion model
* *Affine motion*.

    $$u(x,y)=a_1 + a_2 x + a_3 y,\quad v(x,y)=a_4 + a_5 x + a_6 y$$

* *Brightness constancy equation*. $I_x u + I_y v + I_t \approx 0$

    $\to$ Each pixel provides a linear constraint in 6 unknowns
* *Least-square minimization*.

    $$E(\vec{a}) = \sum [I_x(a_1 + a_2 x + a_3 y) + I_y(a_1 + a_2 x + a_3 y) + I_t]^2$$
* *Layer estimation*.

    <div style="text-align:center">
        <img src="https://i.imgur.com/bJQcuNJ.png">
        <figcaption>Layer estimation</figcaption>
    </div>
    
    1. Obtain a set of initial affine motion hypotheses, i.e.
        1. Divide the image into blocks and estimate affine motion parameters in each block using least-square method

            $\to$ Hypotheses with high residual error are eliminated then
        2. Map hypotheses into motion parameter space
        3. Perform K-means clustering on affine motion parameters
        4. Merge clusters which are close and retain the largest clusters to obtain a smaller set of hypotheses to describe all the motions in the scene
    2. Repeat until convergence the following steps
        1. Assign each pixel to best hypothesis, and pixels with high residual error remain unassigned
        2. Perform region filtering to enforce spatial constraints
        3. Re-estimate affine motions in each region

## Feature tracking
**Tracking challenges and solutions**.
* *Ambiguity of optical flow*. Find good features to track
* *Large motions*. Use discrete search rather than LK algorithm
* *Changes in shape, orientation, and color*. Allow some matching flexibility
* *Occlusions and dis-occlusion*. Need mechanism for deleting, adding new features
* *Drift-errors may accumulate over time*. Need to know when to terminate a track

**Shi-Tomasi feature tracker**.
1. Find good features using eigenvalues of second-moment matrix
    * *Good features to track*. Ones which can be tracked reliably
2. From frame to frame, track with LK and a pure translation model

    $\to$ More robust for small displacements, and can be estimated from smaller neighborhoods
3. Check consistency of tracks by affine registration to the first observed instance of the feature
    * Affine model is more accurate for larger displacements
    * Comparing to the first frame helps to minimize drift

**Tracking with dynamics**. Given a model of expected motion, predict where objects will occur in the next frame, even before seeing the image
* *Key idea*.
    * Restrict search space for the object
    * Improved estimates since measurement noise is reduced by trajectory smoothness
* *Method*. Kalman filter

## Applications
**Usage of motion**.
* Tracking features
* Segment objects based on motion cues
* Learn dynamical models
* Improve video quality, i.e. motion stabilization and super resolution
* Tracking objects
* Recognize events and activities