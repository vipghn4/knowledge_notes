<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Events and logs](#events-and-logs)
  - [Smart contract return values for the user interface](#smart-contract-return-values-for-the-user-interface)
  - [Asynchronous triggers with data](#asynchronous-triggers-with-data)
  - [A cheaper form of storage](#a-cheaper-form-of-storage)
- [Appendix](#appendix)
  - [Concepts](#concepts)
  - [References](#references)
<!-- /TOC -->

# Events and logs
**Events and logs in Ethereum**. Facilitate communication between smart contracts and their user interfaces
* *Traditional web development communication*. A server response is provided in a callback to the frontend
* *Ethereum smart contract communication*. When a transaction is mined, smart contracts can emit events and write logs to the blockchain
    
    $\to$ The frontend can then process

**Events**. Can be used in different ways, e.g.
* Smart contract return values for the user interface
* Asynchronous triggers with data
* A cheaper form of storage

## Smart contract return values for the user interface
**The simplest use of events**. Pass return values from contracts to an app’s frontend

**Return values from contract calls**.
* *Scenario*. Consider the following contract

    ```js
    contract ExampleContract {
        // some state variables ...
        function foo(int256 _value) returns (int256) {
            // manipulate state ...
            return _value;
        }
    }
    ```

* *Return values from contract execution*. 

    ```js
    // exampleContract is an instance of ExampleContract
    var returnValue = exampleContract.foo.call(2);
    console.log(returnValue) // 2
    ```

* *Return values from contract call as a transaction*. The returned value cannot be obtained

    ```js
    var returnValue = exampleContract.foo.sendTransaction(
        2, {from: web3.eth.coinbase}
    );
    console.log(returnValue) // transaction hash
    ```

    * *Explain*. The return value of a `sendTransaction` method is always the hash of the created transaction
    * *Return values of transaction*. Transactions do not return a contract value to the frontend
        * *Explain*. Transactions are not immediately mined and included in the blockchain

**Solution using events**. This is one of the intended purposes for events
* *Contract code*.

    ```js
    contract ExampleContract {
        event ReturnValue(address indexed _from, int256 _value);
        
        function foo(int256 _value) returns (int256) {
            ReturnValue(msg.sender, _value);
            return _value;
        }
    }
    ```

* *Front-end code*.

    ```js
    var exampleEvent = exampleContract.ReturnValue({_from: web3.eth.coinbase});
    
    exampleEvent.watch(function(err, result) {
        if (err) {
            console.log(err)
            return;
        }
        console.log(result.args._value)
        // check that result.args._from is web3.eth.coinbase then
        // display result.args._value in the UI and call    
        // exampleEvent.stopWatching()
    })

    exampleContract.foo.sendTransaction(2, {from: web3.eth.coinbase})
    ```

* *Explain*. When the transaction invoking foo is mined, the callback inside the watch will be triggered
    
    $\to$ This effectively allows the frontend to obtain return values from `foo`

## Asynchronous triggers with data
**Brief**. Events can be considered as asynchronous triggers with data
* *Explain*. When a contract wants to trigger the frontend, the contract emits an event
    
    $\to$ As, the frontend is watching for events, it can take actions, display a message, etc.

## A cheaper form of storage
**Brief**. We can use events as a significantly cheaper form of storage
* *Events as logs*. In the Ethereum Virtual Machine (EVM) and Ethereum Yellow Paper
    
    $\to$ Events are referred to as logs, i.e. there are `LOG` opcodes
* *Terminology*. 
    * *Events under storage perspective*. It is more accurate to say that data can be stored in logs, as opposed to data being stored in events
    * *Events under application perspective*. It is more accurate to say that contracts emit, or trigger, events, which the frontend can react to
* *Log storage*. Whenever an event is emitted, the corresponding logs are written to the blockchain

**Logs**. Designed to be a form of storage, which costs significantly less gas than contract storage
* *Storage cost*. Logs basically cost 8 gas per byte, whereas contract storage costs 20,000 gas per 32 bytes
* *Drawback*. Logs are not accessible from any contracts

**Using logs as cheap storage**. There are use cases for using logs as cheap storage
* *Example*. Use logs to store historical data, which can be rendered by the frontend
    * *Scenario*. A cryptocurrency exchange may want to show a user all the deposits that they have performed on the exchange
        
        $\to$ Instead of storing these deposit details in a contract, it is much cheaper to store them as logs
    * *Explain*. This is possible because an exchange needs the state of a user's balance, which it stores in contract storage, without knowing about historical deposits
* *Example contract code*.

    ```js
    contract CryptoExchange {
        event Deposit(uint256 indexed _market, address indexed _sender, 
                      uint256 _amount, uint256 _time);
        
        function deposit(uint256 _amount, uint256 _market) returns (int256) {
            // perform deposit, update user’s balance, etc
            Deposit(_market, msg.sender, _amount, now);
        }
    }
    ```

* *Example front-end code*. Suppose we want to update a UI as the user makes deposits

    ```js
    var depositEvent = cryptoExContract.Deposit({_sender: userAddress});
    
    depositEvent.watch(function(err, result) {
        if (err) {
            console.log(err)
            return;
        }
        // append details of result.args to UI
    })
    ```

* *Improved front-end code*. By default, listening for events only starts at the point when the event is instantiated
    
    $\to$ When the UI is first loading, there are no deposits to append to
    * *Solution*. If we want to retrieve the events since block 0 and that is done by adding a `fromBlock` parameter to the event

    ```js
    var depositEventAll = cryptoExContract.Deposit(
        {_sender: userAddress}, {fromBlock: 0, toBlock: 'latest'}
    );
    
    depositEventAll.watch(function(err, result) {
        if (err) {
            console.log(err)
            return;
        }
        // append details of result.args to UI
    })
    ```

    $\to$ When the UI is rendered `depositEventAll.stopWatching()` should be called

# Appendix
## Concepts
**Indexed parameters**. Up to 3 parameters can be indexed
* *Example*. A proposed token standard has
    
    ```js
    event Transfer(address indexed _from, address indexed _to, uint256 _value)
    ```
    
* *Consequence*. A frontend can efficiently watch for token transfers, which are
    * Sent by an address, i.e. `tokenContract.Transfer({_from: senderAddress})`, or
    * Received by an address, i.e. `tokenContract.Transfer({_to: receiverAddress})`, or
    * Sent by an address to a specific address, i.e. `tokenContract.Transfer({_from: senderAddress, _to: receiverAddress})`

## References
* https://consensys.net/blog/developers/guide-to-events-and-logs-in-ethereum-smart-contracts/