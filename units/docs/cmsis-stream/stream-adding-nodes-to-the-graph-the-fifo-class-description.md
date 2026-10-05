---
id: "stream-adding-nodes-to-the-graph-the-fifo-class-description"
type: "concept"
domain: "cmsis-stream"
title: "Adding nodes to the graph: The FIFO class description"
summary: "Option for custom FIFOs require use of a Python class with following constructor:"
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Graph.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Graph.md#the-fifo-class-description"
license: "Apache-2.0"
mode: "V"
---

Option for custom FIFOs require use of a Python class with following constructor:

```Python
def __init__(self,the_type,length):
```

The following API must be provided in the class

```python
@property
def cname(self):
    
@property
def args(self):
```

`cname` is the C++ class name

`args` are the additional arguments for the constructor (following the buffer argument). By default, this is an empty list. Otherwise, it is a list of C arguments.

If the API provided by the FIFO must be different from the one provided by `FIFOBase<T>` then standard nodes will have to be modified. In general, the easiest way is to just modify `GenericNodes.h` in your project and extend the `FIFOBase<T>` API.
