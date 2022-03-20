<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Marketplace](#marketplace)
  - [Non-fungible token (NFT)](#non-fungible-token-nft)
    - [Hitory](#hitory)
    - [Making a token non-fungible](#making-a-token-non-fungible)
    - [Usage of NFTs](#usage-of-nfts)
  - [Content addressing](#content-addressing)
    - [Basic problem](#basic-problem)
    - [A stronger link](#a-stronger-link)
    - [Using content addressing](#using-content-addressing)
  - [Content persistence](#content-persistence)
    - [Content persistence](#content-persistence-1)
    - [Filecoin for content persistence](#filecoin-for-content-persistence)
    - [How NFTs benefit](#how-nfts-benefit)
  - [Lazy minting](#lazy-minting)
    - [How it works](#how-it-works)
- [Appendix](#appendix)
  - [Concepts](#concepts)
<!-- /TOC -->

# Marketplace
## Non-fungible token (NFT)
### Hitory
**Bitcoin and fungible token**. The most famous blockchain
* *Idea*. Introduced a "chain of blocks" to track and secure the history of the system over time
* *Bitcoin Token*. The Bitcoin network has a single token, i.e. Bitcoin
* *Fungible token*. Bitcoin is fungible, i.e. we can replace one Bitcoin with another Bitcoin without changing the value of either
    
    $\to$ There is nothing called "a single Bitcoin" with its own identity
    * *Bitcoin tracking*. The Bitcoin network does not track coins individually and assigns them each an identifier
        
        $\to$ The system keeps track of the quantity in each account, crediting one account and debiting another with each transaction
* *Impact of Bitcoin*. Bitcoin inspired a host of other blockchains that iterated on the same basic idea and introduced new capabilities

**ETH and NFT**. The most significant for NFTs was Ethereum, where the concept of NFTs was first developed
* *Idea*. Ethereum added general-purpose computation to the blockchain consensus model pioneered by Bitcoin
    
    $\to$ ETH positions itself as a "world computer" enabling "programmable money"
* *Etherum token*. Ethereum has a native token, i.e. Ether
    * *Usage*. Used as both a store of value, and to pay for computation fees, ie. gas
    * *Fungibility*. Ether is fungible
* *Custom tokens*. The smart contract computation model allows developers to create their own tokens, which can have special properties according to the logic in the contract
* *NFT*. Tokens used to contain data, hence each token unique and distinguishable from the rest
    
    $\to$ A token cannot easily be exchanged with another arbitrary token of the same type, i.e. a non-fungible token

### Making a token non-fungible
**Uniqueness**. A unique identifier alone is not enough to make a token non-fungible
* *Example*. Consider serial numbers as a way to distinguish one dollar bill from another
    
    $\to$ We can tell them apart, two dollar bills are still fungible because they each have the same value as currency

**NFT for artworks**. By allowing each token to contain a small amount of data

$\to$ NFTs become a medium for creative expression, and a unit of exchange and account
* *Value of an NFT*. Highly dependent on the data it contains and represents
    * *Example*. The same NFT may be valued completely differently by different people, based on factors like aesthetic taste or the identity of the creator

**NFT and fungible tokens**.
* *NFT without fungibility*. An NFT is not much good as currency
* *NFT with fungibility*. By existing on the same networks enabling digital currency
    
    $\to$ NFTs can leverage the payment and account infrastructure for transactions and benefit from the security guarantees of the blockchain

### Usage of NFTs
**Digital collectibles**. CryptoPunks is one of the earliest NFT experiments, which is a set of 10,000 pixel art characters, which can be collected and traded on Ethereum
* *NFT owner*. Each character can only have one official owner on the Ethereum blockchain at a given time
* *Digital collectibles*. One of the most popular and compelling use cases for NFTs
* *Subsequent development* NFTs have become a vehicle for all kinds of creative projects

**Gaming**. NFTs can represent plots of virtual land, avatars and skins for game characters, in-game items, etc. 
* *Benefits*. By putting a player's "inventory" of these items on a shared blockchain
    
    $\to$ NFT-powered games can enable new mechanics and allow players to use their custom items across multiple potential games and experiences
* *NFT trading*. Players can buy, sell, and trade items among themselves without locking their purchases into a company's storefront or marketplace

## Content addressing
**Content addressing**. A technique for organizing and locating data in an information system
* *Idea*. The key used to locate content is derived from the content itself

### Basic problem
**Basic key-value store**.
* *Idea*.
    * *Insertion*. We can associate any value with a key
    * *Retrieval*. When we need the value
        
        $\to$ we can look up the key and hopefully get our value
* *Deciding which keys to use*. One of the most important decisions is what to use for the keys
    * *Case 1*. If we are building an application, where we control the access patterns
        * *Option 1*. Use any keys and keep track of them in our code
        * *Option 2*. Use each type of keys for each kind of data
    * *Case 2*. When many uncoordinated parties are writing to the store concurrently
        * *Option 1*. Everybody needs to agree on the same rules
        * *Option 2*. The space needs to be split into many domains or namespaces

**Using domains in the key space**. Consder when each user has its own domain in the key space
* *Pros*. Users can manage their keys without others' interference
* *Cons*. It is less clear where to look for the desired data
    * *Explain*. 
        * Each domain following its own rules
            
            $\to$ It is hard to know what key to use to retrieve things
        * Without coordination between different domains
            * The same value may be stored multiple times in different domains
            * It is hard to tell that many keys are referencing the same value

**DNS-based approach for key lookup**. 
* *Idea*. Use the idea of DNS, i.e. consider looking up for a desired value with a key
    1. Our system queries a global shared key-value store, which is split into many domains, i.e. the DNS
    2. The DNS returns an IP address used to send HTTP requests over the network
    3. Our system queries the returned IP address
        
        $\to$ The naming conventions at the address turn our key into a response payload
* *Drawback*. The keys at the store are mutable, i.e. they can change over time
    
    $\to$ The web never ensures permanence, either in content or in the "meta-structure" of links between content
    * *Consequence*. The mutability of keys result in link rot
* *Link rot and NFT*. A digital artifact, e.g. an NFT, which is permanent, link rot is an existential concern, i.e.
    * *NFT storage*. Data storage on most blockchain networks is much more expensive than traditional online storage systems, i.e.
        
        $\to$ The artwork must be stored "off-chain", where storage costs are manageable, limiting "on-chain" storage to minimal
    * *Naive solution*. Store only the link to the off-chain data inside the NFT itself
        
        $\to$ The permanence of the blockchain only applies to on-chain data

### A stronger link
**Brief**. To safely link from an NFT to off-chain assets like images and metadata

$\to$ We need (almost) permanent links
* *Ideal link*. 
    * The link always resolve to the same piece of content, which was originally referenced in the permanent blockchain record
    * The link would not be tied to a single server owner or "domain"

**Content addressing**. An ideal solution for linking problem
* *Content-addressed system*. Work like a key-value store, without the needs of choosing keys
    * *Idea*. The keys are derived directly from the corresponding values, using a deterministic function, which always generates the same key for the same content
* *Value retrieval*. Instead of accepting a key and a value, the `put` method takes only the value and returns the key to the caller
    * *Benefits*.
        * We do not have to coordinate multiple writers to our store by splitting the key space into domains
            
            $\to$ There is one universal domain, i.e. the domain of all possible values
        *  Our values become location-independent
* *Location dependence of traditional key-value store with multiple domains*. 
    * We have to include the domain inside the key to prevent name collisions
    * To retrieve a value, the corresponding domain and the specific location within the domain's keys must be known
    * If we store a location-based key on the blockchain
        
        $\to$ Our ability to retrieve the data depends on the one domain containing our key
        * *Explain*. Even if the same content is replicated other domains
            
            $\to$ Our lookup will fail if the domain we depend on disappears or changes its naming conventions
* *Concurrent writes*. If multiple people add the same value
    
    $\to$ There is no collision in the key space, and they will each get the same key back from the `put` method
    * *Cons*. We cannot choose your own keys

### Using content addressing
**Simple approach**. Use the InterPlanetary File System (IPFS)
* *NFT storage and retrieval*. When your data is stored on IPFS
    
    $\to$ Users can fetch it from any IPFS node having a copy
    * *Consequence*. 
        * Data transfers is more efficient
        * The load is balanced across multiple servers
    * *P2P storage*. As each user fetches a piece of data
        
        $\to$ They keep a local copy around to help other users, who may request it later

## Content persistence
**Location addressing**. Building block for web browsing operations
* *Idea*. Retrieve online information from specific locations on the web, i.e. from URLs
* *Drawbacks*. 
    * Location addressing is centralized, i.e. whoever controls the location controls the content
    * Anything behind a location-addressed URL can be changed, i.e. location-addressed URLs are exploitable

**Content addressing**. Allow us to access data based on a unique fingerprint, i.e. a hash, of the data

$\to$ We should be able to retrieve the content independent of the location
* *Data replication*. If we use content-addressed storage
    * Pieces of content can be located on many nodes
    * Content can be retrieved either entirely from one node, or assembled in bits and pieces from multiple nodes
* *Drawback*. Content addressing does not guarantee data permanance
    
    $\to$ To have a complete solution, content persistence is key
    * *Explain*. Content addressing only guarantee that there is no link rot

### Content persistence
**Problem of interest**. Ensure that content persists
* *Explain*. Without content that is reliably stored over time, even a content-addressed web suffers similar dangers to today
    
    $\to$ Unless content persists, we run the risk of a fragmented, incomplete, and amnesic web

**Solutions for content persistence**.
* *Centralized solution*. Use a service, which promises to always store the content on their servers
    * *Drawback*. Centralized storage does not achieve true persistence
        * *Explain*. It is subject to a single centralized point of failure
* *Decentralized solution*. The only way to ensure that content remains persistent
    * *Idea*. Use completely separate, interoperable nodes to store data, which is backed by strong cryptographic guarantees
        
        $\to$ This protects information from becoming unavailable due to the action, or inaction, of any centralized service

### Filecoin for content persistence
**Brief**. Using Filecoin with IPFS provides a complete solution by combining an incentivization layer for content persistence with IPFS' solution to content addressing
* *Explain*.
    * IPFS ensures that content cannot change over time without a clear audit trail
        
        $\to$ This solves the issue of URLs not resolving
    * Filecoin ensures that the content-based addressing provided by IPFS permanent

**Filecoin**. 
* *Idea*. Use a novel cryptography, consensus protocols, and game-theoretic incentives
    * *Explain*. True decentralized storage for data stored on the Filecoin network
* *Problem for decentralized storage*. 
    * How can storage providers prove that they are really storing the data they say they are through time
    * How can storage providers prove that they are dedicating unique physical space to it
* *Solution of centralized storage*. Users place their trust in well-known companies
    
    $\to$ These companies should guarantee system integrity and security

**Filecoin proof system**. Anyone in the world can offer storage space
* *Idea*. To maintain trust on a decentralized network like Filecoin
    
    $\to$ We need to establish trust in Filecoin
* *Requirements of storage offer*. Anyone who wants to offer verified storage on Filecoin's decentralized network needs to prove the followings
    * The right set of data is stored in a given storage space
    * The same set of data has been stored continuously over a given period of time
* *Filecoin's proving algorithms*. 
    * *Proof-of-Replication*. Prove that a given storage provider is storing a physically unique copy of a client's original data
    * *Proof-of-Spacetime*. Proves that the client's data is stored continuously over time
* *Reference*. https://filecoin.io/blog/posts/what-sets-us-apart-filecoin-s-proof-system/

**Malicious or negligent activity prevention**. Filecoin network relies on game-theoretic incentives to discourage malicious or negligent activity
* *Idea*. All Filecoin storage providers must provide collateral, i.e. Filecoin tokens (FIL), at the time of agreeing to become providers
    
    $\to$ Any storage provider that fails Proof-of-Spacetime checks is penalized, loses a portion of their collateral
    * *Consequence*. The provider is eventually prevented from offering storage to clients again

### How NFTs benefit
**Key problem of NFTs**. Availability and permanence

**NFT minting or trading**. "Minting an NFT" or "trading an NFT" does not refer to the creative work itself

$\to$ These terms refer to the record of the work
* *Explain*. The terms refer to not the content, e.g. the colors, shapes, or sounds, but the metadata, e.g. descriptive text, artist information, or a pointer to the location of the content
* *Problem*. Neither that content nor that data automatically live on the blockchain
    
    $\to$ This exposes many NFTs to issues of addressing availability and persistence if their content and metadata are not stored reliably
* *Consequence*. Using IPFS to solve the addressing problem of NFTs is common

## Lazy minting
**NFT minting costs**. Minting an NFT on a blockchain mainnet costs some gas for the computation and storage

$\to$ This can be a barrier for NFT creators
* *Explain*. NFT creators may not want to invest a lot of money before knowing whether their work will sell
* *Solution*. Defer the NFT minting cost until it is sold to the first buyer
    * *Explain*. 
        * The gas fees for minting are rolled into the same transaction assigning the NFT to the buyer
            
            $\to$ The NFT creator never has to pay to mint
        * A portion of the purchase price will cover the additional gas needed to create the initial NFT record

**Lazy minting**. Minting "just in time", at the moment of purchase
* *Usage*. This has been adopted by marketplaces, e.g. OpenSea, to lower the barrier to entry for NFT creators
    * *Explain*. Allow users to create NFTs without any up-front costs

### How it works
**Brief procedure**.
* *NFT listing*. Instead of creating an NFT directly by calling a contract function 
    
    $\to$ the NFT creator prepares a cryptographic signature of some data using their Ethereum account's private key
    * *NFT voucher*. The signed data acts as a "voucher" or ticket, which can be redeemed for an NFT
        * *Voucher content*.
            * Contain all the information, which will go into the actual NFT
            * Optionally contain additional data, which is not recorded in the blockchain
        * *Proof of NFT authorization*. The signature proves that the NFT creator authorized the creation of the specific NFT described in the voucher
* *NFT purchase*. When a buyer wants to purchase the NFT
    1. They call a `redeem` function to redeem the signed voucher
    2. If the signature is valid and belongs to an account authorized to mint NFTs
        
        $\to$ A new token is created based on the voucher and transfered to the buyer
* *Reference*. https://www.linkedin.com/pulse/everything-you-never-needed-know-lazy-minting-nfts-tucker-higgins/

**NFT voucher information**.

```cpp
struct NFTVoucher {
    uint256 tokenId;
    uint256 minPrice; // Used in ``redeem`` function
    string uri; // URI for the token's metadata
    bytes signature; // A signature prepared by the NFT creator
}
```

* *On-chain components*. The unique tokenId, and the uri for the token's metadata
* *`minPrice`*. Not recorded, but used in `redeem` function to allow the creator to set a purchase price
    
    $\to$ If the minPrice is greater than zero, the buyer will need to send at least that much Ether when they call `redeem`
* *Signature*. A signature prepared by the NFT creator

**Purchase price**. Setting a purchase price inside the voucher is not always necessary

$\to$ We will probably need some kind of condition
* *Explain*. Otherwise, anyone who has the voucher could claim the NFT for just the gas cost

# Appendix
## Concepts
**Cryptocurrency burning**. The process, in which users can remove tokens, i.e. coins, from circulation

$\to$ The number of coins in use is reduced
* *Implementation*. The tokens are sent to a wallet address, which cannot be used for transactions other than receiving the coins
    * *Explain*. The wallet is outside the network, and the tokens can no longer be used
    * *Example*. Transfer the tokens to address `0`

**Token swap**. Have two definitions within the crypto sphere
* *Definition 1*. The process of instantaneously exchanging one cryptocurrency to another, without having to first undertake a crypto-to-fiat exchange
* *Definition 2*. The migration of projects or platforms from one blockchain to another, with some the coin swapping requirements
    * *Explain*. A project has for one reason or the other chosen to switch its operation base to another blockchain with unique token standards

        $\to$ The development team must provide the means for investors and users to swap the project’s native token to another token compatible with the new blockchain network
    * *Conclusion*. The process involved is what called token swapping or token migration

**Link rot**. The phenomenon of hyperlinks tending over time to cease to point to their originally targeted file, web page, or server due to that resource being relocated to a new address or becoming permanently unavailable

**The InterPlanetary File System (IPFS)**. A protocol and P2P network for storing and sharing data in a distributed file system
* *Addressing mechanism*. Content-addressing is used to uniquely identify each file in a global namespace connecting all computing device