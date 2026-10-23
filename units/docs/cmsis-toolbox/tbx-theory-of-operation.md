---
id: "tbx-theory-of-operation"
type: "concept"
domain: "project"
title: "Theory of Operation"
summary: "This chapter contains technical details about the operation of the CMSIS Toolbox."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-operation.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/"
license: "Apache-2.0"
mode: "V"
---

<!-- markdownlint-disable MD009 -->
<!-- markdownlint-disable MD013 -->
<!-- markdownlint-disable MD036 -->
<!-- markdownlint-disable MD060 -->

This chapter contains technical details about the operation of the CMSIS Toolbox.

- [Build Process Overview](#build-process-overview) details the build process.
- [Adding a Toolchain to CMSIS-Toolbox](#adding-a-toolchain-to-cmsis-toolbox) contains details about the Compiler support.
- [Native CMake Project Integration](#native-cmake-project-integration) describes direct orchestration of CMake projects.
- [CMake Script Integration with `executes:`](#cmake-script-integration-with-executes) describes CMake-based custom build steps.
- [West Integration](#west-integration) describes the integration of the West build system for Zephyr applications.
- [Generator Integration](#generator-integration) explains the integration of device configuration tools.
- [Debug Adapter Integration](#debug-adapter-integration) explains the integration of debuggers.
