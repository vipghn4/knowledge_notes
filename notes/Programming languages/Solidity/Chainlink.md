<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Chainlink](#chainlink)
  - [Introduction](#introduction)
  - [Working with Oracles](#working-with-oracles)
<!-- /TOC -->

# Chainlink
## Introduction
**Blockchain Oracles**. Devices that connect our smart contracts and objects with data and computation from the real world
* *Example*. Pricing data on currencies, random number generators, and any other data we can think of
* *Purpose*. Provide a way for the decentralized Web3.0 ecosystem to access existing data sources, legacy systems, and advanced computations
* *Decentralized oracle networks (DONs)*. Enable the creation of hybrid smart contracts
    * *Hybrid smart contracts*. Where on-chain code and off-chain infrastructure are combined to support dApps, which react to real-world events and interoperate with traditional systems
    * *dApps*. Decentralized applications
* *Blockchain oracle problem*. Consider Alice and Bob wanting to bet on the outcome of a sports match
    
    $\to$ Alice bets \$20 on team B, with the \$40 total held in escrow by a smart contract
    * *Problem*. When the game ends, how does the smart contract know whether to release the funds to Alice or Bob
    * *Solution*. It requires an oracle mechanism to fetch accurate match outcomes off-chain, and deliver it to the blockchain in a secure and reliable manner

**Solving the blockchain oracle problem**. Outline a fundamental limitation o smart contracts, i.e. they cannot inherently interact with data and systems existing outside their native blockchain environment
* *Off-chain and on-chain*.
    * *Off-chain*. Resources external to the blockchain
    * *On-chain*. Data stored on the blockchain
* *Benefits of isolation from external systems*.
    * Strong consensus on the validity of user transactions
    * Prevention of double-spending attacks
    * Mitigation of network downtime
* *Securely interoperating with off-chain systems from a blockchain*. Require an additional piece of infrastructure known as an “oracle” to bridge the two environments

**Blockchain oracle mechanisms using a centralized entity**. Introduce a single point of failure, defeating the entire purpose of a decentralized blockchain application
* *Explain*.
    * If the single oracle goes offline, the smart contract will not have access to the data required for execution, or will execute improperly based on stale data
    * If the single oracle is corrupted, the data being delivered on-chain may be highly incorrect and lead to smart contracts executing very wrong outcomes
    * Since blockchain transactions are automated and immutable, a smart contract outcome based on faulty data cannot be reversed

        $\to$ User funds can be permanently lost
* *Consequence*. Centralized oracles are a non-starter for smart contract applications

**Decentralized oracle network (DON)**. Combine multiple independent oracle node operators and multiple reliable data sources to establish end-to-end decentralization
* *Motivation*. To truly overcoming the oracle problem necessitates decentralized oracles to prevent data manipulation, inaccuracy, and downtime
* *Chainlink DONs*. Many chainlink DONs incorporate three layers of decentralization to eliminate any single point of failure

    <div style="text-align:center">
        <img src="https://i.imgur.com/ONwB5ry.png">
        <figcaption>Layers of decentralization</figcaption>
    </div>

    * *Layers of decentralization*. Data source, individual node operator, and oracle network levels

**Types of blockchain oracles**. Each type of oracle involves some combination of fetching, validating, computing upon, and delivering data to a destination

<div style="text-align:center">
    <img src="https://i.imgur.com/L8ZPnhz.png">
    <figcaption>Different types of oracles enable the creation of hybrid smart contracts</figcaption>
</div>

* *Input oracles*. Fetches data from the real-world (off-chain) and delivers it onto a blockchain network for smart contract consumption
    * *Usage*. 
        * Power Chainlink Price Feeds
        * Providing DeFi smart contracts with on-chain access to financial market data 
* *Output oracles*. Allow smart contracts to send commands to off-chain systems that trigger them to execute certain actions
    * *Example*. 
        * Informing a banking network to make a payment
        * Telling a storage provider to store the supplied data
        * Pinging an IoT system to unlock a car door once the on-chain rental payment is made
* *Cross-chain oracles*. Can read and write information between different blockchains

    $\to$ This enables interoperability for moving both data and assets between blockchains
* *Compute-enabled oracles*. A new type of oracle becoming more widely used by smart contract applications
    * *Idea*. Use secure off-chain computation to provide decentralized services that are impractical to do on-chain due to technical, legal, or financial constraints

**Oracle reputation derived from on-chain performance history**. Reputation is key to choosing between oracle service providers
* *Reputation in blockchain oracle systems*. Give users and developers the ability to monitor and filter between oracles based on parameters they deem important
    * *Support for oracle reputation*. Oracle reputation is aided by the fact that oracles sign and deliver their data onto an immutable public blockchain ledger
        
        $\to$ Their historical performance history can be analyzed and presented to users
* *Reputation frameworks*. Provide transparency into the accuracy and reliability of each oracle network and individual oracle node operator
    * *Consequence*.
        * Users can then make informed decisions about which oracles they want to service their smart contracts
        * Oracle service providers can also leverage their off-chain business reputation to provide users additional guarantees of their reliability

## Working with Oracles
**Basic request model of working with oracles**.
* *Two-transaction architecture*. A two transaction event, which takes at the minimum two blocks to complete
    1. Callee contract makes a request in a transaction to a Chainlink node
        * *Chainlink node*. Comprised of a smart contract and the corresponding off-chain node
    2. When the Chainlink node receives the request, the callee contract or oracle contract emits an event
        
        $\to$ Chainlink node (Off-chain) is listening for the event, where the details of the request are logged in the event
    3. In a second transaction created by the Chainlink node, it returns the data on-chain by calling a function described by the callee contract
        * *Example*. In the case of the Chainlink VRF, a randomness proof is done to ensure the number is truly random
* *Benefits*. Brute force attacks on randomness or data requests are throttled and impossible to hack without costing the attacker insane fees in gas costs
* *LINK or Chainlink token*. Similar making a transaction on Ethereum, where we have to pay some transaction gas
    
    $\to$ Working with oracles needs paying a little bit of oracle gas, i.e. the LINK or Chainlink token
    * *LINK token*. Designed to work with oracles and ensure the security of the Chainlink oracle networks
        * *Explain*. Whenever we make a request following the basic request model
            
            $\to$ Our contracts must be funded with a set amount of LINK
        * *Required amount of LINK*. Defined by the specific oracle service we are using
            
            >**NOTE**. Each service has different oracle gas fees

**`VRFConsumerbase` contract**. Include all the code we need to send a request to a Chainlink oracle, including all the event logging code
* *Related variables when working with a Chainlink node*. The following variables can be found in [Chainlink VRF contact addresses document page](https://docs.chain.link/docs/vrf-contracts/)
    * *The address of the Chainlink token contract*. Needed so our contract can tell if we have enough LINK tokens to pay for the gas
    * *The VRF coordinator contract address*. Needed to verify that the number we get is actually random
        * *Explain*. The Chainlink node will call the VRF Coordinator first to verify the number is random
            
            $\to$ The VRF Coordinator then will be the one to call our contract
    * *The Chainlink node keyhash*. Used to identify which Chainlink node we want to work with
    * *The Chainlink node fee*. Represent the fee (gas) the Chainlink will charge us, expressed in LINK tokens
* *Required functions to interact with Chainlink node*.
    * A function to request the random number, i.e.
        1. This function checks to see that our contract has LINK tokens to pay a Chainlink node
        2. Then, it sends some LINK tokens to the Chainlink node
        3. Emits an event that the Chainlink node is looking for
        4. Assigns a `requestId` to our request for a random number on-chain
    * A function for the the Chainlink node to return the random number to, i.e.
        1. The Chainlink node first calls a function on the VRF Coordinator and includes a random number
        2. The VRF Coordinator checks to see if the number is random
        3. Then, it returns the random number the Chainlink node created, along with the original `requestId` from our request