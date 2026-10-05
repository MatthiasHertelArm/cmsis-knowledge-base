---
id: "helium-introduction-where-to-start"
type: "concept"
domain: "optimization"
title: "Introduction: Where to start"
summary: "As for any kind of SW optimization process, it is important to get a grasp on where and how cycles are spent across the application."
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:Performance_analysis/ml-dsp-front-end-optimization-with-helium.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Performance_analysis/ml-dsp-front-end-optimization-with-helium.md#where-to-start"
license: "Apache-2.0"
mode: "V"
---

As for any kind of SW optimization process, it is important to get a
grasp on where and how cycles are spent across the application.

For ML applications, the ratio between the DSP front-end contribution
and the NN back-end contribution is key to determine the level of
optimization which should be achieved. As an example, having a very low
level of cycle contribution in the front-end (let’s say \< 5%), will
tell us that the return of investment (ROI) for optimizing DSP routines
will be marginal and optimizations will not translate in evident
performance improvement.

For these categories, optimization should be limited to low-hanging
fruits and opportunistic type of improvements like replacing loops or
functions with CMSIS-DSP kernels.

Even if these are not immediately translating to a significant
performance boost, these will be beneficial for other generations of
products using the same software because guaranteed to stay aligned with
the latest architectures enhancements.

Enabling Helium for example is likely to change the DSP front-end
contribution versus NN back-end contribution ratio in favor of the first
one for 2 main reasons:

- 8-bit operations involved in a Neural Net will get a higher boost than
  16/32-bit operations involved in the DSP part

- Contrary to NN parts which are predominantly built with standard
  operators and completely covered by the CMSIS-NN library when based on
  TensorFlow Lite for Micro (TFLM) framework, the DSP front-end is never
  a pure aggregate of DSP library routines.

As a result, enabling Helium is generally increasing the relative
front-end contribution compared to its non-Helium counterpart, hence
increasing potential for optimization.

On the other side of the spectrum, enabling NN hardware offloading using
NPUs like Ethos-U will change the ratio even more drastically and
depending on the network, the NPU capabilities and the application
complexity, it is possible to have DSP front-end MCU contribution to be
significantly higher than Neural Network processing, which make
optimization stage even more relevant and necessary.

The following illustration summarize the relative DSP front-end / NN
back-end ratio evolution after Helium and NPU addition.


We will use Audiomark to illustrate these points in the next paragraphs.
