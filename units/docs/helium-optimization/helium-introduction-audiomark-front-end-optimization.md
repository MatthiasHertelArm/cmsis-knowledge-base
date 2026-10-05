---
id: "helium-introduction-audiomark-front-end-optimization"
type: "concept"
domain: "optimization"
title: "Introduction: Audiomark Front-end optimization"
summary: "Enabling Helium leads DSP front-end to consume approximately 32.3 %, corresponding to 21.7 sec."
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:Performance_analysis/ml-dsp-front-end-optimization-with-helium.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Performance_analysis/ml-dsp-front-end-optimization-with-helium.md#audiomark-front-end-optimization"
license: "Apache-2.0"
mode: "V"
---

Enabling Helium leads DSP front-end to consume approximately **32.3 %**,
corresponding to **21.7 sec**.

Some parts have also automatically benefited from Helium, mainly thanks
to existing CMSIS-DSP calls in the ABF and MFCC, plus auto-vectorization
opportunities.

The global cycle repartition, gathered with the MDK Performance Analyser is now the
following:

| **Audiomark component**          | **contribution** |
|----------------------------------|:------------------:|
| Neural Net                       | **67.7%**            |
| Kiss FFT (AEC/ANR)               | 13.2%            |
| CMSIS-DSP FFT (ABF, MFCC)        | 2.0%             |
| ANR                              | 5.7%             |
| ABF                              | 3.6%             |
| AEC                              | 4.6%             |
| MFCC                             | 0.1%             |
| CMSIS-DSP misc. (ABF and MFCC)   | 1.5%             |
| Misc (memcpy, memset, math.lib.) | 1.8%             |


At this stage, further improvements in the front-end will start making
visible effects on the benchmark score.

Before digging into straight Helium conversion, it is recommended to try
identifying if certain CMSIS-DSP kernels could possibly be used as a
replacement of existing SW fragments.

This library covers most of the standard signal processing APIs, derived
for all data parts so it can be expected to find equivalence with some
of the DSP front-end parts.

Audiomark ANR and AEC components are based on the LibSpeexDSP libraries
which are heavily relying on traditional signal processing techniques
involving spectral manipulation involving Fourier Transform and other
vector operations and consequently, chances of finding suitable CMSIS
DSP kernels match are high.
