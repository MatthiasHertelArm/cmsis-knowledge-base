---
id: "alp-silero-vad-ethos-u-2-run-example-prepare-to-export-the-model"
type: "concept"
domain: "edge-ai"
title: "Deploy Silero VAD on Arm Ethos-U with ExecuTorch: Export Silero VAD for Ethos-U85: Prepare to export the model"
summary: "You prepared the model and two audio clips earlier. Now, use the calibration clip to quantize Silero VAD and the validation clip to create a host reference."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/2-run-example.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/2-run-example/#prepare-to-export-the-model"
license: "CC-BY-SA-4.0"
mode: "V"
---

You prepared the model and two audio clips earlier. Now, use the calibration clip to quantize Silero VAD and the validation clip to create a host reference.

From the ExecuTorch repository root, activate the environment:

```bash
source .venv/bin/activate
source examples/arm/arm-scratch/setup_path.sh
```
