---
id: "helium-helium-optimization-topics-1-the-b-processor-initialization"
type: "concept"
domain: "optimization"
title: "Helium optimization topics #1 - the basics: Processor initialization"
summary: "Several steps are involved in the processor’s initialization. These are:"
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:General_optimizations/basic_optimization_topics.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/General_optimizations/basic_optimization_topics.md#processor-initialization"
license: "Apache-2.0"
mode: "V"
---

Several steps are involved in the processor’s initialization. These are:

- Enabling the Low-overhead branch feature
- Enabling the Helium hardware
- If needed, enabled the instruction and data caches – if the software is executed from memories with wait state, both instruction and data caches should be enabled because program image contains various read-only data which can benefit from caching.
- Enable branch predication if you are using the Cortex-M85 processor.
- Potentially, you need to adjust the power control settings in the Core Power Domain Low Power State Register (CPBLPSTATE).

The details of these processor initialization steps are covered in the following blog: [Getting started with Armv8.1-M based processor: software development hints and tips](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/armv8_2d00_m-based-processor-software-development-hints-and-tips)
