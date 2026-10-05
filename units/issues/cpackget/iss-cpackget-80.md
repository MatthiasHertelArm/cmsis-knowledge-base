---
id: "iss-cpackget-80"
type: "troubleshooting"
domain: "pack"
title: "cpackget: cpackget add: 'pack version not found' for versions like 2.0.0-alpha.0.5"
summary: "The semantic-version expression taken from the pack index specification had a repeating capture group that returned a variable number of matches for dotted pre-release parts, which broke version splitting."
status: "draft"
tool: "cpackget"
symptoms: ["E: pack version not found in the pdsc file"]
symptom_regex: "E:\\s+pack\\s+version\\s+not\\s+found\\s+in\\s+the\\s+pdsc\\s+file"
collection: "issues-cpackget"
source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/80"
doc_source: "https://github.com/Open-CMSIS-Pack/cpackget/issues/80"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cpackget"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`E: pack version not found in the pdsc file`

## Cause

The semantic-version expression taken from the pack index specification had a repeating capture group that returned a variable number of matches for dotted pre-release parts, which broke version splitting.

## Fix

Use a cpackget release after 0.4.1 with the merged bugfix; a matching correction of the specification's regex was proposed.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/cpackget #80](https://github.com/Open-CMSIS-Pack/cpackget/issues/80), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
