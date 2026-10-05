---
id: "etarm-silero-vad-ethos-u-example"
type: "concept"
domain: "edge-ai"
title: "Silero VAD Ethos-U Example"
summary: "Voice activity detection (VAD) identifies whether each audio chunk contains speech. Silero VAD processes 512 audio samples per step, preserves recurrent state between steps, and produces a speech probability for each chunk."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:examples/arm/silero_vad_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/examples/arm/silero_vad_example_ethos_u/README.md"
license: "BSD-3-Clause"
mode: "V"
---

Voice activity detection (VAD) identifies whether each audio chunk contains
speech. Silero VAD processes 512 audio samples per step, preserves recurrent
state between steps, and produces a speech probability for each chunk.

This end-to-end example shows how to:

- load the Silero VAD JIT model, re-export it through PT2E
  quantization, and lower it for Ethos-U85.
- build a bare-metal Corstone-320 application that embeds the exported
  `.pte` and a 16 kHz mono WAV file.
- run the app on the Corstone-320 Fixed Virtual Platform (FVP), print
  speech probabilities over serial, and validate those probabilities on the
  host.
