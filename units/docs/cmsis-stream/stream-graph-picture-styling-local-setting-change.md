---
id: "stream-graph-picture-styling-local-setting-change"
type: "concept"
domain: "cmsis-stream"
title: "Graph picture styling: Local setting change"
summary: "To change the setting for a particular element of the graph (like a specific node), you need to inherit from theStyle class and override a specific method."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Styling.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Styling.md#local-setting-change"
license: "Apache-2.0"
mode: "V"
---

To change the setting for a particular element of the graph (like a specific node), you need to inherit from the`Style` class and override a specific method.

For instance, to change the filling color of a specific node, you could define:

```python
class MyStyle(Style):
    def node_color(self,node):
        if node.isPureNode:
           return("burlywood1")
        return super().node_color(node)
```

This node function will change the filling color of all nodes that are pure functions (like CMSIS-DSP functions with no state). Otherwise, the default styling will be used.

This object can be created with a dictionary of global settings:

```python
MyStyle(globalStyle)
```

but if no dictionary is used, the default settings are used by `MyStyle`

### Information access in the Style object

When you write the methods of your style object, you may need to access some information about the node, edge or port. Most of the time, this information is passed as arguments to the method. But sometimes, you need to extract some information from those arguments.

You can use the methods of the node object when you receive a node object. The method of a FIFO when it is a FIFO object. But the style object is also providing some additional methods to make it simpler to access some information:

```python
def isFIFO(self,edge):
```

Since the graph can be either pre-compute or post compute, the edge may have different description.

In pre-compute mode, an edge is a just a pair of node. In post-compute mode, it is a FIFO.

```python
def fifoLength(self,edge):
```

Return the length of the FIFO (in number of samples). If it is applied to a pre-compute edge, it will return `None`. 

```python
def edgeSrcNode(self,edge):
```

Get the source node in pre or post compute graphs

```python
def edgeDstNode(self,edge):
```

Get the destination node in pre or post compute graphs

```python
def edgeSrcPort(self,edge):
```

Get the source port in pre or post compute graphs

```python
def edgeDstPort(self,edge):
```

Get the destination port in pre or post compute graphs

```python
def getPort(self,node,i,input=False):
```

Get the port number `i` on `inputs` or `outputs` of a node. It will raise an exception if the index `i` is negative or bigger than the number of inputs or outputs.
