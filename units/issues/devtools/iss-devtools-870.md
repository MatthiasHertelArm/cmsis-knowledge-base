---
id: "iss-devtools-870"
type: "troubleshooting"
domain: "project"
title: "cbuild: IAR object files get a double suffix (file.c.o) unlike the IAR IDE (file.o)"
summary: "Object file naming is left to CMake, whose IAR module sets .o as extension without replacing the source extension, so linker scripts that name objects like fsl_clock.o do not match."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/870"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/870"
resolution: "workaround"
versions: "1.6.1"
confidence: "low"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cbuild"], "toolchain": ["IAR"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Object file naming is left to CMake, whose IAR module sets .o as extension without replacing the source extension, so linker scripts that name objects like fsl_clock.o do not match.

## Fix

Proposed: enable CMAKE_C_OUTPUT_EXTENSION_REPLACE, CMAKE_CXX_... and CMAKE_ASM_OUTPUT_EXTENSION_REPLACE (set to 1) in IAR.<version>.cmake; the thread did not confirm the final release.

## Source

Resolution: workaround

Versions: 1.6.1

From [Open-CMSIS-Pack/devtools #870](https://github.com/Open-CMSIS-Pack/devtools/issues/870), summarized in own words; confidence low, checked against the thread, not reviewed yet.
