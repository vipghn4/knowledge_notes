<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Advanced Solidity](#advanced-solidity)
  - [Immutability of contracts](#immutability-of-contracts)
  - [Ownable contracts](#ownable-contracts)
  - [Function modifier](#function-modifier)
  - [Struct packing to save gas](#struct-packing-to-save-gas)
  - [Storage is expensive](#storage-is-expensive)
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