---
id: "stream-adding-nodes-to-the-graph-options-for-the-graph"
type: "concept"
domain: "cmsis-stream"
title: "Adding nodes to the graph: Options for the graph"
summary: "Those options needs to be used on the graph object created with Graph()."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Graph.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Graph.md#options-for-the-graph"
license: "Apache-2.0"
mode: "V"
---

Those options needs to be used on the graph object created with `Graph()`.

For instance :

```python
g = Graph()
g.defaultFIFOClass = StreamFIFO
```

### defaultFIFOClass (default = "StreamFIFO")

Class used for FIFO by default. Can also be customized for each connection (`connect` of `connectWithDelay` call). This must be a Python class name. This class is used to specify the name of the FIFO in the C++ and the argument to pass to the constructor (see below).

Standard nodes may have to be modified to use a custom FIFO if the FIFOBase API must be changed.

### duplicateNodeClassName(default="Duplicate")

Prefix used to generate the duplicate node classes like `Duplicate2`, `Duplicate3` ...

Those nodes are inserted automatically to implement one-to-many connections.

If you need to connect an output to more than 3 nodes, you'll have to create the `Duplicate` nodes.
