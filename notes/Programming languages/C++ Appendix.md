---
title: C++ Appendix
tags: Programming languages
---

## Introduction
**Development philosophy**. https://en.wikipedia.org/wiki/C%2B%2B#Philosophy
* It must be driven by actual problems and its features should be immediately useful in real world programs.
* Every feature should be implementable (with a reasonably obvious way to do so).
* Programmers should be free to pick their own programming style, and that style should be fully supported by C++.
* Allowing a useful feature is more important than preventing every possible misuse of C++.
* It should provide facilities for organising programs into separate, well-defined parts, and provide facilities for combining separately developed parts.
* No implicit violations of the type system (but allow explicit violations; that is, those explicitly requested by the programmer).
* User-created types need to have the same support and performance as built-in types.
* Unused features should not negatively impact created executables (e.g. in lower performance).
* There should be no language beneath C++ (except assembly language).
* C++ should work alongside other existing programming languages, rather than fostering its own separate and incompatible programming environment.
* If the programmer's intent is unknown, allow the programmer to specify it by providing manual control.

**Philosophy**. https://www.modernescpp.com/index.php/c-core-guidelines-the-philosophy
* *P.1*: Express ideas directly in code
* *P.2*: Write in ISO Standard C++
* *P.3*: Express intent
* *P.4*: Ideally, a program should be statically type safe
* *P.5*: Prefer compile-time checking to run-time checking
* *P.6*: What cannot be checked at compile time should be checkable at run time
* *P.7*: Catch run-time errors early
* *P.8*: Don’t leak any resources
* *P.9*: Don’t waste time or space
* *P.10*: Prefer immutable data to mutable data
* *P.11*: Encapsulate messy constructs, rather than spreading through the code
* *P.12*: Use supporting tools as appropriate
* *P.13*: Use support libraries as appropriate

## Basic
**Control structures**.
* [Functions](http://www.cplusplus.com/doc/oldtutorial/functions2/)
    * Pass arguments as values and references
    * Default arguments
    * Overloaded functions
    * Inline function
    * Declaring functions prototypes

        ```cpp
        // declaring functions prototypes
        #include <iostream>
        using namespace std;

        void odd (int a);
        void even (int a);

        int main (){
            int i;
            do {
                cout << "Type a number (0 to exit): ";
                cin >> i;
                odd (i);
            } while (i!=0);
            return 0;
        }

        void odd (int a){
            if ((a%2)!=0) cout << "Number is odd.\n";
            else even (a);
        }

        void even (int a){
            if ((a%2)==0) cout << "Number is even.\n";
            else odd (a);
        }
        ```
* [Class](http://www.cplusplus.com/doc/oldtutorial/classes/)
    * Constructor and destructor
    * Overloaded constructors and default constructor
    * Pointers to classes
    * Overloading operators
    * `this`, `static`, `friend`
    * Inheritance and multiple inheritance
    * `virtual`
    * Abstract class
* Misc
    * Union, struct, enum

**Advanced**.
* [Parameter pack](https://en.cppreference.com/w/cpp/language/parameter_pack)
* [Template](http://www.cplusplus.com/doc/oldtutorial/templates/)
* [Namespace and using keyword](http://www.cplusplus.com/doc/oldtutorial/namespaces/)
* [Exceptions](http://www.cplusplus.com/doc/oldtutorial/exceptions/)
* [Type casting](http://www.cplusplus.com/doc/oldtutorial/typecasting/)
* [Preprocessor directives and predefined macro names](http://www.cplusplus.com/doc/oldtutorial/preprocessor/)
    * `#define identifier replacement`
    * `#define func(param_list) func_content`
    * `#undef identifier`
    * `#ifdef condition ... #elif condition ... #else ... #endif`
    * `#line number "filename"`
    * `#error`
    * `#include "file"` or `#include <file>`
* [New features in C++](https://www.learncpp.com/cpp-tutorial/b-1-introduction-to-c11/)
* [How C linker links library](https://docs.oracle.com/cd/E19683-01/816-1386/chapter2-41106/index.html)

## Appendix
**Tricks**.
* Use `g++` to quick unit test C++ code, e.g. 

    ```
    g++ SignClassificationCalibrator.cpp -I . -o SignClassificationCalibrator.fuckyou -lnvinfer -I/usr/local/cuda-10.2/targets/aarch64-linux/include `pkg-config --cflags --libs opencv4` -L/usr/local/cuda-10.2/targets/aarch64-linux/lib -lcudart -lstdc++fs && ./SignClassificationCalibrator.fuckyou ~/giangh/AutoPilot/tmp/calib_sample_data/
    ```

**Misc**.
* [`const` the the end of function declaration](https://stackoverflow.com/questions/751681/meaning-of-const-last-in-a-function-declaration-of-a-class)
* [Range-based for loop](https://en.cppreference.com/w/cpp/language/range-for)
* [`seekp` and `seekg` in C++](https://stackoverflow.com/questions/14329261/are-seekp-seekg-interchangeable)

**References**
* http://www.cplusplus.com/doc/oldtutorial/polymorphism/
* https://thecandcppclub.com/
* https://thispointer.com/c11-tutorial/
* http://www.doc.ic.ac.uk/lab/cplus/c++.rules/chap5.htm