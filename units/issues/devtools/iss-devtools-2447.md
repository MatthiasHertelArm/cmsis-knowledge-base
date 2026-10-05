---
id: "iss-devtools-2447"
type: "troubleshooting"
domain: "project"
title: "csolution: cbuild-run.yml rejected: flash blocks must be unique, but pdsc repeats blocks"
summary: "A flashinfo section with several identical block elements separated by gaps is valid per the PDSC specification, but the cbuild-run schema demanded unique array items."
status: "draft"
tool: "csolution"
symptoms: ["csolution error: Blank_solution+PIC32CZ8110CA90208.cbuild-run.yml:702:7\n  - items have to be unique for this array"]
symptom_regex: "csolution\\s+error:\\s+Blank_solution\\+PIC32CZ8110CA90208\\.cbuild\\-run\\.yml:\\S+:\\S+\\\\s+\\-\\s+items\\s+have\\s+to\\s+be\\s+unique\\s+for\\s+this\\s+array"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2447"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2447"
resolution: "fixed-in-release"
versions: "fixed in toolbox nightly 2026-04-22"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`csolution error: Blank_solution+PIC32CZ8110CA90208.cbuild-run.yml:702:7
  - items have to be unique for this array`

## Cause

A flashinfo section with several identical block elements separated by gaps is valid per the PDSC specification, but the cbuild-run schema demanded unique array items.

## Fix

Schema relaxed (uniqueItems false for the blocks array); fixed in toolbox builds from late April 2026 onward.

## Source

Resolution: fixed-in-release

Versions: fixed in toolbox nightly 2026-04-22

From [Open-CMSIS-Pack/devtools #2447](https://github.com/Open-CMSIS-Pack/devtools/issues/2447), summarized in own words; confidence high, not reviewed yet.
