---
id: "alp-observing-ethos-u-on-nxp-7-build-executorch-pte-what-you-ve-learned-and-what-s"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Build ExecuTorch models for Ethos-U65: What you've learned and what's next"
summary: "With both .pte files ready, you can now build the Cortex-M33 executor_runner firmware that will load and execute them."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/7-build-executorch-pte.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/7-build-executorch-pte/#what-you-ve-learned-and-what-s-next"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this section you've:

- Compiled a simple add model to verify the Ethos-U65 toolchain setup
- Built a MobileNet V2 `.pte` file with 100% NPU operator coverage
- Staged the models on your SD card for deployment

With both `.pte` files ready, you can now build the Cortex-M33 `executor_runner` firmware that will load and execute them.
