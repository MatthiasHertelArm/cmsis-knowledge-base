---
id: "alp-observing-ethos-u-on-alif-5-prepare-firmware-artif-what-you-ve-accomplished-and-w"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Prepare the ExecuTorch model and static libraries for the Alif E8 CMSIS project: What yo"
summary: "You've now prepared the embedded ExecuTorch model (mnist_model_data.h), ExecuTorch headers (third_party/executorch/et_bundle/include), and the static libraries used by the firmware build (third_party/executorch/et_bundle/lib)."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/5-prepare-firmware-artifacts.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/5-prepare-firmware-artifacts/#what-you-ve-accomplished-and-what-s-next"
license: "CC-BY-SA-4.0"
mode: "V"
---

You've now prepared the embedded ExecuTorch model (`mnist_model_data.h`), ExecuTorch headers (`third_party/executorch/et_bundle/include`), and the static libraries used by the firmware build (`third_party/executorch/et_bundle/lib`).

Next, you'll create the MNIST firmware project by duplicating the Blinky example and replacing relevant files to fit the application.
