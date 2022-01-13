<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [More about Bitcoin's transaction](#more-about-bitcoins-transaction)
  - [Transaction](#transaction)
    - [Transaction I/O](#transaction-io)
    - [Transaction fee](#transaction-fee)
    - [Transaction chaining and orphan transactions](#transaction-chaining-and-orphan-transactions)
  - [Packing transactions into blocks](#packing-transactions-into-blocks)
- [Appendix](#appendix)
  - [Discussion](#discussion)
<!-- /TOC -->

# More about Bitcoin's transaction
## Transaction
**Transaction (tx)**. A transfer of bitcoin value from one or more inputs to one or more outputs
* *Transaction structure*.

    | Size | Field | Description |
    | --- | --- | --- |
    | 4 bytes | Version | Specify which rules this transaction follows |
    | 1 - 9 bytes | Input counter | How many inputs are included |
    | Variable | Inputs | One or more transaction inputs |
    | 1 - 9 bytes | Output counter | How many outputs are included |
    | Variable | Outputs | One or more transaction outputs |
    | 4 bytes | Locktime | A UNIX timestamp or block number |

* *Transaction locktime*. Define the earliest time that a transaction can be added to the blockchain
    * *Locktime value*.
        * *Zero locktime (in most transactions)*. Indicate immediate execution
        * *Low locktime*. If locktime is nonzero and below 500 million, it is interpreted as a block height
            
            $\to$ The transaction is not included in the blockchain prior to the specified block height
        * *High locktime*. If it is above 500 million, it is interpreted as a Unix Epoch timestamp
            
            $\to$ The transaction is not included in the blockchain prior to the specified time
* *Number of I/O*. A bitcoin transaction can have many inputs and many outputs
    * *Explain*. Bitcoin has a transaction oriented logic, where amounts are transferred from previous transactions
        * *Example 1*. Neglecting the fees, to be able to spend 1 bitcoin
            * When the wallet has 2 previous tx with amounts of 0.5 BTC
                
                $\to$ A new tx is created with two inputs
            * Same logic would apply, if 4 previous tx existed, each @0.25 BTC
                
                $\to$ A tx with 4 inputs would be created
        * *Example 2*. For the outputs, we can create tx with one or more outputs
            * *Explain*. Faucets pay to many outputs, instead of creating single transactions, to save fee

### Transaction I/O
**Unspent transaction output (UTXO)**. Indivisible chunks of bitcoin currency locked to a specific owner, recorded on the blockchain

$\to$ These are recognized as currency units by the entire network
* *UTXO tracking in the network*. The bitcoin network tracks all available (unspent) UTXO currently numbering in the millions
* *UTXOs of a user*. Whenever a user receives bitcoin, that amount is recorded within the blockchain as a UTXO
    
    $\to$ User’s bitcoin might be scattered as UTXO amongst hundreds of transactions and hundreds of blocks 
    * *Consequence*. There is no such thing as a stored balance of a bitcoin address or account
        
        $\to$ There are only scattered UTXO, locked to specific owners
* *Transaction inputs*. UTXO consumed by a transaction
* *Transaction outputs*. UTXO created by a transaction

    $\to$ Chunks of bitcoin value move forward from owner to owner in a chain of transactions consuming and creating UTXO
* *UTXO consumption*. Transactions consume UTXO by 
    1. Unlock it with the signature of the current owner
    2. Create UTXO by locking it to the bitcoin address of the new owner
* *Coinbase transaction*. The first transaction in each block

    $\to$ This is placed by the winning miner can creates a brand-new bitcoin payable to that miner as a reward for mining
    * *Consequence*. Outputs come first, rather than inputs
        * *Explain*. Coinbase transactions, which generate new bitcoin, have no inputs and create outputs from nothing

**Transaction outputs**. Every bitcoin transaction creates outputs, which are recorded on the bitcoin ledger
* *Transaction outputs and UTXO*. Almost all of these outputs, with one exception, i.e. see Data Output, create spendable UTXO
    
    $\to$ These are then recognized by the whole network and available for the owner to spend in a future transaction
* *Sending bitcoin*. Sending someone bitcoin is creating an UTXO registered to their address and available for them to spend
* *Transaction outputs structure*.

    | Size | Field | Description |
    | --- | --- | --- |
    | 8 bytes | Amount | Bitcoin value in satoshis |
    | 1 - 9 bytes | Locking script size | Locking script length in bytes |
    | Variable | Locking-script | A script defining the conditions required to spend the output |

* *Spending conditions*. In most cases, the locking script will lock the output to a specific bitcoin address, transferring ownership to the new owner

**Transaction inputs**. Pointers to UTXO, i.e. by reference to the transaction hash and sequence number where the UTXO is recorded in the blockchain
* *Spending UTXO with transaction input*. A transaction input also includes unlocking scripts that satisfy the spending conditions set by the UTXO
    * *Unlocking script*. Usually a signature proving ownership of the bitcoin address in the locking script
* *Transaction inputs structure*.

    | Size | Field | Description |
    | --- | --- | --- |
    | 32 bytes | Transaction Hash | Pointer to the transaction containing the UTXO to be spent |
    | 4 bytes | Output Index | The index number of the UTXO to be spent |
    | 1-9 bytes (VarInt) | Unlocking-Script Size | Unlocking-Script length in bytes |
    | Variable | Unlocking-Script | A script that fulfills the conditions of the UTXO locking script |
    | 4 bytes | Sequence Number | Currently disabled Tx-replacement feature |

### Transaction fee
**Transaction fee**. The difference between the sum of inputs and the sum of outputs

$\to$ This fee that is collected by the miners
* *Change and fee*. If we are constructing transactions, we must ensure we do not inadvertently include a very large fee by underspending the inputs
    * *Explain*. We must account for all inputs, if necessary by creating change
        
        $\to$ Otherwise we will end up giving the miners a very big tip

### Transaction chaining and orphan transactions
**Transaction chain**. Transactions form a chain, where one transaction spends the outputs of the parent transaction and creates outputs for a child transaction

**Orphan transaction pool**. When a chain of transactions is transmitted across the network

$\to$ They do not always arrive in the same order, i.e. the child might arrive before the parent
* *Solution*. The nodes seeing a child first can see that it references an unknown parent transaction
    
    $\to$ Rather than reject the child
    1. They put it in a temporary pool to await the arrival of its parent 2. They then propagate it to every other node
* *Orphan transaction pool*. The pool of transactions without parents
* *Releasing orphans from pool*. Once the parent arrives
    1. Any orphans referencing the UTXO created by the parent are released from the pool
    2. The orphans are revalidated recursively
    3. The entire chain of transactions can be included in the transaction pool, ready to be mined in a block
* *Consequence*. 
    * Valid transactions will not be rejected due to out-of-order data transmission
    * Eventually the chain the orphans belong to is reconstructed in the correct order, regardless of the order of arrival
* *Maximum number of orphans*. There is a limit to the number of orphan transactions stored in memory, to prevent a denial-of-service attack against bitcoin nodes
    * *Consequence*. If the number of orphan transactions in the pool exceeds `MAX_ORPHAN_TRANSACTIONS`
        
        $\to$ One or more randomly selected orphan transactions are evicted from the pool, until the pool size is back within limits

## Packing transactions into blocks
**Stage 1 - Transaction**. The process of mining a new block starts when a user wants to send a certain amount of cryptocurrency to another person
* *Transaction creation*.
    1. The user sends transaction with the data from his wallet

        $\to$ The user broadcasts the transaction to the network so that miners can collect the transaction to their `mempool`
    2. The user waits for the network to do and confirm
        
        $\to$ The transaction remain there until a block is mined where they can be included and validated

**Stage 2 - Compilation**. The pending transactions on the network are collected and grouped into a block of transactions by mining nodes

$\to$ The collected transactions are stored in the miner's `mempool`

>**NOTE**. Multiple miners are likely to collect the same transactions

>**NOTE**. Transactions will all be unconfirmed until the block is mined

**Stage 3 - Training**. Each miner will select the transactions they want to include and build their own block
* *Handling validated transactions*. If there are transactions already validated and included in the previous block
    
    $\to$ they will be eliminated from the block
* *Candidate block*. This new block is known as a candidate, as it is not yet valid because it does not have a valid proof of work

**Stage 4 - PoW**. Once each miner has formed their own transaction block, they need to find a valid signature for that block

$\to$ They need carry out a proof of work

**Stage 5 - Transmission**. When a mining node manages to find a valid output hash for a block

$\to$ It transmits that block together with the signature to the other nodes in the network so that they can validate it
* *Rewarding*. The miner receives the reward set by the mining, putting new bitcoins into circulation

**Stage 6 - Verification**. The other nodes of the network are in charge of 
* Validating and verifying that the block and the hash comply with the conditions of the system
* Verifying its legitimacy and whether it really contains the established number of zeros

**Stage 7 - Confirmation**. Once the new block is added to the blockchain, all the others that are added to it will count as a confirmation
* *Problem*. Since each miner started the process with his own block, they can continue mining, ignoring the newly confirmed block
    * *Solution*. Once a block is generated, all mining nodes must begin the process by forming a new transaction block
        
        $\to$ They cannot continue mining the previous block
        * *Explain*. Each block must add the output hash of the preceding block

# Appendix
## Discussion
