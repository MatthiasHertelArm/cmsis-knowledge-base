---
id: "iss-cmsis6-230"
type: "troubleshooting"
domain: "core"
title: "CMSIS-Core: SCB_VTOR_TBLOFF_Msk differs from the vendor manual"
summary: "CMSIS implements VTOR.TBLOFF as the Armv7-M architecture specifies it (mask 0xFFFFFF80); implementers such as ST may restrict the implemented bits and require stronger alignment (512 bytes on this STM32)."
status: "draft"
tool: "cmsis-core"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/230"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/230"
resolution: "not-a-bug"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-core"], "core": ["Cortex-M4"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

CMSIS implements VTOR.TBLOFF as the Armv7-M architecture specifies it (mask 0xFFFFFF80); implementers such as ST may restrict the implemented bits and require stronger alignment (512 bytes on this STM32).

## Fix

Align the vector table as the device manual requires; CMSIS cannot encode implementation specifics.

## Source

Resolution: not-a-bug

From [ARM-software/CMSIS_6 #230](https://github.com/ARM-software/CMSIS_6/issues/230), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
