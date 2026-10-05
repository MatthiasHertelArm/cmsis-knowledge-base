---
id: "mlek-arm-ml-embedded-evaluation-kit-building"
type: "concept"
domain: "edge-ai"
title: "Arm® ML embedded evaluation kit: Building"
summary: "This section explains the build process and intra-project dependencies, describes how to build the code sample applications from sources and includes illustrating the build options and the process."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/documentation.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/documentation.md#building"
license: "Apache-2.0"
mode: "V"
---

This section explains the build process and intra-project dependencies, describes how to build the code sample
applications from sources and includes illustrating the build options and the process.

The following graph of source modules aims to explain better intra-project code and build execution dependencies.
(figure: intra-project dependencies)

The project can be built for MPS3 FPGA, MPS4 FPGA, FVP emulating MPS3 and FVP emulating MPS4.
Using default values for configuration parameters builds executable models that support the *Ethos-U* NPU.

For further information, please see:

- [Building the ML embedded code sample applications from sources](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#building-the-ml-embedded-code-sample-applications-from-sources)
  - [Build prerequisites](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#build-prerequisites)
  - [Build options](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#build-options)
  - [Build process](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#build-process)
    - [Preparing build environment](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#preparing-build-environment)
      - [Fetching submodules](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#fetching-submodules)
      - [Fetching resource files](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#fetching-resource-files)
    - [Create a build directory](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#create-a-build-directory)
    - [Configuring the build for MPS3 SSE-300](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#configuring-the-build-for-mps3-sse_300)
      - [Using GNU Arm embedded toolchain](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#using-gnu-arm-embedded-toolchain)
      - [Using Arm Compiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#using-arm-compiler)
      - [Generating project for Arm Development Studio](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#generating-project-for-arm-development-studio)
      - [Configuring with custom TPIP dependencies](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#configuring-with-custom-tpip-dependencies)
    - [Configuring the build for MPS3 SSE-310](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#configuring-the-build-for-mps3-sse_310)
    - [Configuring the build for MPS4 SSE-315](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#configuring-the-build-for-mps4-sse_315)
    - [Configuring the build for MPS4 SSE-320](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#configuring-the-build-for-mps4-sse_320)
    - [Configuring native unit-test build](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#configuring-native-unit_test-build)
    - [Building the configured project](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#building-the-configured-project)
  - [Building timing adapter with custom options](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#building-timing-adapter-with-custom-options)
  - [Add custom inputs](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#add-custom-inputs)
  - [Add custom model](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#add-custom-model)
  - [Optimize custom model with Vela compiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#optimize-custom-model-with-vela-compiler)
  - [Building for different Ethos-U NPU variants](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#building-for-different-ethos_u-npu-variants)
  - [Automatic file generation](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#automatic-file-generation)
