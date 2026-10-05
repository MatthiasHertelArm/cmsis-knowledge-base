---
id: "iss-devtools-469"
type: "troubleshooting"
domain: "pack"
title: "packchk: ERROR M371 Device Feature unknown for a feature that PACK.xsd allows (MIPI)"
summary: "packchk keeps its own hard-coded table of device features that lagged behind the feature list of PACK.xsd."
status: "draft"
tool: "packchk"
symptoms: ["*** ERROR M371: <pack>.pdsc (Line 761)\n  Device Feature for 'STM32U599/5A9': 'MIPI' unknown."]
symptom_regex: "<pack>\\.pdsc\\s+\\(Line\\s+\\S+\\)\\\\s+Device\\s+Feature\\s+for\\s+'.*?':\\s+'.*?'\\s+unknown\\."
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/469"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/469"
resolution: "fixed-in-release"
versions: "fixed in packchk 1.3.98"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** ERROR M371: <pack>.pdsc (Line 761)
  Device Feature for 'STM32U599/5A9': 'MIPI' unknown.`

## Cause

packchk keeps its own hard-coded table of device features that lagged behind the feature list of PACK.xsd.

## Fix

Use packchk 1.3.98 or later, which knows MIPI.

## Source

Resolution: fixed-in-release

Versions: fixed in packchk 1.3.98

From [Open-CMSIS-Pack/devtools #469](https://github.com/Open-CMSIS-Pack/devtools/issues/469), summarized in own words; confidence high, checked against the thread, not reviewed yet.
