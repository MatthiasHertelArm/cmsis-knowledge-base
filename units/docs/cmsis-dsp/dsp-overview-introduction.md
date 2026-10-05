---
id: "dsp-overview-introduction"
type: "concept"
domain: "optimization"
title: "Overview: Introduction"
summary: "This user manual describes the CMSIS DSP software library, a suite of common compute processing functions for use on Cortex-M and Cortex-A processor based devices."
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/mainpage.md#introduction"
license: "Apache-2.0"
mode: "V"
---

This user manual describes the CMSIS DSP software library, a suite of common compute processing functions for use on Cortex-M and Cortex-A processor based devices.

The library is divided into a number of functions each covering a specific category:

 - Basic math functions
 - Fast math functions
 - Complex math functions
 - Filtering functions
 - Matrix functions
 - Transform functions
 - Motor control functions
 - Statistical functions
 - Support functions
 - Interpolation functions
 - Support Vector Machine functions (SVM)
 - Bayes classifier functions
 - Distance functions
 - Quaternion functions
 - Window functions

The library has generally separate functions for operating on 8-bit integers, 16-bit integers, 32-bit integer and 32-bit floating-point values and 64-bit floating-point values.

The library is providing vectorized versions of most algorithms for Helium and of most f32 algorithms for Neon.

When using a vectorized version, provide a little bit of padding after the end of a buffer (3 words) because the vectorized code may read a little bit after the end of a buffer. You don't have to modify your buffers but just ensure that the end of buffer + padding is not outside of a memory region.
