---
id: "mlek-automatic-speech-recognition-code-introduction"
type: "concept"
domain: "edge-ai"
title: "Automatic Speech Recognition Code Sample: Introduction"
summary: "This document describes the process of setting up and running the Arm® Ethos™-U NPU Automatic Speech Recognition example."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/use_cases/asr.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/asr.md#introduction"
license: "Apache-2.0"
mode: "V"
---

This document describes the process of setting up and running the Arm® *Ethos™-U* NPU Automatic Speech Recognition
example.

Use-case code could be found in the following directory: [source/app/use_case/asr](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../../source/app/use_case/asr).

### Preprocessing and feature extraction

The preprocessing implementation is similar for both the *wav2letter* and *Conformer* versions of the
use case, however there are some differences.

#### Preprocessing for *wav2letter*

The *wav2letter* automatic speech recognition model that is used with the code samples, expects audio data to be
preprocessed in a specific way before performing an inference.

First, the audio data is normalized to the range (`-1`, `1`).

> **Note:** Mel-Frequency Cepstral Coefficients (MFCCs) are a common feature that is extracted from audio data and can
> be used as input for machine learning tasks such as keyword spotting and speech recognition. For implementation
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

(figure: ASR preprocessing)

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

#### Preprocessing for *Conformer*

For the *Conformer* version of the automatic speech recognition use case, the preprocessing differs from
what we have for *wav2letter*.

The process starts the same way, by normalising the audio input to the range (`-1`, `1`).

Next, we compute a Mel Spectrogram of the input audio sample.  For *wav2letter* we went a step further and
computed the MFCC from this spectrogram, but for *Conformer* the Mel Spectrogram is all we need.

Our implementation of the Mel Spectrogram computation is intended to be as close as possible
to that found in the
[torchaudio](https://docs.pytorch.org/audio/2.11.0/generated/torchaudio.transforms.MelSpectrogram.html) project,
as this was used for training the model.

Unlike *wav2letter* where we run inference for a sliding window over the input audio data,
for *Conformer* we consider the entire input audio clip at once up to a fixed length.
In the case of the specific *Conformer* model provided, the audio input length is 7 seconds
(this duration is a configurable parameter when training, quantizing and exporting the model).
For input audio clips shorter than this, we right-pad the Mel Spectrogram with a placeholder value of `-20.0`.
In our case, the input tensor is of size 700*80 where 80 is the number of mels
and 700 corresponds to each 100ms time interval for which spectrogram data has been calculated.

At this point, no further preprocessing is needed; unlike *wav2letter*,
we have no need to consider left/right contexts or compute first or second-order derivatives.
This input data is now ready to be passed into the model for inference.

### Postprocessing

The postprocessing between *wav2letter* and *Conformer* is similar, but there is more to consider for
the *wav2letter* use case as we have to combine model consecutive model outputs to get the final result.

#### Postprocessing for *wav2letter*

After performing an inference, the raw output must be postprocessed to get a usable result.

The raw output from the model is a tensor of shape 148x29 where each row is a probability distribution over the possible
29 characters that can appear at each of the 148 time steps.

This *wav2letter* model is trained using context windows. This means that, depending on the bit of the audio clip that
is currently being processed, only certain parts of the output are usable.

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

#### Postprocessing for *Conformer*

The output tensor for our *Conformer* model is of size 174*129, where 174 is the number of output tokens
(related to the audio input length, which is 15 seconds for our specific trained *Conformer* model)
and 129 is a probability distribution over the vocabulary range (the vocabulary size is a configurable
parameter of the SentencePiece tokeniser used in the *Conformer* training process).

Similarly to the *wav2letter* postprocessing, we take the highest probability token at each time step which is obtained
by taking the index of the highest value in the probability distribution (argmax) and looking up the corresponding
label from the vocabulary data.  We then deduplicate any repeating tokens and return the resulting string
as the decoded text.

### Prerequisites

See [Prerequisites](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../documentation.md#prerequisites)
