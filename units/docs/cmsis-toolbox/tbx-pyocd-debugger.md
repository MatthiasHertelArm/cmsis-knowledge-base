---
id: "tbx-pyocd-debugger"
type: "concept"
domain: "debug"
title: "pyOCD Debugger"
summary: "The pyOCD Debugger connects to CMSIS-DAP (for example ULINKplus) or ST-Link debug adapters. The CMSIS-Toolbox defines the debug configuration as part of the csolution project, ensuring consistent debug sessions across development teams, CI/CD environments, and different host platforms."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/"
license: "Apache-2.0"
mode: "V"
---

<!-- markdownlint-disable MD033 -->

The pyOCD Debugger connects to CMSIS-DAP (for example ULINKplus) or ST-Link debug adapters.
The CMSIS-Toolbox defines the [debug configuration](https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/YML-Input-Format.md#debugger-configuration) as part of the *csolution project*, ensuring consistent debug sessions across development teams, CI/CD environments, and different host platforms.
This chapter describes how to use the [pyOCD](https://pyocd.io/) Debugger with the CMSIS-Toolbox.

- [Extended Options](#extended-options) explains additional configuration features that are required in specific use-cases.
- [Minimal Setup](#minimal-setup) explains how to create a `*.cbuild-run.yml` file for a minimal pyOCD setup.
- [Command Line Invocation](#command-line-invocation) describes how to call pyOCD directly from the command-line.
- [`cbuild-run:`](#cbuild-run) explains the configuration file that describes the overall pyOCD system setup.

Other manual sections describe how to configure debuggers:

- [Run and Debug Configuration](https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/build-overview.md#run-and-debug-configuration) explains overall structure and how projects and images are configured.
- [Debugger Configuration: pyOCD](https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/YML-Input-Format.md#pyocd) contains details about the options that are specific to pyOCD.
