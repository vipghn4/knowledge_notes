<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [What is NEAR protocol](#what-is-near-protocol)
  - [Introduction](#introduction)
    - [The evolution of blockchain technology](#the-evolution-of-blockchain-technology)
    - [Sharding](#sharding)
    - [The needs for scalable blockchains](#the-needs-for-scalable-blockchains)
  - [How NEAR blockchain works](#how-near-blockchain-works)
  - [NEAR token](#near-token)
- [Appendix](#appendix)
  - [Concepts](#concepts)
  - [Discussion](#discussion)
<!-- /TOC -->

# What is NEAR protocol
## Introduction
**NEAR**. A decentralized application platform running atop the NEAR Protocol blockchain
* *NEAR Protocol blockchain*. Organized to be permissionless, performant and secure enough to create a strong and decentralized data layer for the new web
* *Purpose*. Present an ideal platform for running applications having access to a shared and secure pool of money, identity and data owned by users
* *Idea*. Combine the features of partition-resistant networking, serverless compute and distributed storage

### The evolution of blockchain technology
**Bitcoin**. The perfect example fo firts-gen blockchain
* *Purpose*. Create a simple and straightforward payment system
* *Drawback*. It is infeasible to conduct complicated transactions with Bitcoin, which may have several layers of metadata and logic attached to it

**Etherum and smart contract platforms**. Ushered in the second-gen blockchain platforms with smart contracts

$\to$ Developers were able to program sophisticated transactions through these smart contracts
* *Decentralized applications (dApps)*. Developers now can create dApps, through which blockchain's use cases went through the roof
* *Scalability issues*. Bitcoin has a throughput of 7 transactions per second, while Ethereum can only manage 25
* *Layer-two solutions by Ethereum and Bitcoin*. Lightning network, raiden, plasma protocol etc.
    * *Idea*. Create an additional layer over the underlying blockchain
        
        $\to$ The main protocol can delegate repetitive and cumbersome tasks
    * *Drawback*.
        * These layer-2 solutions have not achieved acceptance from the masses
        * These layer-2 solutions ruin the original architecture of the protocol, which may have long-lasting implications

**NEAR**. Aim to solve the scalability issues and allow both the end-users and developers to enjoy the full potential of smart contracts and blockchain technology
* *Idea*. Every single node in the network doe not have to run all of the code
    * *Explain*. It essentially creates one big wasteful bottleneck and slows down all of the other approaches
* *Solution*. Use sharding, i.e. a layer-1 scalability

### Sharding
**Sharding**. Horizontally partition the database and turn into smaller, more manageable tables

<div style="text-align:center">
    <img src="https://i.imgur.com/Vn5rdNZ.png">
    <figcaption>DB sharding</figcaption>
</div>

* *Motivation from DBMS*. In a database, you sometimes have to deal with large bulky data

    $\to$ This dramatically hinders performance and throughput and makes the entire process extremely inefficient
* *Reason for not using vertical partition*. To make partitions homogeneous

**Sharding and blockchain**. Sharding breaks the global state of the blockchain into tinier more manageable shards
* *Effects of sharding*.
    * The state of the blockchain is splitted into shards
    * Each unique account is in one shard, and the accounts in that shard will only transact with the other accounts in the same shard
* *Example*. Consider three nodes A, B, and C which are to verify data T
    * *Sharding*. The data T is broken down into three shards T1, T2, and T3
    * *Consequence*. Each node can individually work on a shard at the same time

**Sharding and NEAR**. 
* *Other sharding approaches*. Require nodes to be run on increasingly complex hardware
    
    $\to$ This reduces the ability of more people to participate in the network
* *NEAR’s sharding*. Allow nodes to stay small enough to run on simple cloud-hosted instances

### The needs for scalable blockchains
**Cuuent blockchain platforms**. 
* They do not have the sophistication required to host high quality apps
* Speed is a vital factor when it comes to application usability

## How NEAR blockchain works
**NEAR consensus algorithm**.
* *Consensus protocols*. Used to reach agreement on a single value between multiple participants in a system
    * *Consequence*. If all network participants collaborate in accordance with the consensus protocol
        
        $\to$ New values may be appended to the ledger and verified by nodes
    * *Dispute handling*. In these cases, the network may focus on either safety or liveness
* *Nightshade*. The consensus mechanism implemented on NEAR, which models the system as a single blockchain
    * *Sharding*. The list of all the transactions in each block is split into physical chunks, one chunk per shard
        
        $\to$ All chunks accumulate to one block
    * *Chunk validation*. Chunks can only be validated by nodes that maintain the state of that shard

**Validator**. A key component of NEAR, which is responsible for maintaining consensus within the protocol
* *Validator*. Specialized nodes which must be alive forever while keeping their systems continually updated
* *Validator election*. NEAR determines its network validators every new epoch, electing them based on their stake
    * *Idea*.
        * *Existing validators*. The already elected validators are re-enrolled by automatically re-staking their tokens plus the accrued rewards
        * *Potential validators*. Potential validators have to have their stake above a dynamically determined level
    * *Stake gain*. A validator can strengthen their stake by two methods, i.e. buy tokens or borrow via stake delegation
    * *Rewarding*. The reward you receive is directly proportional to your stake
        
        $\to$ More your stake, more your rewards

**Consensus method**. Based on the heaviest chain consensus
* *Idea*. Once a block producer publishes a block, they collect the signatures of validator nodes
* *The weight of a block*. The cumulative stake of all the signers, whose signatures are included in the block
* *The weight of a chain*. The sum of the block weights
* *Slashing conditions*. Introduced for higher chain security

**NEAR runtime layer**. Used to execute smart contracts and other actions created by the users and preserve the state between the executions

## NEAR token
**NEAR token**. The fundamental native asset of the NEAR ecosystem and its functionality is enabled for all accounts
* *Token*. A unique digital asset similar to Ether which can be used to
    * Pay the system for processing transactions and storing data
    * Run a validating node as part of the network by participating in the staking process
    * Help determine how network resources are allocated and where its future technical direction will go by participating in governance processes
* *Benefits*.
    * Enables the economic coordination of all participants who operate the network
    * Enables new behaviors among the applications which are built on top of that network

# Appendix
## Concepts
**Network partition**. A division of a computer network into relatively independent subnets, by design, i.e. to optimize them separately, or due to the failure of network devices
* *Partition tolerant*. Distributed software must be designed to be partition-tolerant
    * *Explain*. Even after the network is partitioned, the software still works correctly

**Network partition resistance**. For the Bitcoin network to remain in consensus, the network of nodes must not be partitioned
* *Consequence*. For an individual node to remain in consensus with the network
    
    $\to$ It must have at least one connection to that network of peers that share its consensus rules
* *Reference*. https://gist.github.com/sdaftuar/c2a3320c751efb078a7c1fd834036cb0

**Layer-2 solution by ETH and BTC**. Scale an application by processing transactions off of the Ethereum Mainnet (layer 1) while still maintaining the same security measures and decentralization as the mainnet
* *Idea*. Built on top of the ETH blockchain, keeping transactions secure, speedy, and scalable
* *Benefits*. 
    * Increase throughput, i.e. transaction speed, and reduce gas fees
    * Keep the integrity of the Ethereum blockchain
        
        $\to$ This allows for complete decentralization, transparency, and security
    * Reducing the carbon footprint, i.e. less gas means less energy used
* *Layer 2 rollups*. Perform transaction operations off the main Ethereum blockchain then post the transaction data onto layer 1
    * *Properties*.
        * Transactions are executed outside of layer 1, i.e. reduces gas fees
        * Data and proof of transactions reside on layer 1, i.e. maintains security
        * By using the transaction data that is stored on layer 1
            
            $\to$ A rollup smart contract which is found on layer 1, can enforce proper transaction execution on layer 2
    * *Types of rollups*.
        * *Optimistic rollups*. Assume transactions are valid by default

            $\to$ Only run computation, via a fraud proof, in the act of a challenge
        * *Zero-knowledge rollups*. Run computation off-chain and submits a validity proof to the main-chain

**Staking**.
* *Consensus mechanism by Bitcoin and ETH*. Proof of Work
    * *Idea*. The network throws a huge amount of processing power at solving problems
        * *Example*. Validate transactions between strangers to make sure nobody is spending the same money twice
    * *Earning rewards*. Part of the process involves “miners” all over the world competing to be the first to solve a cryptographic puzzle
        
        $\to$ The winner earns the right to add the latest “block” of verified transactions onto the blockchain
        * *Reward for solving puzzles*. Some crypto
    * *Drawback*. 
        * For a relatively simple blockchain like Bitcoin
            
            $\to$ Proof of Work is a scalable solution
        * For something more complex like ETH

            $\to$ PoW can cause bottlenecks when there is too much activity
* *Proof of Stake*. A newer consensus mechanism
    * *Benefits*. Increasing speed and efficiency while lowering fees
        
        $\to$ This is mainly achieved by not requiring all those miners to churn through math problems
    * *Idea*. Transactions are validated by people who are literally invested in the blockchain via staking
        1. Users put their tokens on the line for a chance to add a new block onto the blockchain in exchange for a reward

            $\to$ Their staked tokens act as a guarantee of the legitimacy of any new transaction they add to the blockchain
        2. The network chooses validators based on the size of their stake and the length of time they held it
            * *Explain*. The most invested participants are rewarded
    * *Staking and mining*. Both are the processes, by which a network participant gets selected to add the latest batch of transactions to the blockchain and earn some crypto in exchange
    * *Handling invalid transactions*. If transactions in a new block are discovered to be invalid
        
        $\to$ Users can have a certain amount of their stake burned by the network
        * *Slashing event*. An event that a user's stake is burned by the network
* *Pros and cons*.
    * *Pros*.
        * Staking is a way of making assets work for us by generating rewards
        * Enhance the security and efficiency of the blockchain
            * *Explain*. By staking some of your funds
                
                $\to$ You make the blockchain more resistant to attacks and strengthen its ability to process transactions
    * *Cons*. A lookup or vesting period is required, where our crypto cannot be transferred for a certain period of time

**Epoch**. https://bisontrails.co/epoch/

**Decentralized autonomous organization (DAO)**. An organization represented by rules encoded as a computer program
* *Other name*. Decentralized autonomous corporation (DAC)
* *Characteristics*.
    * Transparent
    * Controlled by the organization members
    * Not influenced by a central governmen
* *Example*. A DAO's financial transaction record and program rules are maintained on a blockchain

## Discussion
**Why decentralization matters**.
* *Developers*. In the centralized world, the developers are often at the mercy of cloud platforms or even the government to make sure that they can continue to run the apps
    
    $\to$ In the decentralized world, there are no domineering intermediaries
* *End Users*. The transparency of decentralized applications can 
    * Allow users to see the backend code 
    * Users know exactly how the apps are going to use your personal information

**Can validator stake tokens during verifying a transaction**.

**Why we need to separate gas unit and gas price**. Gas unit is objective and gas price is subjective
* *Example*. Gas unit is TFLOPs, and gas price is model runtime

**Drawback of NEAR**. Data reliability, i.e. since there are fewer validators for each block in the chain