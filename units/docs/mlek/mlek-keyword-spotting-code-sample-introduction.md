---
id: "mlek-keyword-spotting-code-sample-introduction"
type: "concept"
domain: "edge-ai"
title: "Keyword Spotting Code Sample: Introduction"
summary: "This document describes the process of setting up and running the Arm® Ethos™-U NPU Keyword Spotting example."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/use_cases/kws.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/kws.md#introduction"
license: "Apache-2.0"
mode: "V"
---

This document describes the process of setting up and running the Arm® *Ethos™-U* NPU Keyword Spotting example.

Use-case code could be found in the following directory: [source/app/use_case/kws](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../../source/app/use_case/kws).

> **NOTE**: This use case only supports `TensorFlow Lite Micro`.

### Preprocessing and feature extraction

The `MicroNet` keyword spotting model that is used with the Code Samples expects audio data to be preprocessed in a
specific way before performing an inference.

Therefore, this section aims to provide an overview of the feature extraction process used.

First, the audio data is normalized to the range (`-1`, `1`).

> **Note:** Mel-Frequency Cepstral Coefficients (MFCCs) are a common feature that is extracted from audio data and can
> be used as input for machine learning tasks such as keyword spotting and speech recognition. For implementation
> details, please refer to: `source/lib/mlek/common/Mfcc.hpp`

Next, a window of 640 audio samples is taken from the start of the audio clip. From these 640 samples, we calculate 10
MFCC features.

The whole window is shifted to the right by 320 audio samples and 10 new MFCC features are calculated. This process of
shifting and calculating is repeated until the end of the 16000 audio samples required to perform an inference is
reached.

In total, this is 49 windows that each have 10 MFCC features calculated for them, giving an input tensor of shape 49x10.

These extracted features are quantized and an inference is performed.

(figure: KWS preprocessing)

If the audio clip is longer than 16000 audio samples, then the initial starting position is offset by `16000/2 = 8000`
audio samples. From this new starting point, MFCC features for the next `16000` audio samples are calculated and another
inference is performed. In other words, do an inference for samples `8000-24000`.

> **Note:** Parameters of the MFCC feature extraction all depend on what was used during model training. These values
> are specific to each model.\
If you try a different keyword spotting model that uses MFCC input, then values check to see if the values need changing
to match the new model.

In addition, MFCC feature extraction methods can vary slightly with different normalization methods or scaling being
used.

### Postprocessing

After an inference is complete, the word with the highest detected probability is output to console. Providing that the
probability is larger than a threshold value. The default is set to `0.7`.

If multiple inferences are performed for an audio clip, then multiple results are output.

### Prerequisites

See [Prerequisites](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../documentation.md#prerequisites)
