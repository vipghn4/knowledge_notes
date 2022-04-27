<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Binary indexed tree](#binary-indexed-tree)
  - [Two's complement](#twos-complement)
  - [Binary indexed tree](#binary-indexed-tree-1)
  - [2D Fenwick tree](#2d-fenwick-tree)
<!-- /TOC -->

# Binary indexed tree
## Two's complement
**Ones' complement of a binary number**. The value obtained by inverting all the bits in the binary representation of the number
* *Ones' complement system or ones' complement arithmetic*. A system, in which negative numbers are represented by the one's complement of their corresponding positive numbers

**Two's complement**. A mathematical operation on binary numbers
* *Two's complement of an $N$-bit number*. Its complement w.r.t $2^N$
    * *Explain*. The sum of a number and its two's complement is $2^N$
    * *Example*. Consider the three-bit number $011_2$
        
        $\to$ Its two's complement is $101_2$, since $011_2 + 101_2 = 1000_2 = 8_{10}$
* *Computation*. The two's complement is calculated by inverting the bits and adding one
* *Usage*. Used as a method of signed number representation
    * *Idea*. When the most Significant bit is a one
        
        $\to$ The number is signed as negative

**Two's complement representation of signed integers**. Consider a fixed point binary values

$\to$ The two's complement of its binary representation encodes its negative
* *Example*. Consder the binary number $011_2=3_{10}$
    
    $\to$ Its two's complement $101_2$ encodes the inverse $−3_{10}$
    * *Explain*. The sign of most integers, all but one of them, can be reversed in this scheme by taking the two's complement of its binary representation
* *Advantages*.
    * As long as the inputs are represented in the same number of bits as the output, and any overflow beyond those bits is discarded from the result
        
        $\to$ The fundamental arithmetic operations of addition, subtraction, and multiplication are identical to those for unsigned binary numbers
        * *Consequence*. The system is simpler to implement, especially for higher-precision arithmetic
    * Unlike ones' complement systems, two's complement has no representation for negative zero
        
        $\to$ Two's complement does not suffer from its associated difficulties

**Alternative method for finding two's complement of a number**. Take its ones' complement and add one

## Binary indexed tree
**Problem of interest**. Consider an array `arr[0..n-1]`
1. Compute the sum of the first `i` elements 
2. Modify the value of a specified element of the array, i.e. `arr[i] = x` where `0 <= i <= n-1`

**Naive solution**.
* *Solution 1*. 
    * *Sum computation*. Run a loop from `0` to `i-1` and calculate the sum of the elements
        * *Complexity*. $O(n)$
    * *Array update*. Carry out `arr[i] = x`
        * *Complexity*. $O(1)$
* *Solution 2*. Create an extra array and store the sum of the first i-th elements at the i-th index in this new array
    * *Sum computation*. Can be calculated in $O(1)$ time
    * *Array update*. Take $O(n)$ time

**Binary indexed tree (Fenwick tree)**. An alternative solution achieving $O(\log n)$ time complexity for both operations
* *Representation*. Binary Indexed Tree is represented as an array `BITree[]`
    * *Tree node*. Each node stores the sum of some elements of the input array
    * *Tree size*. Equal to the the input array's size $n$
* *Initialization*. Initialize all the values in `BITree[]` as `0`

**Operations**.
* *`getSum(x)`*. 
    * *Procedure*. Compute the sum of the sub-array `arr[0..x]`
        1. Initialize the output sum as `0`, the current index as `x+1`
        2. While the current index is greater than `0`, do the following
            1. Add `BITree[index]` to sum 
            2. Go to the parent of `BITree[index]`
                * *Explain*. Removing the last set bit from the current index, i.e.

                    ```
                    index = index – (index & (-index))
                    ```

        3. Return sum
* *`update(x, val)`*. 
    * *Procedure*. Updates the BIT by performing `arr[index] += val`
        1. Initialize the current index as `x+1`
        2. While the current index is smaller than or equal to `n`, do the following 
            1. Add the `val` to `BITree[index]` 
            2. Go to next element of `BITree[index]`
                * *Explain*. Incrementing the last set bit of the current index, i.e.
                    
                    ```
                    index = index + (index & (-index))
                    ```
    
    * *Idea*. Make sure that all the BITree nodes containing `arr[i]` within their ranges being updated 
        
        $\to$ We loop over such nodes in the BITree by repeatedly adding the decimal number corresponding to the last set bit of the current index

**How BIT work**. 
* *Motivation*. All positive integers can be represented as the sum of powers of `2`
    
    $\to$ Every node of the BITree stores the sum of `n` elements where `n` is a power of `2`
        
    <div style="text-align:center">
        <img src="https://i.imgur.com/7sFjZCQ.png">
        <figcaption>BIT tree</figcaption>
    </div>

    <div style="text-align:center">
        <img src="https://i.imgur.com/IGmMIss.png">
        <figcaption>Original BIT tree</figcaption>
    </div>

    * *Example*. The sum of the first 12 elements can be obtained by 
        * The sum of the last 4 elements, i.e. from 9 to 12, plus
        * The sum of 8 elements, i.e. from 1 to 8
* *Responsibility range of a node in BIT*. According to its last set bit
    * *Examples*.
        * The last set bit of $6_{10}=00110_2$ is a 2-bit

            $\to$ It will be responsible for a range of 2 nodes, i.e. 
            * From $00101_2$ to $00110_2$, i.e. latest version, or
            * From $00110_2$ to $00111_2$, i.e. original version
        * The last set bit of $12_{10}=01100_2$ is a 4-bit

            $\to$ It will be responsible for a range of 4 nodes, i.e. 
            * From $01001_2$ to $01100_2$, i.e. latest version, or
            * From $01100_2$ to $01111_2$, i.e. original version
    * *Sum operation*. Consider the latest version, since `BIT[index]` holds the sum of `BIT[index-(index & (-index))+1:index]`

        $\to$ We iterate to `BIT[index-(index & (-index))]` to accumulate remaining sums
    * *Update opeartion*. Consider the latest version, since `index` is within the range `[index-(index & (-index))+1..index+(index & (-index))]`

        $\to$ We iterate to `BIT[index+(index & (-index))]` to move to the parent node
    * *Consequence*. By increasing the last set bit of $12_{10}$

        $\to$ We move on to its parent node, i.e. $10000_2$ 
* *Complexity*. 
    * The number of set bits in the binary representation of a number $n$ is $O(\log n)$
        
        $\to$ We traverse at-most $O(\log n)$ nodes in both `getSum()` and `update()` operations
    * The complexity of the construction is $O(n \log n)$ as it calls `update()` for all `n` elements

## 2D Fenwick tree
**2D BIT**. A BIT where each element is another BIT
* *Assumptions*. The total rectangle is `[(0, 0), (max_x, max_y)]`
* *Operations*.
    * *Updating by adding `v` on `(x, y)`*. The effect will be found throughout the rectangle `[(x, y), (max_x, max_y)]`
    * *Query for `(x, y)`*. Return the result of the rectangle `[(0, 0), (x, y)]`
* *Cautions*. When querying and updating on a 2D BIT
    
    $\to$ We must be careful about how many times we are subtracting a rectangle and adding it

**Simple set formula**. If we want to get the result of a specific rectangle `[(x1, y1), (x2, y2)]`, the following steps are necessary

```asm
Query(x1,y1,x2,y2) = getSum(x2, y2)-getSum(x2, y1-1) -
                     getSum(x1-1, y2)+getSum(x1-1, y1-1)
```

where `Query(x1,y1,x2,y2)` means the sum of elements enclosed in the corresponding rectangle

>**NOTE**. `x1<=x2` and `y1<=y2` must hold

**Pseudo-code**.
* *Least significant bit operation*.

    ```
    function LSB(i):
        return i & (-i)
    ```

* *Updating array at index `x`*. Complexity $O[\log (M N)]$
    
    ```
    function update(x, y, value):
        while x <= m:
            # cannot directly use y since y becomes 0 after single loop
            y' = y
            while y' <= n:
                ft[x][y'] = ft[x][y'] + val
                y' = y' + LSB(y')
            x = x + LSB(x)
    ```

* *Querying an interval*. Complexity $O[\log (M N)]$

    ```
    function query(x, y):
        sum = 0
        while x > 0:
            # cannot directly use y since y becomes 0 after single loop
            y' = y
            while y > 0:
                # Process appropriately
                sum = sum + ft[x][y]
                y' = y' + LSB(y')
            x = x + LSB(x)
        return sum
    ```