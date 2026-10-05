---
id: "iss-devtools-2491"
type: "troubleshooting"
domain: "project"
title: "csolution: CLANG fatal backend error on Cortex-M55 when the FPU is selected on its own"
summary: "With Compiler CLANG (LLVM Embedded Toolchain 22.1) and a Cortex-M55 device with FPU enabled, the option pair -mcpu=cortex-m55 -mfpu=fpv5-sp-d16 can trigger a fatal compiler backend error (a toolchain bug)."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2491"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2491"
resolution: "workaround"
versions: "LLVM Embedded Toolchain 22.1.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"], "core": ["Cortex-M55"], "toolchain": ["CLANG"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

With Compiler CLANG (LLVM Embedded Toolchain 22.1) and a Cortex-M55 device with FPU enabled, the option pair -mcpu=cortex-m55 -mfpu=fpv5-sp-d16 can trigger a fatal compiler backend error (a toolchain bug).

## Fix

Do not choose the FPU separately for Cortex-M55 with CLANG; if one must be given use -mfpu=fp-armv8-fullfp16-d16. The toolbox mitigation was validated in a nightly.

## Source

Resolution: workaround

Versions: LLVM Embedded Toolchain 22.1.0

From [Open-CMSIS-Pack/devtools #2491](https://github.com/Open-CMSIS-Pack/devtools/issues/2491), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
