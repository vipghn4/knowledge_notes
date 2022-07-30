<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Bash script](#bash-script)
  - [Introduction](#introduction)
  - [Conditionals](#conditionals)
  - [Loops `for`, `while`, and `until`](#loops-for-while-and-until)
  - [Functions](#functions)
  - [User interfaces](#user-interfaces)
  - [Miscellaneous](#miscellaneous)
- [Appendix](#appendix)
  - [References](#references)
<!-- /TOC -->

# Bash script
## Introduction
**Hello World**.

```bash
#!/bin/bash
echo Hello World
```

## Conditionals
**Conditionals**. Let us decide whether to perform an action or not, this decision is taken by evaluating an expression

**Base synax for the `if` constructions**.

```bash
if [ expression ];
then
    # code if 'expression' is true.
elif [ expression ];
then
    # some code
else
    # some code
fi
```

## Loops `for`, `while`, and `until`
**Types of loops**.
* *`for` loop*. A little bit different from other programming languages, it basically iterates over a series of words within a string
* *`while` loop*. Execute a piece of code if the control expression is `true`, and only stops when it is `false`, or a explicit break is found within the executed code
* *`until` loop*. Almost equal to the `while` loop, except that the code is executed while the control expression evaluates to `false`

## Functions

## User interfaces

## Miscellaneous
**Reading user input with `read`**.

**Arithmetic evaluation**.

**Finding bash**.

**Getting the return value of a program**.

**Capturing a command's output**.

# Appendix
## References
* https://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-6.html
* https://linuxize.com/post/bash-if-else-statement/