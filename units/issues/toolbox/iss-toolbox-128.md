---
id: "iss-toolbox-128"
type: "troubleshooting"
domain: "project"
title: "cbuild: Function-like macro in define: is split into many -D options"
summary: "Without escaping or inner quotes the function-like define is split into separate -D tokens."
status: "draft"
tool: "cbuild"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/128"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/128"
resolution: "workaround"
versions: "CMSIS-Toolbox 2.3.0; CMake ^3.25.2"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Without escaping or inner quotes the function-like define is split into separate -D tokens. Quoted forms reach the generated CMakeLists.txt intact, but CMake may then drop function-style definitions with a warning.

## Fix

Escape the characters (e.g. _LIBCPP_VERBOSE_ABORT\(\.\.\.\): \(\(void\)0\)) or use YAML quoting that keeps the inner quotes, e.g. - '"NAME(...)=((void)0)"'. The reporter's CMake (^3.25.2) accepted the macro; where CMake drops it, define the macro in a header file.

## Source

Resolution: workaround

Versions: CMSIS-Toolbox 2.3.0; CMake ^3.25.2

From [Open-CMSIS-Pack/cmsis-toolbox #128](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/128), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
