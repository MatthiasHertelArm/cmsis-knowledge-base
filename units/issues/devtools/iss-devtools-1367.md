---
id: "iss-devtools-1367"
type: "troubleshooting"
domain: "project"
title: "csolution: Duplicate entry error in cbuild.yml when a define repeats one set by the device"
summary: "The solution defined CPU_K32L3A60VPJ1A_cm4 itself although the pack's device description already adds that define, so the generated cbuild.yml listed it twice and the schema reported a duplicate."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1367"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1367"
resolution: "fixed-in-release"
versions: "2.2.1, fixed in 2.3.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The solution defined CPU_K32L3A60VPJ1A_cm4 itself although the pack's device description already adds that define, so the generated cbuild.yml listed it twice and the schema reported a duplicate.

## Fix

Remove the redundant define from the csolution. The duplicate tolerance was addressed in CMSIS-Toolbox 2.3.0.

## Source

Resolution: fixed-in-release

Versions: 2.2.1, fixed in 2.3.0

From [Open-CMSIS-Pack/devtools #1367](https://github.com/Open-CMSIS-Pack/devtools/issues/1367), summarized in own words; confidence high, checked against the thread, not reviewed yet.
