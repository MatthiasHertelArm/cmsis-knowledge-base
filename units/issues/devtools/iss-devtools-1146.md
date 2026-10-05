---
id: "iss-devtools-1146"
type: "troubleshooting"
domain: "project"
title: "cbuild: IAR build error for Cortex-M55 when Dfpu is SP_FPU"
summary: "The IAR toolchain file mapped single-precision FPU to ERROR on Cortex-M55/M85, but the hardware FPU there is double precision or none."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1146"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1146"
resolution: "fixed-in-release"
versions: "before 2.2"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"], "core": ["Cortex-M55", "Cortex-M85"], "toolchain": ["IAR"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The IAR toolchain file mapped single-precision FPU to ERROR on Cortex-M55/M85, but the hardware FPU there is double precision or none.

## Fix

Fixed in the IAR toolchain files of the toolbox (2.2 timeframe): SP_FPU now maps to the double-precision hardware setting on M55 and M85.

## Source

Resolution: fixed-in-release

Versions: before 2.2

From [Open-CMSIS-Pack/devtools #1146](https://github.com/Open-CMSIS-Pack/devtools/issues/1146), summarized in own words; confidence high, not reviewed yet.
