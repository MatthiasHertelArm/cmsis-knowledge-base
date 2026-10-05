---
id: "dsp-guidelines"
type: "concept"
domain: "optimization"
title: "Guidelines"
summary: "If you use dynamic objects in your algorithms and some temporaries need to be allocated, they'll generally be allocated through a malloc since the size is not known at build time. It can be an issue:"
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/guidelines.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/guidelines.md"
license: "Apache-2.0"
mode: "V"
---

If you use dynamic objects in your algorithms and some temporaries need to be allocated, they'll generally be allocated through a `malloc` since the size is not known at build time. It can be an issue:

* Cost of the memory allocation
* Fragmentations

If you need to allocate those temporaries very often then it may be better to write the algorithm in such a way that the temporary can be reused between different calls.

The function implementing your algorithm would have additional arguments for the temporary matrixes and vectors required in the algorithm.
