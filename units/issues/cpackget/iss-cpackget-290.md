---
id: "iss-cpackget-290"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add of a local pdsc registers a wrong path (no drive letter, C: vs c:)"
summary: "On Windows, cpackget add with a pdsc path that starts with a backslash but has no drive letter stored a wrong path built from the current directory."
status: "draft"
tool: "cpackget"
symptoms: ["The system cannot find the path specified."]
symptom_regex: "The\\s+system\\s+cannot\\s+find\\s+the\\s+path\\s+specified\\."
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/290"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/290"
resolution: "workaround"
versions: "cpackget 2.1.1 affected"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`The system cannot find the path specified.`

## Cause

On Windows, cpackget add with a pdsc path that starts with a backslash but has no drive letter stored a wrong path built from the current directory. An upper-case drive letter also produced a 'malformed path' warning and a reinstall, while a lower-case one did not.

## Fix

Give the full pdsc path including the drive letter. A later cpackget handles lower- and upper-case drive letters; the thread names no version.

## Source

Resolution: workaround

Versions: cpackget 2.1.1 affected

From [Open-CMSIS-Pack/cpackget #290](https://github.com/Open-CMSIS-Pack/cpackget/issues/290), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
