---
id: "tbx-experimental-features-directory-and-file-structure"
type: "concept"
domain: "project"
title: "Experimental Features: Trace / Directory and File Structure"
summary: "Trace-related files are stored relative to the directory that contains the .csolution.yml file."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#directory-and-file-structure"
license: "Apache-2.0"
mode: "V"
---

_Part of: Trace_

Trace-related files are stored relative to the directory that contains the `*.csolution.yml` file.

Directory or File                      | Created by                | Description
:--------------------------------------|:--------------------------|:------------------------------------
`.`                                    | User                      | Contains the `*.csolution.yml` project file.
`.cmsis/<solution-set>.ctrace.yml`     | CMSIS-Debugger            | User trace intent and "solution-set specific" trace capture configuration.
`.trace/<solution-set>.ctrace-run.yml` | [pyTS](#pyts-utility)     | Generated trace run information, including resolved symbols and register values.
`.trace/<solution-set>.<channel>.raw`  | pyOCD                     | Raw trace data files, specific to a `<channel>` (`SWO`, `TB`, or `ER`).
`.trace/<solution-set>.<channel>.csv`  | [ctrace](#ctrace-utility) | CSV files that represent raw trace data files.
`.trace/<solution-set>.ctf/`           | [ctrace](#ctrace-utility) | Directory for CTF files such as `metadata`, `stream_0`, and `stream_1`.

The file `.cmsis/<solution-set>.ctrace.yml` configures the trace generation. It is created or updated by the user interface of the CMSIS-Debugger Trace View.

The [`pyTS`](#pyts-utility) utility resolves symbol-based settings in `*.ctrace.yml` against the ELF/DWARF information of the active `<solution-set>` and generates the register setup for the hardware configuration. The output is the file `.trace/<solution-set>.ctrace-run.yml` which is used by the debugger for register setup in target hardware. During trace analysis the information of this file connects the raw trace data back to the `*.ctrace.yml` configuration.

Raw trace streams are stored as binary files, for example `.trace/<solution-set>.SWO.raw`. The [`ctrace`](#ctrace-utility) utility converts raw trace data files into [CSV](#csv-format) and [CTF](#ctf-format) for viewers and analysis tools.
