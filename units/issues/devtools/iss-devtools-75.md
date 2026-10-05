---
id: "iss-devtools-75"
type: "troubleshooting"
domain: "pack"
title: "packchk: ERROR M310 Filename mismatch for an example doc attribute with ../ segments"
summary: "packchk did not resolve the ../ segments of the example's doc attribute relative to the example folder before comparing the names."
status: "draft"
tool: "packchk"
symptoms: ["*** ERROR M310: <pack>.pdsc (Line 465)\n  Filename mismatch (case sensitive):"]
symptom_regex: "<pack>\\.pdsc\\s+\\(Line\\s+\\S+\\)\\\\s+Filename\\s+mismatch\\s+\\(case\\s+sensitive\\):"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/75"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/75"
resolution: "unresolved"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** ERROR M310: <pack>.pdsc (Line 465)
  Filename mismatch (case sensitive):`

## Cause

packchk did not resolve the ../ segments of the example's doc attribute relative to the example folder before comparing the names.

## Fix

The thread gives no confirmed fix.

## Source

Resolution: unresolved

From [Open-CMSIS-Pack/devtools #75](https://github.com/Open-CMSIS-Pack/devtools/issues/75), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
