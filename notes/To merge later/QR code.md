<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [QR code demystification](#qr-code-demystification)
  - [Introduction](#introduction)
  - [QR code structure](#qr-code-structure)
    - [Patterns](#patterns)
    - [Data](#data)
  - [Data encoding](#data-encoding)
- [Appendix](#appendix)
  - [Reference](#reference)
<!-- /TOC -->

# QR code demystification
## Introduction
**Quick Response (QR) code**. Refer to a kind of 2D “bar code”, which are generally meant to be scanned by mobile devices
* *QR code visual structure*. Square grids filled with black and white squares
    * *Finder Patterns*. Three of the corners have distinctive concentric squares, i.e. Finder Patterns
    * *Modules*. Little squares making up the symbol, each of which represents one bit of data, and is either white or black, i.e. 0 or 1
        * *Colorized modules*. We can use other colors with sufficient contrast
        * *Usage*. 
            * Most of the modules are used for data and error correction
            * Some modules are reserved for Finder Patterns, Timing Patterns, Version Information, Format Information, and Alignment Patterns
        * *Module size*. There is no requirement on the dimensions of the modules
            * *Too small size*. Readers will have a difficult time with very tiny symbols
            * *Too large size*. Readers will need to be quite far away from especially large ones to capture the code
    * *Code size*. There are 40 QR Code versions, which basically refers to the size, i.e.
        * Version 1 has 21 modules wide by 21 modules tall
        * Each successive version increases this by 4 modules in each direction
    * *Bounding blank space*. Each version also must be surrounded by blank white space equal in thickness to 4 modules
* *QR code scanning*. Use an application with the devices camera to scan the code
* *Usage*. The data stored in a QR Code can be used to
    * Direct users to a specific URL
    * Provide contact information via vCard
    * Cause the device to compose a text-message or email

**Error correction in QR code**. 
* *Types of error correction modes*. Each of the 40 versions support 4 types of error correction, i.e. L, M, Q, and H
    * *L-type error correction*. Support roughly 7% of data to be restored
    * *M-type error correction (default)*. Support restoration of roughly 15% of the data
    * *Q-type error correction*. Support about 25% of restoration
    * *H-type error correction*. Support about 30% of restoration
* *Choice of error correction mode*. 
    * Higher EC modes allow more of the data to be recovered in case the symbol is damaged or obscured
    * Lower EC modes require less modules to be used for EC, leaving more to be used for data

## QR code structure
**QR code structure**.

<div style="text-align:center">
    <img src="https://i.imgur.com/DYsEekw.png">
    <figcaption>QR code structure</figcaption>
</div>

### Patterns
**Finder pattern**. Concentric squares of alternating colors lying in all corners of the symbol except the bottom right
* *Purposes*. Used by decoders to identify the symbol as a QR Code, and to establish orientation
* *Structure*. A full pattern 7x7 modules
    * *Inner structure*. The center is a 3x3 black square and is surrounded by a one-thick white box, which is surrounded by a one-thick black box
    * *Outer structure*. The sides not placed against the edges of the symbol are surrounded by one module of white space
* *Dark module*. A single black module located to the right of the top-right corner of the white space around the bottom-left module

**Alignment pattern**. Used in symbols of version 2 and higher to help decoders adjust for skewing in the symbol
* *Explain*. Without this pattern, it would be much harder for a decoder to convert a skewed photograph into the virtual grid of data
* *Structure*. Concentric squares with a single black module at the center
    * *Surrounding modules*. The pattern is surrounded by a one-thick white box, which is surrounded by a one-thick black box, with no white space outside of that
* *Number of alignment patterns*. Higher versions have more alignment patterns placed across the symbol

**Timing pattern**. An alternating stripe of black and white modules located vertically and horizontally between the finder patterns
* *Structure*. Starting with black on the innermost black corner of the finder patterns
    
    $\to$ The patterns alternate values toward the adjacent finder patterns
* *Number of timing patterns*. There are two lines to the timing pattern, i.e.
    * One running horizontally between the two top finder patterns
    * One running vertically between the two left-side finder patterns

### Data
**Format data**. The data in a QR symbol is masked by reversing modules in certain positions
* *Picking modules for reading*. For the decoder to know which modules to read as reversed
    
    $\to$ The selected mask is stored twice, along with the EC version
    * *Explain*. After the format information is encoded to 15 bits, it is placed in the symbol twice
* *Format data placement*.
    * *First copy*. Start on the far left, directly beneath the white space around the top-left finder pattern
        * *Horizontal part*. 
            * The highest-order bit is placed at the left-most pixel, and subsequent bits are placed to the right
            * The module of the timing pattern in the way is ignored
            * Two more bits are placed to the right
        * *Vertical part*. 
            * The module from the other timing pattern is ignored
            * The remaining modules are placed vertically until the 15th bit, i.e. the lowest-order, is placed on the top row of the symbol
    * *Second copy*. Begin on the bottom just to the right of the white space around the bottom-left finder pattern
        * *Vertical part*. The bits are placed in descending order upward, alongside the white space, until the black module by the corner of the finder pattern is reached
        * *Horizontal part*. Placed immediately below the bottom-left of the white space around the top-right finder pattern
            
            $\to$ Subsequent bits are placed to the right, with the final bit located in the last column

**Version data**. Indicate which version is being used
* *Structure*. The data takes 18 modules and is located against the top of the symbol, to the left of the top-right finder pattern
    * *Data region size*. 3 modules wide and 6 modules high
    * *Data replication*. A duplicate is placed against the left side of the symbol, above the bottom-right finder pattern
        * *Replicated data size*. 3 modules high and 6 modules wide

**Data and error correction**. After the data is encoded

$\to$ An EC algorithm is applied to ensure the symbol can be decoded, even if part of it is obscured or smudged
* *Data and EC location*. Stored in the modules that are not used by anything else mentioned above

**Mandatory blank space**. The QR specification requires a space equal to the width of four modules all around the symbol to be blank

$\to$ This is to prevent interference from the other things on the same surface

## Data encoding
**Encoding methods**. Numeric, Alphanumeric, Binary, and Kanji
* *Numeric encoding*. Only support the digits `0-9`, but can store 3 of them in only 10 bits
* *Alphanumeric encoding*. Support letters `A-Z`, i.e. upper-case only, digits `0-9`, and the special characters `$%*+-./:` and space
    
    $\to$ It is good for encoding URLs and simple text
    * *Storage consumption*. It takes 11 bits to store 2 alphanumeric characters
* *Binary encoding*. Stored 8 bits per character, and supports the 256 characters in the extended ASCII table
* *Kanji encoding*. Take 11 bits for a single character

**Encoding method and data length indication**. To encode data with an encoding method

$\to$ We indicate which method to use, and how much data to store
* *Method indication*. Use 4 bits, i.e. `0001` for numeric, `0010` for alphanumeric, `0100` for binary, and `1000` for Kanji
* *Data length indication*. The encoding method determines how many bits we use to indicate the data length
    * *Example*. Consider encoding 5 binary characters to a version 1 symbol
        
        $\to$ The binary data we start with will be `0100 00000101`, i.e.
        * `0100` to indicate binary
        * `00000101` is the 8-bit representation of 5, i.e. the data length
* *Combination of encoding methods and data lengths*. It is also possible to use different methods
    * *Explain*. By appending a new method/size indicator after the previous data, followed by the new data
        * *Example*. `Method1, Size1, Data1, Method2, Size2, Data2`

**Appending data to the symbol**. Once indicated encoding method and data length, we add the data
* *Adding binary data*. Simply take the 8-bit representation of the character and add it to the data
* *Adding numeric data*. Take sets of three digits
    1. For each set of three, encode them directly to their 10-bit binary representations
    2. If at the end of the data, we have some digits left
        * If there is 1 digit left, encode it to 4 bits
        * If there are 2 digits left, encode it into 7 bits
* *Adding alphanumeric data*. 
    1. Convert each character to its numerical value
    2. Take pairs of characters, multiply the first numerical value by `45`, and add the second numerical value
    3. Convert the pair to 11-bit binary
    4. If there is one character left at the end of the data
        
        $\to$ Encode its value to 6-bits
* *Handling excessive space*. If there is some space left after adding all the data
    
    $\to$ We need to add some padding, i.e.
    1. Add `0000`, then, if the number of bits in your data is not divisible by 8, add `0`s until it is
    2. Alternately add `11101100` and `00010001` until we reach the limit for the version and EC mode

# Appendix
## Reference
* https://www.matchadesign.com/news/blog/qr-code-demystified-part-1/