---
id: "iss-devtools-2611"
type: "troubleshooting"
domain: "project"
title: "csolution: GDB call stack loops or never ends with AC6/ATfE code built with debug enabled"
summary: "AC6 and ATfE optimise functions with the noreturn attribute (threads) so that they use or destroy the link register without emitting the matching debug information (.cfi_undefined 14), which seems to be a compiler issue (not yet confirmed)."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2611"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2611"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"], "toolchain": ["AC6", "CLANG"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

AC6 and ATfE optimise functions with the noreturn attribute (threads) so that they use or destroy the link register without emitting the matching debug information (.cfi_undefined 14), which seems to be a compiler issue (not yet confirmed). GDB then cannot stop unwinding the stack.

## Fix

Compile debug builds with -funwind-tables: the code keeps LR on the stack (slightly more stack) and unwinding works reliably. The issue proposes adding it by default for AC6 and CLANG when debug: on, and #2612 suggests adding it to cdefault.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/devtools #2611](https://github.com/Open-CMSIS-Pack/devtools/issues/2611), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
