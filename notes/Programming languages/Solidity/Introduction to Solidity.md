<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction to Solidity](#introduction-to-solidity)
  - [Basic syntax](#basic-syntax)
  - [Contract](#contract)
    - [Data types](#data-types)
    - [Data location](#data-location)
    - [Function](#function)
      - [Function visibility](#function-visibility)
      - [Exceptions and assertion](#exceptions-and-assertion)
  - [Event](#event)
  - [Global built-in objects](#global-built-in-objects)
  - [Import files and packages](#import-files-and-packages)
  - [Interacting with other contracts](#interacting-with-other-contracts)
- [Appendix](#appendix)
  - [Concepts](#concepts)
  - [Discussions](#discussions)
<!-- /TOC -->

# Introduction to Solidity
## Basic syntax
**`if...else` statement**. The same as C/C++

**`for` loop**. The same as C/C++

**Comment**. The same as C / C++
* *Standard comment format in Solidity*. `natspec`.

## Contract
**Contract**. Solidity's code is encapsulated in contracts, which is the fundamental building block of Ethereum applications

$\to$ All variables and functions belong to a contract
* *Version pragma*. All solidity source code should start with a "version pragma", i.e. a declaration of the version of the Solidity compiler this code should use
    * *Usage*. Prevent issues with future compiler versions potentially introducing changes that would break the code
    * *Example*.

        ```js
        pragma solidity >=0.5.0 <0.6.0;

        contract HelloWorld {

        }
        ```

* *State variables*. Permanently stored in contract storage, i.e. they are written to the Etherum blockchain

    $\to$ We can think of them as writing to a DB
    * *Example*.

        ```js
        pragma solidity >=0.5.0 <0.6.0;

        contract HelloWorld {
            uint myUnsignedInteger = 100;
        }
        ```

**Inheritance**.
* *Example*. If we compile this program and deploy `BabyDoge`, it will have access to both `catchphrase()` and `anotherCatchphrase()`

    ```js
    contract Doge {
        function catchphrase() public returns (string memory) {
            return "So Wow CryptoDoge";
        }
    }

    contract BabyDoge is Doge {
        function anotherCatchphrase() public returns (string memory) {
            return "Such Moon BabyDoge";
        }
    }
    ```

* *Multi-inheritance*.

    ```js
    contract SatoshiNakamoto is NickSzabo, HalFinney {
        // Omg, the secrets of the universe revealed!
    }
    ```

* *Virtual functions*. A function that allows an inheriting contract to override its behavior will be marked at `virtual`

### Data types
**Basic data types**.
* *Boolean*. `bool`
    * *Values*. `true` and `false`
    * *Operators*. `!`, `&&`, `\|\|`, `==`, `!=`
* *Integers*. `int`, `uint`
    * *Variations*. `uint8` to `uint256` in steps of `8`, and `int8` to `int256` in steps of `8`
    * *Operators*.
        * *Comparisons*. `<=`, `<`, `==`, `!=`, `>=`, `>`
        * *Bit operators*. `&`, `|`, `^`, `~`
        * *Shift operators*. `<<`, `>>`
        * *Arithmetic operators*. Like Python
            * *Division*. Since the type of the result of an operation is always the type of one of the operands
            
                $\to$ In Solidity, division rounds towards zero
    * *Maximum and minimum values of type*. Given an integer `x`, then use `type(x).min` and `type(x).max`
* *Fixed point numbers*. `fix`, `ufixed`, i.e. signed and unsigned fixed point number of various sizes
    * *Keywords*. `ufixedMxN` and `fixedMxN`
        * `M` represents the number of bits taken by the type
            * *Requirement*. `M` must be divisible by `8`, and goes from `8` to `256` bits
        * `N` represents how many decimal points are available
            * *Requirement*. `N` must be between `0` and `80`
    * *Operators*.
        * *Comparisons*. `<=`, `<`, `==`, `!=`, `>=`, `>`
        * *Arithmetic operators*. Like `int` and `uint`
* *String*. `string`
* *Type cast*. `type_name(var_name)`, e.g. `int256(x)`

**String literals and types**.
* *String literals*. 
    * *Types of string literals expressions*.
        * *Single-quote literals*. String literals are written with either double or single-quotes (`"foo"` or `'bar'`)
        * *Multi-quote literals*. Strings can also be split into multiple consecutive parts (`"foo" "bar"` is equivalent to `"foobar"`) which can be helpful when dealing with long strings
    * *Trailing zeros*. String literals do not imply trailing zeroes as in C, i.e. `"foo"` represents three bytes, not four
    * *String literal interpretation*. As with integer literals, their type can vary, but they are implicitly convertible to `bytes1`, …, `bytes32`, if they fit, to `bytes` and to `string`
        * *Examples*. Consider the expression `bytes32 samevar = "stringliteral"`

            $\to$ The string literal is interpreted in its raw byte form when assigned to a `byte332` type
* *Types of string literals*.
    * *Regular literals*. Can only contain ASCII
    * *Unicode literals*. Prefixed with the keyword `unicode`, and can contain any valid UTF-8 sequence

        ```js
        string memory a = unicode"Hello :)";
        ```
    
    * *Hexadecimal literals*. Prefixed with the keyword `hex` and are enclosed in double or single-quotes, e.g. `hex"001122FF"`, `hex'0011_22_FF'`
        * *Literal content*. Must be hexadecimal digits which can optionally use a single underscore as separator between byte boundaries
        * *Literal value*. The binary representation of the hexadecimal sequence

**Address**.
* *Accounts*. The Ethereum blockchain is made up of accounts, which has a balance of Ether
    
    $\to$ We can send and receive Ether payments to other accounts
    * *Address*. Each account has an address, which is a unique identifier that points to that account, e.g. `0x0cE446255506E92DF41614C46F1d6df9Cc969183`
        * *Address owner*. A specific user, i.e. external account, or a smart contract, i.e. contract account
* *Types of addresses*. `address payable` is an address you can send Ether to, while a plain `address` cannot be sent Ether
    * *`address`*. Hold a 20-byte value, i.e. size of an Etherum address
    * *`address payable`*. Same as `address`, but with additional members `transfer` and `send`
* *Type conversion*.
    * *Implicit conversion*. Implicit conversions from `address payable` to `address` are allowed, whereas conversions from `address` to `address payable` must be explicit via `payable(<address>)`
    * *Explicit conversion*. Explicit conversions to and from `address` are allowed for `uint160`, integer literals, `bytes20` and contract types
        * *Conversion to `address payable`*. Only expressions of type `address` and contract-type can be converted to the type `address payable` via the explicit conversion `payable(...)`
            
            >**NOTE**. For contract-type, this conversion is only allowed if the contract can receive Ether, i.e., the contract either has a receive or a payable fallback function
            
            >**NOTE**. `payable(0)` is valid and is an exception to this rule
        
        >**NOTE**. If you need a variable of type address and plan to send Ether to it, then declare its type as address payable to make this requirement visible
        >$\to$ Also, try to make this distinction or conversion as early as possible

        * *Address truncation*. If you convert a type that uses a larger byte size to an `address`, e.g. `bytes32`, then the `address` is truncated
            * *Explicit truncation*. To reduce conversion ambiguity version `0.4.24` and higher of the compiler force you make the truncation explicit in the conversion
                * *Example*. Consider the 32-byte value `0x111122223333444455556666777788889999AAAABBBBCCCCDDDDEEEEFFFFCCCC`
                    * Using `address(uint160(bytes20(b)))` results in `0x111122223333444455556666777788889999aAaa`
                    * Using `address(uint160(uint256(b)))` results in `0x777788889999AaAAbBbbCcccddDdeeeEfFFfCcCc`
* *Operators*. `<=`, `<`, `==`, `!=`, `>=`, `>`

**Structs**. Solidity provides `struct` for more complex data type
* *Example code*.

    ```hs
    struct Person {
        uint age;
        string name;
    }
    ```

* *Objecg creation*. `Person satoshi = Persion(172, "Satoshi")`

**Mappings**. Another way of storing organized data in Solidity, i.e. a key-value store for storing and looking up data

```js
// For a financial app, storing a uint that holds the user's account balance:
mapping (address => uint) public accountBalance;
// Or could be used to store / lookup usernames based on userId
mapping (uint => string) userIdToName;
```

**Array**.
* *Types of arrays*. Fixed arrays and dynamic arrays, e.g.
    * *Examples*.

        ```js
        uint[2] fixedArray;
        string[5] stringArray;
        uint[] dynamicArray;
        StructName[] structArray;
        ```
    
    >**NOTE**. State variables are stored permanently in the blockchain, hence creating a dynamic array of structs can be useful for storing structured data in your contract, kind of like a database

* *Public arrays*. You can declare an array as `public`, and Solidity will automatically create a getter method for it, e.g.

    ```js
    Person[] public people;
    ```

    $\to$ Other contracts would then be able to read from, but not write to, the object
    * *Usage*. Useful pattern for storing public data in a contract
* *Operations on arrays*.
    * *Append elements*. `uint new_arr_len = array_name.push(new_element)`
    * *Array declaration in memory*.

        ```js
        function getArray() external pure returns(uint[] memory) {
            // Instantiate a new array in memory with a length of 3
            uint[] memory values = new uint[](3);

            // Put some values to it
            values[0] = 1;
            values[1] = 2;
            values[2] = 3;

            return values;
        }
        ```

**Tuple**. Similar as Python
* *Function return tuples*.

    ```js
    function latestRoundData() external view returns (
      uint80 roundId,
      int256 answer,
      uint256 startedAt,
      uint256 updatedAt,
      uint80 answeredInRound
    );
    ```

* *Assign variables to each return variable*.

    ```js
    (uint80 roundId, int answer, uint startedAt, uint updatedAt, uint80 answeredInRound) = priceFeed.latestRoundData();
    ```

* *Assign variables with ignorance*.

    ```js
    (,int price,,,) = priceFeed.latestRoundData();
    ```

### Data location
**Storage and Memory variables**. Think of storage and memory variables like your computer's hard disk vs RAM
* *Storage variables*. Refer to variables stored permanently on the blockchain
* *Memory variables*. Temporary variables, which are erased between external function calls to your contract

>**NOTE**. The Solidity compiler will also give you warnings to let you know when you should be using one of these keywords

**Storage and Memory keywords in Solidity**. Analogous to Computer’s hard drive and Computer’s RAM
* *Memory and Storage*. Much like RAM, Memory in Solidity is a temporary place to store data, whereas Storage holds data between function calls
    * *Memory*. The Solidity Smart Contract can use any amount of memory during the execution but once the execution stops
        
        $\to$ The Memory is completely wiped off for the next execution
    * *Storage*. Storage is persistent, each execution of the Smart contract has access to the data previously stored on the storage area
* *Gas cost for storage*. Every transaction on Ethereum Virtual Machine costs us some amount of Gas
    
    $\to$ The lower the Gas consumption the better is your Solidity code
    * *Gas consumption of Memory and Storage*. Gas consumption of Memory is not very significant as compared to the gas consumption of Storage
    
        $\to$ Therefore, it is always better to use Memory for intermediate calculations and store the final result in Storage
* *Default rules*.
    * State variables, i.e. variables declared outside of functions, are `storage` and written permanently to the blockchain
    * Variables declared inside functions are `memory` and will disappear when the function call ends

**Assignment rules**.
* *Cross-data-location assignment*. When assigning a storage variable the value of a memory (or calldata) one, it will create a copy

    $\to$ The other way around is true as well
* *Value type assignment*. Assignments between value types from the same data location, e.g. storage to storage or memory to memory, will make a copy
* *Reference type assignment*. For reference types, 
    * When assigning from one memory variable to another memory variable, it will create a reference
        
        $\to$ They will point to the same data location, i.e. if you modify one of them, it will reflect in both
    * Assigning from storage to local storage variables will also result in a reference

### Function
**Function declarations**.
* *Example*.

    ```js
    function eatHamburgers(string memory _name, uint _amount) public { }
    ```

* *Function visibility*. By default, the visibility of a function is `public`
* *Function arguments*.
    * *Variable storage location*. Keyword `memory` indicates that `_name` should be stored in memory

        $\to$ This is required for all reference types, e.g. arrays, structs, mappings, and strings
        * *Reference type*. Used by a reference which holds a reference, i.e. address, to the object but not the object itself
            * *Consequence*. Assigning a reference variable to another doesn't copy the data
                
                $\to$ Instead it creates a second copy of the reference, which refers to the same location of the heap as the original value
    * *Reference type*.
        * *Pass by value*. The Solidity compiler creates a new copy of the parameter's value and passes it to your function

            $\to$ This allows your function to modify the value without worrying that the value of the initial parameter gets changed
        * *Pass by reference*. The function is called with a reference to the original variable

            $\to$ If your function changes the value of the variable it receives, the value of the original variable gets changed
    * *Naming convention*. It's convention, but not required, to start function parameter variable names with an underscore `_` to differentiate them from global variables
* *Return values*. In Solidity, the function declaration contains the type of the return value

    ```js
    string greeting = "What's up dog";

    function sayHello() public returns (string memory) {
        return greeting;
    }
    ```

* *Function invocation*. `eatHamburgers("vitalik", 100);`

**Struct arguments**. You can pass a storage pointer to a struct as an argument to a `private` or `internal` function

```js
function _doStuff(Zombie storage _zombie) internal {
    // do stuff with _zombie
}
```

**Multiple return values**.

```js
function multipleReturns() internal returns(uint a, uint b, uint c) {
    return (1, 2, 3);
}

function processMultipleReturns() external {
    uint a;
    uint b;
    uint c;
    // This is how you do multiple assignment:
    (a, b, c) = multipleReturns();
}

// Or if we only cared about one of the values:
function getLastReturnValue() external {
    uint c;
    // We can just leave the other fields blank:
    (,,c) = multipleReturns();
}
```

**View and pure functions**. 
* *View functions*. Functions which is only viewing the data without modifying it, e.g.

    ```js
    string greeting = "fuck";

    function sayHello() public view returns (string memory) {
        return greeting;
    }
    ```

* *Pure functions*. Functions which do not access any data in the app
    
    ```js
    function _multiply(uint a, uint b) private pure returns (uint) {
        return a * b;
    }
    ```

    * *Explain*. This function doesn't even read from the state of the app, i.e. its return value depends only on its function parameters

#### Function visibility
**Private and public functions**. In Solidity, functions are public by default, i.e. anyone, or any other contract, can call your contract's function and execute its code

$\to$ This can make your contract vulnerable to attacks
* *Private function*. It is good practice to mark your functions as `private` by default, and then only make public the functions you want to expose to the world

    ```js
    uint[] numbers;

    function _addToArray(uint _number) private {
    numbers.push(_number);
    }
    ```

    * *Explain*. This means only other functions within our contract will be able to call the private function
* *Naming convention*. It is convention to start private function names with an underscore `_`

**Internal and external**.
* *Internal*. The same as private, but it is also accessible to contracts inheriting from this contract, i.e. like `protected` in Java
* *External*. Similar to `public`, but these functions can only be called outside the contract, and cannot be called by other functions inside the contract

    ```js
    contract Sandwich {
        uint private sandwichesEaten = 0;

        function eat() internal {
            sandwichesEaten++;
        }
    }

    contract BLT is Sandwich {
        uint private baconSandwichesEaten = 0;

        function eatWithBacon() public returns (string memory) {
            baconSandwichesEaten++;
            // We can call this here because it's internal
            eat();
        }
    }
    ```

#### Exceptions and assertion
**Require**. We use `require`, which makes it so that the function will throw an error and stop executing if some condition is not true

$\to$ `require` is useful for verifying certain conditions that must be true before running a function
* *Example*.

    ```js
    function sayHiToVitalik(string memory _name) public returns (string memory) {
        require(keccak256(abi.encodePacked(_name)) == keccak256(abi.encodePacked("Vitalik")));
        return "Hi!";
    }
    ```

**Assertion**. `assert` is similar to `require`, where it will throw an error if false
* *Difference from `require`*. `require` will refund the user the rest of their gas when a function fails, whereas assert will not
    
    $\to$ Most of the time you want to use require in your code
* *Usage of `assert`*. Typically used when something has gone horribly wrong with the code, e.g. like a `uint` overflow
* *Example*.

    ```js
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        uint256 c = a + b;
        assert(c >= a);
        return c;
    }
    ```

## Event
**Events**. A way for your contract to communicate that something happened on the blockchain to your app front-end

$\to$ The app front-end can be "listening" for certain events and take action when they happen
* *Formal definition*. Event is an inheritable member of a contract
    * *Example*.

        ```js
        pragma solidity ^0.5.0;

        contract Test {
            event Deposit(address indexed _from, bytes32 indexed _id, uint _value);
            
            function deposit(bytes32 _id) public payable {      
                emit Deposit(msg.sender, _id, msg.value);
            }
        }
        ```
    
* *Event emission*. An event is emitted, it stores the arguments passed in transaction logs
    
    $\to$ These logs are stored on blockchain and are accessible using the address of the contract till the contract is present on the blockchain
    
    >**NOTE**. An event generated is not accessible from within contracts, not even the one which have created and emitted them

* *Event listening*. Your app front-end could then listen for the event
    * *JS implementation example*. The app front-end can access the contract's event in JavaScript code

                ```js
        var abi = /* abi as generated using compiler */;
        var ClientReceipt = web3.eth.contract(abi);
        var clientReceiptContract = ClientReceipt.at("0x1234...ab67" /* address */);

        var event = clientReceiptContract.Deposit(function(error, result) {
            if (!error)console.log(result);
        });
        ```

    * *Expected output*.

        ```json
        {
            "returnValues": {
                "_from": "0x1111...FFFFCCCC",
                "_id": "0x50...sd5adb20",
                "_value": "0x420042"
            },
            "raw": {
                "data": "0x7f...91385",
                "topics": ["0xfd4...b4ead7", "0x7f...1a91385"]
            }
        }
        ```

**Event arguments**.
* *String arguments*. Should be in storage, rather than in memory (WHY)

## Global built-in objects
**`msg.sender`**. Refer to the `address` of the person, or smart contract, who called the current function
* *`msg.sender` and function invocation*. In Solidity, function execution always needs to start with an external caller
    
    $\to$ A contract will just sit on the blockchain doing nothing until someone calls one of its functions
    * *Consequence*. There will always be a `msg.sender`
* *Purpose*. Using `msg.sender` gives you the security of the Ethereum blockchain
    * *Explain*. The only way someone can modify someone else's data would be to steal the private key associated with their Ethereum address

**`msg.value`**. Return how much Ether was sent to the contract
* *Built-in unit*. `ether`

**`now`**. Return the current UNIX timestamp of the latest block
* *UNIX time representation problem*. Unix time is traditionally stored in a 32-bit number, leading to the "Year 2038" problem
    * *"Year 2038" problem*. When 32-bit unix timestamps will overflow and break a lot of legacy systems
    * *Consequence*. If we wanted our DApp to keep running 20 years from now, we could use a 64-bit number instead
        
        $\to$ Our users would have to spend more gas to use our DApp in the meantime

**`block`**. Return the information about the current block as an object, i.e. refer to https://docs.soliditylang.org/en/latest/units-and-global-variables.html?highlight=block#block-and-transaction-properties
* *`block.timestamp`*. Current block timestamp as seconds since UNIX epoch (or UNIX time)

## Import files and packages
**`import`**. When you have multiple files and you want to import one file into another, Solidity uses the `import` keyword
* *Import local files*.

    ```js
    import "./someothercontract.sol";

    contract newContract is SomeOtherContract {}
    ```

* *Import remote files*. The below code import files from Github or NPM packages

    ```js
    // Start here
    import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

    contract PriceConsumerV3 {

    }
    ```

## Interacting with other contracts
**Interface**. For our contract to talk to another contract on the blockchain that we don't own, first we need to define an `interface`
* *Example*. Consider an external contract wanting to read the data in this contract using the `getNum` function of `LuckyNumber` contract below
    * *Main contract*.

        ```js
        contract LuckyNumber {
            mapping(address => uint) numbers;

            function setNum(uint _num) public {
                numbers[msg.sender] = _num;
            }

            function getNum(address _myAddress) public view returns (uint) {
                return numbers[_myAddress];
            }
        }
        ```

    * *Interface contract*. 

        ```js
        contract NumberInterface {
           function getNum(address _myAddress) public view returns (uint);
        }
        ```
    
    * *Using interface contract*.

        ```js
        contract MyContract {
            address NumberInterfaceAddress = 0xab38... 
            // ^ The address of the FavoriteNumber contract on Ethereum
            NumberInterface numberContract = NumberInterface(NumberInterfaceAddress);
            // Now `numberContract` is pointing to the other contract

            function someFunction() public {
                // Now we can call `getNum` from that contract:
                uint num = numberContract.getNum(msg.sender);
                // ...and do something with `num` here
            }
        }
        ```

* *Contract body*. This contract looks like a contract skeleton, i.e. this is how the compiler knows this contract is an interface
    * Only declares the functions we want to interact with, without mentioning any other functions or state variables
    * Do not define the function bodies
* *Interface exposure*. By including this interface in our dapp's code our contract knows what the other contract's functions look like, how to call them, and what sort of response to expect

**Interface address**.
* *Option 1*. Use the on-chain [Feeds Registry](https://docs.chain.link/docs/feed-registry/) which is an on-chain contract that keeps track of where all these feeds are
* *Option 2*. Choose a contract address of our choosing by browsing all the [contract addresses](https://docs.chain.link/docs/reference-contracts/)

>**NOTE**. Each network will have a different address for each piece of data you want

# Appendix
## Concepts
**Pragma**. A pragma is a compiler directive that allows you to provide additional information to the compiler

$\to$ This information can change compilation details that are not otherwise under your control

**Keccak256**. Ethereum has the hash function keccak256 built in, which is a version of SHA3
* *Hash function*. Basically maps an input into a random 256-bit hexadecimal number
    * *Characteristics*. A slight change in the input will cause a large change in the hash
* *Usage*. Many purposes in Etherum
* *Invocation*. `keccak256` expects a single parameter of type bytes, i.e. we have to "pack" any parameters before calling `keccak256`

    ```js
    keccak256(abi.encodePacked("aaaab"));
    ```

>**NOTE**. Secure random-number generation in blockchain is a very difficult problem and our method here is insecure

**Time units in Solidity**. `seconds`, `minutes`, `hours`, `days`, `weeks` and `years`

$\to$ These will convert to a `uint` of the number of seconds in that length of time
* *Example*. `1 minutes` is `60`, `1 hours` is `3600`, etc.

## Discussions
**Why reference type arguments must be `memory`**.

**Public functions and security**. An important security practice is to examine all your public and external functions, and try to think of ways users might abuse them
* *Explain*. Unless these functions have a modifier like onlyOwner, any user can call them and pass them any data they want to

**View functions do not cost gas**. `view` functions don't cost any gas when they're called externally by a user
* *Explain*. 
    * `view` functions don't actually change anything on the blockchain, i.e. they only read the data
    * A `view` function tells `web3.js` that it only needs to query your local Ethereum node to run the function
        
        $\to$ It doesn't actually have to create a transaction on the blockchain, which would need to be run on every single node, and cost gas
* *Consequence*. You can optimize your DApp's gas usage for your users by using read-only `external view` functions wherever possible
* *View functions invoked internally from another function in the same contract*. If a `view` function is called internally from another function in the same contract that is not a `view` function, it will still cost gas
    * *Explain*. The other function creates a transaction on Ethereum, and will still need to be verified from every node
        
        $\to$ `view` functions are only free when they're called externally