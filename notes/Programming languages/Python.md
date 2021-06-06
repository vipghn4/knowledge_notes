---
title: Python
tags: Programming languages
---

# Python
## Table of Contents
[toc]

## Discussion
### `__name__` in Python
**`__name__`**. A built-in variable which evaluates to the name of the current module
* *Explain*. Assume two files
    
    ```python=
    # ~/file1.py
    print(f"file 1 name: {__name__}")
    ```
    
    and 
    
    ```python=
    # ~/file2.py
    import file1
    
    print(f"file 2 name: {__name__}")
    ```
    
    then the output when running `file2.py` would be
    
    ```
    file 1 name: file1
    file 2 name: __main__
    ```

### `Namespace`
**Create namespace object**.
* *Approach 1*. Manually
    
    ```python=
    clas Namespace:
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
    ```

* *Approach 2*. Use `argparse`

    ```python=
    from argparse import Namespace
    
    args = Namespace(a=1, b="c")
    ``