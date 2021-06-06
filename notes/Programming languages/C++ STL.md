---
title: C++ STL
tags: Programming languages
---

# Table of Contents
[toc]

# C++ STL
## Introduction
**Containers library**.
* *Sequence containers*. Vector, Deque, List
* *Containers adaptors*. Stack, Queue, PriorityQueue
* *Associative containers*. Set, Multiset, Map, Multimap, Bitset

**Algorithms library**. Contain algorithms to work with data

**Iterator library**. Work as pointers, to access elements of containers

**Numeric lilbrary**. Contain numerical functions

>**NOTE**. To use STL libraries, we must use name space `std`
>```cpp
>using namespace std;
>```

## Iterators
**Iterator**. Any object pointing to an element among a collection of elements, e.g. array or container
* *Usage*. Iterate over elements of the collection, using a set of operators, e.g. comparison, increment, etc.
* *Example*. A pointer

**Operators for iterator**.
* *Comparison*. `==` or `!=`
* *Assigment*. `=`
* *Addition or subtraction*. `+` or `-`
* *Value extraction*. `*`

## Containers
**Container**. An object implemented as a template, which contains a collection of elements
* *Usage*. Manage memory space for the associated elements
* *Access container's elements*. We can either
    * Use member functions to access the elements
    * Use iterator to access the elements
* *Container structure*. A container uses special structures to store its element, e.g.

| Container | Structure |
| --- | --- |
| `vector` | Dynamic array |
| `queue` | Queue |
| `priority_queue` | Heap |
| `list` | Doubly-linked list |
| `set` | Tree |
| `map` | Associative arrays |

### Iterator
**Common iterators**. Both sequence containers and associative containers support these following iterators, with complexity $O(1)$
* `container_name.begin()`
* `container_name.end()`
* `container_name.rbegin()`
* `container_name.rend()`

>**NOTE**. `rend()` is not the same as `begin()`

### Vector
**Vector**. Work as a dynamic array

**Declaration**.
* *1D vectors*.
    ```cpp=
    #include <vector>

    // Create an empty vector
    vector<int> first;

    // Create a vector of N elements, whose values are all V
    vector<int> second(N, M);

    // Vector slice
    vector<int> third(second.begin(), second.end());

    // Copy vector
    vector<int> forth(third);
    ```
* *2D vectors*.
```cpp=
#include <vector>

// Create an empty 2D vector
vector<int, vector<int> > first;

// Create a 2D vector of shape MxN
vector<int, vector<int> > second(M, N);

// Create N empty 1D vectors
vector<int, vector<int> > third(N);
```

**Member functions**
* *Capacity*. `size()` ($\sim O(1)$) and `empty()` ($\sim O(1)$)
* *Access elements*.
    * `operator[]` ($\sim O(1)$)
    * `at()` ($\sim O(1)$)
    * `front()` ($\sim O(1)$)
    * `back()` ($\sim O(1)$)
* *Modify elements*.
    * `push_back()` ($\sim O(1)$)
    * `pop_back()` ($\sim O(1)$)
    * `insert(iterator, x)` ($\sim O(n)$)
    * `erase(iterator)` ($\sim O(1)$)
    * `swap(other_vector)` ($\sim O(1)$)
    * `clear()` ($\sim O(n)$)

### Deque
**Declaration**.
```cpp=
#include <deque>
```

**Member functions**
* *Capacity*. `size()` ($\sim O(1)$) and `empty()` ($\sim O(1)$)
* *Access elements*.
    * `operator[]` ($\sim O(1)$)
    * `at()` ($\sim O(1)$)
    * `front()` ($\sim O(1)$)
    * `back()` ($\sim O(1)$)
* *Modify elements*.
    * `push_back()` ($\sim O(1)$)
    * `push_front()` ($\sim O(1)$)
    * `pop_back()` ($\sim O(1)$)
    * `pop_front()` ($\sim O(1)$)
    * `insert(iterator, x)` ($\sim O(n)$)
    * `erase(iterator)` ($\sim O(1)$)
    * `swap(other_vector)` ($\sim O(1)$)

### List
**Declaration**.
```cpp=
#include <list>
```

**Member functions**
* *Capacity*. `size()` ($\sim O(1)$) and `empty()` ($\sim O(1)$)
* *Access elements*.
    * `front()` ($\sim O(1)$)
    * `back()` ($\sim O(1)$)
* *Modify elements*.
    * `push_back()` ($\sim O(1)$)
    * `push_front()` ($\sim O(1)$)
    * `pop_back()` ($\sim O(1)$)
    * `pop_front()` ($\sim O(1)$)
    * `insert(iterator, x)` ($\sim O(n)$)
    * `erase(iterator)` ($\sim O(1)$)
    * `swap(other_vector)` ($\sim O(1)$)
    * `clear()` ($\sim O(n)$)
* *Operations*.
    * `splice`, i.e. move an element from a list, ($\sim O(n)$)
    * `remove(const)`, i.e. remove all elements with value `const`, ($\sim O(n)$)
    * `remove_if(function)`, i.e. remove all elements which `function` returns `true`, ($\sim O(n)$)
    * `unique`, i.e. remove duplicate elements, ($\sim O(n)$)
        
        >**NOTE**. Elements in list must be sorted beforehand
    * `sort` ($\sim O(n\log n)$)
    * `reverse` ($\sim O(n)$)

### Stack
**Stack**. An adaptor container, working in LIFO manner

**Declaration**.
```cpp=
#include <stack>

stack<int> s;
```

**Member functions**
* *Capacity*. `size()` ($\sim O(1)$) and `empty()` ($\sim O(1)$)
* *Modify elements*. `push()` and `pop()`
* *Access elements*. `top()`

### Queue
**Queue**. An adaptor container, working in FIFO manner

**Declaration**.
```cpp=
#include <queue>

queue<int> q;
```

**Member functions**
* *Capacity*. `size()` ($\sim O(1)$) and `empty()` ($\sim O(1)$)
* *Modify elements*. `push()` and `pop()`
* *Access elements*. `front()` and `back()`

### Priority queue
**Priority queue**. An adaptor container, as a max heap
* *Default comparison operator*. `operator<`

**Declaration**.
```cpp=
#include <queue>

priority_queue<int> pqueue;

// Priority queue with custom comparison operator
priority_queue<dtype, container_type, comparison_operator> pqueue;
```

**Member functions**
* *Capacity*. `size()` ($\sim O(1)$) and `empty()` ($\sim O(1)$)
* *Modify elements*. `push()` and `pop()`
* *Access elements*. `top()`

### Set
**Set**. Contain unique elements, called keys
* *Traverse elements*. We traverse from `begin()` to `end()`, with elements increase according to some comparison function
* *Default comparison*. `operator<`
* *Implementation*. Binary search tree

**Declaration**.
```cpp=
#include <set>

set<int> s;
set<int, greater<int> > s;

// Custom comparison function
struct cmp{
    bool operator() (int a, int b){
        return a < b;
    }
}
set<int, cmp> s;
```

**Member functions**
* *Capacity*. `size()` ($\sim O(1)$) and `empty()` ($\sim O(1)$)
* *Modify elements*.
    * `insert(iterator, x)` ($\sim O(\log n)$)
    * `erase(iterator)` ($\sim O(\log n)$)
    * `swap(other_vector)` ($\sim O(n)$)
    * `clear()` ($\sim O(n)$)
* *Operations*.
    * `find`, i.e. return iterator to desired element, otherwise return `end()`, ($\sim O(\log n)$)
    * `lower_bound`, i.e. least but not less than, ($\sim O(\log n)$)
    * `upper_bound`, i.e. least but greater than, ($\sim O(\log n)$)
    * `count`, i.e. number of occurrences of a key in the container, ($\sim O(\log n)$)

### Multi-set
**Multiset**. The same as set but allow duplicate elements

**Member functions**
* *Capacity*. `size()` ($\sim O(1)$) and `empty()` ($\sim O(1)$)
* *Modify elements*.
    * `insert(iterator, x)` ($\sim O(\log n)$)
    * `erase(iterator)` 
        * Erase by iterator ($\sim O(\log n)$)
        * Erase by key, i.e. remove all elements with a specific key ($\sim O(\log n + n)$)
    * `swap(other_vector)` ($\sim O(n)$)
    * `clear()` ($\sim O(n)$)
* *Operations*.
    * `find`, i.e. return iterator to desired element, otherwise return `end()`, ($\sim O(\log n)$)
    * `lower_bound`, i.e. least but not less than, ($\sim O(\log n)$)
    * `upper_bound`, i.e. least but greater than, ($\sim O(\log n)$)
    * `count`, i.e. number of occurrences of a key in the container, ($\sim O(\log n)$)

### Map
**Associative container**. Each element of a map consists of a key and its mapped value, i.e. a key-value pair

>**NOTE**. Map does not allow duplicate keys

* *Comparison operator*. Elements of a map are sorted in some order, depending on the comparison operator
* *Implementation*. Red-black tree, whose nodes are `pair`

**Declaration**.
```cpp=
#include <map>

map<dtypeA, dtypeB> m;
```

**Member functions**
* *Capacity*. `size()` ($\sim O(1)$) and `empty()` ($\sim O(1)$)
* *Access elements*.
    * `operator[key]`, i.e. return value if key is in the map, otherwise add the key-value pair to the map, ($\sim O(\log n)$)
* *Modify elements*.
    * `insert()`, i.e. insert a pair, ($\sim O(\log n)$)
    * `erase()` ($\sim O(\log n)$)
        * Erase by iterator
        * Erase by key
    * `swap(other_vector)` ($\sim O(n)$)
    * `clear()` ($\sim O(n)$)
* *Operations*.
    * `find`, i.e. return iterator to desired element, otherwise return `end()`, ($\sim O(\log n)$)
    * `lower_bound`, i.e. least but not less than, ($\sim O(\log n)$)
    * `upper_bound`, i.e. least but greater than, ($\sim O(\log n)$)
    * `count`, i.e. number of occurrences of a key in the container, ($\sim O(\log n)$)

### Multi-map
**Multi-map**. THe same as map but allow duplicate elements

## STL algorithms
**Declaration**.
```cpp=
#include <algorithm>
```

>**NOTE**. When working with functions acting on a substring of elements, C++ functions usually act on open intervals, i.e. $[\dots )$

**Functions**.
* *Min, max*. `min()`, `max()`, `next_permutation`, `prev_permutation`
* *Sort*. `sort` with default operator `operator<`
* *Binary search*. `binary_search`, `lower_bound`, `upper_bound`

# Appendix
## Tricks and advices
**Best practices**.
1. Use vectors when
    * Accessing elements within $O(1)$
    * Insert or remove last element within $O(1)$
2. Use deques when
    * Accessing elements by indices within $O(1)$
    * Insert or remove first or last element within $O(1)$
3. Use list when
    * Insert or remove within $O(1)