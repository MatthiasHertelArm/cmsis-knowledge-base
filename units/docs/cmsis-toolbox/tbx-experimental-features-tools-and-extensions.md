---
id: "tbx-experimental-features-tools-and-extensions"
type: "concept"
domain: "project"
title: "Experimental Features: Trace / Tools and Extensions"
summary: "The trace workflow is split across the command-line tools and VS Code extensions as shown below."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#tools-and-extensions"
license: "Apache-2.0"
mode: "V"
---

_Part of: Trace_

The trace workflow is split across the command-line tools and VS Code extensions as shown below.

(figure: Trace components and data flow)

Tool or Extension              | Input                                         | Output                         | Description
:------------------------------|:----------------------------------------------|:-------------------------------|:------------------------------------
[Arm CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) | `*.csolution.yml`, optional `.cmsis/*.dbgconf` | `*.cbuild-run.yml` | Generates the run and debug information consumed by debuggers.
[Arm CMSIS Debugger](https://marketplace.visualstudio.com/items?itemName=Arm.vscode-cmsis-debugger)
Trace Generation Setup View | `.cmsis/*.ctrace.yml` | Updated `.cmsis/*.ctrace.yml` | Configures trace capture.
[pyTS](#pyts-utility)          | `.cmsis/*.ctrace.yml`, ELF/DWARF symbols       | `.trace/*.ctrace-run.yml`      | Resolves symbols and generates CoreSight trace register values.
[pyOCD](https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/pyOCD-Debugger.md)     | `*.cbuild-run.yml`, `.trace/*.ctrace-run.yml`  | Raw trace data files in `.trace/` | Programs trace registers and captures trace streams during the debug session.
[`ctrace`](#ctrace-utility)    | Raw trace data files, `.trace/*.ctrace-run.yml` | CSV, CTF files, Trace Compass XML Analysis file | Generates CSV files (human readable) and CTF files
[Trace Viewer for VS Code](https://marketplace.visualstudio.com/items?itemName=eclipse-cdt.vscode-trace-extension) and
 [VS Code Trace Server](https://marketplace.visualstudio.com/items?itemName=eclipse-cdt.vscode-trace-server) | CTF files, Trace Compass XML Analysis file | Trace viewer panes | Visualizes the CTF output in VS Code.

**Interactive Debug Workflow:**

It is possible to change the **Trace Generation Setup** during debugging. For this workflow:

- pyTS generates a new `*.ctrace-run.yml` file.
- pyOCD reloads this `*.ctrace-run.yml` file and deletes existing **Raw Trace Stream** files when changes are detected and a new trace collection is started.

**CI Workflow:**

CI requires a prepared `.cmsis/<solution-set>.ctrace.yml` file. This file may be under source control or maintained manually.

**Trace Buffer Workflow:**

Existing **Raw Trace Stream** files containing trace buffer data are deleted each time the trace buffer is captured, for example after hitting a breakpoint. This prevents gaps that could otherwise be introduced by concatenating capture runs in which the trace buffer has wrapped around.
