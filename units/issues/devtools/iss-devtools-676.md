---
id: "iss-devtools-676"
type: "troubleshooting"
domain: "project"
title: "cbuild: ERROR M204 path not found when a custom rtedir contains a space"
summary: "cbuildgen replaces spaces in the RTE path with underscores (meant for component classes such as 'CMSIS Driver') and also did so for spaces above the RTE folder, so a custom rtedir containing a space pointed to a path that …"
status: "draft"
tool: "cbuild"
symptoms: ["*** ERROR M204:\n  Path not found: 'C:/Temp/csolution_test/reproducer/white_space/RTE/Device/ARMCM3/ARMCM3_ac6.sct'!"]
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/676"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/676"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** ERROR M204:
  Path not found: 'C:/Temp/csolution_test/reproducer/white_space/RTE/Device/ARMCM3/ARMCM3_ac6.sct'!`

## Cause

cbuildgen replaces spaces in the RTE path with underscores (meant for component classes such as 'CMSIS Driver') and also did so for spaces above the RTE folder, so a custom rtedir containing a space pointed to a path that does not exist.

## Fix

The tool was changed to replace only spaces below the RTE folder; with a version lacking the change, keep spaces out of the rtedir path.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/devtools #676](https://github.com/Open-CMSIS-Pack/devtools/issues/676), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
