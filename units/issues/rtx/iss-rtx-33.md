---
id: "iss-rtx-33"
type: "troubleshooting"
domain: "rtos"
title: "RTX: osKernelInitialize fails because osRtxInfo memory is all 0xFF at startup"
summary: "A broken scatter file generated for a deprecated device pack left RAM uninitialised and damaged the stack before startup."
status: "draft"
tool: "cmsis-rtx"
collection: "issues-rtx"
source: "https://github.com/ARM-software/CMSIS-RTX/issues/33"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/issues/33"
resolution: "user-error"
versions: "RTX 5.8.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-rtx"], "device": ["LPC1768"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A broken scatter file generated for a deprecated device pack left RAM uninitialised and damaged the stack before startup.

## Fix

Replace the old DFP or fix the linker script generation.

## Source

Resolution: user-error

Versions: RTX 5.8.0

From [ARM-software/CMSIS-RTX #33](https://github.com/ARM-software/CMSIS-RTX/issues/33), summarized in own words; confidence medium, not reviewed yet.
