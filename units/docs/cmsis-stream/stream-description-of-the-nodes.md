---
id: "stream-description-of-the-nodes"
type: "concept"
domain: "cmsis-stream"
title: "Description of the nodes"
summary: "The generic and function nodes are the basic nodes that you use to create other kind of nodes in the graph."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Generic.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Generic.md"
license: "Apache-2.0"
mode: "V"
---

The generic and function nodes are the basic nodes that you use to create other kind of nodes in the graph. 

There are several generic classes provided by the framework to be used to create new nodes.

There are also classes provided to define the datatype of the samples processed by the nodes.

- [Description of the nodes](#description-of-the-nodes)
  - [1 Overview](#1-overview)
    - [1.1 Basic generic nodes](#11-basic-generic-nodes)
    - [1.2 Complex generic nodes](#12-complex-generic-nodes)
      - [1.2.1 Many-to-many cases:](#121-many-to-many-cases)
      - [1.2.2 Function nodes](#122-function-nodes)
  - [2 Details about basic generic nodes](#2-details-about-basic-generic-nodes)
    - [2.1 Methods](#21-methods)
    - [2.2 Datatypes](#22-datatypes)
      - [2.2.1 CType](#221-ctype)
      - [2.2.2 CStructType](#222-cstructtype)
      - [2.2.3 PythonClassType](#223-pythonclasstype)
  - [3 Details about many-to-many nodes](#3-details-about-many-to-many-nodes)
    - [3.1 GenericToManyNode](#31-generictomanynode)
    - [3.2 GenericFromManyNode](#32-genericfrommanynode)
    - [3.3 GenericManyToManyNode](#33-genericmanytomanynode)
  - [4 Function and constant nodes](#4-function-and-constant-nodes)
    - [`GenericFunction`](#genericfunction)
