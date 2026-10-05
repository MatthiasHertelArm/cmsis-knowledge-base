---
id: "iss-devtools-110"
type: "troubleshooting"
domain: "pack"
title: "packchk: ERROR M310 Filename mismatch for pdsc paths that begin with a dot (.config/...)"
summary: "The case-sensitivity check trims leading ./ characters with find_first_not_of, which also strips the dot of a hidden folder name."
status: "draft"
tool: "packchk"
symptoms: ["*** ERROR M310: <pack>.pdsc (Line 597)\n  Filename mismatch (case sensitive):"]
symptom_regex: "<pack>\\.pdsc\\s+\\(Line\\s+\\S+\\)\\\\s+Filename\\s+mismatch\\s+\\(case\\s+sensitive\\):"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/110"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/110"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** ERROR M310: <pack>.pdsc (Line 597)
  Filename mismatch (case sensitive):`

## Cause

The case-sensitivity check trims leading ./ characters with find_first_not_of, which also strips the dot of a hidden folder name.

## Fix

Use the older PackChk from CMSIS 5 until a fixed devtools packchk is used, or avoid names starting with a dot.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/devtools #110](https://github.com/Open-CMSIS-Pack/devtools/issues/110), summarized in own words; confidence medium, not reviewed yet.
