<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Advanced Solidity](#advanced-solidity)
  - [Immutability of contracts](#immutability-of-contracts)
  - [Ownable contracts](#ownable-contracts)
  - [Function modifier](#function-modifier)
    - [Payable modifiers](#payable-modifiers)
  - [Struct packing to save gas](#struct-packing-to-save-gas)
  - [Storage is expensive](#storage-is-expensive)
  - [Random numbers](#random-numbers)
  - [Token](#token)
  - [Preventing overflows](#preventing-overflows)
- [Appendix](#appendix)
  - [Concepts](#concepts)
<!-- /TOC -->

# Advanced Solidity
## Immutability of contracts
**Immutability of contracts**. After we deploy a contract to Ethereum, it’s immutable, which means that it can never be modified or updated again

$\to$ The initial code you deploy to a contract is there to stay, permanently, on the blockchain
* *Consequence*. Security is such a huge concern in Solidity
    * *Explain*. If there's a flaw in your contract code, there's no way for you to patch it later
        
        $\to$ You would have to tell your users to start using a different smart contract address that has the fix
* *Immutability as feature of smart contracts*. The code is law, i.e. if you read the code of a smart contract and verify it
    
    $\to$ You can be sure that every time you call a function it's going to do exactly what the code says it will do, i.e. no one can later change that function and give you unexpected results

**External dependencies**. It often makes sense to have functions that will allow you to update key portions of the DApp
* *Example*. Consider the `CryptoKitties` contract, whose address was hard-coded into our DApp, had a bug and someone destroyed all the kitties, which is to be eaten by the zombies

    $\to$ Our DApp would point to a hardcoded address that no longer returned any kitties
    * *Consequence*. Our zombies would be unable to feed on kitties, and we'd be unable to modify our contract to fix it

## Ownable contracts
**Motivation**. We do want the ability to update the internal state of our contract, but we do not want everyone to be able to update it

$\to$ We can make contracts `Ownable`, i.e. they have an owner, who has special priviledges

**`Ownable` contract from OpenZeppelin**. 

```js
/**
 * @title Ownable
 * @dev The Ownable contract has an owner address, and provides basic authorization control
 * functions, this simplifies the implementation of "user permissions".
 */
contract Ownable {
  address private _owner;

  event OwnershipTransferred(
    address indexed previousOwner,
    address indexed newOwner
  );

  /**
   * @dev The Ownable constructor sets the original `owner` of the contract to the sender
   * account.
   */
  constructor() internal {
    _owner = msg.sender;
    emit OwnershipTransferred(address(0), _owner);
  }

  /**
   * @return the address of the owner.
   */
  function owner() public view returns(address) {
    return _owner;
  }

  /**
   * @dev Throws if called by any account other than the owner.
   */
  modifier onlyOwner() {
    require(isOwner());
    _;
  }

  /**
   * @return true if `msg.sender` is the owner of the contract.
   */
  function isOwner() public view returns(bool) {
    return msg.sender == _owner;
  }

  /**
   * @dev Allows the current owner to relinquish control of the contract.
   * @notice Renouncing to ownership will leave the contract without an owner.
   * It will not be possible to call the functions with the `onlyOwner`
   * modifier anymore.
   */
  function renounceOwnership() public onlyOwner {
    emit OwnershipTransferred(_owner, address(0));
    _owner = address(0);
  }

  /**
   * @dev Allows the current owner to transfer control of the contract to a newOwner.
   * @param newOwner The address to transfer ownership to.
   */
  function transferOwnership(address newOwner) public onlyOwner {
    _transferOwnership(newOwner);
  }

  /**
   * @dev Transfers control of the contract to a newOwner.
   * @param newOwner The address to transfer ownership to.
   */
  function _transferOwnership(address newOwner) internal {
    require(newOwner != address(0));
    emit OwnershipTransferred(_owner, newOwner);
    _owner = newOwner;
  }
}
```

* *Constructor*. An optional special function that has the same name as the contract

    $\to$ This will get executed only one time, when the contract is first created
* *Function modifiers*. Kind of half-functions that are used to modify other functions, e.g. usually to check some requirements prior to execution
    * *Example*. `onlyOwner` can be used to limit access so only the owner of the contract can run this function
* *`onlyOwner` function*. `onlyOwner` is a common requirement for contracts, hence most Solidity DApps start with a copy/paste of this `Ownable` contract, and then their first contract inherits from it
* *Problems*. 
    * Giving the owner special powers over the contract like this is often necessary, but it could also be used maliciously
        * *Example*. The owner could add a backdoor function that would allow him to transfer anyone's zombies to himself
    * It is important that a DApp being on Ethereum does not mean it is decentralized
        
        $\to$ You have to actually read the full source code to make sure it's free of special controls by the owner that you need to potentially worry about
        * *Consequence*. There is a careful balance as a developer between maintaining control over a DApp such that you can fix potential bugs, and building an owner-less platform that your users can trust to secure their data

## Function modifier
**Function modifier**. Look like a function
* *Differences from functions*.
    * Use the keyword `modifier` instead of `function`
    * It can't be called directly like a function can
        
        $\to$ Instead we can attach the modifier's name at the end of a function definition to change that function's behavior
* *Example*. Consider `onlyOwner()` modifier above, when you call renounceOwnership, the code inside onlyOwner executes first
    
    $\to$ When it hits the `_;` statement in `onlyOwner`, it goes back and executes the code inside `renounceOwnership`
* *Usage*. So while there are other ways you can use modifiers, one of the most common use-cases is to add a quick require check before a function executes

**Function modifies with arguments**. Function modifiers can take arguments

```js
// A mapping to store a user's age:
mapping (uint => uint) public age;

// Modifier that requires this user to be older than a certain age:
modifier olderThan(uint _age, uint _userId) {
    require(age[_userId] >= _age);
    _;
}

// Must be older than 16 to drive a car (in the US, at least).
// We can call the `olderThan` modifier with arguments like so:
function driveCar(uint _userId) public olderThan(16, _userId) {
    // Some function logic
}
```

**Function modifiers summary**. 
* *Common function modifiers*. `private`, `internal`, `external`, `public`, `view`, `pure`, `onlyOwner`, etc.
* *Function modifiers stacking*.

    ```js
    function test() external view onlyOwner anotherModifier { /* ... */ }
    ```

### Payable modifiers
**`payable` functions**. Special type of function which can receive Ether
* *Explain*. In Ethereum, where both the money (Ether), the data (transaction payload), and the contract code itself all live on Ethereum
    
    $\to$ It is possible for you to call a function and pay money to the contract at the same time
* *Consequence*. This allows for some really interesting logic, e.g. requiring a certain payment to the contract to execute a function

>**NOTE**. If a function is not marked payable and you try to send Ether to it as above, the function will reject your transaction

**Example for online store**.
* *`OnlineStore` contract*.

    ```js
    contract OnlineStore {
        function buySomething() external payable {
            // Check to make sure 0.001 ether was sent to the function call:
            require(msg.value == 0.001 ether);
            // If so, some logic to transfer the digital item to the caller of the function:
            transferThing(msg.sender);
        }
    }
    ```

* *Calling function from `web3.js`*.

    ```js
    // Assuming `OnlineStore` points to your contract on Ethereum:
    OnlineStore.buySomething({from: web3.eth.defaultAccount, value: web3.utils.toWei(0.001)})
    ```

**Withdraws**. After you send Ether to a contract, it gets stored in the contract's Ethereum account

$\to$ It will be trapped there, unless you add a function to withdraw the Ether from the contract
* *Example*.

    ```js
    contract GetPaid is Ownable {
        function withdraw() external onlyOwner {
            address payable _owner = address(uint160(owner()));
            _owner.transfer(address(this).balance);
        }
    }
    ```

* *`address payable`*. You cannot transfer Ether to an address unless that address is of type `address payable`
    * *Example*. The `_owner` variable is of type `uint160`, i.e. we must explicitly cast it to `address payable`
* *`transfer()`*. Once you cast the address from `uint160` to `address payable`
    
    $\to$ You can transfer Ether to that address using the `transfer` function
    * *`transfer()`*. You can use `transfer` to send funds to any Ethereum address, e.g.

        ```js
        uint itemFee = 0.001 ether;
        msg.sender.transfer(msg.value - itemFee);
        ```

        ```js
        seller.transfer(msg.value)
        ```

* *`address(this).balance`*. Return the total balance stored on the contract
    * *Example*. If 100 users had paid 1 Ether to our contract, `address(this).balance` would equal 100 Ether

## Struct packing to save gas
**Struct packing**. 
* *Gas charging for primitive types*. Normally there's no benefit to using these sub-types, since Solidity reserves `256` bits of storage regardless of the `uint` size
    * *Example*. Using `uint8` instead of `uint` (`uint256`) won't save you any gas
* *Gas charging for structs*. If you have multiple `uint`s inside a `struct`
    
    $\to$ Using a smaller-sized uint when possible will allow Solidity to pack these variables together to take up less storage
    * *Consequence*. Inside a struct you will want to use the smallest integer sub-types you can get away with
* *Struct member clustering*. Clustering identical data types together, i.e. put them next to each other in the struct, can make Solidity minimize the required storage space
    * *Example*. A `struct` with fields `uint c; uint32 a; uint32 b;` will cost less gas than a `struct` with fields `uint32 a; uint c; uint32 b;`
        * *Explain*. The `uint32` fields are clustered together

## Storage is expensive
**Storage cost**. One of the more expensive operations in Solidity is using `storage`, particularly writes
* *Explain*. When you write or change a piece of data, it’s written permanently to the blockchain
    
    $\to$ Thousands of nodes across the world need to store that data on their hard drives, and this amount of data keeps growing over time as the blockchain grows
* *Consequence*. You want to avoid writing data to storage except when absolutely necessary
    
    $\to$ Sometimes this involves seemingly inefficient programming logic. e.g. like rebuilding an array in memory every time a function is called
    * *Explain*. 
        * In most programming languages, looping over large data sets is expensive
        * In Solidity, this is way cheaper than using `storage` if it is in an `external view` function, since view functions don't cost your users any gas

## Random numbers
**Random number generation via `keccak256`**. The best source of randomness we have in Solidity is the keccak256 hash function

```js
// Generate a random number between 1 and 100:
uint randNonce = 0;
uint random = uint(keccak256(abi.encodePacked(now, msg.sender, randNonce))) % 100;
randNonce++;
uint random2 = uint(keccak256(abi.encodePacked(now, msg.sender, randNonce))) % 100;
```

* *Drawback*. 
    * *Function invocation*. In Ethereum, when you call a function on a contract
        1. You broadcast it to a node, or nodes on the network, as a transaction
        2. The nodes on the network then collect a bunch of transactions, try to be the first to solve a computationally-intensive mathematical problem as a "Proof of Work"
        3. The nodes then publish that group of transactions along with their Proof of Work (PoW) as a block to the rest of the network
        4. Once a node has solved the PoW, the other nodes stop trying to solve the PoW
        5. The other nodes verify that the other node's list of transactions are valid
        6. The other nodes then accept the block and move on to trying to solve the next block
    * *Consequence*. Our random number function is exploitable
* *Motivation for attack*. 
    * Since tens of thousands of Ethereum nodes on the network are competing to solve the next block, my odds of solving the next block are extremely low
        
        $\to$ It would take me a lot of time or computing resources to exploit this profitably
        * *Consequence*. If the reward were high enough, it would be worth it for me to attack
    * While this random number generation is not secure on Ethereum, in practice unless our random function has a lot of money on the line
        
        $\to$ The users of your game likely will not have enough resources to attack it

**Safe random generation in Etherum**. Because the entire contents of the blockchain are visible to all participants, this is a hard problem
* *Idea*. Use an oracle to access a random number function from outside of the Ethereum blockchain

**Chainlink VRF**. A way to get randomness from outside the blockchain, but in a proven cryptographic manner

$\to$ This is important since we always want our logic to be truly incorruptible

<div style="text-align:center">
    <img src="https://cryptozombies.io/course/static/image/lesson-19/chainlink-vrf.png">
    <figcaption>Chainlink VRF</figcaption>
</div>

* *Alternative approach for getting randomness outside the blockchain*. Use an off-chain API call to a service returning a random number
    * *Problem*. If that services goes down, is bribed, hacked, or otherwise
        
        $\to$ You could potentially be getting back a corrupt random number
    * *Solution*. Chainlink VRF includes on-chain verification contracts that cryptographically prove that the random number the contract is getting is really random

## Token
**Token on Etherum**. A smart contract following some common rules

$\to$ Namely, it implements a standard set of functions, which all other token contracts share, e.g.

```js
transferFrom(address _from, address _to, uint256 _tokenId)
```

```js
balanceOf(address _owner)
```

* *Internal mapping of token*. Internally the smart contract usually has a mapping, `mapping(address => uint256)` balances keeping track of how much balance each address has
    * *Consequence*. Basically a token is just a contract that keeps track of who owns how much of that token, and some functions so those users can transfer their tokens to other addresses

**ERC20 tokens**. All ERC20 tokens share the same set of functions with the same names, they can all be interacted with in the same ways
* *Homogeneous token*. If you build an application that is capable of interacting with one ERC20 token
    
    $\to$ It is also capable of interacting with any ERC20 token
* *Consequence*. That way more tokens can easily be added to your app in the future without needing to be custom coded
    
    $\to$ You could simply plug in the new token contract address, and boom, your app has another token it can use
* *Example*. When an exchange adds a new ERC20 token, it just needs to add another smart contract it talks to
    * *Consequence*. The exchange only needs to implement this transfer logic once, then when it wants to add a new ERC20 token
        
        $\to$ it adds the new contract address to its database
        * Users can tell that contract to send tokens to the exchange's wallet address
        * The exchange can tell the contract to send the tokens back out to users when they request a withdraw

**ERC721 tokens**. Another token standard, which is much better fit for crypto-collectibles, e.g. collection of items
* *Idea*. ERC721 tokens are not interchangeable since each one is assumed to be unique, and are not divisible

    $\to$ You can trade them only in whole units, and each one has a unique ID

**ERC721 transfer logic**.
* *Option 1*. The sender of the token calls the transferFrom function

    ```js
    function transferFrom(address _from, address _to, uint256 _tokenId) external payable;
    ```

    * *Procedure*. The token's owner calls `transferFrom` with 
        * His `address` as the _from `parameter`
        * The `address` he wants to transfer to as the `_to` parameter
        * The `_tokenId` of the token he wants to transfer
* *Option 2*. The owner or the approved receiver of the token calls it

    ```js
    function approve(address _approved, uint256 _tokenId) external payable;

    function transferFrom(address _from, address _to, uint256 _tokenId) external payable;
    ```

    1. Token's owner first calls `approve` with the `address` he wants to transfer to, and the `_tokenID`    
        
        $\to$ The contract then stores who is approved to take a token, usually in a `mapping (uint256 => address)`
    2. When the owner or the approved address calls `transferFrom`
    3. The contract checks if that `msg.sender` is the owner or is approved by the owner to take the token
        
        $\to$ If so it transfers the token to him

**Extra features**. There are extra features we may want to add to our implementation
* Some extra checks to make sure users don't accidentally transfer their zombies to address `0`, "burning" a token
    
    $\to$ Basically it is sent to an address that no one has the private key of, essentially making it unrecoverable
* Put some basic auction logic in the DApp itself

## Preventing overflows
**Contract security enhancement - Overflows and underflows**. A major security feature you should be aware of when writing smart contracts
* *Overflow*. When the number value exceeds the maximum value in the representation range of its data type
* *Underflow*. When the number value is lower than the minimum value in the representation range of its data type
* *Effects of overflow and underflow*. Cause unexpected behavior in DApp

**`SafeMath`**. A library created by OpenZeppelin to prevent these issues by default
* *Library*. A special type of contract in Solidity
    * *Usage*. Attach functions to native data types
    * *Example*.
        
        ```js
        using SafeMath for uint256;

        uint256 a = 5;
        uint256 b = a.add(3); // 5 + 3 = 8
        uint256 c = a.mul(2); // 5 * 2 = 10
        ```

* *`SafeMath` library*. Have 4 functions, i.e. `add`, `sub`, `mul`, and `div`, which we can access from `uint256` as given above

**Writing a library**.
* *`library` keyword*. Libraries are similar to `contract`s but with a few differences
    * *Example*. Libraries allow us to use the `using` keyword, which automatically tacks on all of the library's methods to another data type, e.g.

        ```js
        using SafeMath for uint;
        // now we can use these methods on any uint
        uint test = 2;
        test = test.mul(3); // test now equals 6
        test = test.add(5); // test now equals 11
        ```

        * *Explain*. The `mul` and `add` functions (below) require 2 arguments, but when we declare `using SafeMath for uint`
            
            $\to$ The uint we call the function on, i.e. `test`, is automatically passed in as the first argument
* *Example*.

    ```js
    library SafeMath {

        function mul(uint256 a, uint256 b) internal pure returns (uint256) {
            if (a == 0) {
            return 0;
            }
            uint256 c = a * b;
            assert(c / a == b);
            return c;
        }

        function div(uint256 a, uint256 b) internal pure returns (uint256) {
            // assert(b > 0); // Solidity automatically throws when dividing by 0
            uint256 c = a / b;
            // assert(a == b * c + a % b); // There is no case in which this doesn't hold
            return c;
        }

        function sub(uint256 a, uint256 b) internal pure returns (uint256) {
            assert(b <= a);
            return a - b;
        }

        function add(uint256 a, uint256 b) internal pure returns (uint256) {
            uint256 c = a + b;
            assert(c >= a);
            return c;
        }
    }
    ```

# Appendix
## Concepts
**Usage of constructor in Solidity**. https://www.geeksforgeeks.org/solidity-constructors/

**Calling a contract in another contract**. https://www.zupzup.org/smart-contract-interaction/#:~:text=A%20deployed%20contract%20always%20resides,storage)%20of%20the%20calling%20contract.