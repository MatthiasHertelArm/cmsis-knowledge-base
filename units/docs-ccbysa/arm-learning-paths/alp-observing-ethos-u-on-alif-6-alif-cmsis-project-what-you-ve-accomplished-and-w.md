---
id: "alp-observing-ethos-u-on-alif-6-alif-cmsis-project-what-you-ve-accomplished-and-w"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Create the Alif E8 CMSIS project: What you've accomplished and what's next"
summary: "You've now created the mnist_executorch firmware project, configured CMSIS packs, and set up the linker to include ExecuTorch libraries with the correct archive flags."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/6-alif-cmsis-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/6-alif-cmsis-project/#what-you-ve-accomplished-and-what-s-next"
license: "CC-BY-SA-4.0"
mode: "V"
---

You've now created the `mnist_executorch` firmware project, configured CMSIS packs, and set up the linker to include ExecuTorch libraries with the correct archive flags.

You've also added the application code that loads the model and runs inference on the Ethos-U85 NPU.

Next, you'll load and prepare a test image to copy into the firmware project.
