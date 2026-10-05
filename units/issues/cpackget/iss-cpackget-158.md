---
id: "iss-cpackget-158"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add panics 'index out of range' for pre-release versions like -alpha.1.9"
summary: "cpackget 0.9.2 crashed while checking the pack's requirements because a required pack version with a complex pre-release part (2.0.0-alpha.1.9) did not fit its internal version representation; 0.9.0 installed the pack."
status: "draft"
tool: "cpackget"
symptoms: ["panic: runtime error: index out of range [1] with length 1"]
symptom_regex: "panic:\\s+runtime\\s+error:\\s+index\\s+out\\s+of\\s+range\\s+\\[\\S+\\]\\s+with\\s+length\\s+\\S+"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/158"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/158"
resolution: "workaround"
versions: "cpackget 0.9.2 affected, 0.9.0 works"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`panic: runtime error: index out of range [1] with length 1`

## Cause

cpackget 0.9.2 crashed while checking the pack's requirements because a required pack version with a complex pre-release part (2.0.0-alpha.1.9) did not fit its internal version representation; 0.9.0 installed the pack.

## Fix

Skip dependency installation with the -n flag until a patched cpackget is available.

## Source

Resolution: workaround

Versions: cpackget 0.9.2 affected, 0.9.0 works

From [Open-CMSIS-Pack/cpackget #158](https://github.com/Open-CMSIS-Pack/cpackget/issues/158), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
