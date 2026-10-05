---
id: "iss-devtools-2611"
type: "troubleshooting"
domain: "project"
title: "csolution: GDB call stack loops or never ends with AC6/ATfE code built with debug enabled"
summary: "Armclang and the Arm Toolchain for Embedded optimise functions marked noreturn (such as RTOS threads) so that they reuse the link register without emitting the matching unwind info."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2611"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2611"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"], "toolchain": ["AC6", "CLANG"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Armclang and the Arm Toolchain for Embedded optimise functions marked noreturn (such as RTOS threads) so that they reuse the link register without emitting the matching unwind info. GDB then cannot stop walking the stack.

## Fix

Add -funwind-tables to the compile options of debug builds (for example via misc: in the project or cdefault). The code keeps LR on the stack, costing a little stack, and unwinding becomes reliable. The thread was closed as a duplicate of a proposal to add it by default.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/devtools #2611](https://github.com/Open-CMSIS-Pack/devtools/issues/2611), summarized in own words; confidence medium, not reviewed yet.
