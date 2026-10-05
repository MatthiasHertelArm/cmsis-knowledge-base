---
id: "iss-cmsis6-129"
type: "troubleshooting"
domain: "core"
title: "CMSIS-Core: \"unknown type name IRQn_Type\" when using only CMSIS-Core with a TI device"
summary: "CMSIS-Core does not define device interrupt numbers; the device header from the vendor DFP provides IRQn_Type and includes the core header."
status: "draft"
tool: "cmsis-core"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/129"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/129"
resolution: "user-error"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-core"], "core": ["Cortex-M0+"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

CMSIS-Core does not define device interrupt numbers; the device header from the vendor DFP provides IRQn_Type and includes the core header.

## Fix

Use the device header and startup file from the DFP or SDK, or write a minimal one following the Cortex_DFP template.

## Source

Resolution: user-error

From [ARM-software/CMSIS_6 #129](https://github.com/ARM-software/CMSIS_6/issues/129), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
