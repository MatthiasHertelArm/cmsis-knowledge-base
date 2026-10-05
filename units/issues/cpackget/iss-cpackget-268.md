---
id: "iss-cpackget-268"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add ARM::CMSIS@6.0.0+meta fails with 'pack version not found in the pdsc file'"
summary: "Build metadata after + must be ignored for comparison (SemVer), but cpackget compared it literally against the releases in the pdsc."
status: "draft"
tool: "cpackget"
symptoms: ["E: pack version not found in the pdsc file"]
symptom_regex: "E:\\s+pack\\s+version\\s+not\\s+found\\s+in\\s+the\\s+pdsc\\s+file"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/268"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/268"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: pack version not found in the pdsc file`

## Cause

Build metadata after + must be ignored for comparison (SemVer), but cpackget compared it literally against the releases in the pdsc. Packs differing only in metadata are the same version and share one install folder.

## Fix

Use a cpackget with the fix (PR 273, March 2024) or omit the +meta part from the pack specification.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/cpackget #268](https://github.com/Open-CMSIS-Pack/cpackget/issues/268), summarized in own words; confidence medium, not reviewed yet.
