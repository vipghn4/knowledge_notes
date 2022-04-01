<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Etherum whitepaper](#etherum-whitepaper)
  - [A next-generation smart contract and decentralized application platform](#a-next-generation-smart-contract-and-decentralized-application-platform)
  - [Introduction to Bitcoin and existing concepts](#introduction-to-bitcoin-and-existing-concepts)
    - [History](#history)
    - [Bitcoin as a state transition system](#bitcoin-as-a-state-transition-system)
    - [Mining](#mining)
    - [Merkle trees](#merkle-trees)
    - [Alternative blockchain applications](#alternative-blockchain-applications)
    - [Scripting](#scripting)
  - [Etherum](#etherum)
    - [Etherum accounts](#etherum-accounts)
    - [Messages and transactions](#messages-and-transactions)
      - [Transactions](#transactions)
      - [Messages](#messages)
    - [Etherum state transition function](#etherum-state-transition-function)
    - [Code execution](#code-execution)
    - [Blockchain and mining](#blockchain-and-mining)
  - [Applications](#applications)
- [Appendix](#appendix)
  - [References](#references)
<!-- /TOC -->

# Etherum whitepaper
## A next-generation smart contract and decentralized application platform
**Bitcoin and its consequences**. Satoshi Nakamoto's development of Bitcoin in 2009 has often been hailed as a radical development in money and currency
* *Digital asset with no backing value*. Bitcoin is the first example of a digital asset, which simultaneously has no backing or "intrinsic value" and no centralized issuer or controller
* *Blockchain technology*. The blockchain technology is a tool of distributed consensus
    
    $\to$ Attention is rapidly starting to shift to this aspect of Bitcoin
* *Commonly cited applications of blockchain*. Using on-blockchain digital assets to represent 
    * Custom currencies and financial instruments, i.e. colored coins
    * The ownership of an underlying physical device, i.e. smart property
    * Non-fungible assets, e.g. as domain names, i.e. Namecoin
    * Digital assets directly controlled by a piece of code implementing arbitrary rules, i.e. smart contracts
    * Blockchain-based decentralized autonomous organizations, i.e. DAOs

**Etherum**. Provide a blockchain with a built-in fully fledged Turing-complete programming language

$\to$ This can be used to create "contracts" used to encode arbitrary state transition functions
* *Consequence*. Users can create any system by writing up the logic in a few lines of code

## Introduction to Bitcoin and existing concepts
### History
**Decentralized digital currency**. This concept has been around for decades
* *Anonymous e-cash protocols of the 1980s and the 1990s*. Mostly reliant on a cryptographic primitive, i.e. Chaumian blinding
    
    $\to$ This provided a currency with a high degree of privacy
    * *Drawback*. This relies on a centralized intermediary
* *Wei Dai's b-money in 1998*. The first proposal introducing the idea of creating money through solving computational puzzles and decentralized consensus
    * *Drawbacks*. The proposal was scant on details as to how decentralized consensus could actually be implemented
* *Hal Finney's concept of "reusable proofs of work"*. A system using ideas from b-money and Adam Back's computationally difficult Hashcash puzzles to create a concept for a cryptocurrency
    * *Drawback*. This relies on trusted computing as a backend
* *Bitcoin*. First implemented in practice by Satoshi Nakamoto
    * *Idea*. Combine established primitives for managing ownership through public key cryptography with a consensus algorithm
        
        $\to$ This allows for keeping track of who owns coins, i.e. proof-of-work

**Proof-of-work**. A breakthrough in the space
* *Breakthrough points*. POW simultaneously solved two problems
    * POW provided a simple and moderately effective consensus algorithm
        
        $\to$ Nodes in the network are allowed to collectively agree on a set of canonical updates to the state of the Bitcoin ledger
    * POW provided a mechanism for allowing free entry into the consensus process
        * *Benefits*.
            * This solves the political problem of deciding who gets to influence the consensus
            * This prevents sybil attacks
* *Idea*. Substitute a formal barrier to participation, e.g. requirement to be registered as a unique entity on a particular list, with an economic barrier
    * *Economic barrier in POW*. The weight of a single node in the consensus voting process is directly proportional to the computing power that the node brings

**Proof-of-stake**. An alternative approach to POW
* *Idea*. The weight of a node is proportional to its currency holdings, not computational resources

>**NOTE**. Both POW and POS approaches can be used to serve as the backbone of a cryptocurrency

### Bitcoin as a state transition system
**Bitcoin as a state transition system**. From a technical standpoint, the ledger of a cryptocurrency such as Bitcoin can be thought of as a state transition system

<div style="text-align:center">
    <img src="https://d33wubrfki0l68.cloudfront.net/6168a5d4745322fca62ea084043aaaa8a9f0115e/7ebb2/static/0aeff9bcdfb1f5fd002610b4a5cff197/c1b63/ethereum-state-transition.png">
    <figcaption>Bitcoin as state transition system</figcaption>
</div>

* *System state*. Consist of 
    * The ownership status of all existing bitcoins, and
    * A state transition function, which takes a state and a transaction and outputs a new state as the result
* *Formal*.

    ```bash
    APPLY(S, TX) -> S' or ERROR
    ```

**State transistion system in a standard banking system**.
* *State*. A balance sheet
* *State transition function*. A transaction to move $X from A to B
    * *Explain*. 
        * The transition function reduces the value in A's account by $X
        * The transaction function increases the value in B's account by $X
        * If A's account has less than $X in the first place
            
            $\to$ The state transition function returns an error. Hence
* *Formal*.

    ```bash
    APPLY({ Alice: $50, Bob: $50 },"send $20 from Alice to Bob") = {
        Alice: $30, Bob: $70
    }
    ```
    
    and

    ```bash
    APPLY({ Alice: $50, Bob: $50 },"send $70 from Alice to Bob") = ERROR
    ```

**State transition system in Bitcoin**.
* *State*. The collection of all coins, i.e. UTXO, minted and not spent
    * *UTXO structure*. Each UTXO having a denomination and an owner 
* *State transition function*. A transaction contains one or more inputs and one or more outputs
    * Each input containing 
        * A reference to an existing UTXO
        * A cryptographic signature produced by the private key associated with the owner's address
    * Each output containing a new UTXO to be added to the state

**State transition function in Bitcoin**. The state transition function `APPLY(S,TX) -> S'` can be defined roughly as follows
1. For each input in `TX`
    * If the referenced UTXO is not in `S`, return an error.
    * If the provided signature does not match the owner of the `UTXO`, return an error
2. If the sum of the denominations of all input `UTXO` is less than the sum of the denominations of all output UTXO, return an error
3. Return `S` with all input UTXO removed and all output `UTXO` added

### Mining

<div style="text-align:center">
    <img src="https://d33wubrfki0l68.cloudfront.net/9520a1abaae162e4b4fa0672afcc1fe3bfb3f5ee/6169e/static/6f7d50fd4fab9f8abb94b5e610ade7e4/c1b63/ethereum-blocks.png">
    <figcaption>Bitcoin blocks</figcaption>
</div>

**Consensus mechanism for a decentralized currency system**. We need to combine the state transaction system with a consensus system

$\to$ This is to ensure that everyone agrees on the order of transactions
* *Bitcoin's decentralized consensus process*. 
    * *Idea*. Require nodes in the network to continuously attempt to produce packages of transactions, i.e. "blocks"
    * *Expected block production rate*. The network is intended to produce roughly one block every ten minutes
* *Bitcoin's block structure*. Each block contains
    * A timestamp
    * A nonce
    * A reference to, i.e. hash of, the previous block
    * A list of all of the transactions taking place since the previous block
* *Bitcoin's block chain*. Over time, Bitcoin creates a persistent, ever-growing, "blockchain"
    
    $\to$ This chain constantly updates to represent the latest state of the Bitcoin ledger

**Block validation mechanism**.
* *Idea*. Each transaction in the block must provide a valid state transition from the canonical state before the transaction was executed to some new state
* *Procedure*.
    1. Check if the previous block referenced by the block exists and is valid
    2. Check that the timestamp of the block is greater than that of the previous block and less than 2 hours into the future
    3. Check that the proof-of-work on the block is valid
    4. Let `S[0]` be the state at the end of the previous block
    5. Suppose `TX` is the block's transaction list with `n` transactions
        
        $\to$ For all `i` in `0...n-1`, set 
        
        ```
        S[i+1] = APPLY(S[i],TX[i])
        ```
        
        If any application returns an error, exit and return false
    6. Return true, and register `S[n]` as the state at the end of this block
* *State encoding in block*. System state is not encoded in the block in any way
    * *Explain*. The state is purely an abstraction to be remembered by the validating node
        
        $\to$ It can only be securely computed for any block by starting from the genesis state and sequentially applying every transaction in every block
* *Block validation order*. The order in which the miner includes transactions into the block matters
    * *Explain*. If there are two transactions A and B in a block such that B spends a UTXO created by A
    
        $\to$ The block will be valid if A comes before B but not otherwise

**Proof-of-work as validity condition**. The one validity condition present in the above list, which is not found in other systems
* *Precise condition*. The double-SHA256 hash of every block, treated as a 256-bit number, must be less than a dynamically adjusted target
    
    $\to$ This is accomplished in Bitcoin by finding the hash with a certain number of leading zeros
* *Purpose of POW*. Make block creation computationally "hard"

    $\to$ Sybil attackers are prevented from remaking the entire blockchain in their favor
* *Breaking the POW*. Since SHA256 is designed to be a completely unpredictable pseudorandom function

    $\to$ The only way to create a valid block is simply trial and error
    * *Explain*. Repeatedly incrementing the nonce and seeing if the new hash matches
* *Difficulty modification for average block production rate*. The target is recalibrated by the network every 2016 blocks
    
    $\to$ On average a new block is produced by some node in the network every ten minutes

**Inceptive for miners**. To compensate miners for this computational work
* The miner of every block is entitled to include a transaction giving themselves 25 BTC out of nowhere
* If any transaction has a higher total denomination in its inputs than in its outputs

    $\to$ The difference goes to the miner as a transaction fee
    
    >**NOTE**. This is the only mechanism by which BTC are issued

### Merkle trees
**Scalability feature of Bitcoin**. The block is stored in a multi-level data structure
* *Hash of a block*. The hash of the block header only
    * *Block header*. A roughly 200-byte piece of data that contains the timestamp, nonce, previous block hash and the root hash of a Merkle tree storing all transactions in the block

### Alternative blockchain applications
**Brief**. The idea of taking the underlying blockchain idea and applying it to other concepts has a long history

**Nick Szabo's 2005 work**. In 2005, Nick Szabo came out with the concept of "secure property titles with owner authority"
* *Idea*. This is a document describing how "new advances in replicated database technology" will allow for a blockchain-based system for 
    * Storing a registry of who owns what land
    * Creating an elaborate framework including concepts such as homesteading, adverse possession and Georgian land tax
* *Development of the work*. 
    * There was unfortunately no effective replicated database system available at the time
        
        $\to$ The protocol was never implemented in practice
    * After 2009, however, once Bitcoin's decentralized consensus was developed
        
        $\to$ A number of alternative applications rapidly began to emerge

**Namecoin**. A decentralized name registration database
* *Motivation*. 
    * In decentralized protocols, e.g. Tor, Bitcoin and BitMessage
        
        $\to$ There needs to be some way of identifying accounts so that other people can interact with them
    * In all existing solutions, the only kind of identifier available is a pseudorandom hash
        
        $\to$ Ideally, one would like to be able to have an account with a name
* *Problem for naming*. If one person can create an account named "george"
    
    $\to$ Someone else can use the same process to register "george" for themselves as well and impersonate them
* *Solution*. A first-to-file paradigm, where the first registerer succeeds and the second fails
    
    $\to$ This is a problem perfectly suited for the Bitcoin consensus protocol

**Colored coins**. A protocol allowing people to create their own digital currencies
* *Idea*. One "issues" a new currency by publicly assigning a color to a specific Bitcoin `UTXO`
    
    $\to$ The protocol recursively defines the color of other `UTXO` to be the same as the input colors of the transaction
    
    >**NOTE**. Some special rules apply in the case of mixed-color inputs
    
* *Consequence*. Users can 
    * Maintain wallets containing only `UTXO` of a specific color
    * Send the `UTXO` around like regular bitcoins
    * Backtrack through the blockchain to determine the color of any `UTXO` that they receive

**Metacoins**. A protocol living on top of Bitcoin
* *Idea*. 
    * Use Bitcoin transactions to store metacoin transactions
    * Have a different state transition function `APPLY'`
* *Error prevention*. Since the metacoin protocol cannot prevent invalid metacoin transactions from appearing in the Bitcoin blockchain
    
    $\to$ A rule is added that if `APPLY'(S,TX)` returns an error, the protocol defaults to `APPLY'(S,TX) = S`
* *Pros*. This provides an easy mechanism for creating an arbitrary cryptocurrency protocol
    * Potentially with advanced features that cannot be implemented inside of Bitcoin itself
    * With a very low development cost, i.e. since the complexities of mining and networking are already handled by the Bitcoin protocol

**Approaches toward building a consensus protocol**.
* *Option 1*. Build an independent network
    
    $\to$ This approach reasonably successful in Namecoin
    * *Implementation difficulty*. This is difficult to implement, i.e.
        * Each individual implementation needs to bootstrap an independent blockchain
        * Each individual implementation needs to build and test all necessary state transition and networking code
    * *Needs for independent network*.
        * The set of applications for decentralized consensus technology will follow a power law distribution
            * *Explain*. The vast majority of applications would be too small to warrant their own blockchain
        * There exist large classes of decentralized applications, particularly decentralized autonomous organizations, that need to interact with each other
* *Option 2*. Build a protocol on top of Bitcoin
    * *Simplified payment verification (SPV)*. This approach does not inherit the simplified payment verification features of Bitcoin
        * *Explain*. 
            * SPV works for Bitcoin because it can use blockchain depth as a proxy for validity
                * *Idea*. At some point, once the ancestors of a transaction go far enough back
                    
                    $\to$ It is safe to say that they were legitimately part of the state
            * *Blockchain-based meta-protocols, on the other hand, cannot force the blockchain not to include transactions that are not valid within the context of their own protocols
                * *Consequence*. A fully secure SPV meta-protocol implementation would need to backward scan all the way to the beginning of the Bitcoin blockchain to determine whether or not certain transactions are valid
    * *Current solution*. All "light" implementations of Bitcoin-based meta-protocols rely on a trusted server to provide the data
        
        $\to$ This is suboptimal since the primary purposes of a cryptocurrency is to eliminate the need for trust

### Scripting
**Weak version of smart contracts provided by Bitcoin**. `UTXO` in Bitcoin can be owned not only by a public key, but also by a more complicated script expressed in a simple stack-based programming language

$\to$ A transaction spending that `UTXO` must provide data satisfying the script
* *Public-key ownership mechanism implementation*. Even the basic public key ownership mechanism is implemented via a script, i.e.
    1. The script takes an elliptic curve signature as input
    2. The script verifies it against the transaction and the address owning the `UTXO`
    3. The script returns 1 if the verification is successful and 0 otherwise
* *Other scripts in Bitcoin*. Other, more complicated, scripts exist for various additional use cases

**Limitation of scripting language in Bitcoin**.
* *Lack of Turing-completeness*. While there is a large subset of computation that the Bitcoin scripting language supports
    
    $\to$ It does not nearly support everything
    * *Lack of loops*. The main category that is missing is loops
        
        $\to$ This is done to avoid infinite loops during transaction verification
        * *Drawbacks of having no loop*. Theoretically it is a surmountable obstacle for script programmers
            * *Explain*. Any loop can be simulated by simply repeating the underlying code many times with an if statement
                
                $\to$ However, it does lead to scripts that are very space-inefficient
* *Value-blindness*. There is no way for a `UTXO` script to provide fine-grained control over the amount, which can be withdrawn
    * *Example*. Consider A and B putting in $1000 worth of BTC and after 30 days the script sends $1000 worth of BTC to A and the rest to B
        
        $\to$ An oracle must be used to determine the value of 1 BTC in USD
        * *Solution*. Since `UTXO` are all-or-nothing, the only way to achieve this is through the very inefficient hack, i.e.
            * Have many UTXO of varying denominations
            * The oracle picks which UTXO to send to A and which to B
    * *Reference*. https://www.quora.com/What-is-meant-by-value-blindness-and-blockchain-blindness-in-the-bitcoin-blockchain
* *Lack of state*. `UTXO` can either be spent or unspent
    
    $to$ There is no opportunity for multi-stage contracts or scripts keeping any other internal state beyond that
    * *Consequence*. 
        * It is hard to make multi-stage options contracts, decentralized exchange offers or two-stage cryptographic commitment protocols
        * `UTXO` can only be used to build simple, one-off contracts and not more complex "stateful" contracts, e.g. decentralized organizations
            
            $\to$ This makes meta-protocols difficult to implement
    
    >**NOTE**. Binary state combined with value-blindness mean that  withdrawal limits is impossible

* *Blockchain-blindness*. `UTXO` are blind to blockchain data, e.g. the nonce, the timestamp and previous block hash
    
    $\to$ This severely limits applications in gambling, and several other categories
    * *Explain*. The scripting language is deprived of a potentially valuable source of randomness

**Approaches to building advanced applications on top of cryptocurrency**.
* Build a new blockchain
    * *Pros*. Allow for unlimited freedom in building a feature set
    * *Cons*. The cost of development time, bootstrapping effort and security
* Use scripting on top of Bitcoin
    * *Pros*. Easy to implement and standardize
    * *Cons*. Very limited in capabilities
* Build a meta-protocol on top of Bitcoin
    * *Pros*. While easy
    * *Cons*. Faults in scalability

**Etherum**. With Ethereum intend to be an alternative framework to 
* Provide larger gains in ease of development and stronger light client properties
* Allow applications to share an economic environment and blockchain security

## Etherum
**Ethereum intention**. 
* Create an alternative protocol for building decentralized applications
* Provide a different set of tradeoffs which can be very useful for a large class of decentralized applications
    * *Emphasized situations*. Situations where the following points are important
        * Rapid development time
        * Security for small and rarely used applications
        * The ability of different applications to very efficiently interact

**Idea**. Build an ultimate abstract foundational layer, i.e. a blockchain with a built-in Turing-complete programming language

$\to$ This allows anyone to write smart contracts and decentralized applications where they can create their own arbitrary rules for ownership, transaction formats and state transition functions
* *Smart contracts*. Cryptographic "boxes" containing value and only unlocking it if certain conditions are met
    
    $\to$ Such contracts can also be built on top of the platform
    * *Benefits*. Smart contracts have vastly more power than that offered by Bitcoin scripting
        * *Explain*. Smart contracts have the added powers of Turing-completeness, value-awareness, blockchain-awareness and state

### Etherum accounts
**Etherum accounts**. The state is made up of accounts, with each account having a 20-byte address

$\to$ State transitions are direct transfers of value and information between accounts
* *Account structure*.
    * The nonce, i.e. a counter used to make sure each transaction can only be processed once
    * The account's current ether balance
    * The account's contract code, if present
    * The account's storage (empty by default)
* *Types of accounts*. 
    * *Externally owned accounts*. Controlled by private keys

        $\to$ An externally owned account has no code
    * *Contract accounts*. Controlled by contract code
    * *Interactions between external accounts and contract accounts*.
        * *External account side*. One can send messages from an externally owned account by creating and signing a transaction
        * *Contract account side*. Every time the contract account receives a message, its code activates
            
            $\to$ The contract account can now read and write to internal storage, and send other messages, or create contracts in turn

**Ether**. The main internal crypto-fuel of Ethereum, and is used to pay transaction fees

**More about contracts**. Contracts in Ethereum should not be seen as something, which should be "fulfilled" or "complied with"
* *Explain*. 
    * Contracts are more like "autonomous agents" living inside of the Ethereum execution environment
    * Contracts is always executing a specific piece of code when "poked" by a message or transaction
    * Contracts is always having direct control over their own ether balance and their own key/value store to keep track of persistent variables

### Messages and transactions
#### Transactions
**Transaction in Ethereum**. The signed data package storing a message to be sent from an externally owned account
* *Transactions structure*.
    * The recipient of the message
    * A signature identifying the sender
    * The amount of ether to transfer from the sender to the recipient
    * An optional data field
    * A `STARTGAS` value, i.e. the maximum number of computational steps the transaction execution is allowed to take
    * A `GASPRICE` value, i.e. the fee the sender pays per computational step

**Basic transaction fields**.
* *First three fields*. Standard fields expected in any cryptocurrency
* *Data field*. Have no function by default, however the virtual machine has an opcode
    
    $\to$ The opcode can be used by a contract to access the data
    * *Example*. If a contract is functioning as an on-blockchain domain registration service
        1. It may wish to interpret the data being passed to it as containing two "fields", i.e.
              * A domain to register
              * The IP address to register it to
        2. The contract would read the values from the message data and appropriately place them in storage

**Transaction gas cost**.
* *`STARTGAS` and `GASPRICE` fields*. Crucial for Ethereum's anti-denial of service model
* *Idea*. To prevent accidental or hostile infinite loops or other computational wastage in code
    
    $\to$ Each transaction is required to set a limit to how many computational steps of code execution it can use
* *Gas*. The fundamental unit of computation
    * *Usual gas cost*. 
        * Usually, a computational step costs 1 gas
        * Some operations cost higher amounts of gas
            * *Explain*. 
                * Higher-cost operations are more computationally expensive, or 
                * Higher-cost operations increase the amount of data that must be stored as part of the state
        * There is a fee of 5 gas for every byte in the transaction data
    * *Purposes*. Require an attacker to pay proportionately for every resource that they consume, including computation, bandwidth and storage
        * *Consequence*. Any transaction leading to the network consuming a greater amount of any of these resources must have a gas fee roughly proportional to the increment

#### Messages
**Messages**. Contracts have the ability to send "messages" to other contracts
* *Messages*. Virtual objects, which are never serialized and exist only in the Ethereum execution environment
* *Message structure*.
    * The sender of the message (implicit)
    * The recipient of the message
    * The amount of ether to transfer alongside the message
    * An optional data field
    * A `STARTGAS` value
* *Interpretation*. A message is essentially like a transaction, except it is produced by a contract and not an external actor
    * *Message production*. A message is produced when a contract currently executing code executes the `CALL` opcode
        
        $\to$ The opcode will produce and execute a message
    * *Similarity to transaction*. A message leads to the recipient account running its code
        
        $\to$ Contracts can have relationships with other contracts in exactly the same way that external actors can

**Gas allowance**. The gas allowance assigned by a transaction or contract applies to the total gas consumed by that transaction and all sub-executions
* *Example*. 
    * *Scenario*. 
        * An external actor A sends a transaction to B with 1000 gas
        * B consumes 600 gas before sending a message to C
        * The internal execution of C consumes 300 gas before returning
    * *Consequence*. B can spend another 100 gas before running out of gas

### Etherum state transition function
**Ethereum state transition function**. The state transition function `APPLY(S,TX) -> S'`
* *Data flow*.
    1. Check if the following condition holds, if not, return an error
        * The transaction is well-formed, i.e. has the right number of values)
        * The signature is valid
        * The nonce matches the nonce in the sender's account
    2. Calculate the transaction fee as `STARTGAS` * `GASPRICE`
    3. Determine the sending address from the signature
    4. Subtract the fee from the sender's account balance and increment the sender's nonce
    5. If there is not enough balance to spend, return an error
    6. Initialize `GAS = STARTGAS`, and take off a certain quantity of gas per byte to pay for the bytes in the transaction
    7. Transfer the transaction value from the sender's account to the receiving account
    8. If the receiving account does not yet exist, create it
    9. If the receiving account is a contract, run the contract's code either to completion or until the execution runs out of gas
    10. If the value transfer failed because the sender did not have enough money, or the code execution ran out of gas
        1. Revert all state changes except the payment of the fees
        2. Add the fees to the miner's account
    11. Otherwise, refund the fees for all remaining gas to the sender, and send the fees paid for gas consumed to the miner

**Reversion of messages**. Messages work equivalently to transactions in terms of reverts
* *Idea*. If a message execution runs out of gas
    
    $\to$ The message's execution, and all other executions triggered by that execution, revert, but parent executions do not need to revert. 
* *Consequence*. It is "safe" for a contract to call another contract
    * *Explain*. If A calls B with G gas 
        
        $\to$ A's execution is guaranteed to lose at most G gas

**Contract creation**. There is an opcode `CREATE` to create a contract
* *Execution mechanics*. Generally similar to `CALL`, with the exception that the output of the execution determines the code of a newly created contract

### Code execution
**Ethereum virtual machine code (EVM code)**. The code in Ethereum contracts is written in a low-level, stack-based bytecode language, i.e. EVM code
* *Code structure*. A series of bytes, where each byte represents an operation
* *Code execution*. An infinite loop that consists of repeatedly 
    1. Carry out the operation at the current program counter, which begins at zero
    2. Increment the program counter by one
    3. Stop when the end of the code is reached, or an error, or `STOP`, or `RETURN` instruction is detected

**Data accessible to EVM code**.
* *Data storage spaces*. The operations have access to three types of space in which to store data
    * *Stack*. A last-in-first-out container, to which values can be pushed and popped
    * *Memory*. An infinitely expandable byte array
    * *Contract's long-term storage*. A key/value store
        * *Difference from stack and memory*.
            * Stack and memory reset after computation ends
            * Storage persists for the long term
* *Other data accessible to the code*. 
    * The value, sender and data of the incoming message
    * Block header data
* *Data returned by the code*. A byte array of data as an output

**Formal execution model of EVM code**.
* *Computational state*. While the EVM is running
    
    $\to$ Its full computational state can be defined by the tuple `(block_state, transaction, message, code, memory, stack, pc, gas)`
    * *`block_state`*. The global state containing all accounts, including balances and storage
* *Instruction definition*. Each instruction has its own definition in terms of how it affects the tuple
    * *Examples*.
        * `ADD` pops two items off the stack and pushes their sum, reduces `gas` by 1 and increments `pc` by 1
        * `SSTORE` pushes the top two items off the stack and inserts the second item into the contract's storage at the index specified by the first item 
* *Current instruction determination*. At the start of every round of execution
    
    $\to$ The current instruction is found by taking the `pc`-th byte of code, or `0` if `pc >= len(code)`
* *Basic implementation of Etherum*. Although there are many ways to optimize Ethereum virtual machine execution via just-in-time compilation
    
    $\to$ A basic implementation of Ethereum can be done in a few hundred lines of code

### Blockchain and mining
**Main difference between Ethereum and Bitcoin in blockchain architecture**. Unlike Bitcoin, Ethereum blocks contain 
* A copy of both the transaction list
* The most recent state
* The block number
* The difficulty

**Basic block validation algorithm**.
1. Check if the previous block referenced exists and is valid
2. Check that the timestamp of the block is 
    * Greater than that of the referenced previous block, and
    * Less than 15 minutes into the future
3. Check that the block number, difficulty, transaction root, uncle root and gas limit are valid
4. Check that the proof-of-work on the block is valid
5. Let `S[0]` be the state at the end of the previous block
6. Let `TX` be the block's transaction list, with `n` transactions
7. For all `i` in `0...n-1`, set `S[i+1] = APPLY(S[i],TX[i])`
8. If any applications returns an error, or if the total gas consumed in the block up until this point exceeds the `GASLIMIT`, return an error
9. Let `S_FINAL` be `S[n]`, but adding the block reward paid to the miner
10. Check if the Merkle tree root of the state `S_FINAL` is equal to the final state root provided in the block header
    
    $\to$ If it is, the block is valid, otherwise, it is not valid

**Block validation efficiency**. The procedure needs to store the entire state with each block

$\to$ The approach may seem highly inefficient at first glance
* *Real efficiency compared to Bitcoin*. Etherum efficiency should be comparable to that of Bitcoin
    * *Explain*. 
        * The state is stored in the tree structure
            
            $\to$ After every block only a small part of the tree needs to be changed
        * Hence, in general, between two adjacent blocks, the vast majority of the tree should be the same
            
            $\to$ The data can be stored once and referenced twice using pointers, i.e. hashes of subtrees
* *Patricia tree*. A special kind of tree used to accomplish the efficiency of validation
    * *Idea*. Include a modification to the Merkle tree concept
        
        $\to$ This allows for nodes to be inserted and deleted, and not just changed, efficiently
* *Other optimization*. Since all of the state information is part of the last block
    
    $\to$ There is no need to store the entire blockchain history

**Contract code execution location**. Where contract code is executed, in terms of physical hardware?
* *Answer*. The process of executing contract code is part of the definition of the state transition function, which is part of the block validation algorithm
    * *Consequence*. If a transaction is added into block B
        
        $\to$ The code execution spawned by that transaction will be executed by all nodes, now and in the future, that download and validate block B

## Applications
**Common types of applications on top of Etherum**.
* *Financial applications*. Provide users with more powerful ways of managing and entering into contracts using their money
    * *Examples*. Sub-currencies, financial derivatives, hedging contracts, savings wallets, wills, and ultimately even some classes of full-scale employment contracts
* *Semi-financial applications*. Applications, where money is involved but there is also a heavy non-monetary side to what is being done
    * *Examples*. Self-enforcing bounties for solutions to computational problems
* *Online voting and decentralized governance*.

# Appendix
## References
* https://ethereum.org/en/whitepaper/