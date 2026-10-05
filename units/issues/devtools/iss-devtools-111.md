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
checked: "partly"
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

Fixed and verified with #123; in the meantime use the PackChk binary from the CMSIS_5 develop branch (CMSIS/Utilities). The thread names no release.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/devtools #111](https://github.com/Open-CMSIS-Pack/devtools/issues/111), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
