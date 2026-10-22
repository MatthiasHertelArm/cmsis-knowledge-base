---
id: "mlek-building-the-ml-embedded-code-samp"
type: "concept"
domain: "edge-ai"
title: "Building the ML embedded code sample applications from sources"
summary: "This section assumes that you are using an x86_64 Linux build machine."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/building.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/building.md"
license: "Apache-2.0"
mode: "V"
---

- [Building the ML embedded code sample applications from sources](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#building-the-ml-embedded-code-sample-applications-from-sources)
  - [Build prerequisites](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#build-prerequisites)
    - [Third-party build prerequisites](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#third-party-build-prerequisites)
  - [Build options](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#build-options)
  - [Build process](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#build-process)
    - [Preparing build environment](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#preparing-build-environment)
      - [Fetching submodules](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#fetching-submodules)
      - [Fetching resource files](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#fetching-resource-files)
    - [Building for default configuration](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#building-for-default-configuration)
    - [Create a build directory](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#create-a-build-directory)
    - [Configuring the build for MPS3 SSE-300](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#configuring-the-build-for-mps3-sse_300)
      - [Using GNU Arm Embedded toolchain](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#using-gnu-arm-embedded-toolchain)
      - [Using Arm Compiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#using-arm-compiler)
      - [Using Arm Toolchain for Embedded](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#using-arm-toolchain-for-embedded)
      - [Configuring applications to run with single sample input](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#configuring-applications-to-run-with-single-sample-input)
      - [Generating project for Arm Development Studio](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#generating-project-for-arm-development-studio)
      - [Configuring with custom TPIP dependencies](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#configuring-with-custom-tpip-dependencies)
    - [Configuring the build for MPS3 SSE-310](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#configuring-the-build-for-mps3-sse_310)
    - [Configuring the build for MPS4 SSE-315](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#configuring-the-build-for-mps4-sse_315)
    - [Configuring the build for MPS4 SSE-320](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#configuring-the-build-for-mps4-sse_320)
    - [Configuring native unit-test build](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#configuring-native-unit_test-build)
    - [Building with CMake Presets](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#building-with-cmake-presets)
    - [Building the configured project](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#building-the-configured-project)
  - [Building timing adapter with custom options](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#building-timing-adapter-with-custom-options)
  - [Add custom inputs](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#add-custom-inputs)
  - [Add custom model](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#add-custom-model)
  - [Optimize custom model with Vela compiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#optimize-custom-model-with-vela-compiler)
  - [Building for different Ethos-U NPU variants](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#building-for-different-ethos_u-npu-variants)
  - [Automatic file generation](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#automatic-file-generation)

This section assumes that you are using an **x86_64 Linux** build machine.
