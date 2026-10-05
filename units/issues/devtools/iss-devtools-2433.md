---
id: "iss-devtools-2433"
type: "troubleshooting"
domain: "pack"
title: "svdconv: Header type name uses peripheral name (WDT0_Type) instead of groupName"
summary: "SVDConv names the struct after the peripheral name unless told otherwise; groupName is not used for this."
status: "draft"
tool: "svdconv"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2433"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2433"
resolution: "user-error"
versions: "3.3.49"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["svdconv"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

SVDConv names the struct after the peripheral name unless told otherwise; groupName is not used for this.

## Fix

Add <headerStructName>WDT</headerStructName> to the peripheral, then all peripherals of the group share the WDT_Type struct.

## Source

Resolution: user-error

Versions: 3.3.49

From [Open-CMSIS-Pack/devtools #2433](https://github.com/Open-CMSIS-Pack/devtools/issues/2433), summarized in own words; confidence high, checked against the thread, not reviewed yet.
