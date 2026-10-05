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
checked: "partly"
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

For the time being use the PackChk binary from CMSIS_5 (develop branch, CMSIS/Utilities); the maintainer named the code fix (use find("./") instead), no release is shown.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/devtools #110](https://github.com/Open-CMSIS-Pack/devtools/issues/110), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
