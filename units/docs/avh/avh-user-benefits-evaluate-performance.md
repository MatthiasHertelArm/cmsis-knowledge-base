---
id: "avh-user-benefits-evaluate-performance"
type: "concept"
domain: "test"
title: "User Benefits: Evaluate Performance"
summary: "Software algorithms for digital signal processing (DSP) or machine learning (ML) frequently require significant CPU resources and need to be optimized for the target hardware."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/overview/src/benefits.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/overview/src/benefits.md#evaluate-performance"
license: "Apache-2.0"
mode: "V"
---

Software algorithms for digital signal processing (DSP) or machine learning (ML) frequently require significant CPU
resources and need to be optimized for the target hardware. Comparing performance of such "load heavy" algorithms
requires that they can be automatically executed with different configurations parameters but using identical input.

The timing in Arm FVP models is based on a instruction count, therefore it is not timing accurate. However, the results
can still be used for performance estimation and A/B comparison of algorithms.  

**Arm FVP** simulation models allow users to test their programs at scale with reproducible input patterns. This allows
you to validate and optimize application performance. Usage examples are:

- Compare speed of different implementations of an algorithm (A/B test).
- Optimize resources (i.e. RTOS memory buffers for stream processing) towards application requirements.
