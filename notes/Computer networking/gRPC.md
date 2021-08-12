---
title: gRPC
tags: Networking
---

<!-- TOC titleSize:1 tabSpaces:2 depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 skip:0 title:1 charForUnorderedList:* -->
# Table of Contents
* [Protocol buffers](#protocol-buffers)
  * [Introduction](#introduction)
  * [Discussion](#discussion)
* [Google Remote procedure call (gRPC)](#google-remote-procedure-call-grpc)
  * [Introduction](#introduction)
  * [Discussion](#discussion)
<!-- /TOC -->

# Protocol buffers
## Introduction
**Example**. Example `.proto` file

```proto=
message SearchRequest {
    required string query = 1;
    optional int32 page_number = 2;
    optional int32 result_per_page = 3;
}
```

* `SearchRequest` message definition specifies three fields


**Field**. Describe each data piece we want to include in this type of message
* *Syntax*. Has a name and a type

    ```proto=
    {field rule} {field type} {field name}
    ```

* *Field number*. Each field in a message definition has a unique number
    * *Usage*. Identify the fields in the message binary format

        >**NOTE**. Field number should not be changed once our message type is in use

    * *Valid field numbers*. $\{1,\dots,2^{29}-1\} / \{19000,\dots,19999\}$
        * *Explain*. $\{19000,\dots,19999\}$ are reserved for the PB implementation
* *Field rule*.
    * `required`. A well-formed message must have exactly one of this field
    * `optional`. A well-formed message can have zero or one of this field
    * `repeated`. The field can be repeated any number of times, including zero, in a well-formed message

## Discussion
**Protocol buffer vs JSON**. See [here](https://stackoverflow.com/questions/52409579/protocol-buffer-vs-json-when-to-choose-one-over-another)
* *JSON*. JSON is text data
    * *Pros*.
        * Human readable
        * Directly consumed by web browsers
        * Easy to combine with JS-based servers
    * *Cons*.
        * JSON is textual, its integers and floats can be slow to encode and decode
        * Parsing JSON strings, arrays, and objects requires a sequential scan
        *
* *Protocol buffers*. PB uses binary message format
    * *Pros*.
        * Relatively smaller size
        * Guarantee type-safety
        * Fast serialization and deserialization
        * Especially faster at encoding integers and floating point numbers
        * Easier to bind objects and faster
    * *Cons*.
        * Programmers need to specify a schema for the data
        * Supported by Java, Python, Objective-C, and C++ only

# Google Remote procedure call (gRPC)
## Introduction

**Brief description**. A client application can directly call a method on a server application on a different machine, as if it were a local object

$\to$ This makes it easier for us to create distributed applications and services

<div style="text-align:center">
    <img src="/media/landing-2.svg">
</div>

* *Key idea*. Define a service, specifying the methods which can be called remotely with their parameters and return types
    * *Server side*. The server implements the interface and runs a gRPC server to handle client calls
    * *Client side*. The client has a stub providing the same methods as the server
* *Multi-platforn*. gRPC clients and servers can run and take to each other in a variety of environments

**Protocol buffer**. Google's mature open source mechanism for serializing structured data

## Discussion
**RPC and RESTful**.
* *Remote procedure call (RPC)*. Expose functionality as function calls which accept parameters and invoke these functions via HTTP verbs which seems most appropriate
    * *Example*. `GET` for a query
* *Representation state transfer (REST)*. Model the various entities within the problem domain as resources, and use HTTP verbs to represent transactions against these resources
    * *Example*. `POST` to create, `PUT` to update, and `GET` to rea
