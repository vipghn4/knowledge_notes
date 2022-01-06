<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Hole punching](#hole-punching)
  - [NAT terminology](#nat-terminology)
  - [Hole punching](#hole-punching-1)
<!-- /TOC -->

# Hole punching
## NAT terminology
**Session**. A session endpoint for TCP or UDP is an (IP address, port number) pair, and a particular session is uniquely identified by its two session endpoints

$\to$ From the perspective of one of the hosts involved, a session is identified by a 4-tuple (local IP, local port, remote IP, remote port)
* *Session direction*. Normally the flow direction of the packet initiating the session, i.e.
    * *UDP case*. The first user datagram
    * *TCP case*. The initial `SYN` packet for TCP

**Traditional NAT (outbound NAT)**. Provide an asymmetric bridge between a private network and a public network
* *Idea*. Allow only outbound sessions to traverse the NAT
    
    $\to$ Incoming packets are dropped unless the NAT identifies them as being part of an existing session initated from within the private network
* *Problem with P2P*. Outbound NAT conflicts with P2P protocols, since both peers want to communicate are behind two different NATs
* *NAT traversal*. Entail making P2P sessions look like outbound sessions to both NATs
* *Types of NAT*.
    * *Basic NAT*. Only translate the IP addresses
    * *Network address/port translation (NAPT)*. Translate entire session endpoints

        $\to$ This is more common since it enables the hosts on a private network to share the use of a single public IP address

**Relaying**. The most reliable bust least efficient method of P2P communication across NAT
* *Idea*. Make the communication look to the network like standard client-server communication, through relaying
    * *Explain*. Two client hosts $A$ and $B$ in two private networks have initialized TCP or UDP connections to a well-known server $S$

        $\to$ $A$ and $B$ can simply use $S$ to relay messages between them
* *Pros*. Always work, as long as both clients can connect to the server
* *Cons*. 
    * The server's processing power and network bandwidth are consumed
    * Communication latency between the peering clients is likely increased, even if the server is well-connected
* *Usage*. Relaying is useful if maximum robustness is desired

**Connection reversal**. If one of the hosts is in the public network, and wants to connect to the other host in a private network

$\to$ The other host can "reverse" connection by actively connecting to the public host

## Hole punching
**Hole punching**. A technique in computer networking for establishing a direct connection between two parties, in which one or both are behind firewalls, or behind NAT routers
* *Idea*. 
    * When an outbound connection from a private endpoint passes through a firewall,
        * It receives a public endpoint, i.e. public IP address and port number, and
        * The firewall translates traffic between them
    * Until the connection is closed, the client and server communicate through the public endpoint, and the firewall directs traffic appropriately
* *Types of endpoint translation methods*.
    * *Consistent endpoint translation*. Reuse the same public endpoint, and the firewall directs traffic appropriately, instead of allocating a new public endpoint for every new connection
    * *Hairpin translation*. Create a loopback connection between two of its own private endpoints when it recognizes that the destination endpoint is itself

        $\to$ This is necessary for hole punching only when used within a multi-layered NAT
* *Requirements*. Reliable hole punching requires consistent endpoint translation, and, for multiple levels of NATs, hairpin translation
* *Procedure*. 
    1. Each client connects to an unrestricted third-party server, which temporarily stores external and internal address and port information for each client
    2. The sever relays each client's information to each other
    3. Using the information, each client tries to establish direct connection
    4. As a result of connections using valid port numbers, restrictive firewalls or routers accept and forward the incoming packets on each side
* *Hole punching techniques*.
    * *ICMP hole punching*. Use Internet control message
    * *UDP hole punching*. Use datagram
    * *TCP hole punching*. Use transmission protocols
* *Pros and cons*.
    * *Pros*. Hole punching offloads the server with the cost of connection re-initialization after NAT table entry expiration 
    * *Cons*. Hole punching, in fact, still requires a public server for P2P connections

**UDP hole punching**. A commonly used techinque used in NAT applications for maintaining UDP packet streams traversing the NAT
* *NAT traversal techniques*. Required for client-to-client networking applications on the Internet involving hosts connected in private networks
* *Assumptions*.
    * $A$ and $B$ are two hosts, each in its own private network
    * $N_A$ and $N_B$ are two NAT devices with globally reachable IP addresses $\ce{EIP_A}$ and $\ce{EIP_B}$ respectively
    * $S$ is a public server with a well-known, globally reachable IP address
* *Workflow*.
    1. $A$ and $B$ each begin a UDP conversation with $S$

        $\to$ $N_A$ and $N_B$ create UDP translation states and assign temporary external port numbers $\ce{EP_A}$ and $\ce{EP_B}$
    2. $S$ examines the UDP packets to get $\ce{EP_A}$ and $\ce{EP_B}$
    3. $S$ passes $\ce{EIP_A:EP_A}$ to $B$ and $\ce{EIP_B:EP_B}$ to $A$
    4. $A$ sends a packet to $\ce{EIP_B:EP_B}$

        $\to$ $N_A$ examines $A$;s packet and creates the tuple $(\ce{Source-IP-A,EP_A,EIP_B,EP_B})$ in its translation table
    5. $B$ sends a packet to $\ce{EIP_A:EP_A}$

        $\to$ $N_B$ examines $B$;s packet and creates the tuple $(\ce{Source-IP-B,EP_B,EIP_A,EP_A})$ in its translation table
    6. Depending on the state of $N_A$' translation table when $B$'s first packet arrives, i.e. whether the tuple $(\ce{Source-IP-A,EP_A,EIP_B,EP_B})$ has been created

        $\to$ $B$'s first packet is dropped, i.e. no entry in translation table, or passed, i.e. entry has been made
    7. Depending on the state of $N_B$' translation table when $A$'s first packet arrives, i.e. whether the tuple $(\ce{Source-IP-B,EP_B,EIP_A,EP_A})$ has been created

        $\to$ $A$'s first packet is dropped, i.e. no entry in translation table, or passed, i.e. entry has been made
    8. At worst, the second packet from $A$ reaches $B$ and vice versa

        $\to$ Holes have been punched in the NAT and both hosts can directly communicate

**TCP NAT traversal (TCP hole punching)**. Occur when two hosts behind a NAT are trying to connect to each other with outbound TCP connections

$\to$ This is important in P2P communications

>**NOTE**. TCP hole punching does not work with all types of NATs, since their behavior is not standardized

* *Requirements*. The availability of TCP hole punching depends on the type of computer port allocation used by the NAT
    * *Explain*. For two peers behind a NAT to connect to each other via TCP simultaneously open

        $\to$ They need to know about each other, i.e. the address and port of the remote endpoint of each other
    * *NAT port prediction*. How to discover the public remote endpoint of the other peer, when both peers are behind a NAT

        $\to$ All TCP NAT traversal and hole punching techniques have to solve the port prediction problem
* *Types of NAT*. A NAT port allocation can be one of the two
    * *Predictable*. The gateway uses a simple algorithm to map the local port to the NAT port
    * *Non-predictable*. The gateways use an algorithm, which is either random or too impractical to predict
* *Possibility of port prediction given types of NAT*. Depending on whether the NATs exhibits a predictable or non-predictable behavior

    $\to$ It will be possible or not to perform the TCP connection via TCP simultaneous open
    * *Explain*. At least one of $A$ or $B$ must be behind a predictable NAT, for port prediction to be possible
* *Port prediction methods*. There are some methods used by NATs to allow peers to perform port prediction
    * *Case 1*. NAT assigns to sequential internal ports sequential external ports
    * *Case 2*. NAT uses the port preservation scheme, i.e. the NAT maps the source port of the internal peer to the same public port
    * *Case 3*. NAT uses endpoint independent mapping, i.e. two successive TCP connections coming from the same internal endpoint are mapped to the same public endpoint
* *Workflow*. Assuming that each peer knows the remote peer endpoint, and port prediction is possible

    <div style="text-align:center">
        <img src="https://imgur.com/1CLA3re">
        <figcaption>TCP hole punching</figcaption>
    </div>

    1. Peer $A sends a `SYN` to peer $B$, and vice versa
    2. When $N_A$ receives the outgoing `SYN` from $A$, it creates a mapping in its state machine

        $\to$ $N_B$ behaves in the same manner when received `SYN` from $B$
    3. Both `SYN` cross somewhere along the network path, then
        1. `SYN` from $A$ reaches $N_B$, and vice versa
        2. Depending on the timing of these events, where in the network the `SYN` cross

            $\to$ At least one of the NAT will let the incoming `SYN` through, and map it to the internal destination peer
    4. Upon receipt of `SYN`, the peer sends a `SYN+ACK` back and the connection is established