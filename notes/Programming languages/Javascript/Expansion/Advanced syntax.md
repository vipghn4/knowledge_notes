<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Advanced syntax](#advanced-syntax)
  - [Variable declaration](#variable-declaration)
    - [`let` and `var` keywords](#let-and-var-keywords)
    - [`const` keyword](#const-keyword)
  - [JS operators](#js-operators)
<!-- /TOC -->

# Advanced syntax
## Variable declaration
### `let` and `var` keywords
**Redeclaration**. Variables defined with let cannot be redeclared, i.e. we cannot accidentally redeclare a variable

$\to$ With `var`, variable redeclaration is allowed
* *Motivation*. Redeclaring a variable using the var keyword can impose problems, i.e. eedeclaring a variable inside a block will also redeclare the variable outside the block

    $\to$ Redeclaring a variable using `let` can solve this problem
    * *Explain*. Redeclaring a variable inside a block will not redeclare the variable outside the block
* *Redeclaration in the some block*.
    * *`var`*. Redeclaring a variable is allowed anywhere in a program
    * *`let`*. Redeclaring a variable in the same block is not allowed

**Block scope**. Before ES6 (2015), JavaScript had only Global Scope and Function Scope.

$\to$ ES6 introduced two important new JavaScript keywords: `let` and `const`, which provide Block Scope in JavaScript
* *Block scope*. Variables declared inside a `{ }` block cannot be accessed from outside the block:
    * *Example*.
        
        ```js
        {
        let x = 2;
        }
        // x can NOT be used here
        ```

* *Block scope and `var`*. Variables declared with the `var` cannot have block scope
    
    $\to$ Variables declared inside a `{ }` block can be accessed from outside the block.
    * *Example*.

        ```js
        {
        var x = 2;
        }
        // x CAN be used here
        ```

**Let hoisting**. 
* *`var`*. Variables defined with `var` are hoisted to the top and can be initialized at any time
    
    $\to$ We can use the variable before it is declared
    * *Example*.

        ```js
        carName = "Volvo";
        var carName;
        ```

* *`let`*. Variables defined with `let` are also hoisted to the top of the block, but not initialized
    
    $\to$ Using a `let` variable before it is declared will result in a `ReferenceError`

### `const` keyword
**`const` variables**.
* *Characteristics*.
    * *Value reassignment*. `const` variables cannot be Reassigned
    * *Assignment at declaration*. `const` variables must be assigned a value when they are declared
* *Usage*. Always declare a variable with `const` unless you know that the value will change

    $\to$ Use `const` when we declare
    * A new Array
    * A new Object
    * A new Function
    * A new RegExp

**Constant reference**. The keyword const is a little misleading, i.e. it does not define a constant value

$\to$ It defines a constant reference to a value
* *Consequence*.
    * We cannot
        * Reassign a constant value
        * Reassign a constant array
        * Reassign a constant object
    * We can
        * Change the elements of constant array
        * Change the properties of constant object

**Block Scope**. Declaring a variable with `const` is similar to `let` when it comes to Block Scope

**Const Hoisting**. Variables defined with `const` are also hoisted to the top, but not initialized

$\to$ Using a `const` variable before it is declared will result in a `ReferenceError`

## JS operators
**Arithmetic operators**.

| Operator | Description |
| --- | --- |
| +	| Addition |
| -	| Subtraction |
| *	| Multiplication |
| ** | Exponentiation |
| /	| Division |
| %	| Modulus |
| ++ | Increment |
| -- | Decrement |

**Assignemtn operators**.

| Operator | Example | Same as |
| --- | --- | --- |
| = | x = y | x = y |
| += | x += y | x = x + y |
| -= | x -= y | x = x - y |
| *= | x *= y | x = x * y |
| /= | x /= y | x = x / y |
| %= | x %= y | x = x % y |
| **= | x **= y | x = x ** y |

**String operators**.
* *String concatenation*. `+` and `+=`, e.g.

    ```js
    let text1 = "John";
    let text2 = "Doe";
    let text3 = text1 + " " + text2; // = "John Doe"
    ```

* *String-numebr concatenation*. Adding two numbers, will return the sum, but adding a number and a string will return a string, e.g.

    ```js
    let x = 5 + 5; // = 5
    let y = "5" + 5; // = "55"
    let z = "Hello" + 5; // = "Hello5"
    ```

**Comparison operators**.

| Operator | Description |
| --- | --- |
| == | equal to |
| === | equal value and equal type |
| != | not equal |
| !== | not equal value or not equal type |
| > | greater than |
| < | less than |
| >= | greater than or equal to |
| <= | less than or equal to |
| ? | ternary operator |

**Logical operators**.

| Operator | Description |
| --- | --- |
| && | logical and |
| || | logical or |
| ! | logical not |

**Type operators**. `typeof` and `instanceof`

**Bitwise operators**. Bit operators work on 32 bits numbers
* Any numeric operand in the operation is converted into a 32 bit number
* The result is converted back to a JavaScript number

| Operator | Description | Example | Same as | Result | Decimal |
| --- | --- | --- | --- | --- | --- |
| & | AND | 5 & 1 | 0101 & 0001 | 0001 | 1 |
| | | OR | 5 | 1 | 0101 | 0001 | 0101 | 5 |
| ~ | NOT | ~ 5	 | ~0101 | 1010 | 10 |
| ^ | XOR | 5 ^ 1 | 0101 ^ 0001 | 0100 | 4 |
| << | left shift | 5 << 1 | 0101 << 1 | 1010 | 10 |
| >> | right shift | 5 >> 1 | 0101 >> 1 | 0010 | 2 |
| >>> | unsigned right shift | 5 >>> 1 | 0101 >>> 1 | 0010 | 2 |