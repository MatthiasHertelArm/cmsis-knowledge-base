---
id: "helium-helium-optimization-topics-3-proce-data-alignment"
type: "concept"
domain: "optimization"
title: "Helium optimization topics #3 - Processor specific details: Data alignment"
summary: "When using Helium instructions for data processing, in some cases data alignment can affect the performance:"
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:General_optimizations/processor_specific.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/General_optimizations/processor_specific.md#data-alignment"
license: "Apache-2.0"
mode: "V"
---

When using Helium instructions for data processing, in some cases data alignment can affect the performance:

- For minimum, vector data should be aligned to 32-bit boundaries. This is a requirement of the Helium instructions.
- For Armv8.1-M processors with dual-beat Helium implementations (i.e. Cortex-M55 and Cortex-M85), in some cases aligning vector data to 64-bit boundaries can gain a small performance improvement. For example:
  - When the vector data is expected to be fetched from the main memory instead of cache, having the data aligned to the bus width avoids an additional data access for the unaligned data.
  - When the processing involves certain 64-bit load store instructions
- When using cacheable memories, potentially aligning vector data to 4 word boundaries might help performance in some cases. For Cortex-M processors, the cachelines in the D-cache are 8 words in size. By aligning the vector data to 4 words boundaries it could reduce the number of linefill required when there is a cache miss.
