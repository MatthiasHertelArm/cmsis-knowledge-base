---
id: "alp-nav-mlek-sw-development-environment"
type: "concept"
domain: "edge-ai"
title: "Navigate Machine Learning development with Ethos-U processors: Software development considerations: Development environment"
summary: "You should use an x86_64 development machine running Windows or Linux for the best experience."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/nav-mlek/sw.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/nav-mlek/sw/#development-environment"
license: "CC-BY-SA-4.0"
mode: "V"
---

You should use an `x86_64` development machine running Windows or Linux for the best experience. 

The [Arm ML Evaluation Kit (MLEK)](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit) is not fully supported on Windows. Some of the required tools work only on Linux. Linux is recommended if you plan to use MLEK extensively. 

There are some ML examples which can be developed using Windows tools. 

The same development tools for general embedded projects are needed for ML applications, but there are additional tools and software which are also common in ML applications. 

### C/C++ Compilers 

You can build ML applications with [Arm Compiler for Embedded](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded/) or [Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain/). 

Use the install guides to install the compilers on your computer:
- [Arm Compiler for Embedded](https://learn.arm.com/install-guides/armclang/)
- [Arm GNU Toolchain](https://learn.arm.com/install-guides/gcc/arm-gnu/)
