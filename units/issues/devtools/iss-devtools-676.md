---
id: "iss-devtools-676"
type: "troubleshooting"
domain: "project"
title: "cbuild: ERROR M204 path not found when a custom rtedir contains a space"
summary: "cbuildgen replaces spaces by underscores in the RTE path (meant for component class names like CMSIS Driver) and also did so for spaces above the RTE folder."
status: "draft"
tool: "cbuild"
symptoms: ["*** ERROR M204:\n  Path not found: 'C:/Temp/csolution_test/reproducer/white_space/RTE/Device/ARMCM3/ARMCM3_ac6.sct'!"]
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/676"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/676"
resolution: "fixed-in-release"
versions: "fixed in 1.5.0 era"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** ERROR M204:
  Path not found: 'C:/Temp/csolution_test/reproducer/white_space/RTE/Device/ARMCM3/ARMCM3_ac6.sct'!`

## Cause

cbuildgen replaces spaces by underscores in the RTE path (meant for component class names like CMSIS Driver) and also did so for spaces above the RTE folder.

## Fix

Fixed so that only spaces below the RTE folder are replaced; avoid spaces in the rtedir path on older versions.

## Source

Resolution: fixed-in-release

Versions: fixed in 1.5.0 era

From [Open-CMSIS-Pack/devtools #676](https://github.com/Open-CMSIS-Pack/devtools/issues/676), summarized in own words; confidence medium, not reviewed yet.
