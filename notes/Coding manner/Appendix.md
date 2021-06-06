---
title: Appendix
tags: Coding manner
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
* [Appendix](#appendix)
  * [Coding conventions](#coding-conventions)
    * [Python](#python)
  * [Best practices](#best-practices)
<!-- /TOC -->

# Appendix
## Coding conventions
**C++ convention**.
* [C++ convention](https://google.github.io/styleguide/cppguide.html)

**Python convention**
* [PEP 8 convention](https://www.python.org/dev/peps/pep-0008/)
* [Google's Python convention](https://google.github.io/styleguide/pyguide.html)

### Python
**Data types**
* [Abstract base classes](https://docs.python.org/3/library/collections.abc.html)
* [Type hints](https://github.com/python/cpython/blob/3.8/Lib/typing.py#L1438)

    ```python=
    Hashable = _alias(collections.abc.Hashable, ())  # Not generic.
    Awaitable = _alias(collections.abc.Awaitable, T_co)
    Coroutine = _alias(collections.abc.Coroutine, (T_co, T_contra, V_co))
    AsyncIterable = _alias(collections.abc.AsyncIterable, T_co)
    AsyncIterator = _alias(collections.abc.AsyncIterator, T_co)
    Iterable = _alias(collections.abc.Iterable, T_co)
    Iterator = _alias(collections.abc.Iterator, T_co)
    Reversible = _alias(collections.abc.Reversible, T_co)
    Sized = _alias(collections.abc.Sized, ())  # Not generic.
    Container = _alias(collections.abc.Container, T_co)
    Collection = _alias(collections.abc.Collection, T_co)
    Callable = _VariadicGenericAlias(collections.abc.Callable, (), special=True)
    Callable.__doc__ = \
        """Callable type; Callable[[int], str] is a function of (int) -> str.
        The subscription syntax must always be used with exactly two
        values: the argument list and the return type.  The argument list
        must be a list of types or ellipsis; the return type must be a single type.
        There is no syntax to indicate optional or keyword arguments,
        such function types are rarely used as callback types.
        """
    AbstractSet = _alias(collections.abc.Set, T_co)
    MutableSet = _alias(collections.abc.MutableSet, T)
    # NOTE: Mapping is only covariant in the value type.
    Mapping = _alias(collections.abc.Mapping, (KT, VT_co))
    MutableMapping = _alias(collections.abc.MutableMapping, (KT, VT))
    Sequence = _alias(collections.abc.Sequence, T_co)
    MutableSequence = _alias(collections.abc.MutableSequence, T)
    ByteString = _alias(collections.abc.ByteString, ())  # Not generic
    Tuple = _VariadicGenericAlias(tuple, (), inst=False, special=True)
    Tuple.__doc__ = \
        """Tuple type; Tuple[X, Y] is the cross-product type of X and Y.
        Example: Tuple[T1, T2] is a tuple of two elements corresponding
        to type variables T1 and T2.  Tuple[int, float, str] is a tuple
        of an int, a float and a string.
        To specify a variable-length tuple of homogeneous type, use Tuple[T, ...].
        """
    List = _alias(list, T, inst=False)
    Deque = _alias(collections.deque, T)
    Set = _alias(set, T, inst=False)
    FrozenSet = _alias(frozenset, T_co, inst=False)
    MappingView = _alias(collections.abc.MappingView, T_co)
    KeysView = _alias(collections.abc.KeysView, KT)
    ItemsView = _alias(collections.abc.ItemsView, (KT, VT_co))
    ValuesView = _alias(collections.abc.ValuesView, VT_co)
    ContextManager = _alias(contextlib.AbstractContextManager, T_co)
    AsyncContextManager = _alias(contextlib.AbstractAsyncContextManager, T_co)
    Dict = _alias(dict, (KT, VT), inst=False)
    DefaultDict = _alias(collections.defaultdict, (KT, VT))
    OrderedDict = _alias(collections.OrderedDict, (KT, VT))
    Counter = _alias(collections.Counter, T)
    ChainMap = _alias(collections.ChainMap, (KT, VT))
    Generator = _alias(collections.abc.Generator, (T_co, T_contra, V_co))
    AsyncGenerator = _alias(collections.abc.AsyncGenerator, (T_co, T_contra))
    Type = _alias(type, CT_co, inst=False)
    Type.__doc__ = \
        """A special construct usable to annotate class objects.
        For example, suppose we have the following classes::
          class User: ...  # Abstract base for User classes
          class BasicUser(User): ...
          class ProUser(User): ...
          class TeamUser(User): ...
        And a function that takes a class argument that's a subclass of
        User and returns an instance of the corresponding class::
          U = TypeVar('U', bound=User)
          def new_user(user_class: Type[U]) -> U:
              user = user_class()
              # (Here we could write the user object to a database)
              return user
          joe = new_user(BasicUser)
        At this point the type checker knows that joe has type BasicUser.
        """
    ```

**Flask**.
* *Flask basic*. http://exploreflask.com/en/

## Best practices
**Coding flow**.
* *Top-down approach*.
    * Step 1. Outline the code first, i.e. write the most outer code

        ```python=
        if __name__ == "__main__":
            path = "path/to/image"
            image = read_image(path)
            output = process_image(image)
            display(output)
        ```
    * Step 2. Write down functions to implement
        ```python=
        def read_image(path):
            pass

        def process_image(image):
            pass

        def display(result):
            pass
        ```
    * Step 3. Implement details
        ```python=
        def read_image(path):
            image = cv2.imread(path)
            return image
        ```
* *Try-and-finalize approach*.
    * Step 1. Implement a function without arguments
        ```python=
        def read_image():
            image = cv2.imread("path/to/image")
            return image
        ```
    * Step 2. Put changable values as arguments
        ```python=
        def read_image(path):
            image = cv2.imread(path)
            return image
        ```


**Class**
* *Bottom-up approach*. Whenever finish some job, which can construct a class, then immediately create a class in a separated file from the current code
* *Ordinary class in Python*. It is better to have

    ```python
    class SampleClass(object):
        def __init__(self):
            pass
    ```

    instead of

    ```python
    def SampleClass:
        def __init__(self):
            pass
    ```

* *Single file class*. Each class should be contained within a single file, e.g. class `Display` should be in `display.py
