---
id: "helium-introduction"
type: "concept"
domain: "optimization"
title: "Introduction"
summary: "Most of the ML applications generally use a 2-parts DSP front-end and Neural Network back-end structure."
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:Performance_analysis/ml-dsp-front-end-optimization-with-helium.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Performance_analysis/ml-dsp-front-end-optimization-with-helium.md"
license: "Apache-2.0"
mode: "V"
---

Most of the ML applications generally use a 2-parts DSP front-end and
Neural Network back-end structure.

A DSP Front is needed to reduce the Neural Net complexity as running
brute force ML operations on raw corrupted signals, whatever the signal
nature, which can be audio, vibration, or image, is likely to involve
much bigger networks to reach similar level of performance than smaller
networks operating on cleaned signals.

The DSP front-end typically runs on DSPs or MCUs having good DSP
performance like Cortex-M with Helium.

For illustration of typical ML DSP front-end optimization techniques, we
will use the EEBMC Audiomark benchmark which aimed mimicking a real life
KWS pipeline, running on Cortex-M55.

The techniques described in this document/chapter are not specific to ML
applications, but the presence of the Neural Net software stack has
implication on which parts need to be addressed and how far optimization
should be conducted.

*Note*: All Audiomark scores and profiling data mentioned in this document
are subject to change, depending on platform, toolchain, and library in
use.
