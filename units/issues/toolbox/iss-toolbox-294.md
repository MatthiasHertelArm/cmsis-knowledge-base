---
id: "iss-toolbox-294"
type: "troubleshooting"
domain: "project"
title: "csolution: Project in a directory with a $ in its path fails with malformed access sequence"
summary: "csolution fails when the absolute output path contains '$', which the reporter suspected collides with access sequences; with output redirected to a path without '$' it succeeds."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: malformed access sequence: '/$test/Blinky_FRDM-K32L3A6"]
symptom_regex: "malformed\\s+access\\s+sequence:\\s+'/\\$test/Blinky_FRDM\\-K32L3A6"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/294"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/294"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: malformed access sequence: '/$test/Blinky_FRDM-K32L3A6`

## Cause

csolution fails when the absolute output path contains '$', which the reporter suspected collides with access sequences; with output redirected to a path without '$' it succeeds. A maintainer proposed won't fix.

## Fix

Avoid $ in directory names, or redirect output with -O to a path without it.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/cmsis-toolbox #294](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/294), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
