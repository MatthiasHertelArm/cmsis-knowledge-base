---
id: "tbx-overview-benefits"
type: "concept"
domain: "project"
title: "Overview: Benefits"
summary: "The overall benefits of the CMSIS-Toolbox are:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/overview/#benefits"
license: "Apache-2.0"
mode: "V"
---

The overall benefits of the CMSIS-Toolbox are:

- Common project information is used consistently from the command line, VS Code, and automated CI/DevOps workflows.

- Machine-readable build information connects smart editor features, static code analysis, and test tools to the application development workflow.

- Target information from CMSIS Packs is reused for programming, run and debug configuration, and trace workflows.

- [*Software packs*](https://www.keil.arm.com/packs/) simplify tool setup with `device:` or `board:` selection and provide access to reusable software components.

- Organize solutions with independent projects to support a wide range of use cases, including multi-processor applications or unit testing.

- Integrates with domain-specific [generators](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-overview.md#use-a-generator) (e.g., CubeMX or MCUXpresso Config Tools) for configuring devices/boards and complex software stacks such as motor control.

- Target types allow application deployment to different hardware (test board, production hardware, virtual simulation models, etc.).

- Build types support software testing and verification (debug build, test build, release build, etc.).

- Software layers enable code reuse across similar applications with a pre-configured set of source files and software components.

- [Linker Script Management](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-overview.md#linker-script-management) utilizes device and board information of *software packs* to define available memory and allows flexible control of linker operation.

- The [Run and Debug Configuration](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-overview.md#run-and-debug-configuration) collects all information to program and debug an application in a target system.

- [Product lifecycle management (PLM)](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-overview.md#plm-of-configuration-files) with versioned *software packs* that ease update and management for configuration files.

- Provides a [list of software licenses](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/YML-CBuild-Format.md#nodes-for-license-information) used by the various software packs and software components.

- Supports [MLOps integration](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-overview.md#mlops-integration) for generating AI layers and testing machine learning models that optionally use an NPU.
