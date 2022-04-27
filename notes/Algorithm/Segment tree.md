<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Segment tree](#segment-tree)
<!-- /TOC -->

# Segment tree
**Segment tree**. Used to do preprocessing and query in moderate tim
* *Complexity*. 
    * *Preprocessing time*. $O(n)$
    * *Time complexity for a range query*. $O(\log n)$
    * *Space complexity required to store the segment tree*. $O(n)$
* *Representation*. 
    1. Leaf Nodes are the elements of the input array
    2. Each internal node represents minimum of all leaves under it
* *Tree structure*. For each node at index `i`
    * The left child is at index `2*i+1`
    * The right child is at `2*i+2`
    * The parent is at `⌊(i – 1) / 2⌋`

**Segment tree construction**.
* *Procedure*.
    1. Start with a segment `arr[0..n-1]`
    2. Every time we divide the current segment into two halves, i.e. if it has not yet become a segment of length 1
        
        $\to$ We call the same procedure on both halves
        * *Explain*. For each such segment, we store the minimum value in a segment tree node
* *Consequence*. 
    * All levels of the constructed segment tree will be completely filled except the last level
    * The tree will be a Full Binary Tree with $n$ leaves, since we always divide segments in two halves at every level
        
        $\to$ There will be n-1 internal nodes, i.e. the total number of nodes is $2n – 1$
    * Height of the segment tree will be $⌈\log_2 n⌉$

**Query for minimum value**.

```
// qs --> query start index, qe --> query end index
int RMQ(node, qs, qe)  {
    if range of node is within qs and qe
        return value in node
    else if range of node is completely outside qs and qe
        return INFINITE
    else
        return min(
            RMQ(node's left child, qs, qe),
            RMQ(node's right child, qs, qe)
        )
}
```

**Lazy propagation**. When there are many updates and updates are done on a range

$\to$ We can postpone some updates, i.e. avoid recursive calls in update , and do those updates only when required
* *Problem*. If a node’s range lies within the update operation range
    
    $\to$ All descendants of the node must also be updated
* *Idea*. 
    * Update only required node
    * Postpone updates to its children by storing this update information in separate nodes, i.e. lazy nodes or values
* *Implementation idea*. Create an array `lazy[]` which represents lazy node
    * Size of `lazy[]` is same as the segment tree `tree[]`
    * All elements of `lazy[]` are initialized as `0`
* *Lazy array value*. 
    * `lazy[i] = 0` indicates that there are no pending updates on node `i` in segment tree
    * `lazy[i] != 0` means that this amount needs to be added to node `i` in segment tree, before making any query to the node
* *Update procedure*.

    ```
    // To update segment tree for change in array
    // values at array indexes from us to ue.
    updateRange(us, ue):
    1) If current segment tree node has any pending update
        --> Add that pending update to current node
    2) If current node's range lies completely in update query range
        1. Update current node
        2. Postpone updates to children by setting lazy value for children nodes
    3) If current node's range overlaps with update range
        --> Follow the same approach as above simple update, i.e.
        1. Recur for left and right children
        2. Update current node using results of left and right calls
    ````

* *Query procedure*. Since we have changed update to postpone its operations
    
    $\to$ There may be problems if a query is made to a node that is yet to be updated
    * *Solution*. 
        1. The query method checks if there is a pending update
        2. If there is, updates the node
        3. Once it makes sure that pending update is done
            
            $\to$ It works same as the previous `getSumUtil()`