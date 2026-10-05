---
id: "iss-devtools-111"
type: "troubleshooting"
domain: "pack"
title: "packchk: WARNING M339 Include Path must not be a file for an existing folder"
summary: "The directory test was inverted when the check was ported to RteFsUtils."
status: "draft"
tool: "packchk"
symptoms: ["*** WARNING M339: <pack>.pdsc (Line 631)\n  Include Path 'Inc' must not be a file!"]
symptom_regex: "<pack>\\.pdsc\\s+\\(Line\\s+\\S+\\)\\\\s+Include\\s+Path\\s+'.*?'\\s+must\\s+not\\s+be\\s+a\\s+file!"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/111"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/111"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** WARNING M339: <pack>.pdsc (Line 631)
  Include Path 'Inc' must not be a file!`

## Cause

The directory test was inverted when the check was ported to RteFsUtils.

## Fix

Use a packchk version containing the fix (1.3.9x); in the meantime use the older PackChk binary from CMSIS 5.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/devtools #111](https://github.com/Open-CMSIS-Pack/devtools/issues/111), summarized in own words; confidence medium, not reviewed yet.
