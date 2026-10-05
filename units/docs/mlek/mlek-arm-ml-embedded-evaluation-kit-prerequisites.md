---
id: "mlek-arm-ml-embedded-evaluation-kit-prerequisites"
type: "concept"
domain: "edge-ai"
title: "Arm® ML embedded evaluation kit: Prerequisites"
summary: "Before starting the setup process, please make sure that you have:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/documentation.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/documentation.md#prerequisites"
license: "Apache-2.0"
mode: "V"
---

Before starting the setup process, please make sure that you have:

- A Linux x86_64 based machine. If using Microsoft® Windows®, Windows Subsystem for Linux (WSL) is preferable.
  > **Note:** Currently, Microsoft® Windows® is not supported as a build environment.

- At least one of the following toolchains:
  - GNU Arm Toolchain (version 13.2.1 or above) -
  [GNU Arm Embedded toolchain downloads](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads)
  - Arm Compiler (version 6.22 or above) with a valid license -
  [Arm Compiler download Page](https://developer.arm.com/tools-and-software/embedded/arm-compiler/downloads)
  - Arm Toolchain for Embedded (version 19.1.5 or above) -
  [ATfE releases](https://github.com/arm/arm-toolchain/releases).
  Read more on ATfE [here](https://developer.arm.com/Tools%20and%20Software/Arm%20Toolchain%20for%20Embedded).
  Current level of support for ATfE, in this repository, is **experimental**.

- An Arm® MPS3 FPGA prototyping board and components for FPGA evaluation or an equivalent `Fixed Virtual Platform` binary:
  - An MPS3 board loaded with Arm® Corstone™-300 (`AN552`) or Corstone™-310 reference package (`AN555`). See
    [Download FPGA Images](https://developer.arm.com/downloads/-/download-fpga-images). You
    must have a USB connection between your machine and the MPS3 board - for UART menu and for deploying the
    application.
  - Both `Arm® Corstone™-300` and `Arm® Corstone™-310` based FVPs for MPS3 are available from:
    [Arm® Ecosystem FVPs](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps)
    and as [Arm® Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware)
- An Arm® MPS4 FPGA prototyping board and components for FPGA evaluation or an equivalent `Fixed Virtual Platform` binary:
  - An MPS4 board loaded with Arm® Corstone™-320 reference package. You
    must have a USB connection between your machine and the MPS4 board - for UART menu and for deploying the
    application.
  - Both `Arm® Corstone™-315` and `Arm® Corstone™-320` based FVPs for MPS4 are available from:
    [Arm® Ecosystem FVPs](https://developer.arm.com/tools-and-software/open-source-software/arm-platforms-software/arm-ecosystem-fvps)
    and as [Arm® Virtual Hardware](https://www.arm.com/products/development-tools/simulation/virtual-hardware)

> **Note:**: There are two Arm® Corstone™-300 implementations available for the MPS3 FPGA board - application
> notes `AN547` and `AN552`. We are aligned with the latest application note `AN552`. However, the application built
> for MPS3 target should work on both FPGA packages.

### Additional reading

This document contains information that is specific to Arm® Ethos™-U55, Arm® Ethos™-U65 and Arm® Ethos™-U85 products.
Please refer to the following documents for additional information:

- Arm® ML processors technical overview: <https://developer.arm.com/ip-products/processors/machine-learning>

- Arm® `Cortex-M55`® processor: <https://www.arm.com/products/silicon-ip-cpu/cortex-m/cortex-m55>

- Arm® `Cortex-M85`® processor: <https://www.arm.com/products/silicon-ip-cpu/cortex-m/cortex-m85>

- ML processor, also referred to as a Neural Processing Unit (NPU) - Arm® `Ethos™-U55`:
    <https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u55>

- ML processor, also referred to as a Neural Processing Unit (NPU) - Arm® `Ethos™-U65`:
    <https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u65>

- ML processor, also referred to as a Neural Processing Unit (NPU) - Arm® `Ethos™-U85`:
    <https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u85>

- Arm® MPS3 FPGA Prototyping Board:
   <https://www.arm.com/products/development-tools/development-boards/mps3>

- Arm® MPS4 FPGA Prototyping Board:
    <https://www.arm.com/products/development-tools/development-boards/mps4>

- Arm® Fixed Virtual Platforms: <https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms>

- Arm® Virtual Hardware: <https://www.arm.com/products/development-tools/simulation/virtual-hardware>

- Arm® ML-Zoo: <https://github.com/ARM-software/ML-zoo/>

- Arm® Ethos-U NPU™ software: <https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela>

To access Arm documentation online, please visit: <http://developer.arm.com>
