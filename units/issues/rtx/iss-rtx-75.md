---
id: "iss-rtx-75"
type: "troubleshooting"
domain: "rtos"
title: "RTX: No armasm port for CMSIS-RTX: GCC syntax .S files fail to assemble"
summary: "The GCC-syntax assembly files are also meant for Arm Compiler 6, but must be assembled by armclang, not armasm."
status: "draft"
tool: "cmsis-rtx"
collection: "issues-rtx"
source: "https://github.com/ARM-software/CMSIS-RTX/issues/75"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/issues/75"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-rtx"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The GCC-syntax assembly files are also meant for Arm Compiler 6, but must be assembled by armclang, not armasm.

## Fix

Let the project build the .S files with armclang (set the assembler syntax with -masm=gnu if needed).

## Source

Resolution: configuration

From [ARM-software/CMSIS-RTX #75](https://github.com/ARM-software/CMSIS-RTX/issues/75), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
