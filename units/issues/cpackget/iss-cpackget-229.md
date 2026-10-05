---
id: "iss-cpackget-229"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add crashes with a nil pointer for a local pack whose url is a file:/// location"
summary: "FileExists used the result of os.Stat without checking for an error, which panicked for the file:/// source pack path."
status: "draft"
tool: "cpackget"
symptoms: ["panic: runtime error: invalid memory address or nil pointer dereference"]
symptom_regex: "panic:\\s+runtime\\s+error:\\s+invalid\\s+memory\\s+address\\s+or\\s+nil\\s+pointer\\s+dereference"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/229"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/229"
resolution: "fixed-in-release"
versions: "2.1.x"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`panic: runtime error: invalid memory address or nil pointer dereference`

## Cause

FileExists used the result of os.Stat without checking for an error, which panicked for the file:/// source pack path.

## Fix

Use a cpackget release from after July 2024 where FileExists handles the nil file info.

## Source

Resolution: fixed-in-release

Versions: 2.1.x

From [Open-CMSIS-Pack/cpackget #229](https://github.com/Open-CMSIS-Pack/cpackget/issues/229), summarized in own words; confidence high, not reviewed yet.
