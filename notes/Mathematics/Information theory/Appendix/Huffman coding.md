<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Huffman coding](#huffman-coding)
- [Variations of Huffman coding](#variations-of-huffman-coding)
<!-- /TOC -->

# Huffman coding
**Huffman coding base idea**.
* In an optimum code, symbols with higher probability should have shorter codewords
* In an optimum prefix code, the two symbols having least probabilities will have the same length

    $\to$ Otherwise, the truncation of the longer codeword to the same length still product a decodable code

**Huffman coding redundancy**. 
* *Huffman coding redundancy*. $0 \geq p < 1$ bit per symbol
    * *Explain*. Use mathematical induction proof
    * *Consequence*. Huffman coding is optimal for a symbol-to-symbol coding with a known input probability distribution
* *Theorem*. For any distribution $f_X$, a prefix code can be found, with code rate $H(X) \geq R < H(X)+1$
    * *Explain*. For each possible value $x \in \cal{X}$

        $\to$ We can achieve $R$ by representing each $x$ with $\lceil \log\frac{1}{p(x)} \rceil$ symbols

# Variations of Huffman coding
**Vector Huffman coding**.
* *Drawback of Huffman coding*. Very inefficient when $H(X)$ is much smaller than $1$ bit per symbol
* *Idea*. Combine $m$ successive symbols to a new block-symbol, i.e. Huffman code for block-symbols
* *Redundancy*. $H(X) < R < H(X) + \frac{1}{m}$

>**NOTE**. Vector Huffman coding can be used to exploit statistical dependencies between successive symbols

* *Drawback*. Expontnially growing alphabet size, i.e. $\|\cal{X}\|^m$

**Truncated Huffman coding**.
* *Idea*. Reduce the size of Huffman code table and maximum Huffman code word length by Huffman-coding only the most probable symbols
* *Implementation*.
    * Combine $J$ least probable symbols of an alphabet of size $K$ into an auxillary symbol $\text{ESC}$
    * Use Huffman code for alphabet containing of remaining $K-J$ most probable symbols and $\text{ESC}$
    * If $\text{ESC}$ is encoded, append $\lceil \log_2 J \rceil$ bits to specify exact symbol from the full alphabet
* *Tradeoff*. Longer code word length

**Adaptive Huffman coding**. Used when source statistics are not known beforehand
* *Forward adaption*.
    * Measure source statistics at encoder by analyzing entire data
    * Transmit Huffman code table ahead of compressed bit-stream
    
    >**NOTE**. JPEG uses this concept

* *Backward adaption*.
    * *Idea*.
        * Measure source statistics both at encoder and decoder, using the same previously decoded data
        * Regularly generate identical Huffman code tables at transmitter and receiver
    * *Pros and cons*.
        * *Pros*. Save overhead of forward adaptation, but usually poorer code tables, since based on past observations
        * *Cons*. Generally avoided due to computational burden at decoder