---
id: "stream-description-of-the-nodes-3-details-about-many-to-many-nodes"
type: "concept"
domain: "cmsis-stream"
title: "Description of the nodes: 3 Details about many-to-many nodes"
summary: "All the IOs of a node must be described in its C++ template. When a node is heterogenous (IOs of different datatypes and/or length) the listing of all IOs in the template arguments cannot be avoided."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Generic.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Generic.md#3-details-about-many-to-many-nodes"
license: "Apache-2.0"
mode: "V"
---

All the IOs of a node must be described in its C++ template. When a node is heterogenous (IOs of different datatypes and/or length) the listing of all IOs in the template arguments cannot be avoided.

But when all the inputs or all the outputs have the same datatype and length, it can be very annoying to have to define a long list of template arguments.

Also, we'd like to have the same implementation but working with as many inputs or output of the same kind.

With the normal mechanism, two nodes differing by the number of inputs or outputs have a different datatype : different C++ template.

To make it easier to implement some regular and homogeneous nodes (like a Duplicate node copying its input to its outputs), some new classes have been introduced:

### 3.1 GenericToManyNode

`GenericToManyNode` is very similar to `GenericNode` but instead of providing a function `addOutput`, it is providing:

```python
def addManyOutput(self,theType,theLength,nb):
```

It will define `nb` outputs with the same type `theType` and the same length `theLength`. The node is said homogenous (at least for the outputs) since they are all of the same nature.

Note that you cannot add other outputs of different nature (datatype or length). The function `addOutput` is not available in this context.

The name of those outputs is defined by the node, and different nodes may have a different naming strategy. The naming can be accessed with the function provided by the node:

```python
def outputNameFromIndex(self,i):
```

Let's assume `p` is a node with many outputs. To connect the second output, one could do:

```python
g.connect(p[p.outputNameFromIndex(1)],node.i)
```

The method `outputNameFromIndex` can be customized by a node. It should always return names that are in alphabetical order so that the index used in this method is also the index to use in the C code.

By default the names generated are `oa`, `ob`, ... It means you should not use more than 26 outputs with this naming ...

### 3.2 GenericFromManyNode

It is similar to the previous case but with many inputs. The `addInput` function is replaced with:

```python
def addManyInput(self,theType,theLength,nb):
```

The function to get the input names if:

```python
def inputNameFromIndex(self,i):
```

### 3.3 GenericManyToManyNode

The node is providing the two following functions:

```python
def addManyInput(self,theType,theLength,nb):
```

```python
def addManyOutput(self,theType,theLength,nb):
```
