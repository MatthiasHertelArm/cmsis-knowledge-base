---
id: "alp-silero-vad-ethos-u"
type: "concept"
domain: "edge-ai"
title: "Deploy Silero VAD on Arm Ethos-U with ExecuTorch"
summary: "Export a stateful Silero voice activity detection model with ExecuTorch, run it on an Arm Ethos-U85 Fixed Virtual Platform, and validate its output."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/_index.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/"
license: "CC-BY-SA-4.0"
mode: "V"
---

Export a stateful Silero voice activity detection model with ExecuTorch, run it on an Arm Ethos-U85 Fixed Virtual Platform, and validate its output.

**Who is this for:** This is an introductory topic for embedded machine learning developers who want to evaluate streaming audio inference with ExecuTorch on Arm Ethos-U.

**Learning objectives:**

- Set up ExecuTorch and the Arm development tools for Corstone-320 and Ethos-U85.
- Export and quantize a stateful Silero voice activity detection (VAD) model as a .pte file.
- Build and run a bare-metal voice activity detection application on a Corstone-320 Fixed Virtual Platform (FVP).
- Validate simulated speech probabilities against a host-generated reference.

**Prerequisites:**

- A Linux host using `x86_64` or `arm64`, or an Apple silicon macOS host
- Basic familiarity with PyTorch models and command-line development tools

**Steps:**

1. Prepare the environment and model inputs
2. Export Silero VAD for Ethos-U85
3. Build and run the Corstone-320 application
4. Validate the FVP speech probabilities

Time: about 45 minutes.
