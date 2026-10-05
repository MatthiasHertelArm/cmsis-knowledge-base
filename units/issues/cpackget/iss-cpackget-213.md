---
id: "iss-cpackget-213"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add: 'mkdir ...: permission denied' in a non-writable working directory"
summary: "cpackget created a temporary pdsc working folder relative to the current working directory instead of the system temp directory."
status: "draft"
tool: "cpackget"
symptoms: ["E: mkdir KSLBEmaCod/: permission denied", "E: fail to create directory"]
symptom_regex: "E:\\s+mkdir\\s+KSLBEmaCod/:\\s+permission\\s+denied"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/213"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/213"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: mkdir KSLBEmaCod/: permission denied`
`E: fail to create directory`

## Cause

cpackget created a temporary pdsc working folder relative to the current working directory instead of the system temp directory.

## Fix

Use a later release (fixed in March 2024 with os.TempDir), or run cpackget from a writable directory.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/cpackget #213](https://github.com/Open-CMSIS-Pack/cpackget/issues/213), summarized in own words; confidence high, not reviewed yet.
