---
title: Python
tags: Programming languages
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
* [Python](#python)
  * [Discussion](#discussion)
    * [`__name__` in Python](#name-in-python)
    * [`Namespace`](#namespace)
<!-- /TOC -->

# Python
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
