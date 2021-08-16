---
title: 7. Principles of network applications
tags: Computer networking
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Ubuntu network configuration](#ubuntu-network-configuration)
  - [Fundamental](#fundamental)
    - [Default gateway](#default-gateway)
    - [Subnetwork](#subnetwork)
      - [Introduction](#introduction)
      - [Network addressing and routing](#network-addressing-and-routing)
    - [Metrics in networking](#metrics-in-networking)
  - [IPv4 configuration](#ipv4-configuration)
    - [Manual static IPv4 configuration](#manual-static-ipv4-configuration)
<!-- /TOC -->

# Ubuntu network configuration
## Fundamental
### Default gateway
**Default gateway**. The node in a computer netowrk, using the IP suite, which serves as the forwarding host, e.g. router, to other networks, when no other route specification matches the destination IP address of a packet
* *Gateway*. A network node serving as an access point to another network, often involving a change of addressing, and a different networking technology
    * *Router*. A router merely forwards packets between networks with different network prefixes, i.e. indicated by network mask
        * *Routing table*. The networking software stack of each computer contains a routing table specifying 
            * Which interface is used for transmission
            * Which router on the network is responsible for forwarding to a specific set of addresses
    * *Default gateway's responsibility*. If none of the forwarding rules is appropriate for a given destination address

        $\to$ The default gateway is chosen as the router of last resort
* *Default gateway in home or small office environment*. A device, e.g. DSL router or cable router, which connects the local network to the Internet

    $\to$ It serves as the default gateway for all network devices
* *Default gateway in enterprise network systems*. Enterprise network systems may require many internal network segments

    $\to$ A device wishing to communicate with a host on the public Internet, it will forward the packet to the default gateway for its network segment

### Subnetwork
#### Introduction
**Subnetwork (subnet)**. A logical subdivision of a IP network
* *Subnetting*. The practice of dividing a network into two or more networks
* *Subset addressing*. Computers belonging to the same subnet are addressed with an identical most-significant bit-group in their IP addresses

    $\to$ THis results in the logical division of an IP address into two fields, i.e. the network number, or routing prefix, and the rest field, or host identifier
    * *Rest field (host identifier)*. An identifier for a specific host or network interface
    * *Routing prefix*. May be expressed in class inter-domain routing (CIDR) notation
        * *CIDR*. Written as the first address of a network, followed by a slash character, and neding with the bit-length of the prefix
            * *Example*. `198.51.100.0/24` dedicates 24 bits for network prefix, and the remaining 8 bits are for host addressing
* *Netmask (or subnet mask)*. The bitmask, which when applied by a bitwise AND operation to any IP address in the network, yields the routing prefix
    * *Format*. Expressed in dot-decimal notation, like an address, e.g. `255.255.255.0` is the subnet mask for `198.51.100.0/24`

**Routers**. Traffic is exchanged between subnetworks through routers when the routing prefixes of the source address and destination address differ

$\to$ A router serves as a logical or physical boundary between the subnets

**Benefits of subnetting an existing network**.
* Allow for efficient address space allocation for the address allocation architecture of the Internet using CIDR, and in large organizations
* Enhance routing efficiency
* Have advantages in network management when subnetworks are administratively controlled by different entities in a larger organization

#### Network addressing and routing
**Network address**. 
* *IP address*. Computers joining a network, e.g. the Internet, each have at least one network address, which is unique of each device

    $\to$ An address fulfills the functions of identifying the host and locating it on the network
* *IP address division*. An IP address is divided into two logical parts, i.e.
    * *Network prefix*. All hosts on a subnetwork have the same network prefix, which occupies the most significant bits of the address
        * *Number of bits for network prefix*. May vary between subnets, depending on the network architecture
    * *Host identifier*. A unique local identification, and is either a host number on the local network, or an interface identifier

**Packet transmission**.
* *Benefits for packets transmission*. 
    * Permit the selective routing of IP packets across multiple networks via special gateway computers, called routers, to a destination host, if the network prefixes of origination and destination hosts differ
    * Permit direct packet transmission between origination and destination hosts if their network prefixes are the same
* *Routing prefix of an address*. 
    * *Traditional form*. Identified by the subnet mask, written in the same form used for IP addresses
    * *Modern form*. Use CIDR notation
* *Routing packets across networks*. Given an IPv4 source address, its associated subnet mask, and the destination address

    $\to$ A router can determine whether the destination is on a locally connected or a remote network
    * *Routing table*. Each locally connected subnet must be represented by a separate entry in the routing tables of each connected router

### Metrics in networking
**Router metrics**. Metrics used by a router to make routing decisions, i.e. they help the router choose the best route among multiple feasible routers to a destination

$\to$ A metric is typically one of many fields in a routing table
* *Idea*. The route will go in the direction of the gateway with the lowest metric
* *Metric format*.
    * *Information for metrics*. A metric may include information like path length, bandwidth, hop count, load, path cost, delay, maximum transmission unit, reliability, and communication cost
    * *Composite metric*.A metric can be considered as additive, concave, e.g. min/max, or multiplicative

## IPv4 configuration
### Manual static IPv4 configuration
**Manual static IPv4 configuration**. In order to configure for static IPv4 in Ubuntu, you must provide Ubuntu 

<div style="text-align:center">
    <img src="https://i.imgur.com/t1fWZp0.png">
    <figcaption>Ubuntu 18.04 network configuration</figcaption>
</div>

**Addresses**. This section is to record the static IP addresses we want to assign to our machine
* *Address*. The desired IP address we want to assign to this machine
* *Netmask*. A dexical-converted binary mask indicating subnet bits in the assigned address
    * *Explain*. Assume that the netmask is $n$ and the address is $a$ then we can derive
        * *The subnet address of the host*. $s = a \land n$
        * *The address of the host in its subnet*. $h = a \land (\lnot n)$
* *Gateway*. The address of a network node, which serves as an access point to outer network of our subnet

**DNS**. The DNS servers we want to exploit for hostname-to-IP-address translation

**Routes**. The routing table
* *Address*. The desired IP address of the host, or the network, we want to route to
* *Netmask*. The netmask for the underlying address
* *Gateway*. The gateway, through which we want to access the desired address
* *Metric*. A value assigned to an IP route for a particular network interface
    * *Explain*. Identify the cost associated with using this node
        * *Example*. Valued in terms of link speed, hop count, or time delay
    * *Purpose*. Help the machine to choose the b est route among multiple routes to a destination

        $\to$ The machine will go in the direction of the gateway with the lowest metric