---
id: "stream-adding-nodes-to-the-graph-creating-a-connection"
type: "concept"
domain: "cmsis-stream"
title: "Adding nodes to the graph: Creating a connection"
summary: "Those methods must be applied to a graph object created with Graph(). The Graph class is defined inside cmsis_stream.cg.scheduler from the cmsis-stream Python package."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Graph.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Graph.md#creating-a-connection"
license: "Apache-2.0"
mode: "V"
---

Those methods must be applied to a graph object created with `Graph()`. The `Graph` class is defined inside `cmsis_stream.cg.scheduler` from the cmsis-stream Python package.

```python
def connect(self,input_io,output_io,fifoClass=None,fifoScale = 1.0,fifoAsyncLength=0,buffer=None,customBufferMustBeArray=True):
```

Typically this method is used as:

```python
the_graph = Graph()

# Connect the source output to the processing node input and add this directed
# edge to the object the_graph
the_graph.connect(src.o,processing.i)
```

There are few optional arguments for the `connect` function:

* `fifoClass` : To use a different C++ class for implementing the connection between the two IOs. (it is also possible to change the FIFO class globally by setting an option on the graph. See below). The `FIFO` class is provided by default. Any new implementation must inherit from `FIFObase<T>`.  This must be a Python class name. This class is used to specify the name of the FIFO in the C++ and the argument to pass to the constructor (see below). Standard nodes may have to be modified to use a custom FIFO if the FIFOBase API must be changed.
* `fifoScale` : In asynchronous mode (deprecated), it is a scaling factor to increase the length of the FIFO compared to what has been computed by the synchronous approximation. This setting can also be set globally using the scheduler options. `fifoScale` is overriding the global setting. It must be a `float` (not an `int`).
* `fifoAsyncLength` : In fully asynchronous mode. It is the size to use for the FIFO
* `buffer`: Custom memory buffer to use for this FIFO. When a custom buffer is specified, the FIFO is no more participating to the memory optimization algorithm.
* `customBufferMustBeArray`: True if the custom buffer must be used only as an array

```python
def connectWithDelay(self,input_io,output_io,delay,fifoClass=None,fifoScale=1.0,fifoAsyncLength=0,buffer=None,customBufferMustBeArray=True):  
```

The only difference with the previous function is the `delay` argument. It could be used like:

```python
the_graph.connect(src.o,processing.i, 10)
```

The `delay` is the number of samples contained in the FIFO at start (initialized to zero). The FIFO length (computed by the scheduling) is generally bigger by this amount of sample. The result is that it is delaying the output by `delay` samples.

It is generally useful when the graph has some loops to make it schedulable.
