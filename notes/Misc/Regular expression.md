---
title: Regular expression
tags: Misc
---

# Table of Contents
[toc]

# Regular expression
**Regular expression**. A sequence of symbols, which specifies a set of text strings following some pattern, which match the regular expression

**Basic rules**
* *Special characters*. Can be preceded by `\`, as in C, to get their raw form
* *Set of characters*. Denoted as `[ ]`. This indicates that any of the character in the set will work
    * *Example*. `M[rs]` matches `Mr` or `Ms`
* *Range of characters inside braces*. Use a dash, i.e. `-`
    * *Example*. `[A-Z]`, `[4-7]`, etc.
    * *Special ranges*.

        | Notation | Meaning |
        | --- | --- |
        | `[:lower:]` | The set of lower case letters |
        | `[:upper:]` | The set of upper case letters |
        | `[:alpha:]` | All letters of the alphabet |
        | `[:digit:]` | The numerals 0 - 9 |
        | `[:alnum:]` | The alphanumeric characters, i.e. union of `[:alpha:]` and `[:digit:]` |
        | `[:punct:]` | All the punctuation marks |
        | `[:space:]` | All the whitespace characters |
        | `\w` | Word characters, i.e. `[[:alnum:]_]` |
        | `\W` | Every character not in `\w` |

**Basic operations**.
* *Logical OR*. A vertical bar separates alternatives
    * *Example*. `str1|str2` can match `str1` or `str2`
* *Grouping*. Parentheses are used to define the scope and the precedence of the operators
    * *Example*. `gray|grey` can be rewritten as `gr(a|e)y`
* *Quantification*. A quantifier after a token or group specifies how often that a preceding element is allowed to occur

    | Quantifier | Meaning |
    | --- | --- |
    | `?` | Zero or one occurrences |
    | `*` | Zero or more occurrences |
    | `+` | One or more occurrences |
    | `{n}` | Exactly `n` occurrences |
    | `{min,}` | `min` or more occurrences |
    | `{,max}` | Up to `max` occurrences |
    | `{min,max}` | At least `min` occurrences, but no more than `max` |
* *Wildcard*. The wildcard `.` matches any character
* *Exception*. An initial `^` inside the braces indicates that "every character except those in this range"
    * *Example*. `[^aeiou]`

>**NOTE**. All quantifiers are greedy, and match as many repetitions as possible

>**NOTE**. By default, quantifiers apply to the last character before they appear

**Special characters**.
* *Special tokens*.

    | Character | Meaning |
    | --- | --- |
    | `$` | EOL |
    | `^` (outside of braces) | Begin of string |
    | `\<` | Begin of words |
    | `\>` | End of words |
    | `\b` (boundary) | Either the beginning or the ending of a word |
    
    >**NOTE**. Some special tokens, e.g. `^` and `$`, have different meanings across different regex syntax, e.g. JS and C+