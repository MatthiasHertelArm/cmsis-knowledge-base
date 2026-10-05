---
id: "czep-zephyr-integration-with-cmsis-tool-ci-test-automation"
type: "concept"
domain: "project"
title: "Zephyr Integration with CMSIS-Toolbox: CI Test Automation"
summary: "This repository demonstrates a hybrid CI approach: build steps run on GitHub-hosted runners, while hardware execution runs on a self-hosted Raspberry Pi 5 (RPi5) runner connected to a NUCLEO board."
status: "draft"
collection: "cmsis-zephyr"
source: "Arm-Examples/CMSIS-Zephyr@ef8713c:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Zephyr/blob/ef8713c/README.md#ci-test-automation"
license: "Apache-2.0"
mode: "V"
---

This repository demonstrates a hybrid CI approach: build steps run on GitHub-hosted runners, while hardware execution runs on a self-hosted Raspberry Pi 5 (RPi5) runner connected to a NUCLEO board.

The [CI workflows](https://github.com/Arm-Examples/CMSIS-Zephyr/blob/ef8713c/./.github/workflows) provide full build coverage and hardware-in-the-loop (HIL) testing:

- [Build_All_Variants.yaml](https://github.com/Arm-Examples/CMSIS-Zephyr/blob/ef8713c/./.github/workflows/Build_All_Variants.yaml) builds every project, build type, and supported target combination.
- [Build_NUCLEO-H563ZI.yaml](https://github.com/Arm-Examples/CMSIS-Zephyr/blob/ef8713c/./.github/workflows/Build_NUCLEO-H563ZI.yaml) compiles the selected Zephyr application and produces build outputs that can be consumed by the run workflow.
- [Run_NUCLEO-H563ZI.yaml](https://github.com/Arm-Examples/CMSIS-Zephyr/blob/ef8713c/./.github/workflows/Run_NUCLEO-H563ZI.yaml) executes on the self-hosted RPi5 runner and uses an attached debug probe to download and execute the image on the target board.

The run workflow uses pyOCD to flash and run the application. To avoid duplicating board configuration in multiple places, the workflow relies on the generated `*.cbuild-run.yml` file for target information and uses the ID of the connected debug adapter to select the correct probe. Refer to the [CMSIS-Toolbox - Run and Debug Configuration](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#run-and-debug-configuration) for more information.

In the [GitHub Actions view of Run_NUCLEO-H563ZI.yaml](https://github.com/Arm-Examples/CMSIS-Zephyr/actions/workflows/Run_NUCLEO-H563ZI.yaml), you can review the test results:

- The application output is visible in the action log (for example via RTT-based console output).
- The workflow uploads a SEGGER SystemView trace (`*.SVdat`) as an artifact. This execution trace can be downloaded and analyzed offline.

See [Setup Self-Hosted GitHub Runner on Raspberry Pi 5](https://github.com/Arm-Examples/.github/blob/main/profile/RPI_GH_Runner.md) for details on configuring the self-hosted runner. It explains installing pyOCD and the required DFP and BSP packs for connecting to the target hardware.
