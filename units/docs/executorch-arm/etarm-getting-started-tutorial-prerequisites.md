---
id: "etarm-getting-started-tutorial-prerequisites"
type: "concept"
domain: "edge-ai"
title: "Getting Started Tutorial: Prerequisites"
summary: "To successfully complete this tutorial, you will need a Linux machine with aarch64 or x86_64 processor architecture, or a macOS™ machine with Apple® Silicon."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@6368414:docs/source/backends/arm-ethos-u/tutorials/ethos-u-getting-started.md"
doc_source: "https://github.com/pytorch/executorch/blob/6368414/docs/source/backends/arm-ethos-u/tutorials/ethos-u-getting-started.md#prerequisites"
license: "BSD-3-Clause"
mode: "V"
---

### Hardware

To successfully complete this tutorial, you will need a Linux machine with aarch64 or x86_64 processor architecture, or a macOS™ machine with Apple® Silicon.

To enable development without a specific development board, we will be using a [Fixed Virtual Platform (FVP)](https://www.arm.com/products/development-tools/simulation/fixed-virtual-platforms), simulating [Arm® Corstone™-300](https://developer.arm.com/Processors/Corstone-300)(cs300) and [Arm® Corstone™-320](https://developer.arm.com/Processors/Corstone-320)(cs320)systems. Think of it as virtual hardware.

### Software

First, you will need to install ExecuTorch. Please follow the recommended tutorials to set up a working ExecuTorch development environment.

In addition to this, you need to install a number of SDK dependencies for generating Ethos-U command streams. Scripts to automate this are available in the main [ExecuTorch repository](https://github.com/pytorch/executorch/tree/main/examples/arm/).
To install Ethos-U dependencies, run
```bash
./examples/arm/setup.sh --i-agree-to-the-contained-eula
```
This will install:
- [TOSA Serialization Library](https://gitlab.arm.com/tosa/tosa-tools) for serializing the Exir IR graph into TOSA IR.
- [Ethos-U Vela graph compiler](https://pypi.org/project/ethos-u-vela/) for compiling TOSA flatbuffers into a Ethos-U command stream.
- [Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain) for cross compilation.
- [Corstone SSE-300 FVP](https://developer.arm.com/documentation/100966/1128/Arm--Corstone-SSE-300-FVP) for testing on Ethos-U55 reference design.
- [Corstone SSE-320 FVP](https://developer.arm.com/documentation/109760/0000/SSE-320-FVP) for testing on Ethos-U85 reference design.
