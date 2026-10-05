---
id: "stream-faqs-latencies"
type: "concept"
domain: "cmsis-stream"
title: "FAQs: Latencies"
summary: "The compute graph schedule is computed only based on the dataflow dependencies and with an attempt at minimizing the FIFO sizes."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/FAQ.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/FAQ.md#latencies"
license: "Apache-2.0"
mode: "V"
---

The compute graph schedule is computed only based on the dataflow dependencies and with an attempt at minimizing the FIFO sizes.

No other constraint is used. But in a real application, it is not enough. For instance, this kind of scheduling would be acceptable from a pure data flow point of view (ignoring FIFO sizes for this example):

* source, source, sink, sink

But from a latency point of view it would not be good and the following schedule should be prefered:

* source, sink, source, sink 

The scheduling algorithm is thus using a topological sort of the compute graph to try to schedule the sinks as soon as possible in order to minimize the source to sink latency. This optimization is disabled when the graph has some loops because in this case there is no possible topological sort.

But, even with topological sorting, there may be cases where the latency is unavoidable without changing the amount of samples read and written by the nodes. In a dynamic scheduler it is something which is more difficult to track. With a static scheduler you can see it in the generated schedule.

As an example, if you use 10 ms audio blocks at 16 kHz you get 160 samples.

Now, if you want to want to compute a FFT of 256 samples (smallest power of 2 > 160), then you'll need to receive 2 audio blocks before you can start to compute the FFT and generate output samples.

So, in the generated schedule you'll see sequences like :

* source, source ... sink 

which is showing there will be a latency issue. The connection between the sink and an audio DMA will require more buffers than with a schedule like source ... sink ... source ... sink.

To solve this problem you need either to:

* Use different length for the audio blocks
* Use a FFT which is not a power of 2
