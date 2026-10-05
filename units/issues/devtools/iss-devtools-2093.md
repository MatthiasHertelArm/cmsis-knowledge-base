---
id: "iss-devtools-2093"
type: "troubleshooting"
domain: "pack"
title: "packchk: packchk 2.9.0 warns M300 for XML namespace URLs that start with http"
summary: "The https check looped over all attributes of extension elements, including xmlns declarations."
status: "draft"
tool: "packchk"
symptoms: ["*** WARNING M300: <pack>.pdsc (Line 776) \n  at must use 'https://'"]
symptom_regex: "<pack>\\.pdsc\\s+\\(Line\\s+\\S+\\)\\s+\\\\s+at\\s+must\\s+use\\s+'.*?'"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2093"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2093"
resolution: "fixed-in-release"
versions: "2.9.0"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** WARNING M300: <pack>.pdsc (Line 776) 
  at must use 'https://'`

## Cause

The https check looped over all attributes of extension elements, including xmlns declarations. A namespace URI is only an identifier and cannot be changed, so only schemaLocation should be checked.

## Fix

Harmless warning for xmlns attributes of extensions; the check was reported as a bug in packchk 2.9.0 and narrowed afterwards. Change schemaLocation to https if it triggers.

## Source

Resolution: fixed-in-release

Versions: 2.9.0

From [Open-CMSIS-Pack/devtools #2093](https://github.com/Open-CMSIS-Pack/devtools/issues/2093), summarized in own words; confidence low, not reviewed yet.
