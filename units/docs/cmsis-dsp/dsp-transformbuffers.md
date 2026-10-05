---
id: "dsp-transformbuffers"
type: "concept"
domain: "optimization"
title: "transformbuffers"
summary: "Transform buffer sizes ======================"
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/transformbuffers.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/transformbuffers.md"
license: "Apache-2.0"
mode: "V"
---

Transform buffer sizes
======================

An empty entry in a table means 'Not Applicable'.
For instance, no temporary buffer is needed for a specific configuration.

'X' means configuration is not supported.

All returned lengths are in real numbers. The number of input samples is the transform length.


Several functions are available in the C and Python API to compute the buffer sizes at runtime.
