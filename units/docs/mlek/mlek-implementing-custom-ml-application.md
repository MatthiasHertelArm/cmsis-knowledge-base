---
id: "mlek-implementing-custom-ml-application"
type: "concept"
domain: "edge-ai"
title: "Implementing custom ML application"
summary: "This section describes how to implement a custom Machine Learning application running on Arm® Corstone™-300 based FVP or on the Arm® MPS3 FPGA prototyping board."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/customizing.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/customizing.md"
license: "Apache-2.0"
mode: "V"
---

- [Implementing custom ML application](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#implementing-custom-ml-application)
  - [Software project description](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#software-project-description)
  - [Hardware Abstraction Layer API](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#hardware-abstraction-layer-api)
  - [Main loop function](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#main-loop-function)
  - [Application context](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#application-context)
  - [Profiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#profiler)
  - [NN Model API](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#nn-model-api)
  - [Adding custom ML use-case](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#adding-custom-ml-use-case)
  - [Implementing main loop](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#implementing-main-loop)
  - [Implementing custom NN model](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#implementing-custom-nn-model)
    - [Using GetModelPointer and GetModelLen methods](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#using-getmodelpointer-and-getmodellen-methods)
  - [Executing inference](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#executing-inference)
  - [Printing to console](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#printing-to-console)
  - [Output to MPS3 LCD](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#output-to-mps3-lcd)
  - [Building custom use-case](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#building-custom-use-case)
  - [Adding custom platform support](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#adding-custom-platform-support)

This section describes how to implement a custom Machine Learning application running on Arm® *Corstone™-300* based FVP
or on the Arm® MPS3 FPGA prototyping board.

The Arm® *Ethos™-U* code sample software project offers a way to incorporate more use-case code into the existing
infrastructure. It also provides a build system that automatically picks up added functionality and produces
corresponding executable for each use-case. This is achieved by following certain configuration and code implementation
conventions.

The following sign indicates the important conventions to apply:

> **Convention:** The code is developed using `C++17` and `C11` standards.
