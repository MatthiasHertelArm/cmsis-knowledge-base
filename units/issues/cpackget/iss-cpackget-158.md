---
id: "iss-cpackget-158"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add panics 'index out of range' for pre-release versions like -alpha.1.9"
summary: "Version parsing of requirement entries in the pdsc with a complex pre-release such as 2.0.0-alpha.1.9 produced a different number of regex matches than expected (regression in 0.9.2)."
status: "draft"
tool: "cpackget"
symptoms: ["panic: runtime error: index out of range [1] with length 1"]
symptom_regex: "panic:\\s+runtime\\s+error:\\s+index\\s+out\\s+of\\s+range\\s+\\[\\S+\\]\\s+with\\s+length\\s+\\S+"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/158"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/158"
resolution: "workaround"
versions: "0.9.2 affected, 0.9.0 fine"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`panic: runtime error: index out of range [1] with length 1`

## Cause

Version parsing of requirement entries in the pdsc with a complex pre-release such as 2.0.0-alpha.1.9 produced a different number of regex matches than expected (regression in 0.9.2).

## Fix

Skip dependency installation with -n until a fixed release; later releases align the version regular expression with semver.org.

## Source

Resolution: workaround

Versions: 0.9.2 affected, 0.9.0 fine

From [Open-CMSIS-Pack/cpackget #158](https://github.com/Open-CMSIS-Pack/cpackget/issues/158), summarized in own words; confidence medium, not reviewed yet.
