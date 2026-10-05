---
id: "iss-devtools-1402"
type: "troubleshooting"
domain: "project"
title: "csolution: Warning that key 'selected-by' was not recognized in cbuild-pack.yml"
summary: "The cbuild-pack.yml was written by an older toolbox (2.2) that used selected-by, later renamed selected-by-pack."
status: "draft"
tool: "csolution"
symptoms: ["warning csolution: key 'selected-by' was not recognized"]
symptom_regex: "key\\s+'.*?'\\s+was\\s+not\\s+recognized"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1402"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1402"
resolution: "fixed-in-release"
versions: "2.3.0-dev0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`warning csolution: key 'selected-by' was not recognized`

## Cause

The cbuild-pack.yml was written by an older toolbox (2.2) that used selected-by, later renamed selected-by-pack.

## Fix

Fixed in CMSIS-Toolbox 2.3.0, which accepts both keys. Alternatively delete the stale cbuild-pack.yml and run convert again.

## Source

Resolution: fixed-in-release

Versions: 2.3.0-dev0

From [Open-CMSIS-Pack/devtools #1402](https://github.com/Open-CMSIS-Pack/devtools/issues/1402), summarized in own words; confidence high, not reviewed yet.
