---
id: "mlek-keyword-spotting-and-automatic-spe-introduction"
type: "concept"
domain: "edge-ai"
title: "Keyword Spotting and Automatic Speech Recognition Code Sample: Introduction"
summary: "This document describes the process of setting up and running an example of sequential execution of the Keyword Spotting and Automatic Speech Recognition models on a Cortex-M CPU and Ethos-U NPU."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/use_cases/kws_asr.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/kws_asr.md#introduction"
license: "Apache-2.0"
mode: "V"
---

This document describes the process of setting up and running an example of sequential execution of the Keyword Spotting
and Automatic Speech Recognition models on a *Cortex-M* CPU and *Ethos-U* NPU.

The Keyword Spotting and Automatic Speech Recognition example demonstrates how to run multiple models sequentially.

A Keyword Spotting model is first run on the CPU. If a set keyword is detected on the remaining audio, then an Automatic
Speech Recognition model is run on the *Ethos-U* NPU.

The tensor arena memory region is reused between models to optimize application memory footprint.

The `Yes` keyword is used to trigger full command recognition following the keyword.

Use-case code could be found in the following directory: [source/app/use_case/kws_asr](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../../source/app/use_case/kws_asr).

> **NOTE**: This use case only supports `TensorFlow Lite Micro`.

### Preprocessing and feature extraction

In this use-case, there are two different models being used with different requirements for preprocessing. As such, each
preprocessing process is detailed as follows.

> **Note:** Automatic Speech Recognition only occurs if a keyword is detected in the audio clip.

By default, the KWS model is run purely on the CPU and **not** on the *Ethos-U55*.

#### Keyword Spotting Preprocessing

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

If the audio clip is longer than 16000 audio samples, then the initial starting position is offset by `16000/2 = 8000`
audio samples. From this new starting point, MFCC features for the next `16000` audio samples are calculated and another
inference is performed. In other words, do an inference for samples `8000-24000`.

> **Note:** Parameters of the MFCC feature extraction all depend on what was used during model training. These values
> are specific to each model.

If you try a different keyword spotting model that uses MFCC input, then values check to see if the values need changing
to match the new model.

In addition, MFCC feature extraction methods can vary slightly with different normalization methods or scaling being
used.

#### Automatic Speech Recognition Preprocessing

The *wav2letter* automatic speech recognition model that is used with the Code Samples expects audio data to be
preprocessed in a specific way before performing an inference. This section aims to provide an overview of the feature
extraction process used.

First, the audio data is normalized to the range (`-1`, `1`).

> **Note:** Mel-Frequency Cepstral Coefficients (MFCCs) are a common feature that is extracted from audio data and can
> be used as input for machine learning tasks. Such as keyword spotting and speech recognition. For implementation
> details, please refer to: `source/lib/mlek/common/Mfcc.hpp`

Next, a window of 512 audio samples is taken from the start of the audio clip. From these 512 samples, we calculate 13
MFCC features.

The whole window is shifted to the right by 160 audio samples and 13 new MFCC features are calculated. This process of
shifting and calculating is repeated until enough audio samples to perform an inference have been processed.

In total, this is 296 windows that each have 13 MFCC features calculated for them.

After extracting MFCC features, the first and second order derivatives of these features, regarding time, are
calculated.

These derivative features are then standardized and concatenated with the MFCC features (which also get standardized).
At this point, the input tensor has a shape of 296x39.

These extracted features are quantized and an inference is performed.

For longer audio clips, where multiple inferences must be performed, then the initial starting position is offset by
`(100*160) = 16000` audio samples. From this new starting point, MFCC and derivative features are calculated as before,
until there is enough to perform another inference.

Padding can be used if there are not enough audio samples for at least one inference. This step is repeated until the
whole audio clip has been processed. If there are not enough audio samples for a final complete inference, then the MFCC
features are padded by repeating the last calculated feature until an inference can be performed.

> **Note:** Parameters of the MFCC feature extraction all depend on what was used during model training. These values
> are specific to each model.\
If you switch to a different ASR model than the one supplied, then the feature extraction process could be completely
different to the one currently implemented.

The amount of time that audio samples that are offset for long audio clips is specific to the included *wav2letter*
model.

### Postprocessing

If a keyword is detected, then the ASR process is run and the raw output of that inference must be postprocessed to get
a usable result.

The raw output from the model is a tensor of shape 148x29 where each row is a probability distribution over the possible
29 characters that can appear at each of the 148 time steps.

This *wav2letter* model is trained using context windows. This means that, depending on the bit of the audio clip that
is being processed, only certain parts of the output are usable.

If this is the first inference, and multiple inferences are required, then ignore the final 49 rows of the output.
Similarly, if this is the final inference from multiple inferences, then ignore the first 49 rows of the output.

Finally, if this inference is not the last, or the first inference, then ignore the first and last 49 rows of the model
output.

> **Note:** If the audio clip is small enough, then the whole of the model output is usable and there is no need to
> throw away any of the outputs before continuing.

Once any rows have been removed, the final processing can be done. To process the output, the letter with the highest
probability at each time step is found first. Next, any letters that are repeated multiple times in a row are removed.

For example: [`t`, `t`, `t`, `o`, `p`, `p`] becomes [`t`, `o`, `p`]). Finally, the 29th blank token letter is removed
from the output.

For the final output, the results from all inferences are combined before decoding. What you are left with is then
displayed to the console.

### Prerequisites

See [Prerequisites](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../documentation.md#prerequisites)
