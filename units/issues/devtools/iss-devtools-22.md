---
id: "iss-devtools-22"
type: "troubleshooting"
domain: "general"
title: "other: packgen: packchk not found although the PackChk binary was copied to the working folder"
summary: "packgen runs packchk from the PATH; a copy in the current folder is not found, and the executable name is case-sensitive on Linux."
status: "draft"
tool: "other"
symptoms: ["sh: 1: packchk: not found", "packgen error: packchk failed"]
symptom_regex: "sh:\\s+\\S+:\\s+packchk:\\s+not\\s+found"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/22"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/22"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`sh: 1: packchk: not found`
`packgen error: packchk failed`

## Cause

packgen runs packchk from the PATH; a copy in the current folder is not found, and the executable name is case-sensitive on Linux.

## Fix

Add the folder containing packchk (for example Utilities/Linux64) to PATH, or run packgen with --nocheck to skip the check.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/devtools #22](https://github.com/Open-CMSIS-Pack/devtools/issues/22), summarized in own words; confidence high, checked against the thread, not reviewed yet.
