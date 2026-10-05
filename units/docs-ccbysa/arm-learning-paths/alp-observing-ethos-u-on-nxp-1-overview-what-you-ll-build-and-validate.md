---
id: "alp-observing-ethos-u-on-nxp-1-overview-what-you-ll-build-and-validate"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Understand ExecuTorch deployment on NXP with Ethos-U: What you’ll build and validate"
summary: "By the end of this Learning Path, you'll have:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/1-overview.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/1-overview/#what-you-ll-build-and-validate"
license: "CC-BY-SA-4.0"
mode: "V"
---

By the end of this Learning Path, you'll have:

- A `.pte` model artifact compiled for `ethos-u65-256`
- A Cortex-M33 `executor_runner` firmware image built against prebuilt ExecuTorch libraries
- A repeatable deployment flow that loads the firmware, runs inference, and reports results through the remoteproc trace buffer
