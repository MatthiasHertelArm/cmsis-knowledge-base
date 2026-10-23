---
id: "tbx-experimental-features-configuration-files"
type: "concept"
domain: "project"
title: "Experimental Features: Trace / Configuration Files"
summary: "Trace setup is split between target infrastructure configuration and capture configuration."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#configuration-files"
license: "Apache-2.0"
mode: "V"
---

_Part of: Trace_

Trace setup is split between target infrastructure configuration and capture configuration.

Configuration File             | Description
:------------------------------|:------------------------------------
`*.csolution.yml`              | Selects the solution-set and debug adapter. It may also reference solution-set specific debugger configuration files.
`.cmsis/*.dbgconf`             | Optional solution-set specific debugger configuration, for example trace clock, trace pins, ETB setup, and related hardware setup.
`.cmsis/<solution-set>.ctrace.yml` | User trace generation setup. This file defines which data, events, ITM channels, PC samples, or instruction trace streams are enabled.
`.trace/<solution-set>.ctrace-run.yml` | Generated trace run configuration. This file contains resolved symbols and ordered register accesses for pyOCD or other debug tools.

The trace run configuration (in `.trace/<solution-set>.ctrace-run.yml`) is written to target trace resources such as `DWT`, `ITM`, `ETM`, `MTB`, or `PMU` registers. pyOCD programs these registers after executing the [TraceCapture debug sequence](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html#pdsc_SequenceNameEnum_pg) and enabling capture in the attached debug unit, but before running the CPU. When pyOCD detects an updated `*.ctrace-run.yml` file, it writes the disabled feature values before applying the active register setup and deletes previous raw trace data files.

Based on these settings pyOCD captures raw trace data files in the [directory `.trace`](#directory-and-file-structure). These raw trace data files are converted by the `ctrace` utility.

In a later step, a preprocessing tool may generate `.trace/README.md` with setup instructions and code snippets that can be inserted in the application code.
