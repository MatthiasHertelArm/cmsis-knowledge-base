---
id: "tbx-overview-common-project-information-for-the-devel"
type: "concept"
domain: "project"
title: "Overview: Common Project Information for the Development Workflow"
summary: "A csolution project provides common project information for an embedded application. It combines the application structure and build configurations with device, board, and reusable software information from CMSIS Packs."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/overview/#common-project-information-for-the-development-workflow"
license: "Apache-2.0"
mode: "V"
---

A [*csolution project*](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-overview.md) provides common project information for an embedded application. It combines the application structure and [build configurations](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/YML-Input-Format.md#build-types) with device, board, and reusable software information from [CMSIS Packs](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/YML-Input-Format.md#packs).

The same common project information supports the [command line, VS Code, and automated CI/DevOps workflows](#command-line-and-ide-usage). It can orchestrate [CMSIS projects](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-overview.md#minimal-project-setup), [Zephyr applications built with West](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-overview.md#west-build-system-integration), and [native CMake projects](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-overview.md#native-cmake-build-integration).

CMSIS-Toolbox resolves this information into [machine-readable build information](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-overview.md#overview-of-operation). It connects [smart editor features](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-tools.md#ide-usage), [static code analysis](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-tools.md#static-code-analysis), and test tools to the application development workflow. This avoids duplicating project and target configuration in each tool.

Because CMSIS Packs describe the target hardware, the common project information can also configure [programming, run, and debug tools](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-overview.md#run-and-debug-configuration). The same concept extends to [trace](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/Experimental-Features.md#trace) and [MLOps](https://open-cmsis-pack.github.io/cmsis-toolbox/overview/build-overview.md#mlops-integration), connecting these activities to command-line, VS Code, and CI/DevOps workflows.
