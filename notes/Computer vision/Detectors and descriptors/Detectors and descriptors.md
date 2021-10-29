<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Detectors and descriptors](#detectors-and-descriptors)
  - [Local invariant features](#local-invariant-features)
    - [Introduction](#introduction)
    - [Requirements and invariances](#requirements-and-invariances)
  - [Keypoint localization - Harris corner detector](#keypoint-localization---harris-corner-detector)
  - [Scale invariant region selection](#scale-invariant-region-selection)
    - [Automatic scale selection](#automatic-scale-selection)
    - [Laplacian-of-Gaussian detector](#laplacian-of-gaussian-detector)
    - [Difference-of-Gaussian detector](#difference-of-gaussian-detector)
    - [Combinations](#combinations)
- [Appendix](#appendix)
  - [Concepts](#concepts)
  - [References](#references)
<!-- /TOC -->

# Detectors and descriptors
## Local invariant features
### Introduction
**Motivation**. Global representations have major limitations
* *Advantages of local descriptors*. Describing and matching only local regions increases robustness to occlusions, articulation, and intra-category variations

**Applications**.
* *Image matching*.
    1. Detect feature points in both images
    2. Find corresponding pairs
* *Image stitching*.
    1. Detect feature points in both images
    2. Find corresponding pairs
    3. Use these pairs to align the images

**General approach of using local features**.

<div style="text-align:center">
    <img src="https://i.imgur.com/NJLC8O5.png">
    <figcaption>General approach of using local features</figcaption>
</div>

1. Find a set of distintive key-points
2. Define a region around each keypoint
3. Extract and normalize the region content
4. Compute a local descriptor from the normalized region
5. Match local descriptors 

### Requirements and invariances
**Problems to solve with local descriptors**. There are two problems we need to solve for each local-descriptor-related problems
* *Problem 1*. Detect the same point independently in both images

    <div style="text-align:center">
        <img src="https://i.imgur.com/ONiQHOZ.png">
        <figcaption>Key-points detection</figcaption>
    </div>

* *Problem 2*. For each point, correctly recognize the corresponding one

    <div style="text-align:center">
        <img src="https://i.imgur.com/Lys5ZDV.png">
        <figcaption>Key-point matching</figcaption>
    </div>

**Invariance of local descriptor**. Local descriptors must be invariant to the following transformations
* *Geometric invariance*.

    <div style="text-align:center">
        <img src="https://i.imgur.com/6uBOwQC.png">
        <figcaption>Levels of geometric invariance</figcaption>
    </div>

* *Photometric transfomrations*. These transformations are often modeled as a linear transformation of pixel intensities, i.e. scaling and offset
    * *Example*. Contrast, illumination, etc.

**Requirements on region detectors**.
* *Repeatability and accuracy*. Region extraction needs to be repeatable and accurate, i.e.
    * Invariant to translation, rotation, and scale changes
    * Robust or covariant to out-of-plane, i.e. affine, transformations
    * Robust to lighting variations, noise, blur, quantization
* *Locality*. Features are local, thus robust to occlusion and clutter
* *Quantity*. We need a sufficient number of regions to cover the object
* *Distintiveness*. The region should contain "interesting" structure
* *Efficiency*. Close to real-time performance

**Existing detectors**. The following detectors have become a basic building block for many recent applications in computer vision
* Hessian and Harris
* Laplacian, DoG
* Harris- / Hessian-Laplace
* Harris- / Hessian-Affine
* EBR and IBR
* MSER
* Salient regions

## Keypoint localization - Harris corner detector
**Objectives**. Repeatable detection, precise localization, and interesting region content

**Finding corners**.
* *Key observations*. 
    * In the region around a corner, image gradient has two or more dominant directions
    * Corners are repeatable and distinctive
* *Design criteria*.

    <div style="text-align:center">
        <img src="https://i.imgur.com/AURDt0Q.png">
        <figcaption>Types of region within an image</figcaption>
    </div>

    * We should easily recognize the corner by looking through a small window, i.e. locality
    * Shifting the window in any direction should give a large change in intensity, i.e. good localization

**Harris detector formulation**.
* *Change of intensity for the shift $(u,v)$*.
    * *Assumptions*.
        * $w(x,y)$ is the window function, e.g. ramp function or Gaussian function
        * $I(x,y)$ is the intensity of the image at location $(x,y)$
    * *Change of intensity for the shift $(u,v)$*.

        $$E(u,v) = \sum_{x,y} w(x,y) [I(x + u, y + v) - I(x, y)]^2$$

        where the summation is taken over the region we are checking for corner
    
* *Approximation of $E(u,v)$*.
    * *Assumptions*.
        * $I_x$ is the gradient of the image w.r.t $x$
        * $I_y$ is the gradient of the image w.r.t $y$
        * $M\in\mathbb{R}^{2\times 2}$ is given as

            $$M=\sum_{x,y} w(x,y) \begin{bmatrix}I_x^2 & I_x I_y \\ I_x I_y & I_y^2\end{bmatrix} = \sum_{x,y} w(x,y) \begin{bmatrix}I_x \\ I_y\end{bmatrix} \begin{bmatrix}I_x & I_y\end{bmatrix}$$
    
    * *Conclusion*. $E(u,v)\approx \begin{bmatrix}u & v\end{bmatrix} M \begin{bmatrix}u \\ v\end{bmatrix}$
    * *Explain*. $I(x+u,y+v)\approx I(x,y) + u I_x + v I_y$, thus

        $$(I(x+u,y+v) - I(x,y))^2\approx \begin{bmatrix}u & v\end{bmatrix} \begin{bmatrix}I_x \\ I_y\end{bmatrix} \begin{bmatrix}I_x & I_y\end{bmatrix} \begin{bmatrix}u \\ v\end{bmatrix}$$
    * *Second-order moment matrix (structure tensor)*. $M$
* *Properties of $M$*. 
    * *Eigenvalue decomposition*. Since $M$ is symmetric, we have that

        $$M = R^{-1} \begin{bmatrix}\lambda_1 & 0 \\ 0 & \lambda_2\end{bmatrix} R$$
    
    * *Intuition*. We can visualize $M$ as an ellipse, with axis lengths determined by the eigenvalues and orientation determined by $R$

        <div style="text-align:center">
            <img src="https://i.imgur.com/fM6GtdF.png" width="500">
            <figcaption>Visualization of eigenvalue decomposition</figcaption>
        </div>

* *Classification of image points using eigenvalues of $M$*.

    <div style="text-align:center">
        <img src="https://i.imgur.com/K60Yk0i.png" width="500">
        <figcaption>Classification of eigenvalue space</figcaption>
    </div>

    * *Edge points*. When $\lambda_1 \gg \lambda_2$ or $\lambda_2 \gg \lambda_1$
    * *Corner points*. When $\lambda_1$ and $\lambda_2$ are large, and $\lambda_1 \approx \lambda_2$, i.e. $E$ increases in all directions
    * *Flat region*. When $\lambda_1$ and $\lambda_2$ are small, i.e. $E$ is almost constant in all directions
* *Corner response function*. $\theta = \det M - \alpha \cdot \text{trace}(M)^2 = \lambda_1 \lambda_2 - \alpha (\lambda_1 + \lambda_2)^2$

    <div style="text-align:center">
        <img src="https://i.imgur.com/gn9uYPQ.png">
        <figcaption>Plot of corner response function at alpha = 0.04</figcaption>
    </div>

    * *Motivation*. The computation of eigenvalues is computationally expensive
    * *Typical value of $\alpha$*. From $0.04$ to $0.06$
    * *Classification of image points*.
        * *Edge points*. $\theta < \theta_R^{(1)}$
        * *Corner points*. $\theta > \theta_R^{(2)}$
        * *Flat points*. $\theta \in [\theta_R^{(1)}, \theta_R^{(2)}]$
    * *Explain*.
        * Consider the characteristic polynomial of $M$

            $$f(\lambda)=\lambda^2 - \text{Tr}(M) \lambda + \det (M)$$
        
        * Due to the quadratic formula providing the solutions to $f(\lambda)=0$, we have that
            
            $$b^2-4ac=\text{Tr}(M)^2 - 4 \det(M) \geq 0$$
            
            since $M$ must have at least one eigenvalue, due to its symmetricity
        * In such cases, the equation $f(\lambda)=0$ has two solutions

            $$x=-b\pm\sqrt{b^2-4ac}=\text{Tr}(M)\pm\sqrt{\text{Tr}(M)^2-4\det(M)}$$
        
        * We have that 
            
            $$\begin{aligned}
            \theta>0 &\Leftrightarrow \frac{b^2}{4ac} < \frac{1}{4\alpha}\\
            \theta\approx 0 &\Leftrightarrow \frac{b^2}{4ac} \approx \frac{1}{4\alpha}\\
            \theta<0 &\Leftrightarrow \frac{b^2}{4ac} > \frac{1}{4\alpha}
            \end{aligned}$$
        
        * We also have that $x^T M x \geq 0$ for all $x\in\mathbb{R}^2$ due to the formulation of $M$, thus, the two eigenvalues are competing against each other, since their sum is limited to $\text{Tr}(M)$

            $\to$ The more difference between the two eigenvalues, the more likely that the underlying point is an edge point
        * Thus, by setting $\alpha$, we we setting the threshold for the difference between two eigenvalues, i.e. $2\sqrt{b^2 - 4ac}$, above which a point is considered an edge point
            * If $\text{Tr}(M) \gg 0$ and $\theta > 0$, it indicates that both eigenvalues are large, i.e. this is a corner point
            * If $\text{Tr}(M) \gg 0$ and $\theta < 0$, it indicates that an eigenvalue is small, while the other is large, i.e. this is an edge point
            * If $\text{Tr}(M) \approx 0$, then $b^2-4ac$ is small also, i.e. $b^2-4ac \leq b^2$ due to the positivity of $4ac$

                $\to$ Both eigenvalues are small, i.e. this is a flat point
* *Shi-Tomasi (or Kanade-Tomasi) corner detector*. Use $\min\{\lambda_1,\lambda_2\}$ for corner detection
    * *Motivation*. Corners detected in this manner are more stable for tracking, under cetain assumptions
        * *Explain*. For tracking purposes, it is crucial for detected corners to be very sensitive to translation
    * *Implementation idea by Giang*. Minimize $\frac{x^T M x}{x^T x}$ w.r.t $\|x\|_2=1$
    * *Usage*. In `cv2.goodFeaturesToTrack()`'
* *Window function $w(x,y)$*.
    * *Option 1*. Uniform window, i.e. $w(x,y)=1$ for all $(x,y)$
        
        $\to$ The result is not rotation invariant
    * *Option 2*. Smooth with Gaussian
        
        $\to$ The result is rotation invariant
* *Algorithm procedure*.
    1. Compute second moment matrix (or autocorrelation matrix) $M$
    2. Compute the corner response function
    3. Perform non-maximum suppression, i.e. extract only points with largest corner responses

**Invariance of Harris corner detector**. Harris corner detector is invariant to translation and rotation, but not scaling

## Scale invariant region selection
### Automatic scale selection
**Problem**. Compare interesting points given by Harris and Hessian operators, by computing a descriptor over a region

$\to$ How can we define such a region in a scale invariant manner, i.e. how can we detect scale-invariant interest regions

**Naive approach**. Use exhausive search, i.e. compare descriptors while varying the patch size
* *Drawbacks*.
    * Computationally inefficient
    * Inefficient but possible for matching
    * Prohibitive for retrieval in large databases
    * Prohibitive for recognition

**Automatic scale selection**. Use scale signature functions
* *Idea*. Design a function, i.e. a signature function, on the region, which is scale invariant
    1. For each point in an image, we can consider a function of region size, e.g.  average intensity of the region

        <div style="text-align:center">
            <img src="https://i.imgur.com/K4JdKME.png">
            <figcaption>A function of region size</figcaption>
        </div>

    2. Take a local maximum of this function
    3. Region size, for which the maximum is achieved, should be invariant to image scale

    >**NOTE**. This scale invariant region size is found in each image independently

* *Illustration*.

    <div style="text-align:center">
        <img src="https://i.imgur.com/3L7H2RC.png">
        <figcaption>Automatic scale selection</figcaption>
    </div>

### Laplacian-of-Gaussian detector
**Laplacian-of-Gaussian (LoG)**. Gaussian filter the image first, then use Laplacian operator to detect edges

<div style="text-align:center">
    <img src="https://i.imgur.com/lkZzsJ2.png">
    <figcaption>Laplacian of Gaussian</figcaption>
</div>

* *Explain*. Laplacian operator usually produces noisy edges, thus Gaussian filter preprocessing helps reducing the high frequency noise components prior to the differentiation step
* *Gaussian of Laplace filter*. Since convolution operator is associative, we can convolve the Gaussian smoothing filter with the Laplacian filter first

    $\to$ Then we convolve the resulting filter with the image to achieve the required result

**LoG as a blob detector**.
* *Naive idea*.
    * *Procedure*.
        1. The input image $f(x,y)$ is convovled by a Gaussian kernel

            $$g(x,y,t) = \frac{1}{2\pi t} \exp(-\frac{x^2 + y^2}{2t})$$
            
            at a certain scale $t$ to give a scale space representation $L(x,y;t) = g(x,y,t) * f(x,y)$
        
        2. The result of Laplacian operator is computed, which usually results in strong positive responses for dark blobs of radius $r=\sqrt{2t}$, or $r=\sqrt{dt}$ for $d$-dimensional image, and strong negative responses for bright blobs of similar size
            * *Lapalcian operator*. $\nabla^2 L = L_{xx} + L_{yy}$
            * *Explain*. We assume that the $d$-dimensional Gaussian has a sphere shape with variance along each dimension $X_i$ is $t$

                $\to$ If the dimensions are statistically independent, then $\text{Var}(X_1+\dots+X_d)=dt$, i.e. the standard deviation is then $\sqrt{dt}$ 
    * *Drawback*. Applying this operator at a single scale makes the operator response strongly dependent on the relationship between the size of the blob structures in the image domain, and the size of the Gaussian kernel used for pre-smoothing
    * *Solution*. To automatically capture blobs of different size in the image

        $\to$ A multi-scale approach is used
* *Multi-scale blob detector with automatic scale selection*.
    * *Scale-normalized Laplacian operator*. $\nabla^2_\text{norm} L = t(L_{xx} + L_{yy})$

        <div style="text-align:center">
            <img src="https://i.imgur.com/6MEFplk.png" width="500">
            <figcaption>Gaussian (left) and Laplacian of Gaussian (right) for multiple scales</figcaption>
        </div>

        * *Motivation*. As we go from finer to coarser scales, we blur the image, making the intensity surface more and more smooth

            $\to$ The amplitude of image derivatives gets smaller as we go up the scale volume
            * *Consequence*. This is a problem for finding interes points, i.e. we are looking for local extrema over scales

                $\to$ Without normalization, we will always get the maximum at the finest scale, and the minimum at the coarest scale
        * *Idea*. The derivative decrease exponentially as a function of $\sqrt{t}$

            $\to$ To compensate for that, we have to normalize them by multiplying the $n$-th derivative by $t^{n/2}$
        * *Intuition*. https://math.stackexchange.com/questions/486303/normalized-laplacian-of-gaussian
            * *Observations*.
                * Consider the Gaussian

                    $$G(x,y;\sigma) = \frac{1}{2\pi\sigma^2} \exp(-\frac{x^2 + y^2}{2\sigma^2})$$

                    and its Laplacian

                    $$\begin{aligned}
                    \text{LoG}(x,y;\sigma) &= \nabla_{(x,y)} G(x,y;\sigma)\\
                    &= \frac{1}{\pi\sigma^4} (\frac{x^2 + y^2}{2 \sigma^2} - 1) \exp(-\frac{x^2 + y^2}{2 \sigma^2})
                    \end{aligned}$$
                
                * Multiplying $\text{LoG}(x,y;\sigma)$ by $\sigma^2$ is equivalent to computing the Laplacian of

                    $$G_\text{norm}(x,y;\sigma)=\frac{1}{2\pi} \exp(-\frac{x^2 + y^2}{2\sigma^2})$$

                    hence

                    $$\begin{aligned}
                    \text{LoG}_\text{norm}(x,y;\sigma) &= \nabla_{(x,y)} G_\text{norm}(x,y;\sigma)\\
                    &= \frac{1}{\pi\sigma^2} (\frac{x^2 + y^2}{2 \sigma^2} - 1) \exp(-\frac{x^2 + y^2}{2 \sigma^2})
                    \end{aligned}$$
                
                * Due to the property that $G_\text{norm}(\sigma x, \sigma y;\sigma) = G_\text{norm}(x,y;1)$, we have a very interesting property

                    $$\text{LoG}_\text{norm}(\sigma x, \sigma y;\sigma) = \text{LoG}_\text{norm}(x,y;1)$$
            * *Conclusion*. By normalizing the LoG, we ensure that the LoG of the scaled image is actually the scaled version of LoG of the original image 
    * *Idea*. Consider $\nabla^2_\text{norm} L$ instead of $\nabla^2 L$, then detect scale-space maxima / minima, i.e. points which are simultaneously local maxima / minima of $\nabla^2_\text{norm} L$ w.r.t both space and scale
        * *Explain*. Given a 2D input image $f(x,y)$
            1. Compute a 3D discrete scale-space volume $L(x,y,t)$
            2. A point is a bright, or dark, blob if the value at this point is greater, or smaller, than the value in all of its $3^3-1$ neighbors
    * *Simultaneous selection of interest points $(\hat{x},\hat{y})$ and scale $\hat{t}$*.

        $$(\hat{x},\hat{y};\hat{t})=\argmax\{\text{MinLocal}_{(x,y;t)} [\nabla^2_\text{norm} L (x,y;t)]\}$$

    * *Consequence*. This notion of blob provides a concise and mathematically precise operational definition of "blob"

        $\to$ Thi leads to an efficient and robust algorithm for blob detection
    * *Basic properties of blobs defined from scale-space maxima of the normalized Laplacian operator*. Responses are covariant with translations, rotations, and rescalings in image domain
        * *Explain*. If a scale-space maximum is assumed at $(x_0,y_0;t_0)$, then under a rescaling of the image with a scale factor $s$

            $\to$ There will be a scale-space maximum at $(sx_0, sy_0, s^2t_0)$ in the rescaled image
        * *Consequence*. Local maxima / minima of the scale-normalized Laplacian are also used for scale selection in other contexts, e.g. corner detection, scale-adaptive feature tracking, SIFT, etc.
* *Reference*. https://en.wikipedia.org/wiki/Blob_detection

**Characteristic scale**. The scale producing peak of Laplacian response

**Automatic scale selection using convolution**. Generalization of automatic scale selection using LoG
1. Choose a template, or pattern, e.g. LoG filter, which we want to match against multiple scales of two images
2. Convolve the template upon multiple scales of the images to select, for each image, the scale which is compatible to the scale of the template
3. The two found scales of the two images are both compatible to the scale of the template, hence compatible to each other

**Generalization to scale-invariant CNN**. Automatic scale selection in this manner is similar to running the same CNN over multiple scales of an image for object detection, or feature extraction, purposes

### Difference-of-Gaussian detector
**Difference of Gaussian**. We can efficiently approximate the Laplacian with a difference of Gaussians
* *Formal*.
    * *LoG*. $\text{LoG}=\sigma^2 \cdot (G_{xx}(x,y;\sigma) + G_{yy}(x,y;\sigma))$
    * *DoG*. $\text{DoG}=G(x,y;k\sigma) - G(x,y;\sigma)$
* *Usage*. Used in Lowe's SIFT pipeline for feature detection
* *Pros*. 
    * No need to compute second-order derivatives
    * Gaussians are computed anyway, e.g. in a Gaussian pyramid
* *Key-point localization with DoG*.

    <div style="text-align:center">
        <img src="https://i.imgur.com/e0lPgZF.png">
        <figcaption>Lowe's DoG</figcaption>
    </div>

    1. Detect maxima of DoG in scale space
    2. Reject points with low contrast by thresholding
    3. Eliminate edge responses

### Combinations
**Motivation**. LoG and DoG scale invariant detection can be used on their own, or in combinations with single-scale keypoint detectors, e.g. Harris, Hessian, etc.

**Harris-Laplace**.
* *Initialization*. Multi-scale Harris corner detection
* *Scale selection*. Based on Laplacian

# Appendix
## Concepts
**Image stitching**. The process of combining multiple photographic images with overlapping fields of view to produce a segmented panorama or high-resolution image

**Blob detection**. Detect regions in a digital image, which differ in properties, e.g. brightness or color, compared to surrounding regions
* *Blob*. A region of an image, in which some properties are constant or approximately constant
    
    $\to$ All points in a blob can be considered in some sense to be similar to each other
    * *Most commonly used method*. Convolution
* *Classes of methods*. Consider some property of interest expressed as a function of position on the image
    * *Differential methods*. Based on derivatives of the function w.r.t position
    * *Local-extrema-based methods*. Based on finding the local maxima or minima of the function
* *History and motivation*. One main reason for studying and developing blob detectors is to provide complementary information about regions, which is not obtained from edge detectors or corner detectors, i.e.
    * Blob detections was used to obtain regions of interest for further processing
        * *Explain*. Such regions could signal the presence of objects or parts of objects in the image domain, with application to object recognition or object tracking
    * Blob detection is also used for peak detection, with application to segmentation
    * Blob descriptors is also used as main primitives for texture analysis and texture baseline stereo matching, and to signal the presence of informative image features for appearance-based object recognition based on local image statistics

**Structure tensor**. A matrix derived from the gradient of a function
* *Purpose*. 
    * Describe the distribution of the gradient in a specified neighborhood around a point
    * Make the information invariant w.r.t the observing coordinates
* *Generalization of 2D structure tensor*. Structure tensor can be generalized to 3D case, i.e.

    $$S(p)=\begin{bmatrix}
    I_x(p)^2 & & I_x(p) I_y(p) & I_x(p) I_z(p)\\
    I_x(p) I_y(p) & & I_y(p)^2 & I_y(p) I_z(p)\\
    I_x(p) I_z(p) & & I_y(p) I_Z(p) & I_z(p)^2\\
    \end{bmatrix}$$

## References
* [1] http://vision.stanford.edu/teaching/cs231a_autumn1112/lecture/lecture11_detectors_descriptors_cs231a_marked.pdf