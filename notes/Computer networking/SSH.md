---
title: 4. Delay, loss, and throughput in packet-switched networks
tags: Computer networking
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
- [Table of Contents](#table-of-contents)
- [Secure shell - SSH](#secure-shell---ssh)
  - [Introduction](#introduction)
    - [Definition](#definition)
    - [Authentication - OpenSSH key management](#authentication---openssh-key-management)
    - [Usage](#usage)
  - [SSH protocols](#ssh-protocols)
    - [SSH protocol](#ssh-protocol)
    - [SSH file transfer protocol (SFTP)](#ssh-file-transfer-protocol-sftp)
      - [SFTP is not FTPS](#sftp-is-not-ftps)
      - [Background of FTP](#background-of-ftp)
    - [Privilege separation](#privilege-separation)
  - [Proxies and jump hosts](#proxies-and-jump-hosts)
    - [Jump host - Passing through a gateway or two](#jump-host---passing-through-a-gateway-or-two)
    - [Port forwarding](#port-forwarding)
  - [Tunnels](#tunnels)
    - [Tunneling](#tunneling)
    - [Reverse tunneling](#reverse-tunneling)
- [Appendix](#appendix)
  - [Concepts](#concepts)
<!-- /TOC -->

# Secure shell - SSH
## Introduction
**Secure shell (SSH)**. A cryptographic network protocol for operating network services securely over an unsecured network
* *Idea*. Provide a secure channel over an unsecured network by using a client-server architecture connecting an SSH client application with an SSH server
* *Standard port for SSH*. 22 ports

**Motivation**. SSH was designed as a replacement for telnet and for unsecured remote shell protocols, e.g. the Berkeley's rsh and the related rlogin and rexec protocols
* *Explain*. These protocols send sensitive information, notably passwrods, in plaintext, rendering them susceptible and disclosure using packet analysis

    $\to$ The encryption used by SSH is intended to provide confidentiality and integrity of data over an unsecured network, e.g. the Internet

### Definition
**SSH idea**. Use public-key cryptography to authenticate the remote computer and to allow it to authenticate the user, if necessary

**Different ways to use SSH**.
* *Option 1*. Use automatically generated public-private key pairs to simply encrypt a network connection

    $\to$ Then use password authentication to log on
* *Option 2*. Use a manually public-private key pair to perform authentication, allowing users or programs to log in without having to specify a password

    $\to$ Anyone can produce a matching pair of different keys, i.e. public and private
    * *Public key location*. Placed on all computers which must allow access to the owner of the matching private key
    * *Unknnown public keys*. In SSH, it is important to verify unknown public keys, i.e. associate public keys with identities, before accepting them as valid
        * *Explain*. Accepting an attacker's public key without validation will authorize an unauthorized attacker as a valid user

### Authentication - OpenSSH key management
**Authorized public keys location**. Authorized public keys are stored in the home directory of the user which is allowed to log in remotely, in the file `~/.ssh/authorized_keys`

>**NOTE**. `~/.ssh/authorized_keys` is only respected by SSH if it is not writable by anything apart from the owner and root

>**NOTE**. For additional security, the private key itself can be locked with passphrase

**Private keys location**. The private key can be looked for in standard places
* *Generating SSH key pair*. Use `ssh-keygen`

**Password-based authentication**. SSH also supports password-based authentication, which is encrypted by automatically generated keys
* *Drawbacks*. The attacker could imitate and legitimate server side, asking for password, and obtaining it
    * *Solution*. This is possible only if the two sides have never authenticated before, as SSH remembers the key which the server side previously used

        $\to$ The SSH client raises a warning before accepting the key of a new, previously unknown server

### Usage
**Common usage**. 
* Log into a remote machine and execute commands
* Tunneling to provide a secure path over the Internet, through a firewall to a virtual machine
* Forward TCP ports and X11 connections
* Transfer files using the associated SSH file transfer (SFTP) or secure copy (SCP) protocols
* Used in cloud computing to solve connectivity problems, avoiding the security issues of exposing a cloud-based virtual machine directly on the Internet

**General mechanism**. An SSH client program is typically used for establishing connections to an SSH daemon accepting remote 

## SSH protocols
### SSH protocol
**OpenSSH**. OpenSSH uses the SSH protocol connecting over TCP
* *Multiple SSH sessions over one TCP connection*. Normally, one SSH session per TCP connection is made, but multiple sessions can be multiplexed over a single TCP connection if planned that way

**SSH protocol**. SSH is an open standard, which is vendor-neutral and maintined by the Internet Engineering Task Force (IETF)
* *Reference documentation*. RFC 4250 through RFC 4256, with the overall structure of SSH2, i.e. current version, described in RFC 4251

**Protocol layers**.

<div style="text-align:center">
    <img src="https://i.imgur.com/XxZoVyq.png">
    <figcaption>Sequence diagram for SSH password authentication</figcaption>
</div>

* *SSH-CONNECT*. The connection layers runs over the user authentication protocol
    * *Functionality*. Multiplex many different concurrent encrypted channels into logical channels over the authenticated connection
    * *Responsibility*.
        * Allow for tunneling of login session and TCP-forwarding
        * Provide a flow control service for the tunneling and TCP-forwarding channels

            >**NOTE**. Various channel-specific options can be negotiated

        * Manage the SSH session, session multiplexing, X11 forwarding, TCP forwading, shell, remote program execution, SFTP subsystem invocation
* *SSH-USERAUTH*. The user authentication layer authenticates the client-side to the server
    * *Functionality*. Use the established connection and run on top of the transport layer
    * *Responsibility*.
        * Provide several mechanisms for user authentication, i.e. 
            * Password authentication
            * Public-key or host-based authentication mechanisms
            * Challenge-response
            * Pluggable authentication modules (PAM)
            * Generic s![](https://i.imgur.com/022sQph.png)
curity services API (GSSAPI)
            * Dongles
* *SSH-TRANS*. The transport layer provides server authentication, confidentiality, and data integrity over TCP
    * *Functionality*. Finish its job through algorithm negotiation and a key exchange
    * *Key exchange*. Include server authentication and results in cryptographically secured connection
    * *Responsibility*. Provide integrity, confidentiality, and optional compression

### SSH file transfer protocol (SFTP)
**SFTP**. A binary protocol to provide secure file transfer, acccess, and management

#### SFTP is not FTPS
**Requirements for remote file transfer**. An account on the machine with the OpenSSH server
* *SFTP*. In contrast to old FTP, i.e. SFTP is designed from the ground up to be as secure as possible for both login and data transfer
    * *SSHFS*. As an SFTP client, the other machine is accessible as an open folder on local machine's file system

        $\to$ Any program we normally have to work with files can access the remote machine via that folder
* *FTP*. Inherently insecure, and great for read-only, public data transfer
    * *Explain*. With FTP, the data, passwords, and username are all sent back and forth without encryption

        $\to$ Any man-in-the-middle can sniff the passwords and data when FTP is used
    * *Solution*. Wrap FTP inside SSL or TLS, thus creating FTPS
        * *Drawback*. Tunneling FTP over SSL and TLS is complex and far from an optimum solution

#### Background of FTP
**Historical founding condition**. FTP is from the 1970s, an era when if we were on the net, we were supposed to be there, and if there was trouble, it could usually be cleared up with a short phone or an e-mail or two

**Mechanism**. FTP sends the login name, password, and all of the data unencrypted for anyone to intercept

$\to$ FTP clients can connect to the FTP server in passive or active modes, both of which use two ports, one for control and one for data
* *FTP active mode*. After the client makes a connection to the FTP server, it then allows an incoming connection to be initiated from the server to for data transfer
* *FTP passive mode*. After the client makes a connection to the FTP server, the server then responds with information about a second port for data transfer, and the client initiates the second connection

**Usage**. Great for anonymous FTP, which is still excellent for read-only downloads without login

**FTPS**. FTPS is FTP tunneled over SSL or TLS
* *FTP's goal*. Encourage the use of remote computers, which, along with the Web, has succeeded
* *FTPS' goal*. Secure logins and transfers, and it was a necessary step in securing file transfers with the legacy protocol (FTP)

### Privilege separation
**Privilege separation**. When a process is divided into sub-processes, each of which have just enough access to just the right services to do their part of the job

$\to$ The underlying principle is least privilege, i.e. each process has exactly enough privileges to accomplish a task, neither more or less
* *Goal*. Compartmentalize any corruption and prevent a corrupt process from accessing other parts of the system
* *Mechanism*. Used in OpenSSH by using several levels of access, some higher some lower, to run SSH daemon and its subsystems and components

    <div style="text-align:center">
        <img src="https://i.imgur.com/pLheudN.png">
        <figcaption>Sequence diagram for OpenSSH privilege separation</figcaption>
    </div>

    1. The SSH server, i.e. component 1, starts with a privileged process, i.e. component 2
    2. The privileged process creates an unprivileged process, i.e. component 3, to work with the network traffic
    3. Once the user has authenticated, another unprivileged process, i.e. component 4, is created with the privileges of that authenticated user

## Proxies and jump hosts
**Proxy**. An intermediary which forwards requests from clients to other servers for performance improvement, load balancing, security, or access control purposes

### Jump host - Passing through a gateway or two
**Jump host - Passing through a gateway or two**. It is possible to connect to another host via one or more intermediaries so that the client can act as if the connection were direct
* *Main method*. Use an SSH connection to forward the SSH protocol through one or more "jump hosts" using proxy jumps, to an SSH server running on the target destination
* *Pros*. 
    * This is the most secure method since encryption is end-to-end
    * Whatever other encryption goes on, the end points of the chain encrypt and decrypt each other's traffic

        $\to$ Traffic passing through the intermediate hosts is always encrypted
* *Cons*. Cannot be used if the intermediate hosts deny port forwarding

**Command line usage**.
* *Option 1*. Use `ProxyJump` in the SSH configuration file (deprecated), or `-J` as a runtime parameter
    * *Example*.

        ```bash
        # ssh -p {port} -J {intermediate-host}:{port} {target-host}
        ssh -p 22 -J firewall.example.org:22 server2.example.org
        ```

    * *Command line arguments*. `-J [user@]host[:port]` connects to the target host by first making a SSH connection to the jump host, then establish a TCP forwarding to the ultimate destination from there

        >**NOTE**. Multiple jump hops may be specified separated by comma characters

* *Option 2*. Use `stdio` forwarding, i.e. `-W`, mode to bounce the connection through an intermediate host
    * *Example*.
    
        ```bash
        # first example
        ssh -o ProxyCommand="ssh -W %h:%p firewall.example.org" -p 22 username@server2.example.org
        # another example
        ssh -o ProxyCommand="ssh -W %h:%p localhost" ailab02@118.70.181.146 -p 6969 -v
        ```
    
    * *Command line arguments*.
        * `-W host:port` requests stdio on the client be forwarded to `host:port` over the secure channel
        * `-o option` can be used to give options in the format used in the SSH configuration file
        * `ProxyCommand` specifies the command to use to connect to the server (see Appendix)
        * `%h` and `%p` points to `server2.example.org` and `22`
        * `%r` points to `username`

    >**NOTE**. If `server2.example.org` is given instead of `username@server2.example.org`, i.e. no `username`, then the default username would be the current username in the SSH client 

* *Option 3*. Use `-tt` to force TTY allocation and passes the SSH traffic as though typed
    * *Example*.

        ```
        ssh -tt firewall.example.com ssh -tt server2.example.org
        ```

    * *Command line arguments*. `ssh -tt {host:port} {command}` forwards our terminal to `host:port` and execute `command` using this forwarded terminal 

**Using canonical host names behind jump hosts**. Some LANs have their own internal DNS to assign its own hostnames, and these names are not accessible to systems outside the LAN
* *Consequence*. It is not possible to use `-J` or `ProxyJump` option from the outside, since the client would not be able to look up the names on the LAN on the other side of the jump host
* *Solution*. The jump host can look these names up
    
    $\to$ The `ProxyCommand` option can be used to call an SSH client on the jump host, and use its capabilities to look up a name on the LAN
* *Example*.

    ```bash
    ssh -o ProxyCommand="ssh -W fuloong04.localnet.lan:22 jumphost.example.org" fred@fuloong04
    ```

* *Explain example*.

### Port forwarding
**Port forwarding through one or more intermediate hosts**.
* *Example*. Tunnel port 8900 on the `localhost` to port 80 on `machine2`

    ```bash
    ssh -L 8900:localhost:80 -J jumphost.example.org machine2
    ```

**References**.
* https://en.wikibooks.org/wiki/OpenSSH/Cookbook/Proxies_and_Jump_Hosts

## Tunnels
**Tunneling (port forwarding)**. A local port is connected to a port on a remote host or vice versa

$\to$ Connections to the port on one machine are in effect connections to a port on the other machine

### Tunneling
**Tunneling**. A way of securing an insecure protocol, or making a remote service appear as local
* *Example*.

    ```bash
    ssh -L 5901:localhost:5901 -l fred desktop.example.org
    ```

* *Multiple port forwarding*. Multiple tunnels can be specified at the same time

    ```bash
    ssh -L 5901:localhost:5901 -L 5432:localhost:5432 -l fred desktop.example.org
    ```

**Types of tunneling**.
* Regular forwarding
* Reverse forwarding
* Dynamic forwarding

**Tunneling with SSH configuration file**.

```bash
Host desktop desktop.example.org
        HostName desktop.example.org
        User fred
        LocalForward 5901 localhost:5901

Host postgres
        HostName desktop.example.org
        User fred
        LocalForward 5901 localhost:5901
        LocalForward 5432 localhost:5432

Host server server.example.org
        HostName server.example.org
        User fred
        ExitOnForwardFailure no
        LocalForward 3128 localhost:3128

Host *
        ExitOnForwardFailure yes
```

**Tunneling via a single intermediate host**.

```bash
ssh -fN -L 1880:target.host:80 -l fred bastion.example.org
```

**Finding the PID of a tunnel in the background**. There is not currently an automatic way to find the PID of the task sent to the background

### Reverse tunneling
**Reverse tunneling**. Forwards connections in the opposite direction of a regular tunnel
* *Idea*. An SSH session begins from the local host to a remote host, while a port is forwarded from the remote host to the local host
* *Stages in reverse tunneling*. 
    * *Stages*.
        1. Connect from endpoint A to endpoint B using SSH with remote forwarding enabled
        2. Connect other systems to the designated port on endpoint B, and that port is forwarded to endpoint A
    * *Conclusion*. While system A initiated the SSH connection to system B, the connections to the designated port on B are sent over to A over the reverse tunnel

        $\to$ Once the SSH connection is made, the reverse tunnel can be used on endpoint B the same as regular tunnel
* *Usage*. Forward SSH over SSH to work on an otherwise inaccessible system, e.g. something behind a home router

**Example**.
* *Command line example*.

    ```
    ssh -fNT -R 2022:localhost:22 -l fred server.example.org
    ```

* *SSH configuration file example*. Use `RemoteForward` directive, rather than `LocalForward`

**Reference**. https://en.wikibooks.org/wiki/OpenSSH/Cookbook/Tunnels

# Appendix
## Concepts
**SFTP (SSHFS) and SCP**.
* *SFTP*. An extension to SSH protocol, which is a file transfer protocol similar to FTP, but uses SSH protocol as the network protocol
* *SCP*. Only for transferring files, and cannot do other things like list remote directories or removing files

**SSHFS and NFS**.
* *NFS*. A network filesystem, i.e. a protocol designed for accessing files on a filer
    * *Pros*. Very reliable, and when we know when and how to use it, it is the best tool for the job
    * *Cons*. It consists of multiple services and uses multiple ports, thus a bit clunky and difficult to set up, e.g. firewalls
    * *NFS*. Used for consistent connections which are used constantly
* *SSHFS*. A user-space filesystem layer stacked on rtop of SSH, which is not a filesystem protocol but a remote shell protocol
    * *Pros*. Great when we just want to open some files on a remote server and that is all
    * *Cons*. Not as reliable as NFS and may lack features
    * *Usage*. Used for short connections or over the public Internet

**TCP forwarding**. TCP port forwading, or tunneling, allows other TCP applications to forward their network data over a secure SSH connection
* *Purpose*. Existing TCP applications, which do not encrypt their data before sending it across the network, can send their network traffic through an SSH channel, thus securing it

    $\to$ Without TCP forwading, an application's client connections directly to its server across the network
* *Example*. 

    ```bash
    ssh -L 2001:remotehost:27 billy@remotehost
    ```

    <div style="text-align:center">
        <img src="https://i.imgur.com/022sQph.png">
        <figcaption>SSH tunnel</figcaption>
    </div>

* *Explain example*.
    * The SSH client on Host A listens on port 2001 for connections

        $\to$ The TCP application will now connect to port 2001 on the local host (Host A) rather than its well-known port on Host B, where the server is listening
    * The SSH client accepts the connection on port 2001 and forwards the application's data to the SSH server on Host B
    * SSH server on Host B then forwards the data to the application's well-known port on Host B
* *`-L` option*. Specify that connections to the given TCP port or UNIX socket on the local (client) host are forwarded to the given host and port, or UNIX socket, on the remote side
    * *Mechanism*. 
        1. Allocate a socket to listen to either a TCP port on the local side, or to a UNIX socket
        2. Whenever a connection is made to the local port or socket, the connection is forwarded over the secure channel
        3. A connection is made to either host-port, or the UNIX socket, from the remote machine

**ProxyCommand (`ssh_config`)**. Specify the command to use to connect to the server
* *Idea*. Rather than using ordinary SSH command from terminal, ProxyCommand will be executed to establish a SSH connection to target host
* *Usage*. Used to connect SSH with custom command, e.g. create SSH tunnel with SSH configuration file
* *Command executor*. The command will be executed using the user's `exec` directive to avoid lingering shell process
* *Command requirements*. The command should eventually connect a SSH server running on some machine

**TTY (Linux)**. Early user terminals connected to computers were electromechanical teleprinters or teletypewriters (TeleTYpewriter, TTY)

$\to$ Since then TTY has continued to be used as the name for the text-only console although this text-only console is a virtual console, not a physical one

**`etc/shadow`**. The system file containing hashed system's user's password

**`tcpdump`**. Show what is going on over the network