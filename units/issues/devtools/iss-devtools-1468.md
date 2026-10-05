---
id: "iss-devtools-1468"
type: "troubleshooting"
domain: "project"
title: "csolution: Generated regions header ignores memory defined in the board of a BSP"
summary: "With automatic linker script generation (linker: - auto:) only memory from the device was written to regions_<board>.h; memory elements of the board (for example external RAM and flash from the BSP) were missing."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1468"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1468"
resolution: "fixed-in-release"
versions: "before 2.4.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

With automatic linker script generation (linker: - auto:) only memory from the device was written to regions_<board>.h; memory elements of the board (for example external RAM and flash from the BSP) were missing.

## Fix

Fixed in CMSIS-Toolbox 2.4.0; update.

## Source

Resolution: fixed-in-release

Versions: before 2.4.0

From [Open-CMSIS-Pack/devtools #1468](https://github.com/Open-CMSIS-Pack/devtools/issues/1468), summarized in own words; confidence high, checked against the thread, not reviewed yet.
