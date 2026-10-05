---
id: "helium-introduction-additional-abf-optimizations"
type: "concept"
domain: "optimization"
title: "Introduction: ML application optimization with Ethos-U55 / Additional ABF optimizations"
summary: "Part of: ML application optimization with Ethos-U55"
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:Performance_analysis/ml-dsp-front-end-optimization-with-helium.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Performance_analysis/ml-dsp-front-end-optimization-with-helium.md#additional-abf-optimizations"
license: "Apache-2.0"
mode: "V"
---

_Part of: ML application optimization with Ethos-U55_

Inspecting ABF time annotated sources ([ee_abf_f32.c](https://github.com/eembc/Audiomark/blob/main/src/ee_abf_f32.c#L70))
with the MDK Execution profiler points in the adaptation
loop where most of the cycles are spent. This one is running a loop of
64 iterations running complex conjugate and complex dot product over 6
elements.




This is not efficient for 2 main reasons, which were already mentioned
earlier concerning the use of the CMSIS DSP kernels:

- Vector size involved with 6 complex elements are tiny, and function
  call overhead might be bigger than effective arithmetic operations.

- Chaining CMSIS-DSP complex conjugate and complex dot product calls
  operating on small sizes, causes extra unwanted memory accesses in a
  temporary buffer. Values stored by the complex conjugate are
  immediately read by the complex dot product kernel. Fusing the two
  calls might be more judicious, even if there is no direct CMSIS-DSP
  Kernel equivalent doing these operations at once.


It can also be seen that few other vectorization opportunities are
missing in the loop.

*Note*: A new CMSIS DSP feature, which was experimental at the time of writing this text, enables operator fusion and removing temporary buffer management.
It is using advanced C++ template meta-programming and details can be found here:
https://arm-software.github.io/CMSIS-DSP/main/dsppp_intro.html
