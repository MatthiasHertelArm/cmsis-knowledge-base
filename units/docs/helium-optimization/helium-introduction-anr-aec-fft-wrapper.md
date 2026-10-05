---
id: "helium-introduction-anr-aec-fft-wrapper"
type: "concept"
domain: "optimization"
title: "Introduction: Audiomark Front-end optimization / ANR & AEC FFT wrapper"
summary: "Part of: Audiomark Front-end optimization"
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:Performance_analysis/ml-dsp-front-end-optimization-with-helium.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Performance_analysis/ml-dsp-front-end-optimization-with-helium.md#anr-aec-fft-wrapper"
license: "Apache-2.0"
mode: "V"
---

_Part of: Audiomark Front-end optimization_

LibSpeexDSP Spectral transformation is operated using a FFT wrapper,
allowing choosing platform specific optimized real FFTs. This greatly
simplifies the addition of CMSIS-DSP RFFT which should be called from
the **spx_fft/ spx_ifft** wrappers.

Since FFT output format is not standardized, care must be taken to
ensure that the optimized FFT samples order and scaling is consistent
with the original SW.

CMSIS-DSP F32 RFFT is producing its sample using a MATLAB-like order,
which does not match the expected LibSpeexDSP format, therefore extra
conversion is needed.

CMSIS-DSP RFFT output format is described in:

<https://arm-software.github.io/CMSIS-DSP/main/group__RealFFT.html>

All elements are complex pairs, even real DC and FO frequency elements
which have imaginary parts set to 0.

On the other hand, LibSpeexDSP, which makes use of default KISS FFT,
assumes an alternative format where the 1st element
containing DC frequency is real only, followed by complex pair of
spectral elements.

Is it also expected that forward FFT is scaling output data by the
inverse of FFT length and backward FFT by FFT length. CMSIS-DSP FFT is
scaling scheme is different, requiring extra gain corrections.

To avoid this sample reshuffling and rescaling stage, it is possible to
modify the AEC and ANR FFT consumers to work on the native CMSIS-DSP
order, but it could involve numerous changes across the LibSpeexDSP
library.

Given its marginal cost compared to FFT and the rest of the operations,
it is acceptable to keep it at the current optimization stage.
