<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Truffle concepts](#truffle-concepts)
  - [Introduction to Truffle](#introduction-to-truffle)
    - [Artifacts](#artifacts)
    - [Interacting with contracts](#interacting-with-contracts)
      - [Reading and writing data](#reading-and-writing-data)
      - [Contract abstractions](#contract-abstractions)
      - [Contract initiation and reference](#contract-initiation-and-reference)
      - [Sending ether to a contract](#sending-ether-to-a-contract)
      - [Special methods on Truffle contract objects](#special-methods-on-truffle-contract-objects)
      - [Invoking overloaded methods](#invoking-overloaded-methods)
- [Appendix](#appendix)
  - [References](#references)
<!-- /TOC -->

# Truffle concepts
## Introduction to Truffle
**Truffle**.
* *Functionality*.
    * Compile contracts, and deploy them to multiple networks
    * Run automated tests
    * Provide an interactive debugger
    * Offer a library for interacting with your contracts on the frontend

### Artifacts
**Contract artifacts**. The large JSON files saved in the `build/contracts/` directory
* *Artifact creation and update*. Truffle saves our artifacts when we compile, and updates our artifacts with address information when we migrate
* *Artifact usage*. Whenever we use any part of Truffle, the artifacts are read from disk and processed
* *Applications*. Truffle’s artifacts have served as a common language for representing smart contract development concepts

**Build artifacts**. Artifacts of the compilation will be placed in `build/contracts/` directory, relative to the project root
* *Artifact name*. The name of the generated artifact `.json` files do not reflect the name of the source file
    
    $\to$ It reflects the name of the contract definition
    * *Example*. Changing the contract name string in the `artifacts.require` method to match that of the source file may lead to an error 
        
        ```js
        Error: Could not find artifacts for {yourContract} from any sources
        ```
        
        if the contained smart contract definition is named differently.

### Interacting with contracts
**Brief**. Truffle makes interacting with contracts easier
* *Explain*.
    * Writing raw requests to interact with contracts is clunky and cumbersome
    * Managing the state for each request is complicatedFortunately

#### Reading and writing data
**Reading and writing data**. The Ethereum network makes a distinction between writing data to the network and reading data from it

$\to$ This plays a significant part in how to write your application
* *Reading and writing data*. Transactions and calls are treated very differently
    * *Writing data*. Referred as a transaction
    * *Reading data*. Referred as a call

**Transactions**. Transactions fundamentally change the state of the network
* *Examples*. A transaction can be
    * Sending Ether to another account
    * Executing a contract function
    * Adding a new contract to the network
* *Defining characteristic*. A transaction writes, or changes, data
    * *Consequences*.
        * Transactions cost Ether to run, i.e. gas
        * Transactions take time to process
* *Transaction execution*. When executing a contract's function via a transaction
    
    $\to$ We cannot receive that function's return value
    * *Explain*. The transaction is not processed immediately
    * *Consequence*. Functions meant to be executed via a transaction will return a transaction ID instead
* *Conclusion*.
    * Transactions cost gas, i.e. Ether
    * Transactions change the state of the network
    * Transactions are not processed immediately
    * Transactions will not expose a return value, i.e. only a transaction ID

**Calls**. Calls can be used to execute code on the network, with no data permanently changed
* *Defining characteristic*. A call reads data
    * *Consequences*. Calls are free to run
* *Transaction execution*. When executing a contract's function via a call
    
    $\to$ We will receive the return value immediately
* *Conclusion*. 
    * Calls are free, i.e. do not cost gas
    * Calls do not change the state of the network
    * Calls are processed immediately
    * Calls will expose a return value

**Choosing between a transaction and a call**. As simple as deciding whether we want to read data, or write it

#### Contract abstractions
**Contract abstractions**. Wrapper code making interaction with contracts easier

$\to$ We can forget about the many engines and gears executing under the hood 
* *Truffle's contract abstraction*. Truffle uses its own contract abstraction via the `@truffle/contract` module
    * *Abstraction structure*. The abstraction contains
        * The exact same functions existing in our contract
        * An address pointing to the deployed version of the contract
    * *Example*. Consider `MetaCoin` contract with three methods `sendCoin`, `getBalanceInEth`, and `getBalance`

        ```js
        truffle(develop)> let instance = await MetaCoin.deployed()
        truffle(develop)> instance

        // outputs:
        //
        // Contract
        // - address: "0xa9f441a487754e6b27ba044a5a8eb2eec77f6b92"
        // - allEvents: ()
        // - getBalance: ()
        // - getBalanceInEth: ()
        // - sendCoin: ()
        // ...
        ```

**Contract functions execution**.
* *Contract of interest*.

    ```js
    contract MetaCoin {
        mapping (address => uint) balances;

        event Transfer(address indexed _from, address indexed _to, uint256 _value);

        constructor() public {
            balances[tx.origin] = 10000;
        }

        function sendCoin(address receiver, uint amount) public returns(bool sufficient) { ... }

        function getBalanceInEth(address addr) public view returns(uint){ ... }

        function getBalance(address addr) public view returns(uint) { ... }
    }
    ```

* *Making a transaction*. Consider the following code

    ```js
    truffle(develop)> let accounts = await web3.eth.getAccounts()
    truffle(develop)> instance.sendCoin(accounts[1], 10, {from: accounts[0]})
    ```

    * *Return values of the call*. We called the abstraction's `sendCoin` function directly
        
        $\to$ The function returned a transaction by default, i.e, writing data
    * *Transaction parameters*. The last additional parameter is a special object, which can always be passed as the last parameter to a function
        * *Purposes*. Edit specific details about the transaction
        * *Possible transaction parameters*. `from`, `to`, `gas`, `gasPrice`, `value`, `data`, and `nonce`
* *Making a call*. Consider the following code

    ```js
    truffle(develop)> let balance = await instance.getBalance(accounts[0])
    truffle(develop)> balance.toNumber()
    ```

    * *Return values of the call*. We received a return value, which is a `BN` object, which we then convert to a number
        * *Explain*. The Etherum network can handle very large numbers

**Processing transaction results**.
* *Transaction object returned by a transaction*. Have the following properties
    * *`tx` (string)*. The transaction hash
    * *`logs` (array)*. Decoded events, i.e. logs
    * *`receipt` (object)*. Transaction receipt, including the amount of gas used
* *Catching events*. Contracts can fire events, which you can catch to for debugging purposes
    * *Naive approach to handle events*. Process the logs array within result object of the transaction, which triggered the event, e.g.

        ```js
        truffle(develop)> let result = await instance.sendCoin(accounts[1], 10, {from: accounts[0]})
        truffle(develop)> result.logs[0]
        ```

#### Contract initiation and reference
**Add a new contract to the network**. We can deploy our own version of the contract to the network using the `.new()` function

```js
truffle(develop)> let newInstance = await MetaCoin.new()
truffle(develop)> newInstance.address
```

**Use a contract at a specific address**. If we have an address for a contract

$\to$ We can create a new abstraction to represent the contract at that address

```js
let specificInstance = await MetaCoin.at("0x1234...");
```

#### Sending ether to a contract
**Option 1**. Send a transaction directly to a contract via `instance.sendTransaction()`

```js
instance.sendTransaction({...}).then(function(result) {
    // Same transaction result object as above.
});
```

**Option 2**. There is also shorthand for only sending Ether directly

```js
instance.send(web3.utils.toWei(1, "ether")).then(function(result) {
    // Same result object as above.
});
```

#### Special methods on Truffle contract objects
**`estimateGas` method**. Estimate the amount of gas, which a transaction will require
* *Estimate transaction gas*. Call `estimateGas` it on the contract method, e.g.

    ```js
    const instance = await MyContract.deployed();
    const amountOfGas = await instance.sendTokens.estimateGas(4, myAccount);
    ```

* *Estimate contract creation cost*. We can use `estimateGas` on a contract's `new` method to estimate the deployment cost
    * *Explain*. Use `Contract.new.estimateGas()`

**`sendTransaction` method**. 
* *Truffle default execution mode*. If you execute a contract method, Truffle will intelligently figure out whether it needs to make a transaction or a call

    $\  to$ If your function can be executed as a call, then Truffle will do so and you will be able to avoid gas costs
* *Enforce transaction call*. Use the `sendTransaction` method found on the method itself
    * *Example*.

        ```js
        const instance = await MyContract.deployed();
        const result = await instance.getTokenBalance.sendTransaction(myAccount);
        ```

**`call` method**. Used to explicitly make a call

**`request` method**. Return an object, which can be passed to `web3.eth.sendTransaction` or `web3.eth.call`, if we want to perform the transaction or call ourself

#### Invoking overloaded methods
**Brief**. The current implementation of Truffle's contract abstraction can mistakenly infer the signature of an overloaded method, even though it exists in the contract ABI
* *Consequence*. Some methods may not be accessible through the contract's instance, but their accessors can be invoked explicitly via the `.methods` property of the contract
* *Example*.

    ```js
    const instance = await MyContract.deployed();
    instance.methods['setValue(uint256)'](123);
    instance.methods['setValue(uint256,uint256)'](11, 55);
    ```

# Appendix
## References
* https://trufflesuite.com/docs/truffle/getting-started/running-migrations.html