---
id: "iss-toolbox-294"
type: "troubleshooting"
domain: "project"
title: "csolution: Project in a directory with a $ in its path fails with malformed access sequence"
summary: "The dollar sign is interpreted as the start of an access sequence in the output path."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: malformed access sequence: '/$test/Blinky_FRDM-K32L3A6"]
symptom_regex: "malformed\\s+access\\s+sequence:\\s+'/\\$test/Blinky_FRDM\\-K32L3A6"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/294"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/294"
resolution: "workaround"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: malformed access sequence: '/$test/Blinky_FRDM-K32L3A6`

## Cause

The dollar sign is interpreted as the start of an access sequence in the output path. Marked as won't fix.

## Fix

Avoid $ in directory names, or redirect output with -O to a path without it.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/cmsis-toolbox #294](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/294), summarized in own words; confidence high, not reviewed yet.
