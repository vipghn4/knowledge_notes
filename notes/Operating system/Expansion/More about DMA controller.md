**DMA controller cycle stealind and burst modes**. There are two transfer modes, depending on the data arriving speed relative to the bus bandwidth, and whether a particular application will allow the CPU to be locked off the bus for the duration of one transfer
* *Cycle stealing mode*. DMA controllers can operate in a cycle stealin mode, in which they atke over the bus for each byte of data to be transferred, then return control to the CPU
* *Burst mode*. DMA can operate in burst mode, in which a block of data is transferred, before returning bus control to the CPU

**One- and two-step DMA transfers**. 
* *Two-step DMA transfers*. DMA controllers can transfer data in a two-step process
    1. The DMA controller reads a value from one port, or address in one bus cycle
    2. The DMA controller writes the value to another port, or address in a second bus cycle
* *One-step DMA transfers*. The DMA controller can carry out read and write operations simultaneously

    $\to$ The data is transferred directly between the I/O device and memory in the same bus cycle

**Detailed sequence of steps for a DMA transfer**. 

<div style="text-align:center">
    <img src="https://i.imgur.com/oIvvCeF.png">
    <figcaption>DMA (8237) and CPU (386SX) in computer architecture</figcaption>
</div>

1. Each time the peripheral is ready to transfer a byte, it asserts its DMA-request line to the DMA controller
2. The DMA controller asserts the CPU's hold request (HOLD) pin
3. When the CPU control circuitry is able to suspend its execution, i.e. at the end of an instruction or by inserting wait states in a register

    $\to$ It asserts the hold-acknowledge (HOLDA) signal to the DMA controller, and floats, i.e. releases, the address, data, and control bus signals
4. The DMA then puts the memory address on the addres bus, asserts either `MEMR*` plus `IOW*`, or `MEMW*` plus `IOR*`, on the control bus
5. The DMA then asserts the appropriate DMA-acknowledge line to the peripheral
6. The peripheral responds to the DMA-acknowledge signal by reading or writing its data to the data bus
7. At the same time, the memory responds to the `MEMR*/MEMW*` control signal, causing the data to be read / written directly from / to memory
8. At the end of the bus cycle, the DMA controller then negates hold request line, and the CPU can continue to execute until the next DMA request