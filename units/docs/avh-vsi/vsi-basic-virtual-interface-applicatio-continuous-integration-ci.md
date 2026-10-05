---
id: "vsi-basic-virtual-interface-applicatio-continuous-integration-ci"
type: "concept"
domain: "debug"
title: "Basic Virtual Interface Applications: Continuous Integration (CI)"
summary: "The underlying build system of Keil Studio uses the CMSIS-Toolbox and CMake. CI is effectively supported with:"
status: "draft"
collection: "avh-vsi"
source: "Arm-Examples/AVH-VSI@b897fa6:README.md"
doc_source: "https://github.com/Arm-Examples/AVH-VSI/blob/b897fa6/README.md#continuous-integration-ci"
license: "Apache-2.0"
mode: "V"
---

The underlying build system of [Keil Studio](https://www.keil.arm.com/) uses the [CMSIS-Toolbox](https://open-cmsis-pack.github.io/cmsis-toolbox/) and CMake. [CI](https://en.wikipedia.org/wiki/Continuous_integration) is effectively supported with:

- Tool installation based on a single [`vcpkg-configuration.json`](https://github.com/Arm-Examples/AVH-VSI/blob/b897fa6/./vcpkg-configuration.json) file for desktop and CI environments.
- CMSIS solution files (`*.csolution.yml`) that enable seamless builds in CI, for example using GitHub actions.

| 
 CI Workflow     | Description |
|---                                              |--- |
| [hello_vsi.yml](https://github.com/.github/workflows/hello_vsi.yml) | Build the application for a specific compiler, target, and build type configuration. Save the build output as artifact, execute the generated binary on model and save the FVP UART log as artifact.|
| [hello_video_vsi.yml](https://github.com/.github/workflows/hello_video_vsi.yml) | Build the application for a specific compiler and target pair. Save the build output as artifact. |
