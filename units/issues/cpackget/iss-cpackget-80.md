---
id: "iss-cpackget-80"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add: 'pack version not found' for versions like 2.0.0-alpha.0.5"
summary: "The semantic-version expression in the pack index spec had a repeating capture group that returned a variable number of matches for dotted pre-release parts, breaking version splitting."
status: "draft"
tool: "cpackget"
symptoms: ["E: pack version not found in the pdsc file"]
symptom_regex: "E:\\s+pack\\s+version\\s+not\\s+found\\s+in\\s+the\\s+pdsc\\s+file"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/80"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/80"
resolution: "fixed-in-release"
versions: "0.4.1 affected"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: pack version not found in the pdsc file`

## Cause

The semantic-version expression in the pack index spec had a repeating capture group that returned a variable number of matches for dotted pre-release parts, breaking version splitting.

## Fix

Use a cpackget release after 0.4.1 (the specification regex was also corrected).

## Source

Resolution: fixed-in-release

Versions: 0.4.1 affected

From [Open-CMSIS-Pack/cpackget #80](https://github.com/Open-CMSIS-Pack/cpackget/issues/80), summarized in own words; confidence high, not reviewed yet.
