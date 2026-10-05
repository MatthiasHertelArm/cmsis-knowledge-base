---
id: "armsw-cmsis-rtos2-validation"
type: "concept"
domain: "rtos"
title: "CMSIS-RTOS2 Validation"
summary: "This repository contains a test suite that validates CMSIS-RTOS2 implementations. It uses Arm Virtual Hardware to run a CI/CD flow to verify correct operation of the real-time operating systems (RTOS) under test on various Arm Cortex-M based processors."
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/CMSIS-RTOS2_Validation@f5e2c7f:README.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTOS2_Validation/blob/f5e2c7f/README.md"
license: "Apache-2.0"
mode: "V"
---

This repository contains a test suite that validates CMSIS-RTOS2 implementations. It uses [**Arm Virtual Hardware**](https://www.arm.com/virtual-hardware) to run a CI/CD flow to verify correct operation of the real-time operating systems (RTOS) under test on various Arm Cortex-M based processors.

**Arm Virtual Hardware** provides simulation models, software tooling, and infrastructure that can be integrated into CI/CD and MLOps development flows. The simulation models (called Arm Virtual Hardware Targets) are an implementation of a Cortex-M device sub-systems and are designed for complex software verification and testing. This allows simulation-based test automation of various software workloads, including unit tests, integration tests, and fault injection. Refer to the [Arm Virtual Hardware documentation](https://arm-software.github.io/AVH/main/overview/html/index.html) for more information.
