---
id: "mlek-arm-ml-embedded-evaluation-kit-implementing-custom-ml-application"
type: "concept"
domain: "edge-ai"
title: "Arm® ML embedded evaluation kit: Implementing custom ML application"
summary: "This section describes how to implement a custom Machine Learning application running on a platform supported by the repository, either an FVP or an MPS3 board."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/documentation.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/documentation.md#implementing-custom-ml-application"
license: "Apache-2.0"
mode: "V"
---

This section describes how to implement a custom Machine Learning application running on a platform supported by the
repository, either an FVP or an MPS3 board.

Both the *Cortex-M55* CPU and *Ethos-U* NPU Code Samples software project offers a way to incorporate extra use-case
code into the existing infrastructure. It also provides a build system that automatically picks up added functionality
and produces corresponding executable for each use-case.

For further information, please see:

- [Implementing custom ML application](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/customizing.md#implementing-custom-ml-application)
  - [Software project description](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/customizing.md#software-project-description)
  - [Hardware Abstraction Layer API](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/customizing.md#hardware-abstraction-layer-api)
  - [Main loop function](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/customizing.md#main-loop-function)
  - [Application context](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/customizing.md#application-context)
  - [Profiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/customizing.md#profiler)
  - [NN Model API](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/customizing.md#nn-model-api)
  - [Adding custom ML use-case](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/customizing.md#adding-custom-ml-use-case)
  - [Implementing main loop](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/customizing.md#implementing-main-loop)
  - [Implementing custom NN model](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/customizing.md#implementing-custom-nn-model)
  - [Executing inference](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/customizing.md#executing-inference)
  - [Printing to console](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/customizing.md#printing-to-console)
  - [Reading user input from console](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/customizing.md#reading-user-input-from-console)
  - [Output to MPS3 LCD](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/customizing.md#output-to-mps3-lcd)
  - [Building custom use-case](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/customizing.md#building-custom-use_case)
  - [Adding custom platform support](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/customizing.md#adding-custom-platform-support)
