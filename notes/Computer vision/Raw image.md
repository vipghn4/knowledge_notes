---
title: Raw image
tags: Computer vision
---

# Table of Contents
[toc]

# Raw image format
## Introduction
**Introduction**.
* *Raw image format*. Contain minimally processed data from the image sensor
* *Purpose*. To save, with minimum loss of information, data obtained from the sensor

**Raw image formats**. Capture the radiometric characteristics of the scene at the best of the camera sensor's performance
* *Radiometric characteristics*. Physical information about the light intensity and color of the sense

>**NOTE**. Raw files themselves come in many proprietary file formats, e.g. Nikon's .NEF, Canon's CR2, etc.

>**NOTE**. There is a common open format, which is .DNG, i.e. Digital Negative

* *Dynamic range*. A raw digital image may have wider dynamic range or color gamut than the developed film or print
* *Raw image data*. Most raw image file formats store information sensed according to the geometry of the sensor's individual photo-receptive elements, i.e. pixels, rather than points in the expected final image

## Color sensing
**Color sensing technologies**.
* *Field-sequential*. Shot sequentially through RGB filters
    * *Cons*. May be affected by temporal resolution of the shot sequence
* *3-sensor*. Split the light into 3 colors using prism and dichroic mirrors, each routed to a separate CCD sensor
    * *Pros*. No light loss, as compared to filters
    * *Cons*. Expensive, and complicated lens design
* *Vertically stacked*. Longer wavelengths penetrate deeper into silicon
    * *Motivation*. Longer wavelengths penetrate deeper into silion

        $\to$ We can arrange a set of vertically stacked detectors
    * *Idea*. Top layer gets most blue, middle layer gets green, and bottom layer gets red
    * *Pros*. Fewer color artifacts than CFA
    * *Cons*. Possibly worse noise performance
* *Color filter array*. Use filter arrays such as Bayer CFA
    * *Why more green pixels than red or blue*.
        * Human eyes are most sensitive in the middle of the visible spectrum, which is green's spectrum
        * Sensitivity given by the human luminous efficiency curve
    * *Cons*. May be affected by the spatial resolution of the sensors and the filter blocks

## File contents
**File contents**. Contain the information required to produce a viewable image from the camera's sensor data
* *A short file header*. Typically contain an indicator of the byte-ordering of the file, a file identifier, and an offset into the main file data
* *Camera sensor metadata*. Required to interpret the sensor image data
    * *Example*. Sensor size, attributes of the color filter array (CFA), and its color profile
* *Image metadata*. Useful for inclusion in any content management system (CMS) environment or database
    * *Example*. Exposure settings, camera / scanner / lens model, date of shoot / scan, authoring information, etc.
* *An image thumbnail*. Reduced-size versions of the image, used to help in recognizing and organizing them
* *A full-size JPEG conversion of the image*. Used to preview the file on the camera's LCD panel
* *Timecode, keycode, or frame number*. Commonly appeared in motion picture film scans
* *The sensor image data*

**Sensor image data**. Raw files contain the full resolution, e.g. 12- or 14-bit, data as read out from each of the camera's image sensor pixels

<div style="text-align:center">
    <img src="/media/qppD2pB.png">
    <figcaption>Bayer RGGB CFA layout</figcaption>
</div>

* *Camera sensor*. Almost invariably overlaid with a color filter array (CFA), usually a Bayer filter consisting of $2\times 2$ matrix
    * *Color filter types*. RGGB, RCCB, RCCC
        * *C channel*. Stand for `clear`, which means no-filter, i.e. lights are totally perceived
* *Raw development*. The process of converting the mosaic of data into standard RGB form, which is to obtain a image from a raw file
    * *Luminance information*. Controlled by the green filter pair
        * *Explain*. Green is more sensitive to light

**Standardization**. There is no single raw format, i.e. different manufacturers use their own proprietary and typicall undocumented formats

>**NOTE**. A manufacturer even change the raw format from one camera model to the next

* *Problems*. Valuable raw photos captured recently may someday become inaccessible
    * *Explain*. Computer OSes and software programs become obsolete and abandoned raw formats are dropped in new software
    * *Solutions*. 
        * High-quality open source software for decoding raw image formats
        * Public documentation of RAW formats
        * Adoption of a universal RAW format
* *An example of widely used universal RAW format*. DNG

## Raw image processing
**Processing steps**.
* *Typical steps*.
    * *Decoding*. Image data of raw files are typically encoded for compression purpose, but also for obfuscation purpose
    * *Demosaicing*. Interpolating the partial raw data received from the color-filtered image sensor into a matrix of colored pixels
    * *Defective pixel removal*. Replacing data in known bad locations with interpolations from nearby locations
    * *White balancing*. Adjust color temperature of the light, which is used to take the photograph
    * *Noise reduction*. Trade off detail for smoothness by removing small fluctuations
    * *Color translation*. Convert camera native color space defined by the spectral sensitives of the image sensor to an output color space, e.g. RGB
    * *Tone reproduction*. Render the scene luminance captured by the camera sensors for pleasing effect and correct viewing on low-dynamic-range monitors or prints
        * *Sub-steps*. Tone mapping, and gamma compression
    * *Compression*. Compress the image
* *Common additional steps*.
    * Removal of systematic noise
    * Dark frame subtraction
    * Optical correction, e.g. lens distortion, chromatic aberration, and color fringing correction
    * Contrast manipulation
    * Increasing visual acuity by unsharp marking
    * Dynamic range compression, i.e. lighten shadow regions without blowing out highlight regions
* *Illustration*.
    * *Linearization and normalization*. 
        * *Linearization*. The camera may apply a non-linear transformation to the sensor data for storage purpose. Thus, we need to invert or somehow approximate the original sensor data
        * *Normalization*. Scale the pixels to 0 and 1
        
        <div style="text-align:center">
            <img src="/media/RKR5mnJ.png">
            <figcaption>Linearized and normalized image</figcaption>
        </div>
    
    * *White balancing then debayering*.

        <div style="text-align:center">
            <img src="/media/u1fsRBv.png">
            <figcaption>White balanced and debayered image</figcaption>
        </div>
    
    * *Color space correction*.

        <div style="text-align:center">
            <img src="/media/kvd59jV.png">
            <figcaption>Color corrected image</figcaption>
        </div>
        
    * *Brightness and  gamma correction*.
    
        <div style="text-align:center">
            <img src="/media/rSnMy2e.png">
            <figcaption>Brightness and gamma corrected image</figcaption>
        </div>

# Appendix
## Usecases
**NvMedia raw file**. Consist of metadata at the header and footer of the fail, and image data in the middle
* *Image data format*. Each pixel consists of 8 values totally
    * Each pixel consists of 4 entries, i.e. 4 entries of Bayer matrix
    * Each entry consists of 2 values of type `int` or `uint8_t`
* *Color translation*. Assume that the color filter array is RGGB

    >**NOTE**. The filter array color space may differ, e.g. RCCB, etc.

    * *Red*. Extracted by combining two red values of the red entry, i.e.

        ```c
        #define CONV_CALCULATE_PIXEL(pSrcBuff, srcPitch, x, y, xOffset, yOffset) \
            (pSrcBuff[srcPitch*(y + yOffset) + 2*(x + xOffset) + 1] << 2) | \
            (pSrcBuff[srcPitch*(y + yOffset) + 2*(x + xOffset)] >> 6)

        #define CONV_CALCULATE_PIXEL_UINT(pSrcBuff, srcPitch, x, y, xOffset, yOffset) \
                    pSrcBuff[srcPitch*(y + yOffset) + 2*(x + xOffset) + 1]
        ```
    
    * *Green*. 

        ```c
        *pTmp = ((CONV_CALCULATE_PIXEL(pSrcBuff, srcPitch, x, y, xOffsets[GREEN1], yOffsets[GREEN1])) +
                         (CONV_CALCULATE_PIXEL(pSrcBuff, srcPitch, x, y, xOffsets[GREEN2], yOffsets[GREEN2]))) /2 ;
        ```

    * *Blue*. Similar to Red

## Concepts
**HDR image**. Stand for high-dynamic-range imag