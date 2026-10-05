---
id: "helium-introduction-audiomark-description"
type: "concept"
domain: "optimization"
title: "Introduction: Audiomark Description"
summary: "Audiomark is a recent EEMBC benchmark, implementing a Keyword spotter pipeline involving a signal processing front-end consisting of a 2-microphones Acoustic Beamformer (ABF), an Acoustic Echo Canceller (AEC), an Acoustic Noise Reductor (ANR) and a MFCC spectral analyser."
status: "draft"
collection: "helium-optimization"
source: "Arm-Examples/Helium-Optimization@bc9dfb6:Performance_analysis/ml-dsp-front-end-optimization-with-helium.md"
doc_source: "https://github.com/Arm-Examples/Helium-Optimization/blob/bc9dfb6/Performance_analysis/ml-dsp-front-end-optimization-with-helium.md#audiomark-description"
license: "Apache-2.0"
mode: "V"
---

Audiomark is a recent EEMBC benchmark, implementing a Keyword spotter
pipeline involving a signal processing front-end consisting of a
2-microphones Acoustic Beamformer (**ABF**), an Acoustic Echo Canceller
(**AEC**), an Acoustic Noise Reductor (**ANR**) and a MFCC spectral
analyser. These components are mainly using single-precision floating
point (F32)

The ML back-end classifier consists of a of a DS-CNN Keyword Spotting
(**KWS**). This one mainly uses 8-bit data type operations. It is an
ARM-based model taken from the Arm Model Zoo.

 - <https://github.com/ARM-software/ML-zoo/tree/master/models/keyword_spotting/ds_cnn_small/model_package_tf/model_archive/TFLite/tflite_int8>

More details about the benchmark can be found here:

 - https://www.eembc.org/audiomark/index.php

The source code is available in Github at:

 - https://github.com/eembc/Audiomark

### Scoring

The Audiomark score shall be computed as **iterations per second \* 1000
\* 1.5**.

One iteration consists of an equivalent of processing 24000 samples
sampled at 16kHz.

The Audiomark/MHz score is simply the Audiomark score divided by the
highest core frequency in MHz.

### Helium and Ethos-U support

ABF, which was built from the ground up by EEMBC contributors is using
CMSIS-DSP for spectral transform (real and complex FFT), complex vector
operations (multiplications, dot-product, transpose) and other various
vector operations. As a result, it will automatically benefit from
Helium acceleration when compiled for cores supporting the vector
technology like Cortex-M55 or Cortex-M85.

AEC and ANR, based on LibSpeexDSP, include CMSIS-DSP with extra custom
Helium contributions from ARM. The rationale driving the optimization
additions will be described as follow.

KWS is using an ARM-native model, based on CMSIS-NN library, so as for
the DSP library, it automatically benefits from Helium.

EEMBC rules state that processing offloading is accepted. This will be
typically achieved via DSP, NPU, GPU or Custom Hardware. Arm is
providing Ethos-U55 support for Audiomark to perform KWS offload. We
will see how this could affect optimization decisions for the front-end.

# DSP front-end optimization stages
