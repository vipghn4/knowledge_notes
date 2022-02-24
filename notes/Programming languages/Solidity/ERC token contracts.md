<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [ERC token contracts](#erc-token-contracts)
  - [Tokens](#tokens)
  - [ERC20](#erc20)
  - [ERC721](#erc721)
  - [ERC777](#erc777)
  - [ERC1155](#erc1155)
    - [Multi-token standard](#multi-token-standard)
    - [Batch operations](#batch-operations)
- [Appendix](#appendix)
  - [Discussion](#discussion)
<!-- /TOC -->

# ERC token contracts
## Tokens
**Token**. A representation of something in the blockchain, e.g. money, time, services, shares in a company, a virtual pet, etc.
* *Purposes*. By representing things as tokens
    
    $\to$ We can allow smart contracts to interact with them, exchange them, create or destroy them

**Token contracts and tokens**.
* *Token contract*. An Ethereum smart contract
    *"Sending tokens"*. Calling a method on a smart contract that someone wrote and deployed
    * *Conclusion*. A token contract is not much more a mapping of addresses to balances, plus some methods to add and subtract from those balances
* *Token*. The balances of the addresses
    * *"Has tokens"*. Someone has tokens when their balance in the token contract is nonzero
        * *Examples*. Money, experience points in a game, deeds of ownership, or voting rights
    * *Token storage*. Each of the tokens would be stored in different token contracts

**Types of token**.
* *Fungibility*. There is a big difference between having two voting rights and two deeds of ownership, i.e.
    * *Voting rights*. Each vote is equal to all others
    * *Deeds ownership*. Houses usually are equal to all others
* *Fungible goods*. Equivalent and interchangeable, e.g. Ether, fiat currencies, and voting rights
* *Non-fungible goods*. Unique and distinct, e.g. deeds of ownership, or collectibles
* *Conclusion*. 
    * When dealing with non-fungibles, we care about which ones we have
    * When dealin with fungible assets, what matters is how much we have

**Standards**. Everything in Ethereum is just a smart contract, and there are no rules about what smart contracts have to do

$\to$ The community has developed a variety of standards for how a contract can interoperate with other contracts
* *ERC20*. The most widespread token standard for fungible assets, albeit somewhat limited by its simplicity
* *ERC721*. The de-facto solution for non-fungible tokens, often used for collectibles and games
* *ERC777*. A richer standard for fungible tokens, enabling new use cases and building on past learnings
    
    >**NOTE**. This is backwards compatible with ERC20

* *ERC1155*. A novel standard for multi-tokens, allowing for a single contract to represent multiple fungible and non-fungible tokens, along with batched operations for increased gas efficiency

## ERC20
**ERC20 token contract**. Keep track of fungible tokens
* *Characteristics*. 
    * Any one token is exactly equal to any other token
    * No tokens have special rights or behavior associated with them
* *Usage*. Useful for things like a medium of exchange currency, voting rights, staking, etc.

## ERC721
**ERC-721**. A Non-Fungible Token Standard implementing an API for tokens within Smart Contracts
* *Basic functionalities*.
    * Transfer tokens from one account to another
    * Get the current token balance of an account
    * Get the owner of a specific token
    * Get the total supply of the token available on the network
    * Approve that an amount of token from an account can be moved by a third party account
* *Required methods*.

    ```js
    function balanceOf(address _owner) external view returns (uint256);
    function ownerOf(uint256 _tokenId) external view returns (address);
    function safeTransferFrom(address _from, address _to, uint256 _tokenId, bytes data) external payable;
    function safeTransferFrom(address _from, address _to, uint256 _tokenId) external payable;
    function transferFrom(address _from, address _to, uint256 _tokenId) external payable;
    function approve(address _approved, uint256 _tokenId) external payable;
    function setApprovalForAll(address _operator, bool _approved) external;
    function getApproved(uint256 _tokenId) external view returns (address);
    function isApprovedForAll(address _owner, address _operator) external view returns (bool);
    ```

* *Required events*.

    ```js
    event Transfer(address indexed _from, address indexed _to, uint256 indexed _tokenId);
    event Approval(address indexed _owner, address indexed _approved, uint256 indexed _tokenId);
    event ApprovalForAll(address indexed _owner, address indexed _operator, bool _approved);
    ```

## ERC777
**ERC777**. A standard for fungible tokens, and is focused around allowing more complex interactions when trading tokens
* *Key features*.
    * Bring tokens and Ether closer together by providing the equivalent of a `msg.value` field, but for tokens
    * Get rid of the confusion around `decimals`, minting and burning with proper events, among others
* *Receive hook*. A killer feature of ERC777
    * *Hook*. A function in a contract, which is called when tokens are sent to it
        
        $\to$ Accounts and contracts can react to receiving tokens
    * *Usage*. Enable a lot of interesting use cases, including
        * Atomic purchases using tokens, i.e. no need to do `approve` and `transferFrom` in two separate transactions
        * Reject reception of tokens by reverting on the hook call
        * Redirect the received tokens to other addresses
        * Other use cases
* *Stuck tokens in contract*. Since contracts are required to implement these hooks to receive tokens
    
    $\to$ No tokens can get stuck in a contract that is unaware of the ERC777 protocol, as has happened countless times when using ERC20s
    * *Explain*. 
        * Somebody sent tokens to a smart contract that was not intended to receive tokens
            
            $\to$ We need to find out if a contract actually supports being the receiver or owner of some interface/token
        * We can send tokens to any smart contract, but they will mostly just be locked and not usable
            * *Explain*. A smart contract, in contrast to an EOA, is not able to do arbitrary calls to other smart contracts
                
                $\to$ It only supports the functionality that actually has been implemented
    * *Consequence*. This has resulted in a lot of tokens being lost

**Backward compatibility with ERC20**. ERC777 standard is backwards compatible with ERC20

$\to$ We can interact with these tokens as if they were ERC20, using the standard functions, while still getting all of the niceties, including send hooks

## ERC1155
**ERC1155**. A novel token standard aiming to take the best from previous standards to create a fungibility-agnostic and gas-efficient token contract

### Multi-token standard
**Multi-token standard**. ERC1155 uses a smart contract to represent multiple tokens at once
* *`balanceOf` function*. Have `id` argument for the identifier of the token that we want to query the balance of
    * *Difference from ERC721*. In ERC721, a token id has no concept of balance, i.e. each token is non-fungible and exists or does not
        * *`ERC721`'s `balanceOf` function*. Refer to how many different tokens an account has, not how many of each
* *Consequence*. Massive gas savings for projects requiring multiple tokens
    * *Explain*. Instead of deploying a new contract for each token type
        
        $\to$ Single ERC1155 token contract can hold the entire system state, reducing deployment costs and complexity

### Batch operations
**Batch operations**. Because all state is held in a single contract

$\to$ It is possible to operate over multiple tokens in a single transaction very efficiently
* *Explain*. ERC1155 provides two functions, `balanceOfBatch` and `safeBatchTransferFrom`, making querying multiple balances and transferring multiple tokens simpler and less gas-intensive

# Appendix
## Discussion
**Confusion around ERC20 decimals**. When it comes to decimals with the ERC20 contract, there tends to be a lot of confusion
* *`decimals`*. Determine how divisible a token can be
* *Key problem*. Developers must decide in advance how many decimals they want their ERC20 tokens to have
    
    $\to$ It is important to consider the tokens’ use case. 
* *Rule of thumb*. Choosing the number of decimals is easy to determine when considering the unit of the token’s value
    * *Explain*. The higher the value of the unit, the larger the number of `decimals`