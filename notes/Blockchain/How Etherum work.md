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
    - [Gas and payment](#gas-and-payment)
    - [Transaction and messages](#transaction-and-messages)
    - [Blocks](#blocks)
  - [Transaction execution](#transaction-execution)
    - [Contract creation](#contract-creation)
    - [Message calls](#message-calls)
  - [Execution model](#execution-model)
    - [Block finalization](#block-finalization)
- [Appendix](#appendix)
  - [Concepts](#concepts)
  - [Discussion](#discussion)
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

### Gas and payment
**Fees in Etherum**. Every computation occurring as a result of a transaction on the Etherum network incurs a fee, which is paid in a denomination of "gas"
* *Gas*. The unit used to measure the feeds required for a particular computation

    <div style="text-align:center">
        <img src="https://i.imgur.com/0fmNzCO.png">
        <figcaption>Gas limit and gas price</figcaption>
    </div>

    * *Gas price*. The amount of ETH we are willing to spend on every unit of gas, and is measured in "gwei"
        * *Wei*. "Wei" is the smallest unit of ETH, i.e. $10^{18}$ Wei represents 1 ETH
        * *gwei*. One gwei is $10^9$ Wei
    * *Gas limit*. With every transaction, a sender sets a gas limit and gas price, whose product represents the maximum amount of Wei which the sender is willing to pay for executing a transaction
* *Maxium transaction fee*. If they have enough Ether in their account balance to cover this maximum, they’re good to go
    * *Gas refund*. The sender is refunded for any unused gas at the end of the transaction, exchanged at the original rate

        <div style="text-align:center">
            <img src="https://i.imgur.com/GBQS6fA.png">
            <figcaption>Gas charging</figcaption>
        </div>

    * *Insufficient gas*. In the case that the sender does not provide the necessary gas to execute the transaction, the transaction runs “out of gas” and is considered invalid

        <div style="text-align:center">
            <img src="https://i.imgur.com/kNM1FtH.png">
            <figcaption>Gas flow for failed transactions</figcaption>
        </div>

        * *Consequences*. 
            * The transaction processing aborts and any state changes that occurred are reversed, such that we end up back at the state of Ethereum prior to the transaction
            * A record of the transaction failing gets recorded, showing what transaction was attempted and where it failed
            * Since the machine already expended effort to run the calculations before running out of gas, logically, none of the gas is refunded to the sender
        * *Cash flow for failed transactions*. All the money spent on gas by the sender is sent to the “beneficiary” address, which is typically the miner’s address
            * *Explain*. Miners are expending the effort to run computations and validate transactions, miners receive the gas fee as a reward
    * *Gas price value*. Typically, the higher the gas price the sender is willing to pay, the greater the value the miner derives from the transaction
        
        $\to$ The more likely miners will be to select it
        * *Consequence*. Miners are free to choose which transactions they want to validate or ignore
            
            $\to$ In order to guide senders on what gas price to set, miners have the option of advertising the minimum gas price for which they will execute transactions

**Storage fees**. The total fee for storage is proportional to the smallest multiple of 32 bytes used
* *Storage fee refund*. Since increased storage increases the size of the Ethereum state database on all nodes

    $\to$ There is an incentive to keep the amount of data stored small
    * *Consequence*. If a transaction has a step that clears an entry in the storage, the fee for executing that operation of is waived, and a refund is given for freeing up storage space

**Purposes of fees**. In Etherum, every single operation executed by the network is simultaneously effected by every full node
* *Problem 1*. Computational steps on the Etherum VM are very expensive

    $\to$ Ethereum smart contracts are best used for simple tasks, e.g. running simple business logic or verifying signatures and other cryptographic objects, rather than more complex uses, e.g. file storage, email, or machine learning, which can put a strain on the network
    * *Consequence*. Imposing fees prevents users from overtaxing the network
* *Problem 2*. Ethereum is a Turing complete language, which allows for loops and makes Ethereum susceptible to the halting problem
    * *Halting problem*. A problem in which we cannot determine whether or not a program will run infinitely
    * *Consequence*. If there were no fees, a malicious actor could easily try to disrupt the network by executing an infinite loop within a transaction, without any repercussions
        
        $\to$ Thus, fees protect the network from deliberate attacks

### Transaction and messages
**Transaction's role**. Ethereum is a transaction-based state machine, i.e. transactions occurring between different accounts are what move the global state of Ethereum from one state to the next
* *Transaction*. A cryptographically signed piece of instruction that is generated by an externally owned account, serialized, and then submitted to the blockchain
* *Types of transactions*. Message calls, and contract creations, i.e. transactions creating new Etherum contracts

**Transaction structure**.

<div style="text-align:center">
    <img src="https://i.imgur.com/hCMfa55.png">
    <figcaption>Transaction structure</figcaption>
</div>

* *Nonce*. A count of the number of transactions sent by the sender
* *Gas price*. The number of Wei that the sender is willing to pay per unit of gas required to execute the transaction
* *Gas limit*. The maximum amount of gas that the sender is willing to pay for executing this transaction
    
    $\to$ This amount is set and paid upfront, before any computation is done
* *To*. The address of the recipient
    
    >**NOTE**. In a contract-creating transaction, the contract account address does not yet exist, and so an empty value is used

* *Value*. The amount of Wei to be transferred from the sender to the recipient
    
    >**NOTE**. In a contract-creating transaction, this value serves as the starting balance within the newly created contract account

* *v, r, s*. Used to generate the signature that identifies the sender of the transaction
* *Init (only exists for contract-creating transactions)*. An EVM code fragment, which is used to initialize the new contract account
    * *Execution*. init is run only once, and then is discarded
    * *Return value*. When init is first run, it returns the body of the account code, which is the piece of code that is permanently associated with the contract account
* *Data (optional field which only exists for message calls)*. The input data (i.e. parameters) of the message call
    * *Examples*. If a smart contract serves as a domain registration service, a call to that contract might expect input fields such as the domain and IP address

**Transaction and external owned accounts**. Both message calls and contract-creating transactions are always initiated by externally owned accounts and submitted to the blockchain

$\to$ Transactions are what bridge the external world to the internal state of Ethereum

**Transaction and contract**. Contracts existing within the global scope of Ethereum’s state can talk to other contracts within that same scope
* *Contract communication method*. Via “messages” or “internal transactions” to other contracts
    
    $\to$ We can think of messages or internal transactions as being similar to transactions, with the major difference that they are not generated by externally owned accounts
    * *Internal transaction generation*. Generated by contracts
    * *Internal transaction*. Virtual objects which are not serialized and only exist in the Ethereum execution environment
* *Contract code execution*. When one contract sends an internal transaction to another contract, the associated code that exists on the recipient contract account is executed

    <div style="text-align:center">
        <img src="https://i.imgur.com/uZhgqJa.png">
        <figcaption>Contract code execution</figcaption>
    </div>

* *Gas limit and internal transaction*. Internal transactions or messages do not contain a gas limit
    * *Explain*. Gas limit is determined by the external creator of the original transaction, i.e. some externally owned account
    * *Consequence*. The gas limit that the externally owned account sets must be high enough to carry out the transaction, including any sub-executions that occur as a result of that transaction
    * *Execution reversion*. In the chain of transactions and messages, a particular message execution runs out of gas
        
        $\to$ That message’s execution will revert, along with any subsequent messages triggered by the execution
        
        >**NOTE**. The parent execution does not need to revert

### Blocks
**Block in Etherum**. Consist of the block header, information about the transaction set included in the block, and a set of other block headers for the current block's ommers

**Ommer (or uncle block)**.

<div style="text-align:center">
    <img src="https://i.imgur.com/1NAUokS.png">
    <figcaption>Ommer blocks</figcaption>
</div>

* *Block creation time in Etherum*. Much lower, i.e. about 15 seconds, than those of other blockchains, e.g. like Bitcoin (10 minutes)
    * *Pros*. Faster transaction processing
    * *Cons*. More competing block solutions, i.e. orphaned blocks, are found by miners
        * *Explain*. There are lots of miners validating the same block at roughly the same time, but only the earliest one is made into the main chain, wasting other valid blocks
        * *Orphaned blocks*. Blocks which are not made into the main chain by miners
* *Purpose of ommers*. Help reward miners for including the orphaned blocks
    * *Miner rewarding*. The ommers that miners include must be “valid”, i.e. within the sixth generation or smaller of the present block 
        
        $\to$ After six children, stale orphaned blocks can no longer be referenced
        * *Explain*. Including older transactions would complicate things
    * *Ommer blocks' reward*. Smaller than a full block's reward, but there is still some incentive for miners to include these orphaned blocks and reap a reward

**Block header**.
* *Parent hash*. A hash of the parent block’s header, i.e. this is what makes the block set a “chain”
* *Ommer hash*. A hash of the current block's list of ommers
* *Beneficiary*. The account address, which receives the fees for mining this block
* *State root*. The hash of the root node of the state trie
* *Transaction root*. The hash of the root node of the transaction trie
* *Receipt root*. The hash of the root node of the receipt trie
* *Logs bloom*. A bloom filter, i.e. a data structure, consisting of log information
* *Difficulty*. The difficulty level of the block
* *Number*. The count of current block, with genesis block numbered 0
* *Gas limit*. The gas limit per block
* *Gas used*. The some of total gas used by transactions in this block
* *Timestamp*. The Unix timestamp of this block's inception
* *Extra data*. Extra data related to this block
* *Mix hash*. A hash that, when combined with the nonce, proves that the block has carried out enough computation
* *Nonce*. A hash that, when combined when mix hash, proves that the block has carried out enough computation

**Logs**. Etherum allows for logs to make it possible to track various transactions and messages
* *Contract logging*. A contract can explicitly generate a log by defining events it wants to log
* *Log entry structure*. Consist of
    * The logger's account address
    * A series of topics representing various events carried out by the transaction
    * Any data associated with these events
* *Bloom filter*. Logs are stored in a bloom filter, which stores the endless log data in an efficient manner

**Transaction receipt**. Logs stored in the header come from the log information contained in the transaction receipt
* *Explain*. As we receive a receipt when we buy something at a store, Ethereum generates a receipt for every transaction
    
    $\to$ Like we expect, each receipt contains certain information about the transaction
* *Receipt structure*.
    * The block number
    * Block hash
    * Transaction hash
    * Gas used by the current transaction
    * Cummulative gas used in the current block, after the current transaction has executed
    * Logs created when executing the current transaction
    * Other information

**Block difficulty**. Used to enforce consistency in the time it takes to validate blocks
* *Genesis block's difficulty*. 131,072
* *Difficulties of subsequent blocks*. There is a special formula is used to calculate the difficulty of every block thereafter
    * *Difficulty increment*. If a certain block is validated more quickly than the previous block, the Ethereum protocol increases that block’s difficulty
* *Difficulty and nonce*. $n\leq \frac{2^{256}}{H_d}$ where $H_d$ is the difficulty

    $\to$ The difficulty of a block affects its nonce, which is a hash calculated when mining a block, using the proof-of-work algorithm
* *Finding a nonce which meets a difficulty threshold*. Use the proof-of-work algorithm to enumerate all of the possibilities
    
    $\to$ The expected time to find a solution is proportional to the difficulty
    * *Explain*. The higher the difficulty, the harder it becomes to find the nonce, and so the harder it is to validate the block, which in turn increases the time it takes to validate a new block
    * *Consequence*. By adjusting the difficulty of a block, the protocol can adjust how long it takes to validate a block
* *Ensuring constant block validation time*. If, on the other hand, validation time is getting slower, the protocol decreases the difficulty
    
    $\to$ The validation time self-adjusts to maintain a constant rate, i.e. on average, one block every 15 seconds

## Transaction execution
**Requirements for transaction to be executed**.
* The transaction must be a properly formatted RLP
    * *Recursive Length Prefix (RLP)*. A data format used to encode nested arrays of binary data

        $\to$ RLP is the format Ethereum uses to serialize objects
* Valid transaction signature
* Valid transaction nonce
    * *Explain*. The nonce of an account is the count of transactions sent from that account
        
        $\to$ To be valid, a transaction nonce must be equal to the sender account’s nonce
* The transaction’s gas limit must be equal to or greater than the intrinsic gas used by the transaction
    * *Intrinsic gas*. Include
        * A predefined cost of 21,000 gas for executing the transaction
        * A gas fee for data sent with the transaction, i.e.
            * 4 gas for every byte of data or code that equals zero
            * 68 gas for every non-zero byte of data or code)
        * If the transaction is a contract-creating transaction, an additional 32,000 gas
        * Gas cost of each operation performed by transaction
* The sender’s account balance must have enough Ether to cover the “upfront” gas costs that the sender must pay
    * *Upfront gas cost*. 
        1. The transaction’s gas limit is multiplied by the transaction’s gas price to determine the maximum gas cost
        2. This maximum cost is added to the total value being transferred from the sender to the recipient

**Transaction execution**.
1. We deduct the upfront cost of execution from the sender’s balance
2. We increase the nonce of the sender’s account by 1 to account for the current transaction
3. We then calculate the gas remaining as the total gas limit for the transaction minus the intrinsic gas used
4. The transaction starts executing
    * *Substate*. Kept track by Etherum throughout the execution of a transaction
        * *Purpose*. Record information accrued during the transaction, which will be needed immediately after the transaction completes
        * *Structure*.
            * *Self-destruct set*. A set of accounts, if any, that will be discarded after the transaction completes
            * *Log series*. Archived and indexable checkpoints of the virtual machine’s code execution
            * *Refund balance*. The amount to be refunded to the sender account after the transaction
                * *Idea*. Ethereum keeps track of this using a refund counter
                * *Refund counter*. Start at zero and increments every time the contract deletes something in storage
5. Once all the steps required by the transaction have been processed, and assuming there is no invalid state
    
    $\to$ The state is finalized by determining the amount of unused gas to be refunded to the sender
6. The sender is also refunded some allowance from the refund balance
7. Once the sender is refunded,
    1. The Ether for the gas is given to the miner
    2. The gas used by the transaction is added to the block gas counter 
        * *Block ga counter*. Keep track of the total gas used by all transactions in the block
            * *Purpose*. Useful when validating a block
    3. All accounts in the self-destruct set, if any, are deleted
8. We are left with the new state and a set of the logs created by the transaction

### Contract creation
**Contract creation**.
1. We declare the address of the new account using a special formula
2. We initialize the new account by
    1. Setting the nonce to zero
    2. If the sender sent some amount of Ether as value with the transaction
        
        $\to$ Setting the account balance to that value
    3. Deducting the value added to this new account’s balance from the sender’s balance
    4. Setting the storage as empty
    5. Setting the contract’s `codeHash` as the hash of an empty string
3. Once we initialize the account, we can actually create the account, using the `init` code sent with the transaction
    * *`init` code execution*. Depending on the constructor of the contract

**Gas consumption**. As the code to initialize a contract is executed, it uses gas
* *Out-of-gas (OOG) exception*. The transaction is not allowed to use up more gas than the remaining gas
    
    $\to$ Otherwise the execution will hit an OOG exception and exit
    * *Gas refund*. If the transaction exits due to an out-of-gas exception
        
        $\to$ The state is reverted to the point immediately prior to transaction
        
        >**NOTE**. The sender is not refunded the gas that was spent before running out
    
    * *Ether refund*. Any Ether value included will be refunded if the transaction creation fails

**Sucessful creation**. If the initialization code executes successfully, a final contract-creation cost is paid

$\to$ This is a storage cost, and is proportional to the size of the created contract’s code
* *OOG exception*. If there’s not enough gas remaining to pay this final cost
    
    $\to$ The transaction declares an out-of-gas exception and aborts

### Message calls
**Message call execution**. Similar to that of a contract creation, with a few differences, i.e.
* *I/O data*. A message call execution does not include any `init` code, since no new accounts are being created
    * *Input data*. It can contain input data, if this data was provided by the transaction sender
    * *Output data*. Once executed, message calls also have an extra component containing the output data, which is used if a subsequent execution needs this data
* *Execution failure*. If a message call execution exits because it runs out of gas or because the transaction is invalid
    
    $\to$ None of the gas used is refunded to the original caller
    * *Explain*. All of the remaining unused gas is consumed, and the state is reset to the point immediately prior to balance transfer

**Transaction abort**. There was no way to stop or revert the execution of a transaction without having the system consume all the gas you provided
* *Byzantium update*. Include a new revert code that allowing a contract to stop execution and revert state changes, without consuming the remaining gas, and with the ability to return a reason for the failed transaction

## Execution model
**EVM**. The part of the protocol that actually handles processing the transactions

<div style="text-align:center">
    <img src="https://i.imgur.com/YH6ylV5.png">
    <figcaption>EVM storage</figcaption>
</div>

* *EVM and Turing machine*. The EVM is a Turing complete virtual machine
    * *Limitation of EVM compared to Turing complete machine*. EVM is intrinsically bound by gas
        * *Explain*. The total amount of computation that can be done is intrinsically limited by the amount of gas provided
* *EVM and stack machine*. EVM has a stack-based architecture
    * *Stack machine*. A computer that uses a last-in, first-out stack to hold temporary values
        * *Stack item size in EVM*. 256-bit
        * *Maximum stack size*. 1024
* *Storage*. Storage is non-volatile and is maintained as part of the system state
    * *EVM storage*. EVM stores program code separately, in a virtual ROM that can only be accessed via special instructions
        
        $\to$ The EVM differs from the typical von Neumann architecture, in which program code is stored in memory or storage

**EVM bytecode**. When a programmer writes smart contracts that operate on Ethereum, we typically write code in a higher-level language such as Solidity

$\to$ We then compile that down to EVM bytecode that the EVM can understand

**EVM bytecode execution**.
* *Requirements*. The following information must be available and valid
    * System state
    * Remaining gas for computation
    * Address of the account that owns the code that is executing
    * Address of the sender of the transaction that originated this execution
    * Address of the account that caused the code to execute (could be different from the original sender)
    * Gas price of the transaction that originated this execution
    * Input data for this execution
    * Value (in Wei) passed to this account as part of the current execution
    * Machine code to be executed
    * Block header of the current block
    * Depth of the present message call or contract creation stack
* *Initialization*. Memory and stack are empty, and the program counter is zero
* *Main execution*. EVM executes the transaction recursively, computing the system state and the machine state for each loop
    * *System state*. Ethereum’s global state
    * *Machine state*. Include
        * Gas available
        * Program counter
        * Memory contents
        * Active number of words in memory
        * Stack contents
    * *Gas consumption*. On each cycle, the appropriate gas amount is reduced from the remaining gas, and the program counter increments
    * *Loop termination*. At the end of each loop, there are three possibilities
        * The machine reaches an exceptional state 
            
            $\to$ The execution must be halted, with any changes discarded
        * The sequence continues to process into the next loop
        * The machine reaches a controlled halt, i.e. end-of-execution
* *Successful execution*. If the execution reaches a “controlled” or normal halt, the machine generates 
    * The resultant state
    * The remaining gas after this execution
    * The accrued substate
    * The resultant output

### Block finalization
**Block finalization**. Depending on whether the block is new or existing
* *New block finalization*. Refer to the process required for mining this block
* *Existing block finalization*. Refer to the process of validating the block

**Requirements for a block to be finalized**.
* *Validate, or, if mining, determine, ommers*. Each ommer block within the block header must be a valid header and be within the sixth generation of the present block
* *Validate, or, if mining, determine, transactions*. The `gasUsed` number on the block must be equal to the cumulative gas used by the transactions listed in the block
    * *Explain*. When executing a transaction, we keep track of the block gas counter
* *Apply rewards, only if mining*. The beneficiary address is awarded Ether for mining the block
    * *Ommer reward*. For each ommer
        * The current block’s beneficiary is awarded an additional $1/32$ of the current block reward
        * The beneficiary of the ommer blocks is awarded a certain amount
* *Verify, or, if mining, compute a valid, state and nonce*. 
    1. Ensure that all transactions and resultant state changes are applied
    2. Define the new block as the state after the block reward has been applied to the final transaction’s resultant state
        * *Verification method*. By checking this final state against the state trie stored in the header

# Appendix
## Concepts
**Hasing algorithm used by Etherum**. KECCAK-256

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

**Block time**. The time required to create the next block in a chain
* *Explain*. The time it takes for a blockchain miner to find a solution to the hash, i.e. the random series of characters associated with the block

## Discussion
**Receipt and transaction tries**.
* *Receipt trie*. Record the transaction outcome
* *Transaction trie*. Record transaction request vectors

## References
* https://ethereum.org/en/developers/docs/accounts/
* https://www.preethikasireddy.com/post/how-does-ethereum-work-anyway?utm_source=pocket_mylist&fbclid=IwAR2_Uv33P39c6rLgFzLC6gms6iiVdAUZ8B6xThr4mdcAmd8nIVyFnl7oBb8