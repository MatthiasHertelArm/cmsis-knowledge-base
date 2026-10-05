---
id: "mlek-noise-reduction-code-sample-how-the-default-neural-network-model-wor"
type: "concept"
domain: "edge-ai"
title: "Noise Reduction Code Sample: How the default neural network model works"
summary: "Instead of replicating a \"noisy audio in\" and \"clean audio out\" problem, a simpler version is defined. We use different frequency bands for the audio (22 in the original paper RNNoise: Learning Noise Suppression)."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/use_cases/noise_reduction.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/noise_reduction.md#how-the-default-neural-network-model-works"
license: "Apache-2.0"
mode: "V"
---

Instead of replicating a "noisy audio in" and "clean audio out" problem, a simpler version is
defined. We use different frequency bands for the audio (22 in the original paper
[RNNoise: Learning Noise Suppression](https://jmvalin.ca/demo/rnnoise/)). It is based on a scale like the "Mel scale"
or "Bark scale" and calculates the energies for each band. Using this type of scale, the bands get
divided up and the result is based on what is important to the human ear.

When we have a noisy audio clip, the model takes the energy levels of these different bands as
input. The model then tries to predict a value (called a gain), to apply to each frequency band. It
is expected that applying this gain to each band brings the audio back to what a "clean" audio
sample would have been like. It is like a 22-band equalizer, where we quickly adjust the level of
each band so that the noise is removed. However, the signal, or speech, still passes through.

In addition to the 22 band values calculated, the input features also include:

- First and second derivatives of the first 6 coefficients,
- The pitch period (1/frequency),
- The pitch gain for six bands,
- A value used to detect if speech is occurring.

This provides 42 feature inputs, `22 + 6 + 6 + 1 + 6 + 1 = 42`, and the model produces `22` (gain
values) outputs.

> **Note:** The model also has a second output that predicts if speech is occurring in the given
> sample.

The pre-processing works in a windowed fashion, on 20ms of the audio clip at a time, and the stride
is 10ms. So, for example, if we provide one second of audio this gives us `1000ms/10ms = 100` windows of
features and, therefore, an input shape of `100x42` to the model. The output shape of the model is
then `100x22`, representing the gain values to apply to each of the 100 windows.

These output gain values can then be applied to each corresponding window of the noisy audio clip,
producing a cleaner output.

For more information please refer to the original paper:
[A Hybrid DSP/Deep Learning Approach to Real-Time Full-Band Speech Enhancement](https://arxiv.org/pdf/1709.08243.pdf)
