---
id: "iss-devtools-353"
type: "troubleshooting"
domain: "pack"
title: "packchk: ERROR M371 device feature SON unknown"
summary: "packchk 1.3.95 did not yet contain the SON package feature that PACK.xsd 1.7.7 defines."
status: "draft"
tool: "packchk"
symptoms: ["*** ERROR M371: <pack>.pdsc (Line 35)\n  Device Feature for 'TestDevice': 'SON' unknown."]
symptom_regex: "<pack>\\.pdsc\\s+\\(Line\\s+\\S+\\)\\\\s+Device\\s+Feature\\s+for\\s+'.*?':\\s+'.*?'\\s+unknown\\."
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/353"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/353"
resolution: "fixed-in-release"
versions: "fixed in packchk 1.3.96"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** ERROR M371: <pack>.pdsc (Line 35)
  Device Feature for 'TestDevice': 'SON' unknown.`

## Cause

packchk 1.3.95 did not yet contain the SON package feature that PACK.xsd 1.7.7 defines.

## Fix

Update to packchk 1.3.96 or later.

## Source

Resolution: fixed-in-release

Versions: fixed in packchk 1.3.96

From [Open-CMSIS-Pack/devtools #353](https://github.com/Open-CMSIS-Pack/devtools/issues/353), summarized in own words; confidence high, not reviewed yet.
