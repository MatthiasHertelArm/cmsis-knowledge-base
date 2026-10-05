---
id: "iss-devtools-75"
type: "troubleshooting"
domain: "pack"
title: "packchk: ERROR M310 Filename mismatch for an example doc attribute with ../ segments"
summary: "packchk did not resolve ../ segments of the doc attribute relative to the example folder before comparing the names."
status: "draft"
tool: "packchk"
symptoms: ["*** ERROR M310: <pack>.pdsc (Line 465)\n  Filename mismatch (case sensitive):"]
symptom_regex: "<pack>\\.pdsc\\s+\\(Line\\s+\\S+\\)\\\\s+Filename\\s+mismatch\\s+\\(case\\s+sensitive\\):"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/75"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/75"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** ERROR M310: <pack>.pdsc (Line 465)
  Filename mismatch (case sensitive):`

## Cause

packchk did not resolve ../ segments of the doc attribute relative to the example folder before comparing the names.

## Fix

Fixed in a later packchk release (issue labelled fixed); note that packchk itself does not run a schema check, validate with PACK.xsd separately.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/devtools #75](https://github.com/Open-CMSIS-Pack/devtools/issues/75), summarized in own words; confidence medium, not reviewed yet.
