---
id: "alp-observing-ethos-u-on-nxp-9-build-executorch-runne-executorch-deployment-componen"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Build Cortex-M33 firmware for ExecuTorch: ExecuTorch deployment components"
summary: "In this section, you build the Cortex-M33 executor_runner firmware. You then deploy it to the FRDM i.MX 93 board."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/9-build-executorch-runner-for-cm33.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/9-build-executorch-runner-for-cm33/#executorch-deployment-components"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this section, you build the Cortex-M33 `executor_runner` firmware. You then deploy it to the FRDM i.MX 93 board.

This is a key milestone. You're proving you can control the real-time ML runtime for Ethos-U65 workloads.

On i.MX 93, Linux runs on the application cores, but the real-time ML runtime that talks to Ethos-U65 runs as **firmware on Cortex-M33**.
When you can build and boot your own `executor_runner`, you've proven that the microcontroller side of the system is under your control and ready to host ML workloads.

The project includes prebuilt ExecuTorch static libraries in the repository, so this section focuses on pulling the runner project, applying the required SDK patches, wiring it up to your toolchain, and building it.

In architectural terms:

- The application core (Linux) loads the firmware image and manages its lifecycle
- The Cortex-M33 firmware owns model execution and the delegate path into Ethos-U65
- The `.pte` model remains a separate artifact that you update independently
