---
id: "iss-devtools-2093"
type: "troubleshooting"
domain: "pack"
title: "packchk: packchk 2.9.0 warns M300 for XML namespace URLs that start with http"
summary: "The https check of packchk 2.9.0 (an attribute loop introduced in #1109) also flags xmlns namespace declarations of extension elements."
status: "draft"
tool: "packchk"
symptoms: ["*** WARNING M300: <pack>.pdsc (Line 776) \n  at must use 'https://'"]
symptom_regex: "<pack>\\.pdsc\\s+\\(Line\\s+\\S+\\)\\s+\\\\s+at\\s+must\\s+use\\s+'.*?'"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2093"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2093"
resolution: "unresolved"
versions: "packchk 2.9.0"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** WARNING M300: <pack>.pdsc (Line 776) 
  at must use 'https://'`

## Cause

The https check of packchk 2.9.0 (an attribute loop introduced in #1109) also flags xmlns namespace declarations of extension elements. A namespace URL is only an identifier and cannot be changed without breaking its consumers; only schemaLocation should need https.

## Fix

No fix in the thread. A schemaLocation should use https; the warning on the namespace URL itself cannot be removed from the pdsc.

## Source

Resolution: unresolved

Versions: packchk 2.9.0

From [Open-CMSIS-Pack/devtools #2093](https://github.com/Open-CMSIS-Pack/devtools/issues/2093), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
