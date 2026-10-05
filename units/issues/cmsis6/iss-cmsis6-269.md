---
id: "iss-cmsis6-269"
type: "troubleshooting"
domain: "core"
title: "CMSIS-Core: ITM->LAR / LSR no longer compile after moving a Cortex-M33 project to CMSIS 6"
summary: "CMSIS 6 deliberately dropped the LAR and LSR lock registers from ITM_Type in core_cm33.h, because the common ARMv8-M ground does not require them."
status: "draft"
tool: "cmsis-core"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/269"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/269"
resolution: "workaround"
versions: "Removed in CMSIS 6; CMSIS 5 headers still declare the registers."
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-core"], "core": ["Cortex-M33"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

CMSIS 6 deliberately dropped the LAR and LSR lock registers from ITM_Type in core_cm33.h, because the common ARMv8-M ground does not require them. A vendor SDK that was written against CMSIS 5 and still touches ITM->LAR therefore fails to build.

## Fix

Take the register declaration from the device family pack of the vendor if it provides one, or declare it yourself in the project (for example write the unlock key 0xC5ACCE55 straight to the ITM lock address of your device). Check in the device manual that the part really implements the ITM lock mechanism before adding it.

## Source

Resolution: workaround

Versions: Removed in CMSIS 6; CMSIS 5 headers still declare the registers.

The issue is still open: the fix is a workaround, a later release may change it.

From [ARM-software/CMSIS_6 #269](https://github.com/ARM-software/CMSIS_6/issues/269), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
