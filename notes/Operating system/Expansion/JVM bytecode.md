<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [JVM bytecode](#jvm-bytecode)
  - [JVM architecture](#jvm-architecture)
  - [Compiling for the JVM](#compiling-for-the-jvm)
    - [Format of examples](#format-of-examples)
    - [Use of constants, local variables, and control constructs](#use-of-constants-local-variables-and-control-constructs)
- [Appendix](#appendix)
  - [Concepts](#concepts)
  - [References](#references)
<!-- /TOC -->

# JVM bytecode
## JVM architecture
**JVM architecture**.

<div style="text-align:center">
    <img src="https://www.guru99.com/images/1/2.png">
    <figcaption>JVM architecture</figcaption>
</div>

* *Class loader*. A subsystem used for loading class files
    
    $\to$ It performs three major functions viz, e.g. loading, linking, and initialization
* *Method area*. Store class structures, e.g. metadata, the constant runtime pool, and the code for methods
* *Heap*. All the Objects, their related instance variables, and arrays are stored in the heap
    * *Sharing heap between threads*. This memory is common and shared across multiple threads
* *JVM language stacks*. Store local variables, and it is partial results
    * *Thread stack*. Each thread has its own JVM stack, created simultaneously as the thread is created
    * *Stack frame*.
        * A new frame is created whenever a method is invoked
        * The frame is deleted when method invocation process is complete
* *PC registers*. Store the address of the JVM instruction, which is currently executing
    * *Thread PC*. In Java, each thread has its separate PC register
* *Native method stacks*. Hold the instruction of native code depending on the native library
    
    $\to$ It is written in another language instead of Java
* *Execution engine*. A type of software used to test hardware, software, or complete systems
    
    >**NOTE**. The test execution engine never carries any information about the tested product

* *Native method interface*. A programming framework allowing Java code running in a JVM to call by libraries and native applications
* *Native method libraries*. A collection of the Native Libraries, e.g. C, C++, which are needed by the execution engine

**Software code compilation and execution process**.
1. *Compiler*. Convert the high language program into native machine code
2. *Linker*. Combine different program files reference in the main program together
3. *Loader*. Load the files from the secondary storage device, e.g. Hard Disk, Flash Drive, CD, etc., into RAM for execution
    * *Loading time*. The loading is automatically done when we execute the code
4. *Execution*. Actual execution of the code, which is handled by our OS and processor

**Java class bytecode example**.

```asm
// class version 52.0 (52)
// access flags 0x21
public class java/lang/Object {

  // compiled from: Object.java

  // access flags 0x1
  public <init>()V
   L0
    LINENUMBER 37 L0
    RETURN
    MAXSTACK = 0
    MAXLOCALS = 1

  // access flags 0x101
  public native hashCode()I

  // access flags 0x1
  public equals(Ljava/lang/Object;)Z
   L0
    LINENUMBER 149 L0
    ALOAD 0
    ALOAD 1
    IF_ACMPNE L1
    ICONST_1
    GOTO L2
   L1

    // ...
}
```

## Compiling for the JVM
**Oracle's JDK software**. 
* *Components*.
    * A compiler from source code written in the Java programming language to the instruction set of the JVM
    * A run-time system implementing the JVM itself
* *Needs for understanding JVM*. Useful to the prospective compiler writer, and to one trying to understand the JVM itself

**Compiler**. A translator from the instruction set of a JVM to the instruction set of a specific CPU, or from source code to JVM bytecode

### Format of examples
**JVM code**. Written in the informal "virtual machine assembly language" output by Oracle's javap utility, distributed with the JDK release

**Instruction format**.
* *Format*.

    ```asm
    <index> <opcode> [ <operand1> [ <operand2>... ]] [<comment>]
    ```

    * *`<index>`*. The index of the instruction opcode in the array containing the bytes of JVM code for this method
        * *Alternative definition*. `<index>` is a byte offset from the beginning of the method
    * *`<opcode>`*. The mnemonic for the instruction's opcode
    * *`<operandN>`*. The operands of the instruction
    * *`<comment>`*. Given in end-of-line comment syntax
* *Example*.

    ```asm
    8   bipush 100     // Push int constant 100
    10  ldc #1         // Push float constant 100.0
    9   invokevirtual #4    // Method Example.addTwo(II)I
    ```

* *Control transfer*. `<index>` may be used as the target of a control transfer instruction
    * *Example*. A `goto 8` instruction transfers control to the instruction at index `8`
    * *Actual operands of JVM control transfer instructions*. Offsets from the addresses of the opcodes of those instructions
        
        $\to$ These operands are displayed by `javap` as more easily read offsets into their methods

### Use of constants, local variables, and control constructs
**Variables types in JVM**. JVM code exhibits a set of general characteristics imposed by the JVM's design and use of types
* *Example 1*. Consider the `spin` method simply spinning around an empty for loop 100 times
    * *Java code*.

        ```java
        void spin() {
            int i;
            for (i = 0; i < 100; i++) {
                ;    // Loop body is empty
            }
        }
        ```

    * *JVM bytecode*.

        ```asm
        0   iconst_0       // Push int constant 0
        1   istore_1       // Store into local variable 1 (i=0)
        2   goto 8         // First time through don't increment
        5   iinc 1 1       // Increment local variable 1 by 1 (i++)
        8   iload_1        // Push local variable 1 (i)
        9   bipush 100     // Push int constant 100
        11  if_icmplt 5    // Compare and loop if less than (i < 100)
        14  return         // Return void when done
        ```

* *Example 2*. Consider `spin` with float variables
    * *Java code*.

        ```java
        void dspin() {
            double i;
            for (i = 0.0; i < 100.0; i++) {
                ;    // Loop body is empty
            }
        }
        ```

    * *JVM bytecode*.

        ```asm
        0   dconst_0       // Push double constant 0.0
        1   dstore_1       // Store into local variables 1 and 2
        2   goto 9         // First time through don't increment
        5   dload_1        // Push local variables 1 and 2 
        6   dconst_1       // Push double constant 1.0 
        7   dadd           // Add; there is no dinc instruction
        8   dstore_1       // Store result in local variables 1 and 2
        9   dload_1        // Push local variables 1 and 2 
        10  ldc2_w #4      // Push double constant 100.0 
        13  dcmpg          // There is no if_dcmplt instruction
        14  iflt 5         // Compare and loop if less than (i < 100.0)
        17  return         // Return void when done
        ```

**Stack**. JVM is stack-oriented
* *Stacked-oriented JVM*. Most operations
    * Take one or more operands from the operand stack of the JVM's current frame, or
    * Push results back onto the operand stack
* *Frame creation*. A new frame is created each time a method is invoked
    
    $\to$ With it is created a new operand stack and set of local variables for use by that method
    * Number of concurrent frames*. At any one point of the computation
        
        $\to$ There are many frames and equally many operand stacks per thread of control, corresponding to many nested method invocations
    
    >**NOTE**. Only the operand stack in the current frame is active

**Operand types**. The instruction set of the JVM distinguishes operand types by using distinct bytecodes for operations on its various data types
* *Example*. The method `spin` operates only on values of type `int`
    
    $\to$ The instructions in its compiled code chosen to operate on typed data `(iconst_0, istore_1, iinc, iload_1, if_icmplt)` are all specialized for type `int`

**Constants**. The two constants in `spin`, `0` and `100`, are pushed onto the operand stack using two different instructions
* *`iconst_0`*. `0` is pushed using an `iconst_0` instruction, i.e. one of the family of `iconst_<i>` instructions
    * *Motivation*. The JVM frequently takes advantage of the likelihood of certain operands, e.g. int constants -1, 0, 1, 2, 3, 4 and 5 in the case of the iconst_<i> instructions
        
        $\to$ This is accomplished by making those operands implicit in the opcode
    * *Consequence*. Since `iconst_0` knows it is going to push an int `0`, i.e.
        * It does not need to store an operand to tell it what value to push
        * It does not need to fetch or decode an operand
* *`bipush 100`*. `100` is pushed using a `bipush` instruction, which fetches the value it pushes as an immediate operand
    * *Immediate operand*. An operand that is directly encoded as part of a machine instruction
    * *Drawbacks*. 
        * The compiled code for `spin` is made one byte longer
        * A simple virtual machine would have also spent additional time fetching and decoding the explicit operand each time around the loop
    * *Consequence*. Use of implicit operands makes compiled code more compact and efficient

**Local variables**. Since most JVM instructions operate on values popped from the operand stack rather than directly on local variables

$\to$ Instructions transferring values between local variables and the operand stack are common in code compiled for the JVM

>**NOTE**. These operations also have special support in the instruction set

* *Example*. In `spin`, values are transferred to and from local variables using the `istore_1` and `iload_1` instructions
    
    $\to$ Each instruction implicitly operates on local variable `1`
    * *`istore_1` instruction*. Pop an int from the operand stack and stores it in local variable `1`
    * *`iload_1` instruction*. Push the value in local variable `1` on to the operand stack
* *Use and reuse of local variables*. Belong to the responsibility of the compiler writer
    * *Best practice*. The specialized `load` and `store` instructions should encourage the compiler writer to reuse local variables as much as is feasible
        
        $\to$ The resulting code is faster, more compact, and uses less space in the frame

**Frequenct operations on local variables**. Certain very frequent operations on local variables are catered to specially by the JVM
* *Example*. The `iinc` instruction increments the contents of a local variable by a one-byte signed value
    
    $\to$ This instruction is very handy when implementing looping constructs

**Unit-size opcode**. The JVM's opcode size of 1 byte results in its compiled code being very compact
* *Drawback*. The JVM instruction set must stay small
    
    $\to$ The JVM does not provide equal support for all data types, i.e. it is not completely orthogonal
* *Example*. 
    * The comparison of values of type int can be implemented using a single `if_icmplt` instruction
    * However, there is no single instruction in the JVM instruction set that performs a conditional branch on values of type double
        
        $\to$ `dspin` must implement its comparison of values of type double using a `dcmpg` instruction followed by an `iflt` instruction
* *Wide support for int in JVM bytecode*. The JVM provides the most direct support for data of type int
    * *Explain*. 
        * This is partly in anticipation of efficient implementations of the JVM's operand stacks and local variable arrays
        * This is motivated by the frequency of int data in typical programs
    * *Consequence*. Other integral types have less direct support
        * *Example*. There are no byte, char, or short versions of the store, load, or add instructions
    * *Solution*. The lack of direct support for byte, char, and short types in the JVM is not particularly painful
        * *Example*. Values of those types are internally promoted to int, e.g. byte and short are sign-extended to int, char is zero-extended
            
            $\to$ Operations on byte, char, and short data can thus be done using int instructions
        * *Consequence*. The only additional cost is that of truncating the values of int operations to valid ranges

# Appendix
## Concepts
**Native methods in Java**. Methods starting in a language other than Java

**JVM stacks**. Each JVM thread has a private JVM stack, created at the same time as the thread
* *JVM stack*. Store frames, i.e. analogous to the stack of a conventional language like C
    * *Functionality*. 
        * Hold local variables and partial results
        * Play a part in method invocation and return
* *Heap-allocated frames*. Since the JVM stack is never manipulated directly except to push and pop frames, frames may be heap allocated. 
* *Memory layout for a JVM stack*. Need not be contiguous

**JVM frames**. Used to store data and partial results, as well as to perform dynamic linking, return values for methods, and dispatch exceptions
* *Frame creation*. A new frame is created each time a method is invoked
* *Frame deletion*. A frame is destroyed when its method invocation completes, whether that completion is normal or abrupt
* *Frame allocation*. Frames are allocated from the JVM stack of the thread creating the frame
* *Frame memory*. Each frame has 
    * Its own array of local variables
    * Its own operand stack
    * A reference to the run-time constant pool of the class of the current method

## References
* https://docs.oracle.com/javase/specs/jvms/se11/html/jvms-6.html#jvms-6.5.bipush
* https://docs.oracle.com/javase/specs/jvms/se7/html/jvms-3.html