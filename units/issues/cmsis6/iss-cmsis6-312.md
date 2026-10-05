---
id: "iss-cmsis6-312"
type: "troubleshooting"
domain: "core"
title: "CMSIS-Core: tiarmclang build fails: __PROGRAM_START resolves to _start instead of _c_int00"
summary: "CMSIS 6 uses the generic clang header, where the program start symbol is _start, while the TI compiler runtime uses _c_int00."
status: "draft"
tool: "cmsis-core"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/312"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/312"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-core"], "toolchain": ["TI Clang"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

CMSIS 6 uses the generic clang header, where the program start symbol is _start, while the TI compiler runtime uses _c_int00.

## Fix

Define __PROGRAM_START as _c_int00 (and __INITIAL_SP as __stack) before including the device header for TI clang, or use the CMSIS_6 version containing the TI specifics in the clang header (PR 315).

## Source

Resolution: fixed-in-release

From [ARM-software/CMSIS_6 #312](https://github.com/ARM-software/CMSIS_6/issues/312), summarized in own words; confidence high, not reviewed yet.
