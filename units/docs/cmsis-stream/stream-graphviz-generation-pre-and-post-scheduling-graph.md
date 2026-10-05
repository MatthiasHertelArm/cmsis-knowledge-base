---
id: "stream-graphviz-generation-pre-and-post-scheduling-graph"
type: "concept"
domain: "cmsis-stream"
title: "Graphviz generation: Pre and post scheduling graph"
summary: "There are differences between the pre-schedule graph and the post-schedule graph:"
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/GraphvizGen.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/GraphvizGen.md#pre-and-post-scheduling-graph"
license: "Apache-2.0"
mode: "V"
---

There are differences between the pre-schedule graph and the post-schedule graph:

* In pre-schedule, you don't know the size of the FIFOs (in fact there is no FIFO)
* The `Duplicate` nodes (and additional FIFOs) have not been inserted to implement one-to-many outputs

### Pre-scheduling graph example

In this graph, all sinks are connected to the `oa` output of the `filter` node. That is not correct for the scheduling point of view since each output of the C++ implementation is connected to only one FIFO.

The scheduling phase will introduce a `Duplicate` node

The edges have no information of datatype or capacity (number of samples).

(figure: pre_schedule)

### Post-scheduling graph example

In this graph, datatype (`complex`) and capacity (`11` or `5` samples) have been added to the edges.

A `Duplicate` node has been inserted at the output `oa` of the `filter` node.

(figure: schedule)
