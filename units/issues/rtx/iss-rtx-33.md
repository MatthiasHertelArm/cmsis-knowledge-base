---
id: "iss-rtx-33"
type: "troubleshooting"
domain: "rtos"
title: "RTX: osKernelInitialize fails because osRtxInfo memory is all 0xFF at startup"
summary: "The deprecated LPC1700_DFP was not compatible with the CMSIS-Toolbox, which generated a faulty scatter file, so the stack was broken before startup."
status: "draft"
tool: "cmsis-rtx"
collection: "issues-rtx"
source: "https://github.com/ARM-software/CMSIS-RTX/issues/33"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/issues/33"
resolution: "user-error"
versions: "CMSIS-RTX 5.8.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-rtx"], "device": ["LPC1768"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The deprecated LPC1700_DFP was not compatible with the CMSIS-Toolbox, which generated a faulty scatter file, so the stack was broken before startup.

## Fix

Not spelled out in the thread: the reporter traced the problem to the scatter file generated from the deprecated LPC1700_DFP and closed the issue.

## Source

Resolution: user-error

Versions: CMSIS-RTX 5.8.0

From [ARM-software/CMSIS-RTX #33](https://github.com/ARM-software/CMSIS-RTX/issues/33), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
