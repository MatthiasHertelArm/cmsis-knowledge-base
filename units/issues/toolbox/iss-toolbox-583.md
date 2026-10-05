---
id: "iss-toolbox-583"
type: "troubleshooting"
domain: "project"
title: "csolution: Clang build lacks -mfpu, causing wrong FPU instructions and hard faults"
summary: "-mfpu had been removed from the Clang toolchain description because older Clang versions crashed with it."
status: "draft"
tool: "csolution"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/583"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/583"
resolution: "fixed-in-release"
versions: "missing before 2.13.x nightly; Clang 22 tested"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"], "toolchain": ["CLANG"], "core": ["Cortex-M7"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

-mfpu had been removed from the Clang toolchain description because older Clang versions crashed with it. Without it a single-precision FPU target such as Cortex-M7 FPv5-SP may get double-precision instructions.

## Fix

Use a CMSIS-Toolbox that re-added -mfpu (merged after 2.13.0, in nightlies). Check compile_commands.json for -mfpu=fpv5-sp-d16. If the VS Code extension still shows the old behaviour, point CMSIS_SOLUTION_TOOLBOX to the newer toolbox.

## Source

Resolution: fixed-in-release

Versions: missing before 2.13.x nightly; Clang 22 tested

From [Open-CMSIS-Pack/cmsis-toolbox #583](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/583), summarized in own words; confidence high, checked against the thread, not reviewed yet.
