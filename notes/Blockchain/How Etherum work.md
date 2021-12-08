<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [How Etherum work](#how-etherum-work)
  - [Blockchain](#blockchain)
    - [Introduction to blockchain](#introduction-to-blockchain)
    - [Greedy heaviest observed subtree (GHOST) protocol](#greedy-heaviest-observed-subtree-ghost-protocol)
  - [Fundamental components of Etherum](#fundamental-components-of-etherum)
    - [Accounts](#accounts)
    - [Account state](#account-state)
    - [World state](#world-state)
- [Appendix](#appendix)
  - [Concepts](#concepts)
  - [References](#references)
<!-- /TOC -->

# How Etherum work
## Blockchain
### Introduction to blockchain
**Blockchain**. A cryptographically secure transactional singleton machine with shared-state
* *Terminology*.
    * *"Cryptographically secure"*. The creation of digital currency is secured by complex mathematical algorithms, which are hard to break
    * *"Transactional singleton machine"*. There is a single canonical instance of the machine responsible for all the transactions being created in the system

        $\to$ There is a single global truth that everyone believes in
    * *"With shared-state"*. The state stored on the underlying machine is shared and open to everyone

**Etherum blockchain paradigm**. The Etherum blockchain is essentially a transaction-based state machine
* *Genesis state (blank state)*. The Etherum's state machine starts with a blank state, before any transactions have been on the network
* *Transaction-based state machine*. When transactions are executed, the genesis state transitions into some final state
    
    $\to$ At any point in time, the final state represents the current state of Etherum

    <div style="text-align:center">
        <img src="https://i.imgur.com/uTA1FvT.png">
        <figcaption>State machine of Etherum</figcaption>
    </div>

* *Transactions and blocks*. The state of Ethereum has millions of transactions, which are grouped into “blocks” 

    $\to$ A block contains a series of transactions, and each block is chained together with its previous block
* *State transition*. To cause a transition from one state to the next, a transaction must be valid
    * *Valid transaction*. For a transaction to be considered valid, it must go through a validation process, i.e. mining
    * *Mining*. When a group of nodes, i.e. computers, expend their compute resources to create a block of valid transactions


**Miner**. Any node on the network that declares itself as a miner can attempt to create and validate a block

$\to$ Lots of miners from around the world try to create and validate blocks at the same time
* *Validation of blocks*. Each miner provides a mathematical proof when submitting a block to the blockchain

    $\to$ This proof acts as a guarantee, i.e. if the proof exists, the block must be valid
* *Successful mining*. For a block to be added to the main blockchain, the miner must prove it faster than any other competitor miner
    * *Proof of work*. The process of validating each block by having a miner provide a mathematical proof
    * *Mining rewards*. A miner validating a new block is rewarded with a certain amount of value for doing the work
        * *Rewarded value*. The Etherum blockchain uses an intrinsic digital token, i.e. Ether, which is generated and awarded everytime a miner proves a block

**Main block guarantee**.
* *Problems*. Due to the definition of blockchain, we know that the correct current state is a single global truth, which everyone must accept

    $\to$ Having multiple states, or chains, would ruin the whole system, since it would be impossible to agree on which state was the correct one
    * *Example*. If the chains were to diverge, you might own 10 coins on one chain, 20 on another, and 40 on another
        
        $\to$ There would be no way to determine which chain was the most “valid”
    * *Concrete questions*.
        * What guarantees that everyone sticks to one chain of blocks
        * How can we be sure that there does not exist a subset of miners, who decide to create their own chain of blocks
* *Fork*. Whenever multiple paths are generated, a "fork" occurs

    $\to$ We want to avoid forks, since they disrupt the system and force people to choose which chain they believe in

    <div style="text-align:center">
        <img src="https://i.imgur.com/sQSCRiU.png">
        <figcaption>Forks in blockchain</figcaption>
    </div>

### Greedy heaviest observed subtree (GHOST) protocol
**GHOST protocol**. A mechanism used by Etherum to determine which path is most valid and prevent multiple chains

<div style="text-align:center">
    <img src="https://i.imgur.com/UUpjjd1.png">
    <figcaption>GHOST protocol</figcaption>
</div>

* *Idea*. We must pick the path having the most computation done upon it
* *Implementation*. Use the block number of the most recent block, i.e. the leaf block, which represents the total number of blocks in the current path, excluding the genesis block

    $\to$ The higher the block number, the longer the path and the greater the mining effort, which must have gone into arriving at the leaf

## Fundamental components of Etherum
**Fundamental components of Etherum**. Accounts, state, gas and fees, transactions, blocks, transaction execution, mining, and proof of work

### Accounts
**Accounts**. The global shared-state of Etherum is comprised of many small objects, i.e. accounts, which are able to interact with each other through a message-passing framework
* *Account structure*. Each account has a state associated with it, and a 20-byte address, which is used to identify the account
* *Types of accounts*.

    <div style="text-align:center">
        <img src="https://i.imgur.com/I1gnaMG.png">
        <figcaption>Types of accounts in Etherum</figcaption>
    </div>

    * *Externally owned accounts*. Controlled by private keys and have no code associated with them
    * *Contract accounts*. Controlled by their contract code and hav code associated with them

**Externally owned accounts and contract accounts**.

<div style="text-align:center">
    <img src="https://i.imgur.com/wWEpHRO.png">
    <figcaption>Externally owned accounts and contract accounts</figcaption>
</div>

* *Externally owned account*. Can send messages to other externally own accounts, or to other contract accounts, by creating and signing a transaction using its private key
    * *Messages between two externally owned accounts*. A value transfer
    * *Messages from an externally owned account to a contract account*. Activate the contract account's code, allowing it to perform various actions
        * *Possible actions*. Transfer tokens, write to internal storage, mint new tokens, perform some calculation, create new contracts, etc.
* *Contract account*. Cannot initiate new transactions on their own

    $\to$ Contract accounts can only fire transactions in response to other transactions they have received, from an externally owned account or from another contract account
* *Conclusion*. Any action occuring on the Etherum blockchain is always set in motion by transactions fired from externally controlled accounts

### Account state
**Account state**. Consist of four components, which are present regardless of the type of account

<div style="text-align:center">
    <img src="https://i.imgur.com/3gHP1U0.png">
    <figcaption>Account state</figcaption>
</div>

* *Nonce*. A counter that indicates the number of transactions sent from the account, to ensure transactions are only processed once
    * *Externally owned accounts*. This number represents the number of transactions sent from the account's address
    * *Contract accounts*. This number represents the number of contracts created by the account
* *Balance*. The number of Wei, i.e. a denomination of ETH, owned by the address, i.e. there are $10^{18}$ Wei per Ether
* *Storage root (or storage hash)*. A hash of the root node of a Merkle Patricia tree, which encodes the hash of the storage content of the account, and is empty by default
* *Code hash*. The hash of the EVM (Etherum virtual machine) code of the account

    $\to$ Contract accounts have code fragments programmed in, which can perform different operations
    * *Externally owned accounts*. This field is the hash of the empty string
    * *Contract accounts*. This field is the code, which gets hased and stored as `codeHash`

### World state
**Etherum global state**. Consist of a mapping between account addresses and account states, which is stored in a Merkle Patricia tree

<div style="text-align:center">
    <img src="https://i.imgur.com/61jmCHY.png">
    <figcaption>Merkle Patricia tree</figcaption>
</div>

**Merkle Patricia tree (or Merkle trie)**. A type of binary tree composed of a set of nodes
* *Tree characteristics*.
    * A large number of leaf nodes at the bottom of the tree, which contain the data
    * A set of intermediate nodes, where each node is the hash of its two child nodes
    * A single root node representing the top of the tree
* *Data at leaf nodes*. Generated by 
    1. Split the data we want to store into chunks
    2. Split the chunks into buckets
    3. Take the hash of each bucket
    4. Repeat until the total number of hashes remaining becomes only one, i.e. the root hash
* *Key-value pairs in Merkle trie*. Every value stored in the tree must have a key associated with it
    * *Key's role*. Beginning from the root node of the tree, the key should tell us which child node to follow to get to the corresponding value, which is stored in the leaf nodes

**Key-value mapping for state tree in Etherum**. The mapping is between addresses and their associated accounts, including the balance, nonce, codeHash, and storageRoot for each account, where storageRoot is itself a tree

<div style="text-align:center">
    <img src="https://i.imgur.com/tIl8M1X.png">
    <figcaption>Merkle Patricia tree in Etherum</figcaption>
</div>

**Merkle trie for storing transactions and receipts**. Every block has a header storing the hash of the root node of three different Merkle trie structures, i.e. state trie, transactions trie, and receipts trie

<div style="text-align:center">
    <img src="https://i.imgur.com/G6stg8u.png">
    <figcaption>Block header in Etherum</figcaption>
</div>

$\to$ The ability to store all this information efficiently in Merkle tries is incredibly useful in Ethereum for what we call “light clients” or “light nodes”

**Full nodes and light nodes in blockchain**. A blockchain is maintained by a bunch of nodes of two types, i.e. full nodes and light nodes
* *Full archive node*. Synchronize the blockchain by downloading the full chain, from the genesis block to the current head block, executing all of the transactions contained within
    * *Examples*. 
        * Typically, miners store the full archive node, because they are required to do so for the mining process
        * It is also possible to download a full node without executing every transaction
* *Light nodes*. Unless a node needs to execute every transaction or easily query historical data, there’s really no need to store the entire chain

    $\to$ These nodes are light nodes
    * *Light nodes*. Download only the chain of headers, from the genesis block to the current head, without executing any transactions or retrieving any associated state
    * *Consequence*. Because light nodes have access to block headers, which contain hashes of three tries
        
        $\to$ They can still easily generate and receive verifiable answers about transactions, events, balances, etc.
        * *Explain*. Hashes in the Merkle tree propagate upward, i.e. if a malicious user attempts to swap a fake transaction into the bottom of a Merkle tree
            
            $\to$ This change will cause a change in the hash of the node above, which will change the hash of the node above that, and so on, until it eventually changes the root of the tree

**Merkle proof**. Any node that wants to verify a piece of data can use a “Merkle proof” to do so
* *Merkle proof*. Consist of
    * A chunk of data to be verified and its hash
    * The root hash of the tree
    * The branch, i.e. all of the partner hashes going up along the path from the chunk to the root
* *Producing a Merkle proof*. Anyone reading the proof can verify that the hashing for that branch is consistent all the way up the tree, and therefore that the given chunk is actually at that position in the tree

# Appendix
## Concepts
**Hasing algorithm used by Etherum**. KECCAK-256

**Validating a block in blockchain**.

**EVM code in contract accounts**. EVM code, i.e. as hashed into `codeHash` field of account's state, gets executed if the account gets a message call
* *Immutability*. It cannot be changed unlike the other account fields
* *Code storage*. All code fragments are contained in the state database under their corresponding hashes for later retrieval
    
    $\to$ This hash value is known as a `codeHash`
    
    >**NOTE**. For externally owned accounts, the `codeHash` field is the hash of an empty string

**Smart contract (or contract only) in Ethereum**. A contract is a collection of code, i.e. its functions, and data, i.e. its state, residing at a specific address on the Ethereum blockchain
* *Etherum VM (EVM)*. Contracts live on the blockchain in a Ethereum-specific binary format called Ethereum Virtual Machine (EVM) bytecode
* *Contract programming language*. Contracts are typically written in some high level language such as Solidity and then compiled into bytecode to be uploaded on the blockchain
* *Contract account*. Smart contracts are a type of Ethereum account, i.e. they have a balance and they can send transactions over the network
    * *Controlling contract account*. Smart contracts are not controlled by a user, instead they are deployed to the network and run as programmed
        
        $\to$ User accounts can then interact with a smart contract by submitting transactions, which execute a function defined on the smart contract
    * *Functionality*. 
        * Smart contracts can define rules, like a regular contract, and automatically enforce them via the code
        * Smart contracts cannot be deleted by default, and interactions with them are irreversible

**Roles of externally owned accounts and contract accounts in Etherum**.
* *Externally owned accounts*. Controlled by anyone with the private keys
* *Contract accounts*. A smart contract deployed to the network, controlled by the code
* *Key similarity*. Both account types can
    * Receive, hold, and send ETH and tokens
    * Interact with deployed smart contracts
* *Key differences*.
    * *Externally owned accounts*.
        * Creating an account costs nothing
        * Can initiate transactions
        * Transactions between externally-owned accounts can only be ETH or token transfers
    * *Contract accounts*.
        * Creating a contract has a cost, since we are using network storage
        * Can only send transactions in response to receiving a transaction
        * Transactions from an external account to a contract account can trigger code which can execute many different actions, e.g. transferring tokens or even creating a new contract
* *Account interactions*. By default, the Ethereum execution environment is lifeless, i.e. nothing happens and the state of every account remains the same. 
    * *Action trigger*. Any user can trigger an action by sending a transaction from an externally owned account, setting Ethereum’s wheels in motion
        * If the destination of the transaction is another EOA, then the transaction may transfer some ETH but otherwise does nothing
        * If the destination is a contract, then the contract in turn activates, and automatically runs its code

**How Merkle trie for state, transactions, and receipts are formed in Ethereum**.

**What is inside a block's body within a blockchain**.

**How to produce a Merkle proof**.

## References
* https://ethereum.org/en/developers/docs/accounts/
* https://www.preethikasireddy.com/post/how-does-ethereum-work-anyway?utm_source=pocket_mylist&fbclid=IwAR2_Uv33P39c6rLgFzLC6gms6iiVdAUZ8B6xThr4mdcAmd8nIVyFnl7oBb8