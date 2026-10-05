---
id: "stream-description-of-the-nodes-1-overview"
type: "concept"
domain: "cmsis-stream"
title: "Description of the nodes: 1 Overview"
summary: "To create a new kind of node, you generally inherit from one of those classes. Those are the simplest and most used:"
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Generic.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Generic.md#1-overview"
license: "Apache-2.0"
mode: "V"
---

### 1.1 Basic generic nodes

To create a new kind of node, you generally inherit from one of those classes. Those are the simplest and most used:

* `GenericSource`
* `GenericNode`
* `GenericSink`

They are defined in `cmsis_stream.cg.scheduler`.

### 1.2 Complex generic nodes

#### 1.2.1 Many-to-many cases:

* `GenericToManyNode`
* `GenericFromManyNode`
* `GenericManyToManyNode`

#### 1.2.2 Function nodes

And finally, there are other classes that can be used to create new nodes from functions. A function has no state and a C++ wrapper is not required. In this case, the tool is generating code for calling the function directly rather than using a C++ wrapper.

* `Unary` (unary operators like `negate`, `inverse` ...)
* `Binary` (binary operators like `add`, `mul` ...)
* `GenericFunction` to map any function
