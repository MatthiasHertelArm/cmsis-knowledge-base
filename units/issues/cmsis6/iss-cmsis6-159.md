---
id: "iss-cmsis6-159"
type: "troubleshooting"
domain: "core"
title: "CMSIS-Core: Telling Cortex-M33 and Cortex-M85 apart in the preprocessor"
summary: "Compilers do not agree on the architecture macros: GCC reports the same __ARM_ARCH and __ARM_ARCH_8M_MAIN__ values for both cores, other toolchains differ again, so the ACLE macros cannot reliably separate the two."
status: "draft"
tool: "cmsis-core"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/159"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/159"
resolution: "configuration"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-core"], "core": ["Cortex-M33", "Cortex-M85"], "toolchain": ["GCC", "AC6", "LLVM", "IAR"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Compilers do not agree on the architecture macros: GCC reports the same __ARM_ARCH and __ARM_ARCH_8M_MAIN__ values for both cores, other toolchains differ again, so the ACLE macros cannot reliably separate the two.

## Fix

Test the CMSIS core revision macro instead, for example #if defined (__CM85_REV) for a Cortex-M85. CMSIS provides a fallback value when the device header does not define the revision, so the macro exists for every device.

## Source

Resolution: configuration

The issue is still open: the fix is a workaround, a later release may change it.

From [ARM-software/CMSIS_6 #159](https://github.com/ARM-software/CMSIS_6/issues/159), summarized in own words; confidence medium, not reviewed yet.
