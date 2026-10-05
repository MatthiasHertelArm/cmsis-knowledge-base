---
id: "alp-silero-vad-ethos-u-3-run-on-fvp-build-executorch-for-cortex-m8"
type: "concept"
domain: "edge-ai"
title: "Deploy Silero VAD on Arm Ethos-U with ExecuTorch: Build and run the Corstone-320 application: Build ExecuTorch for Cortex-M85"
summary: "You already have the exported model and validation audio. You'll package both the model and audio into a bare-metal application and run the application on a virtual Cortex-M85 and Ethos-U85 system."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/3-run-on-fvp.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/3-run-on-fvp/#build-executorch-for-cortex-m85"
license: "CC-BY-SA-4.0"
mode: "V"
---

You already have the exported model and validation audio. You'll package both the model and audio into a bare-metal application and run the application on a virtual Cortex-M85 and Ethos-U85 system.

Start by building ExecuTorch for Cortex-M85.

Continue from the ExecuTorch repository root. Activate the environment and build the target libraries:

```bash
source .venv/bin/activate
source examples/arm/arm-scratch/setup_path.sh

cmake --preset arm-baremetal \
  -DCMAKE_BUILD_TYPE=Release \
  -B cmake-out-arm
cmake --build cmake-out-arm --target install --parallel
```

The installed libraries provide the ExecuTorch runtime, portable operators, and Ethos-U backend used by the application.
