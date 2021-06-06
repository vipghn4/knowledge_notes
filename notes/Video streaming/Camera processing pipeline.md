---
title: Camera processing pipeline
tags: Video streaming
---

# Table of Contents
[toc]

# Camera processing pipeline
## Imaging without optics
**Pinhole camera and conventional camera**. 

<div style="text-align:center">
    <img src="/media/OkkFlHF.png">
    <figcaption>Pinhole and lens camera</figcaption>
</div>

* *Pinhole camera*. A simple camera without a lens, but with a tiny aperture, i.e. the pinhole

    $\to$ It is effectively a light-proof box with a small hole in one side
    * *Light capturing*. Light from a scene passes through the aperture and projects an inverted image on the opposite side of the box
    * *Pros and cons*.
        * *Pros*. Easy to implement and optimize
        * *Cons*. Less light
* *Conventional camera*. Use a glass lens with or without a shutter to direct the light to the recording surface
    * *Pros and cons*.
        * *Pros*. More light
        * *Cons*. Hard to implement and optimize

**Effect of pinhole size**.

<div style="text-align:center">
    <img src="/media/nMfYqvN.png">
    <figcaption>Effect of pinhole size</figcaption>
</div>

* *Large pinhole*. Cause geometric blur
* *Optimal pinhole*. Too little light
* *Small pinhole*. Cause diffraction blur

## Implementation of lens camera
**Complexity of real lenses**.

<div style="text-align:center">
    <img src="/media/8lWpkS8.png">
    <figcaption>Real lenses are complex</figcaption>
</div>

* *Thin lens approximation*. Ignore optical effects due to the thickness of lenses and simplifies ray tracing calculations

**Changing the focus distance**.

<div style="text-align:center">
    <img src="/media/Vxcs0cv.png">
    <figcaption>Changing the focus distance</figcaption>
    <figcaption>The two circles are focal lengths relative to the lens</figcaption>
</div>

* To focus on objects at different distances

    $\to$ We move the sensor relative to the lens, i.e. due to the thin-lens equation
* Assume the formula $\frac{1}{f} = \frac{1}{s_o} + \frac{1}{s_i}$, then at $s_o=s_i=2f$

    $\to$ We get $1:1$ imaging macro
* We cannot focus on objects closer to the lens than $f$, i.e. due to the thin-lens equation

**Chromatic aberration**. Different wavelengths refract at different rates

$\to$ This results in different focal lengths
* *Solution*. Correct the focal lengths with achromatic doublet to align red and blue rays

    <div style="text-align:center">
        <img src="/media/b0PnfUd.png">
        <figcaption>Achromatic doublet</figcaption>
    </div>

    * *Convex lens of crown glass*. Low refraction index $n$ and high Abbe number, i.e. low dispersion
    * *Concave lens of flint glass*. High refraction index $n$ and low Abbe number, i.e. high dispersion

**Lens distortion**. A deviation from rectilinear projection
* *Optical magnification*. The ratio between the apparent size of an object, i.e. its size in an image, and its true size
* *Types of optical distortion*.

    <div style="text-align:center">
        <img src="/media/Yp9Soyr.png">
        <figcaption>Types of optical distortion</figcaption>
    </div>

    * *Barrel distortion*. Image magnification decreases with distance from the optical axis
    * *Pincushion distortion*. Image magnification increases with the distances from the optical axis
    * *Mustache distortion*. A mixture of barrel and pincushion distortions
        * *Explain*. Start as barrel distortion close to the image center, and gradually turn into pincushion distortion towards the image periphery

**Vignetting**. A reduction of an image's brightness or saturation toward the periphery compared to the image center

<div style="text-align:center">
    <img src="/media/h7cnw8v.png">
    <figcaption>Vignetting explanation</figcaption>
</div>

* *Solution*. Use calibration, i.e.
    1. Take a photo of uniformly white object

        $\to$ The picture shows the attenuation
    2. Divide the pixel values with the taken photo

## Image sensor
**CMOS sensor**.

<div style="text-align:center">
    <img src="/media/XZ6b5Gt.png">
    <figcaption>CMOS sensor integrated circuit architecture</figcaption>
</div>

**Front- and back-illuminated sensor**. Types of digital image sensor with specific arrangements of imaging elements

<div style="text-align:center">
    <img src="/media/df9cRVe.png">
    <figcaption>Front- and back-illuminated sensor</figcaption>
</div>

* *Photodiode*. A semi-conductor device converting light into an electrical current

**Anti-aliasing filter**. Help remove image aliasing effects of low resolution image sensor board

**Problems with raw images**.
* *Pixel non-uniformity*. Each pixel has a slightly different sensitivity to light, i.e. typically within $1$% to $2$%
    * *Solution*. Calibrate an image with a flat-field image

        $\to$ This also eliminate the effects of vignetting and other optical variations
* *Stuck pixels*. Some pixels are turned always on or off
    * *Solution*. Identify them and replace with filtered values
* *Dark floor*. Temporature adds  noise to the image

**Analog-to-digital (AD) conversion**. Sensor converting the continuous light signal to a continuous electrical signal, i.e. analog signal
* *AD conversion*. The analog signal is converted to a digital signal
    * *Output resolution*. $10$ bits (even on cell phones), often $12$ bits or more
    * *Mapping function*. Roughly linear sensor response
* *Example*. The example below is an example of 2-bit representation

    $$f(x)=\begin{cases}
    00 & x\in[0, 2.5)\\
    01 & x\in[2.5, 5)\\
    10 & x\in[5, 7.5)\\
    11 & x\in[7.5, \infty)
    \end{cases}$$
* *Amplification in AD conversion with ISO*. Before conversion, the signal can be amplified
    * *Example*.
        * *ISO 100*. No amplification
        * *ISO 1600*. 16x amplification
    * *Pros and cons*.
        * *Pros*. We can see details in dark areas better
        * *Cons*. Noise is amplified as well, and the sensor is more likely to saturate

**Color filter array**. Use Bayer pattern
* *Motivation*. From human eyes, i.e.

<div style="text-align:center">
    <img src="/media/Bwcv3gs.png">
    <figcaption>Human eyes pattern is like Bayer pattern</figcaption>
</div>

<div style="text-align:center">
    <img src="/media/lUFOvIg.png">
    <figcaption>Why human eyes have Bayer pattern</figcaption>
</div>

* *Demosaicking*. We need to demosaic the image for visual purpose
    * *Option 1*. Use bilinear interpolation
        * *Pros*. Easy to implement
        * *Cons*. Fail at sharp edges
    * *Option 2*. Bilateral filtering
        * *Pros*. Take edges into account, i.e. avoid interpolating across edges
* *Denoising*. 
    * *Option 1*. Use non-local means
    * *Option 2*. Use block matching 3D (BM3D)
* *Color spaces for conversion*. 
    * *Lab*. Good for image processing
    * *YUV, YCbCr*. Good for video encoding, i.e. computationally cheap and similar to human vision

## Image processing
**Gamma encoding**.
* *Human contrast sensitivity*. About 1%
    * *Explain*. Like black is 1 and white is 100
* *Linear coding*. 
    * *Small step size*. Lead to wasted bits
    * *Large step size*. Lose detail in some range of intensity
* *Gamma coding*. Provide adaptive step size for ranges of intensity

**Luminance from RGB**.
* *Idea*. If 3 sources of same radiance appear R, G, B, then
    * Green
* *Luminance formulas*.
    * *NTSC*. $0.299 \cdot R + 0.687 \cdot G + 0.114 \cdot B$
    * *CIE*. $0.2126 \cdot R + 0.7152 \cdot G + 0.0722 \cdot B$
    * *ITU*. $0.2125 \cdot R + 0.7154 \cdot G + 0.0721 \cdot B$
* *Simplified formula*. $1/4 \cdot R + 5/8 \cdot G + 1/8 \cdot B$

**Camera use sRGB**. 
* *sRGB*. A standard RGB color space since 1996
    * *Color components*. Use the same primaries as used in studio monitors and HDTV, and a gamma curve typical of CRTs
    * *Benefits*. Allow direct display
* *RGB sensor to standard*. Need calibration

**Responsive curves**. A curve showing the relation between the amount of incoming light and image pixel values of a digital camera
* *Linear and nonlinear light-to-pixel relationships*. Using non-linear relationship allows minimizing perceptual errors due to quantization

## 3A - Automated selection of key camera control values
**Automated selection of key camera control values**. Auto-focus, auto-exposure, and auto-white-balance

## Camera data flow architecture

<div style="text-align:center">
    <img src="/media/EyFbpCh.png">
    <figcaption>Camera data flow pipeline</figcaption>
</div>

**Traditional camera APIs**. Real image sensors are pipelined
* *Explain*. While one frame exposing, the next one is being prepared, and the previous one is being read out

**Camera running modes**.
* *View-finding*. 
    * Pipelined, high frame rate
    * Settings changes take effect sometime later
* *Still capture mode*.
    * Need to know which parameters were used
    * Reset pipeline between shosts, i.e. slow

**FCam architecture**. A software architecture for programmable cameras

<div style="text-align:center">
    <img src="/media/RMitp9A.png">
    <figcaption>FCam architecture</figcaption>
</div>

* *Purpose*. Attempt to expose the maximum device capabilities, while remaining easy to program
* *Components*.
    * *Image sensor*. A pipeline converting requests into images
        * *Stateless*. There is no global state, i.e.
            * State travels in the request through the pipeline
            * All parameters are packed into the requests
    * *Image signal processor (ISP)*. 
        * Receive sensor data and optionally transform it

            >**NOTE**. Untransformed raw data must also be available
        
        * Compute helpful statistics, e.g. histograms, sharpness maps, etc.
    * *Devices*. Schedule actions to be triggered at a given time into an exposure, and tag returned images with metadata
        * *Example*. Lens, flash, etc.
* *Case study*. NvMedia architecture

# Appendix
## Concepts
**Circle of confusion**. An optical spot caused by a cone of light rays from lens not coming to a perfect focusing when imaging a point source

<div style="text-align:center">
    <img src="/media/QjNUrk8.png">
    <figcaption>Circle of confusion</figcaption>
</div>

**Depth of field (DoF)**. The distance between the nearest and farthest objects, which are in acceptably sharp focus in an image

<div style="text-align:center">
    <img src="/media/Qp2rmTj.png">
    <figcaption>Depth of field and camera focusing</figcaption>
</div>

**Color temperature of a light source**. The temperature of an ideal black-body radiator, which radiates light of a color comparable to that of the light source
* *Characteristics of visible light*. Color temperature is a characteristic of visible light
* *Application*.
    * Meaningful only for light sources, which corresponds closely to the radiation of some black body
        * *Example*. Light in a range, from red to orange to yello to white to blueish white
    * It does not make sense to consider the color temperature of e.g. a green or a purple light
* *Unit of measurements*. Kelvins (K), i.e. a unit of measure for absolute temperature

## References
* https://web.stanford.edu/class/cs231m/lectures/lecture-11-camera-isp.pd