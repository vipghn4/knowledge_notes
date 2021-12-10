
# Memory management C++
**Heap and stack memory segments**.
* *Stack*. Traditionally adjoined the heap area and grew in the opposite direction
    
    $\to$ When the stack pointer met the heap pointer, free memory was exhausted
    * *Area structure*.
        * *Memory area content*. The stack area contains the program stack, a LIFO structure, typically located in the higher parts of memory
        * *Memory area growth*. On the standard PC x86 computer architecture, it grows toward address zero; on some other architectures, it grows in the opposite direction
        * *Stack pointer register*. Track the top of the stack, i.e. it is adjusted each time a value is “pushed” onto the stack
        * *Stack frame*. The set of values pushed for one function call is termed a “stack frame”, which consists at minimum of a return address
    * *Memory content*. Automatic variables are stored, along with information that is saved each time a function is called
        * *Memory allocation*. Each time a function is called, the address of where to return to and certain information about the caller’s environment, such as some of the machine registers, are saved on the stack
            
            $\to$ The newly called function then allocates room on the stack for its automatic and temporary variables
* *Heap*. The segment where dynamic memory allocation usually takes place
    * *Memory area growth*. The heap area begins at the end of the BSS segment and grows to larger addresses from there
    * *Memory allocation*. The heap area is managed by `malloc`, `realloc`, and `free`, which may use the `brk` and `sbrk` system calls to adjust its size

        $\to$ Memory in heap must be specifically allocated and deallocated
        
        >**NOTE**. The use of brk/sbrk and a single “heap area” is not required to fulfill the contract of `malloc`/`realloc`/`free`
        >$\to$ They may also be implemented using `mmap` to reserve potentially non-contiguous regions of virtual memory into the process’ virtual address space
    
    * *Sharing of heap memory*. The heap area is shared by all shared libraries and dynamically loaded modules in a process

**Memory allocation and deallocation methods**.
* *`malloc()` and `free()`*. `malloc` and `free` do not call the constructor and deconstructor, respectively

    $\to$ Classes won't get initalized or deinitialized automatically, which could be bad, e.g. uninitalized pointers
* *`new` and `delete`*. `new` and `delete` call the constructor and deconstructor
    
    $\to$ Class instances are initalized and deinitialized automatically
    
    >**NOTE**. However, normally there's a performance hit, compared to plain allocation, but that's for the better

**`malloc` and `free`**.
* *`free()`*. Free the memory, i.e. by zeroing, held by a pointer, without changing the value of the pointer itself