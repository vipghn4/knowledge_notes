<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Etherum transaction](#etherum-transaction)
  - [EVM bytecode](#evm-bytecode)
  - [Contract creation and interaction](#contract-creation-and-interaction)
    - [Contract creation](#contract-creation)
    - [Contract interaction](#contract-interaction)
  - [Data payloads of transactions](#data-payloads-of-transactions)
  - [Transaction execution](#transaction-execution)
- [Appendix](#appendix)
  - [Concepts](#concepts)
  - [Discussions](#discussions)
  - [References](#references)
<!-- /TOC -->

# Etherum transaction
**Ethereum VM (EVM)**. A stack-based, big-endian VM with a word size of 256-bits and is used to run the smart contracts on the Ethereum blockchain
* *Smart contracts*. Accounts running EVM bytecode when receiving a transaction
    
    $\to$ This allows them to perform calculations and further transactions
* *Transactions zero payload*. Transaction can carry a payload of 0 or more bytes of data used to specify the type of interaction with a contract and any additional information

**Contract execution**. Start at the beginning of the bytecode
* *Opcode encoding*. Each opcode is encoded as one byte, except for the `PUSH` opcodes, which take a immediate value
* *Opcode operation*. All opcodes pop their operands from the top of the stack and push their result

## EVM bytecode

<div style="text-align:center">
    <img src="https://miro.medium.com/max/1400/1*y3MlDKVKoQcEv03UrCPEHA.png">
    <figcaption>Etherum compilation and execution flow</figcaption>
</div>

**EVM bytecode**. As Ethereum uses EVM(Ethereum Virtual Machine) as a core component of the network

$\to$ Smart contract code written in high-level languages needs to be compiled into EVM bytecode to be run
* *EMV Bytecode*. An executable code on EVM
* *Contract ABI*. An interface to interact with EVM bytecode
    * *ABI in computer science*. An interface between two program modules, e.g. between the OS and user programs
    * *Example*. If we want to call a function in a smart contract with our JavaScript code
        
        $\to$ ABI is an intermediary between our JavaScript code and EVM bytecode to interact with each other

## Contract creation and interaction
### Contract creation
**Contract creation**. 
* *Receiver of contract creation transaction*. Zero address, i.e. the address intended only for contract creation and burning tokens
* *Data payload of a transaction creating a smart contract*. 
    * *Structure*. Bytecode that 
        1. Run the contract constructor
        2. Set up the initial contract state
        3. Return the final contract bytecode, i.e. constructors are not present in the contract once deployed
    * *Data payload structure*. Consist of two sections
        
        ```json
        {
            "to": null,
            "value": 0,
            "data": "<init_code><runtime_code>"
        }
        ```

        * *Runtime code*. The code that the EVM evaluates when a contract on chain has been called
        * *Init code*. The code to construct the contract and returns the runtime code to be stored on chain
* *Query for creation code (or init code) in Solidity*.

    ```js
    type(ContractName).creationCode
    ```

* *Contract storage on blockchain*. When deploying the smart contract
    
    $\to$ The contract is compiled into byte code and this code is stored on the Blockchain
    * *Consequence*. The smart contract will be available at least in two locations, i.e. on the Blockchain and the deployed machine
    * *Reference*. https://www.quora.com/How-are-smart-contracts-stored-on-the-Ethereum-blockchain-Does-a-smart-contract-also-have-a-public-and-a-private-key

**Creation code (or init code)**. Return the runtime code to the EVM

$\to$ This is essentially the constructor function of a contract
* *Workflow*.
    1. Copy the contract's runtime code to memory
    2. Return the runtime code copied to memory
    3. The returning data is accepted as the runtime code of the contract
* *Example*.

    ```asm
    60 0D // PUSH1 13 (The length of our runtime code)
    60 0C // PUSH1 12 (The position of the runtime code in the transaction data)
    60 00 // PUSH1 00 (The destination in memory)
    39 // CODECOPY
    // ---
    60 0D // PUSH1 13 (The length of our runtime code)
    60 00 // PUSH1 00 (The memory location holding our runtime code)
    F3 // RETURN
    ```

**Runtime bytecode (or deployed bytecode)**. The code stored on-chain to describe a smart contract
* *Runtime bytecode versus creation bytecode*. Runtime bytecode does not include the constructor logic or constructor parameters of a contract
    * *Explain*. They are not relevant to the code that was used to actually create the contract
* *Query for runtime bytecode in Solidity*.

    ```js
    type(ContractName).runtimeCode
    ```

* *Example*.

    ```asm
    60 02 // PUSH1 2 - Push 2 on the stack
    60 04 // PUSH1 4 - Push 4 on the stack
    01 // ADD - Add stack[0] to stack[1]

    60 00 // PUSH1 0 - Push 0 on the stack (destination in memory)
    53 // MSTORE - Store result to memory

    60 20 // PUSH1 32 - Push 32 on the stack (length of data to return)
    60 00 // PUSH1 00 - Push 0 on the stack (location in memory)
    F3 // Return
    ```

**Complete contract creation data**.

```asm
0x600D600C600039600D6000F3600260040160005360206000F3
-------^init code^-------|------^runtime code^-----
```

**Constructor with parameters**. Pass parameters into constructor can be achieved by appending the constructor parameters after the runtime code

```json
{
  "to": null,
  "value": 0,
  "data": "<init_code><runtime_code>0000000200000004"
                                  // param1^|param2^
}
```

* *Work flow*.
    1. `init code` will `CODECOPY` the parameters into memory
    2. `SSTORE` will persist the parameters into the contract state
    3. `runtime code` will `SLOAD` the numbers stored in state onto the stack then perform the addition

**Reference**. 
* https://monokh.com/posts/ethereum-contract-creation-bytecode

### Contract interaction
**Contract interaction**. 
* *Contract ABI*. Typically contracts expose a public ABI, which is a list of supported ways a user can interact with a contract
* *Contract interaction payload*. To interact with a contract, a user will submit a transaction carrying
    * Any amount of wei
    * A data payload formatted according to the ABI, specifying the type of interaction and any additional parameters
* *Data handling at contract*. When the contract runs there are 4 main ways it handles data
    * *Call data*. The data associated with a transaction to a smart contract
        * *Format*. It usually contains a 4-byte method identifier followed by serialized arguments
        * *Relevant opcodes*. `CALLDATALOAD`, `CALLDATASIZE`, `CALLDATACOPY`, etc.
    * *Stack*. The EVM maintains a stack of `uint256`s used to hold local variables, function call arguments and return addresses
        
        >**NOTE**. Distinguishing between return addresses and other variables is tricky

        * *Relevant opcodes*. `PUSH1`, `DUP1`, `SWAP1`, `POP`, etc.
    * *Memory*. An array of uint8s used to hold transient data while a contract is being executed
        * *Relevant opcodes*. `MLOAD`, `MSTORE`, etc.
    * *Storage*. A persistent associative map, with `uint256`s as keys and `uint256`s as values

        $\to$ All contract fields and mappings are saved in storage
        * *Relevant opcodes*. `SLOAD`, `SSTORE`, etc.

## Data payloads of transactions
**Payments and invocations**.
* *Payments*. Transactions containing only data
* *Invocations*. Transactions invoking a function on smart contract

**Payload to smart contract**. A hex-serialized encoding of
* *Function selector*. The first 4 bytes if Keccak-256 hash of the function’s prototype along with the argument types
    
    $\to$ This allows the contract to unambiguously identify which function to invoke
    * *Example*. 
    
        ```js
        web3.sha3("transfer(address,uint256)");
        // result is "0xa9059cbb2ab09eb219583f4a59a5d0623ade346d962bcd4e46b11da047c9049b"
        ```
    
* *Function arguments*. The function’s arguments, encoded according to the rules for the various elementary types defined in ABI specification
    * *Example*.
        
        ```js
        0x000000000000000000000000337c67618968370907da31dAEf3020238D01c9de  // address is automatically encoded to Hex
        web3.toHex("10000000000000000000"); // encode uint256
        ```

* *Final payload*.

    ```
    a9059cbb (function selector) +
    000000000000000000000000337c67618968370907da31dAEf3020238D01c9de (first argument) +
    0000000000000000000000000000000000000000000000008ac7230489e80000 (second argument)
    ```

    or equivalently

    ```
    a9059cbb000000000000000000000000337c67618968370907da31dAEf3020238D01c9de0000000000000000000000000000000000000000000000008ac7230489e80000
    ```

## Transaction execution
**Transaction execution**. Executing a transaction and updating the network's state is essentially the same
1. The sender creates a new transaction and broadcast it to the network, until it reaches the miner
2. The miner verifies the transaction
3. The miner includes the transaction in a new block
    * *Explain*. Miners put the transaction into a candidate block, then race to solve the proof of work for that block
        
        $\to$ If they are the first miner to solve the PoW, then their block will be accepted as canonical by the rest of the network
4. The miner executes the transactions of the new block
    * *Explain*. They essentially already have, by checking the state transitions are valid and solving the PoW before anyone else
5. The miner sends the block to the rest of the network, which verifies it and executes its transactions
    * *Explain*. Once a miner solves the PoW for the block
        1. They propagate it to the network
        2. Everyone else then verifies the state transitions are valid, and the PoW for the block is indeed correct
    * *Consequence*. In verifying that the transactions equate to valid state transitions
    
        $\to$ They have, in effect, executed the transactions

**Miners as full nodes**. In order to execute a transaction, the miner needs the blockchain state, including contract's code, and the invocation, i.e. transaction payload

$\to$ A full node is what 99% of miners use
* *Explain*. It uses a lot less space and is easier
  
    $\to$ Full does basically all of the stuff we expect, i.e. verifying, mining, executing
* *Full node versus archive nodes*. 
    * Full nodes store the most recent state and are not interested in historical state even if they do store all the transaction and block data
    * Archive nodes also store all intermediary states
        
        $\to$ The process is very similar to a full node but the state data is not discarded
* *Node sizes*.
    * *Full node (600GB)*. https://etherscan.io/chartsync/chaindefault
    * *Archive node (6TB)*. https://etherscan.io/chartsync/chainarchive

# Appendix
## Concepts
**Application binary interface (ABI)**. A list of the contract's functions and arguments in JSON1 format, i.e.
1. An account wishing to use a smart contract's function uses the ABI to hash the function definition
2. It then create the EVM bytecode required to call the function
3. This is then included in the data field of a transaction
4. The bytecode is then interpreted by the EVM with the code at the target account, i.e. the address of the contract

## Discussions
**Sending payload to externally owned accounts**. We can send data payload to a user account

$\to$ It is a valid ethereum transaction, but that data does not change any state on blockchain
* *Explain*. The data is ignored by the Ethereum protocol
* *Usage*. For wallets to communicate with each other by sending metadata, i.e. as data payload, with the Payment

## References
* https://www.ethervm.io/
* https://medium.com/swlh/understanding-data-payloads-in-ethereum-transactions-354dbe995371
* https://github.com/ethereumbook/ethereumbook/blob/develop/06transactions.asciidoc#transmitting-a-data-payload-to-an-eoa-or-contract
* https://medium.com/authereum/bytecode-and-init-code-and-runtime-code-oh-my-7bcd89065904#:~:text=The%20creation%20bytecode%20is%20equivalent,the%20creation%20bytecode%20as%20bytecode.