---
id: "helium-helium-optimization-topics-1-the-b-selection-of-data-types"
type: "concept"
domain: "optimization"
title: "Helium optimization topics #1 - the basics: Selection of data types"
summary: "Helium technology supports the following data types:"
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:General_optimizations/basic_optimization_topics.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/General_optimizations/basic_optimization_topics.md#selection-of-data-types"
license: "Apache-2.0"
mode: "V"
---

Helium technology supports the following data types:

- 8-bit integer
- 16-bit integer
- 32-bit integer
- 64-bit integer – limited to a few shift instructions (SQRSHRL, UQRSHLL), predication operations and memory accesses.
16-bit floating-point (Note: IEEE-754 version, not bfloat)
- 32-bit single floating-point

While current Armv8.1-M processor supports double precision floating-point data processing, it is for scalar operations only and not in form of vector processing / SIMD. Typically, using a small data type can give better performance because Helium instructions can process more data elements at the same time.
For some software developers, the half precision floating-point data type could be new to them. In C programming, half precision floating-point data are declared as _Float16. More information on this topics can be found near the end of this page [Getting started with Armv8.1-M based processor: software development hints and tips](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/armv8_2d00_m-based-processor-software-development-hints-and-tips).
