---
id: "avh-simulation-models"
type: "concept"
domain: "test"
title: "Simulation Models"
summary: "Arm FVP simulation models are standalone programs that gets executed in the target environment and enable execution of firmware programs on virtual targets. They are:"
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:DoxyGen/overview/src/main.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/overview/src/main.md"
license: "Apache-2.0"
mode: "V"
---

Arm FVP simulation models are standalone programs that gets executed in the target environment and enable execution of
firmware programs on virtual targets. They are:

- Precise simulation models of Arm Cortex-M based reference platforms, such as Corstone-3xx. Learn more at
  [Simulation](https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/overview/src/../../simulation/html/index.html).
- Available for cloud-native and desktop environments. See [Infrastructure](https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/overview/src/../../infrastructure/html/index.html) for
  details.

# Infrastructure

Arm Virtual Hardware models integrate well in various tools and services for development, debug, testing as well as
CI/CD and MLOps flows. Arm FVPs are already supported within many Arm tools, as well as by third-party vendors. See
[Infrastructure](https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/overview/src/../../infrastructure/html/index.html) for more details.

# Developer Resources

Various resources explain how to integrate Arm Virtual Hardware into workflows common for generic embedded software
development, CI testing and MLOps.

Usage examples show typical use cases and range from audio processing, ML algorithm testing, up to IoT applications
that interface to cloud service providers and over-the-air firmware Updates (OTA).

This documentation is structured into following chapters:

Chapter                                                    | Description
:----------------------------------------------------------|:--------------------
[**Overview**](https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/overview/src/index.html)                                 | Introduces **Arm Virtual Hardware** along with the top-level structure.
[**Simulation**](https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/overview/src/../../simulation/html/index.html)         | Explains the FVP simulation technology and the virtual interfaces.
[**Infrastructure**](https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/overview/src/../../infrastructure/html/index.html) | Describes key integrations of FVPs locally and in the cloud.
[**Examples**](https://github.com/ARM-software/AVH/blob/bb8431b/DoxyGen/overview/src/../../examples/html/index.html)             | Guides through the examples that demonstrate how to use FVPs.

# Feedback and Support

Use the [Issues](https://github.com/ARM-software/AVH/issues) tab on the GitHub repository to raise any concerns.
