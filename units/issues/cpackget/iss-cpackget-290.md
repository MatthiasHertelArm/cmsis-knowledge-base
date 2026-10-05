---
id: "iss-cpackget-290"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add of a local pdsc registers a wrong path (no drive letter, C: vs c:)"
summary: "On Windows a path starting with a backslash but no drive letter was joined to the current directory, and drive letters in different case were treated as different entries in local_repository.pidx."
status: "draft"
tool: "cpackget"
symptoms: ["The system cannot find the path specified."]
symptom_regex: "The\\s+system\\s+cannot\\s+find\\s+the\\s+path\\s+specified\\."
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/290"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/290"
resolution: "fixed-in-release"
versions: "2.1.1 affected"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`The system cannot find the path specified.`

## Cause

On Windows a path starting with a backslash but no drive letter was joined to the current directory, and drive letters in different case were treated as different entries in local_repository.pidx.

## Fix

Use a cpackget release after 2.1.1 (fixed September 2024), or give the full path including the drive letter in the same case everywhere.

## Source

Resolution: fixed-in-release

Versions: 2.1.1 affected

From [Open-CMSIS-Pack/cpackget #290](https://github.com/Open-CMSIS-Pack/cpackget/issues/290), summarized in own words; confidence medium, not reviewed yet.
