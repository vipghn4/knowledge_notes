<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Local descriptors and SIFT](#local-descriptors-and-sift)
  - [Local descriptors](#local-descriptors)
    - [Invariance and covariance](#invariance-and-covariance)
    - [Local descriptors](#local-descriptors-1)
    - [Scale invariant feature transform (SIFT)](#scale-invariant-feature-transform-sift)
    - [An assortment of other descriptors](#an-assortment-of-other-descriptors)
  - [Recognition and matching with local features](#recognition-and-matching-with-local-features)
    - [Matching objects with local features](#matching-objects-with-local-features)
- [Appendix](#appendix)
  - [References](#references)
<!-- /TOC -->

# Local descriptors and SIFT
## Local descriptors
### Invariance and covariance
**Problem of interest**. How to describe interesting points for matching purposes

<div style="text-align:center">
    <img src="https://i.imgur.com/7sWriFL.png">
    <figcaption>Local descriptors for matching purposes</figcaption>
</div>

* *Requirements for point descriptor*. Distinctive and invariant to transformations

**Rotation invariant descriptors**.
* *Idea*.
    1. Find local orientation by finding the dominant direction of gradient for each image patch
    2. Rotate patch according to the dominant orientation to put the patch into a canonical orientation
* *Orientation normalization*.
    1. Compute the orientation histogram
    2. Select the dominant orientation
    3. Rotate the patch to to a fixed orientation for normalization

**Affine adaptation**. Required to match regions under viewpoint changes

<div style="text-align:center">
    <img src="https://i.imgur.com/W2zpthL.png">
    <figcaption>Affine adaptation</figcaption>
</div>

* *Problem*.
    * *Assumptions*. Shape can be described by local affine frame
    * *Problem*. Determine the characteristic shape of the region
    * *Solution*. Use an iterative approach
        1. Use a circular window to compute second moment matrix
        2. Compute eigenvectors to adapt the circle to an ellipse
        3. Recompute second moment matrix using new window
        4. Iterate the above steps
* *Iterative affine adaptation*.
    1. Detect key-points, e.g. using multi-scale Harris
    2. Automatically select the scales
    3. Adapt affine shape based on second-order moment matrix
    4. Refine point location
* *Affine normalization - Deskewing*.
    1. Rotate the ellipse's main axis to horizontal
    2. Scale the x axis, such that it forms a circle

**Invariance and covariance**.
* *Assumptions*.
    * $f$ is a feature extractor
    * $t$ is a image transformation
    * $I$ is an image
* *Invariance*. $f(t(I)) = f(I)$
* *Covariance*. $f(t(I)) = t(f(I))$
* *Requirements for detection and description*.
    * Detection algorithms should be covariant
    * Description algorithms should be invariant

### Local descriptors
**Naive descriptor**. List of intensities within a patch
* *Invariance*. This descriptor is invariant to translation
* *Drawbacks*. Small shifts can affect matching score a lot
    * *Solution*. Use histograms

### Scale invariant feature transform (SIFT)
**Benefits of SIFT**.
* Can handle changes in viewpoint up to roughly 60 degrees out-of-plane rotation
* Can handle significant changes in illumination, sometimes even day and night
* Fast and efficient, i.e. can run in real time
* Lots of code available

**SIFT descriptor**
* *Descriptor computation*.
    1. Divide patch into $4\times 4$ sub-patches, i.e. 16 cells in total
    2. Compute historgram of gradient orientations, with 8 reference angles, for all pixels inside each sub-patch

        $\to$ The descriptor has $128 = 4\times 4\times 8$ dimensions
* *Information given for each image*.
    * $n$ 128-D descriptors, i.e. each one is a histogram of gradient orientations within a patch
    * $n$ scale parameters specifying the size of each patch
    * $n$ orientation parameters specifying the angle of the patch
    * $n$ 2D points giving positions of the patches

**SURF descriptor**. A fast approximation of SIFT, which can be efficiently computed using 2D convolution filters and integral images

$\to$ This algorithm is 6 times faster than SIFT, with equivalent quality for object identification
* *Statistics*. GPU implementation available with 100Hz for feature extraction, i.e. detector and descriptor, for $640\times 480$ images

### An assortment of other descriptors
**Gray-scale intensity**.

<div style="text-align:center">
    <img src="https://i.imgur.com/POVqAXO.png">
    <figcaption>Gray-scale intensity feature descriptor</figcaption>
</div>

**Steerable filters**. An orientation-selective convolution kernel used for image enhancement and feature extraction, which can be expressed as a linear combination of a small set of rotated versions of itself

<div style="text-align:center">
    <img src="https://i.imgur.com/HbQ4ngW.png">
    <figcaption>First x-derivative of rotated Gaussians</figcaption>
</div>

* *Steering*. The process, by which the oriented filter is synthesized at any given angle
* *Example*.
    * *Assumptions*.
        * $G(x,y)=\exp(-(x^2 + y^2))$ is the 2D circularly symmetric Gaussian function
            * Scaling and normalization constants are set to one for convenience
        * $G_n$ is the $n$-th derivative of a Gaussian in the $x$ direction
        * $(\cdot)^\theta$ represents the rotation operator, i.e. for any function $f(x,y)$

            $\to$ $f^\theta(x,y)$ is $f(x,y)$ rotated through an angle $\theta$ about the origin
    * *First $x$-derivative of a Gaussian $G_1^{0^o}$*. 
        
        $$G_1^{0^o}=\frac{\partial}{\partial x} \exp(-(x^2 + y^2))=-2x\exp(-(x^2 + y^2))$$
    
    * *Firts $x$-derivative of a Gaussian $G_1^{90^o}$*.

        $$G_1^{90^o} = \frac{\partial}{\partial y} \exp(-(x^2 + y^2))=-2y\exp(-(x^2 + y^2))$$
    
    * *$G_1$ filter at an arbitrary orientation $\theta$*. Can be synthesized by a linear combination of $G_1^{0^o}$ and $G_1^{90^o}$

        $$G_1^\theta = \cos\theta G_1^{0^o} + \sin\theta G_1^{90^o}$$
    * *Consequence*. Given

        $$R_1^{0^o} = G_1^0 * I,\quad R_1^{90^o} = G_1^{90} * I$$

        then

        $$R_1^\theta = \cos\theta R_1^{0^o} + \sin\theta R_1^{90^o}$$

    * *Basis filters for $G^\theta_1$*. $G_1^{0^o}$ and $G^{90^o}$
    * *Interpolation functions for basis filters*. $\cos\theta$ and $\sin\theta$
* *Reference*. http://people.csail.mit.edu/billf/www/papers/steerpaper91FreemanAdelson.pdf

**Gaussian derivative feature descriptor**. Compute Gaussian derivatives up to 4th order

$\to$ The remaining derivatives can be computed by rotation of 90 degrees

<div style="text-align:center">
    <img src="https://i.imgur.com/7nhqsVb.png">
    <figcaption>Gray-scale intensity feature descriptor</figcaption>
</div>

**Gradient location and orientation histogram (GLOH)**. Very similar to SIFT
* *Log-polar location grid*. A coordinate system in 2D, where a point is identified by the logarithm of the distance to a certain point, and the angle
    * *Log-polar grid quantization*. 3 bins in radial direction and 3 bins in angular direction
* *Image quantization*. The image is evenly divided into a $4\times 4$ grid, whose features are extracted independently and concatenated together
* *Feature space*.

    <div style="text-align:center">
        <img src="https://i.imgur.com/AFUVGp6.png">
        <figcaption>17 bins in log-polar location grid</figcaption>
    </div>

**Other local descriptors**. Shape context, geometric blur, etc.

**Advantages of local features**.
* Critical to find distinctive and repeatable local regions for multi-view matching
* Complexity reduction via selection of distinctive points
* Describe images, objects, parts without requiring segmentation
* Robust to clutter, occlusion, moderate view changes, noise, blur, etc.

## Recognition and matching with local features
**Recognition with local features**. Image content is transformed into local features, which are invariant to translation, rotation, and scale

$\to$ We need to verify if they belong to a consistent configuration

**Finding consistent configurations**.
* *Global spatial models*. Generalized Hough transform, RANSAC, etc.
    * *Basic assumption*. Object is planar

### Matching objects with local features
**Generalized Hough transform recognition**. Typically only 3 features matches are required for recognition, though extra matches provide robustness
* *Affine model*. Can be used for planar objects, i.e. 2D obejcts which may exist anywhere in 3D space
* *Idea*. The modification of the Hough transform using the principle of template matching
    * *Hough transform*. Originally developed to detect analytically defined shapes, given the knowledge of the shape

        $\to$ Hough transform will find out the location and orientation of the shape in the ima image
    * *Idea of modification*. Use Hough transform to detect an arbitrary object described with its model
* *Problem of finding the object described with a model in an image*. Solved by finding the model's position in the image

    $\to$ This is transformed to a problem of finding the transformation's parameter mapping the model into the image
    * *Explain*. Given the value of the transformation's parameter, the position of the model in the image can be determined
* *Original implementation*. 
    1. Use edge information to define a mapping from orientation of an edge point to a reference point of the shape

        $\to$ Every pixel of the image votes for its corresponding reference points
    2. The maximum points of the Hough space indicate the possible reference points of the pattern in the image

**View interpolation**.
* *Training*. 
    * Training views from similar viewpoints are clustered based on feature matches
    * Matching features between adjacent views are linked
* *Recognition*. Feature matches may be spread over several training view points

    $\to$ Use the known links to "transfer votes" to other viewpoints

# Appendix
## References
* [1] http://vision.stanford.edu/teaching/cs231a_autumn1112/lecture/lecture12_SIFT_single_obj_recog_cs231a_marked.pdf