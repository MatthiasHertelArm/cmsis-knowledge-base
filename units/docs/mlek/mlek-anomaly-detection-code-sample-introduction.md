---
id: "mlek-anomaly-detection-code-sample-introduction"
type: "concept"
domain: "edge-ai"
title: "Anomaly Detection Code Sample: Introduction"
summary: "This document describes the process of setting up and running the Arm® Ethos™-U NPU Anomaly Detection example."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/use_cases/ad.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/ad.md#introduction"
license: "Apache-2.0"
mode: "V"
---

This document describes the process of setting up and running the Arm® *Ethos™-U* NPU Anomaly Detection example.

Use-case code could be found in the following directory: [source/app/use_case/ad](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../../source/app/use_case/ad).

> **NOTE**: This use case only supports `TensorFlow Lite Micro`.

### Preprocessing and feature extraction

The Anomaly Detection model that is used with the Code Samples and expects audio data to be preprocessed in a specific
way before performing an inference.

Therefore, this section provides an overview of the feature extraction process used.

First, the audio data is normalized to the range (`-1`, `1`).

Next, a window of 1024 audio samples is taken from the start of the audio clip. From these 1024 samples, we calculate 64
Log Mel Energies that form part of a Log Mel Spectrogram.

The window is shifted by 512 audio samples and another 64 Log Mel Energies are calculated. This is repeated until we
have 64 sets of Log Mel Energies.

This 64x64 matrix of values is then resized by a factor of two, resulting in a 32x32 matrix of values.

The average of the training dataset is then subtracted from this 32x32 matrix and an inference can now be performed.

We start this process again, but shift the start by 20\*512=10240 audio samples. This keeps repeating until enough
inferences have been performed to cover the whole audio clip.

### Postprocessing

Softmax is then applied to the result of each inference. Based on the machine ID of the wav clip being processed, we
look at a specific index in each output vector. An average of the negative value at this index across all the inferences
performed for the audio clip is taken.

If this average value is greater than a chosen threshold score, then the machine in the clip is not behaving
anomalously. If the score is lower than the threshold, then the machine in the clip is behaving anomalously.

### Prerequisites

See [Prerequisites](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../documentation.md#prerequisites)
