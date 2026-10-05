---
id: "iss-devtools-1262"
type: "troubleshooting"
domain: "project"
title: "csolution: Warning #500 duplicate pack ignored when the pack vendor is written in a different case"
summary: "Pack names are matched case-insensitively on Windows, so pack: Arm::CMSIS finds the ARM::CMSIS folder while cbuild-pack.yml from an earlier run records the upper-case name, and the pack is seen twice."
status: "draft"
tool: "csolution"
symptoms: ["warning #500: pack 'ARM::CMSIS@6.0.0' is already defined in file <packs>/ARM/CMSIS/6.0.0/ARM.CMSIS.pdsc - duplicate is ignored"]
symptom_regex: "warning\\s+\\#\\S+:\\s+pack\\s+'.*?'\\s+is\\s+already\\s+defined\\s+in\\s+file\\s+<packs>\\S+\\s+\\-\\s+duplicate\\s+is\\s+ignored"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1262"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1262"
resolution: "user-error"
versions: "2.2.1"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`warning #500: pack 'ARM::CMSIS@6.0.0' is already defined in file <packs>/ARM/CMSIS/6.0.0/ARM.CMSIS.pdsc - duplicate is ignored`

## Cause

Pack names are matched case-insensitively on Windows, so pack: Arm::CMSIS finds the ARM::CMSIS folder while cbuild-pack.yml from an earlier run records the upper-case name, and the pack is seen twice.

## Fix

Write the vendor exactly as in the pack (ARM::CMSIS), including in cproject and clayer files, so projects stay portable to case-sensitive systems.

## Source

Resolution: user-error

Versions: 2.2.1

From [Open-CMSIS-Pack/devtools #1262](https://github.com/Open-CMSIS-Pack/devtools/issues/1262), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
