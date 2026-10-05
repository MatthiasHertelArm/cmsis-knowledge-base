---
id: "mlek-memory-considerations-introduction"
type: "concept"
domain: "edge-ai"
title: "Memory considerations: Introduction"
summary: "This section provides useful details on how the Machine Learning use-cases of the evaluation kit use the system memory."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/memory_considerations.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/memory_considerations.md#introduction"
license: "Apache-2.0"
mode: "V"
---

This section provides useful details on how the Machine Learning use-cases of the evaluation kit use the system memory.

Although the guidance provided here is concerning the Arm® *Corstone™-300* system, it is fairly generic and is
applicable for other platforms too. The Arm® *Corstone™-300* is composed of both the Arm® *Cortex™-M55* and the Arm®
*Ethos™-U* NPU. The memory map for the Arm® *Cortex™-M55* core can be found in the [Appendix](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./appendix.md#appendix).

The Arm® *Ethos™-U* NPU interacts with the system through two AXI interfaces. The first one, is envisaged to be the
higher-bandwidth, lower-latency, interface. In a typical system, this is wired to an SRAM as it is required to service
frequent read and write traffic.

The second interface is expected to have a higher-latency, lower-bandwidth characteristic, and is typically wired to a
flash device servicing read-only traffic. In this configuration, the Arm® *Cortex™-M55* CPU and Arm® *Ethos™-U* NPU
read the contents of the neural network model from the flash memory region. With the Arm® *Ethos™-U* NPU requesting
these read transactions over its second AXI bus.

The input and output tensors, along with any intermediate computation buffers, are placed on SRAM. Therefore, both the
Arm® *Cortex™-M55* CPU and Arm® *Ethos™-U* NPU would be reading, or writing, to this region when running an inference.
The Arm® *Ethos™-U* NPU requests these Read and Write transactions over the first AXI bus.
