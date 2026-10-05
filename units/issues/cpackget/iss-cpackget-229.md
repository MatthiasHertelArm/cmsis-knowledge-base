---
id: "iss-cpackget-229"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add crashes with a nil pointer for a local pack whose url is a file:/// location"
summary: "cpackget's FileExists() crashed because the file info returned by os.Stat was nil when adding a local pack whose pdsc gives a file:/// url."
status: "draft"
tool: "cpackget"
symptoms: ["panic: runtime error: invalid memory address or nil pointer dereference"]
symptom_regex: "panic:\\s+runtime\\s+error:\\s+invalid\\s+memory\\s+address\\s+or\\s+nil\\s+pointer\\s+dereference"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/229"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/229"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`panic: runtime error: invalid memory address or nil pointer dereference`

## Cause

cpackget's FileExists() crashed because the file info returned by os.Stat was nil when adding a local pack whose pdsc gives a file:/// url.

## Fix

Use a cpackget with the corrected FileExists(); the thread names no release.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/cpackget #229](https://github.com/Open-CMSIS-Pack/cpackget/issues/229), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
