---
id: "stream-mathematical-principles-cyclo-static-scheduling"
type: "concept"
domain: "cmsis-stream"
title: "Mathematical principles: Cyclo static scheduling"
summary: "In case a node is not always producing or consuming the same amount of data, but is periodically doing so, we can reuse the previous theory and methods."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/MATHS.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/MATHS.md#cyclo-static-scheduling"
license: "Apache-2.0"
mode: "V"
---

In case a node is not always producing or consuming the same amount of data, but is periodically doing so, we can reuse the previous theory and methods.

If we look at a node `n` connected to other nodes, we know that if we want a possible schedule we need to find a periodic execution. 

The node `n` will see a similar environment only when all surrounding node periods have been executed. It implies that the node must be executed a number of times which is a multiple of the least common multiple of the periods.

For instance, if the node is connected to a node of period 3 and a node of period 5, then it is only after 15 executions minimum that we can expect to have a periodic execution. For less than 15 executions, one of the nodes will be still running its cycle. 

Of course, it does not mean that, from a data point of view, 15 may be enough. But we know that it will be a multiple of 15.

So we can reuse the previous theory if we assume that each node execution is in fact the least common multiple of the periods of the surrounding nodes.

Once we have computed the matrix and the scheduling solution, the details of the schedule are computed using a different granularity : the cycles are no more considered as a whole but instead  each execution step inside each cycle is used.

As consequence, the effect of the cyclo-static scheduling is just to increase the length of the final scheduling sequence since each node will have to be executed a number of times which is constrained by the least common multiples of the period of the connected nodes.
