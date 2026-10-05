---
id: "stream-memory-optimizations-duplicate-node-optimizations"
type: "concept"
domain: "cmsis-stream"
title: "Memory optimizations: Duplicate node optimizations"
summary: "This optimization is enabled when memoryOptimization is enabled. It is experimental and can be disabled with disableDuplicateOptimization."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Memory.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Memory.md#duplicate-node-optimizations"
license: "Apache-2.0"
mode: "V"
---

This optimization is enabled when `memoryOptimization` is enabled. It is experimental and can be disabled with `disableDuplicateOptimization`.

Generally, the input and output FIFOs of a node are active at the same time and thus cannot share a buffer.

For the `Duplicate` node, this constraint is relaxed and in some case the output FIFOs are not considered active at the same time as the input one. It enables the input and outputs to share buffers.

When FIFOs are sharing buffers, they are not generated in the C++ initialization of the `Duplicate` node so that copy will occur only for a subset of the FIFOs in the `Duplicate` node.
