---
id: "alp-silero-vad-ethos-u-1-prepare-environment-understand-the-workflow"
type: "concept"
domain: "edge-ai"
title: "Deploy Silero VAD on Arm Ethos-U with ExecuTorch: Prepare the environment and model inputs: Understand the workflow"
summary: "Voice activity detection (VAD) classifies short audio frames as speech or silence. VAD is useful for voice assistants, transcription pipelines, and other systems that should avoid processing silent audio."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/1-prepare-environment.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/1-prepare-environment/#understand-the-workflow"
license: "CC-BY-SA-4.0"
mode: "V"
---

Voice activity detection (VAD) classifies short audio frames as speech or silence. VAD is useful for voice assistants, transcription pipelines, and other systems that should avoid processing silent audio.

You'll deploy the 16 kHz Silero VAD model with ExecuTorch. The workflow quantizes the model, lowers supported operations to the Arm Ethos-U backend, builds a bare-metal application, and runs it on a Corstone-320 Fixed Virtual Platform (FVP). You don't need a physical development board.

The application processes 512 audio samples every 32 ms. It keeps the long short-term memory (LSTM) hidden and cell state inside the ExecuTorch program between frames, then produces one speech probability for each frame.

The host uses the validation clip to generate reference probabilities. The bare-metal application processes the same clip on the FVP. The final comparison verifies that both paths produce the same speech decisions.

(figure: Three-lane workflow showing host preparation from the Silero model and source audio to a stateful PTE, virtual target execution from the embedded PTE and validation audio to an FVP log, and host verification that compares reference probabilities with the FVP result.#center)

Use the FVP for functional validation. The FVP's Ethos-U model is cycle accurate, but don't use its Cortex-M CPU model for CPU performance measurements.
