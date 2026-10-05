---
id: "stream-faqs-sources-and-sinks"
type: "concept"
domain: "cmsis-stream"
title: "FAQs: Sources and Sinks"
summary: "The sinks and the sources are where the graph is connected to the system."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/FAQ.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/FAQ.md#sources-and-sinks"
license: "Apache-2.0"
mode: "V"
---

The sinks and the sources are where the graph is connected to the system.

In the implementation of the sinks and sources you may have to rely on an RTOS to synchronize with another thread or write code to interact with an interrupt. The CMSIS-Stream scheduler would probably run in its own thread. The sources and sinks may block the execution of the scheduler until enough data is available for the source or enough free memory is available for the sink to generate its data.

A simple way to create sources and sinks is to use RTOS queues. 

A schedule is generally interleaving the source and sink execution : **source** ... some other nodes ... **sink** ... some other nodes ... **source** ...

But for some graphs, it may not be possible and you may see successive executions of sources or sinks : **source** ... some other nodes ... **source** ... some other nodes ... **sink** ... some other nodes ... **sink** ...

The [simple example](https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Examples/simple/README.md) is an example of a graph where the scheduling is requiring successive executions of sources and sinks.

In that case, connection between the graph and the system will require more buffering and the graph will introduce more latency. You should try to modify the amount of samples produced and consumed by the nodes so that source and sink execution can be interleaved and the latency introduced by graph scheduling minimized.

For debugging it is sometimes useful to have a sink doing nothing. It is possible for a sink to do nothing with its data. But it still has to manage the FIFO by calling the `getReadBuffer` functions. The scheduling algorithm (in synchronous mode) is assuming that the same amount of data is read or written to a FIFO by a node at each execution. So FIFO pointers must be updated even if you don't want to read the content of thee FIFO or write to the content of the FIFO.
