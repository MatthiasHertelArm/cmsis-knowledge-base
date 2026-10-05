---
id: "iss-devtools-327"
type: "troubleshooting"
domain: "pack"
title: "packchk: WARNING M339 says Include Path must not be a file when the directory does not exist"
summary: "std::filesystem::is_directory also returns false for missing paths, so a non-existing include folder produced the wrong message."
status: "draft"
tool: "packchk"
symptoms: ["*** WARNING M339: **.pdsc (Line **) Include Path '**' must not be a file!"]
symptom_regex: "\\*\\*\\.pdsc\\s+\\(Line\\s+\\*\\*\\)\\s+Include\\s+Path\\s+'.*?'\\s+must\\s+not\\s+be\\s+a\\s+file!"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/327"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/327"
resolution: "fixed-in-release"
versions: "fixed in packchk 1.3.95"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** WARNING M339: **.pdsc (Line **) Include Path '**' must not be a file!`

## Cause

std::filesystem::is_directory also returns false for missing paths, so a non-existing include folder produced the wrong message.

## Fix

Create or correct the path in the pdsc; packchk 1.3.95 reports the missing path properly.

## Source

Resolution: fixed-in-release

Versions: fixed in packchk 1.3.95

From [Open-CMSIS-Pack/devtools #327](https://github.com/Open-CMSIS-Pack/devtools/issues/327), summarized in own words; confidence high, not reviewed yet.
