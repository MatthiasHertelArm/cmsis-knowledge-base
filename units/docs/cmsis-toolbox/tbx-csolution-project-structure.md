---
id: "tbx-csolution-project-structure"
type: "concept"
domain: "project"
title: "CSolution Project Structure"
summary: "This chapter outlines the structure of csolution project files that contain the build information of the software application."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/"
license: "Apache-2.0"
mode: "V"
---

<!-- markdownlint-disable MD013 -->
<!-- markdownlint-disable MD036 -->
<!-- markdownlint-disable MD060 -->

This chapter outlines the structure of *csolution project files* that contain the build information of the software application.

- [Project Examples](#project-examples) and project templates help to get started with the tools.
- [Software Layers](#software-layers) provide reusable configurations  and give projects a better structure.
- [Directory Structure](#directory-structure) describes the overall directory structure of projects.
- [Linker Script Management](#linker-script-management) defines the  available memory and controls the linker operation.
- [Generator Support](#generator-support) integrates configuration tools such as STM32CubeMX or MCUXpresso Config.
- [Run and Debug Configuration](#run-and-debug-configuration) explains how to configure debug adapters such as CMSIS-DAP or J-Link.
- [West Build System Integration](#west-build-system-integration) allows to manage Zephyr applications in context with a *csolution project*.
- [MLOps Integration](#mlops-integration) describes how to generate an ML model layer and integrate it into an application.
