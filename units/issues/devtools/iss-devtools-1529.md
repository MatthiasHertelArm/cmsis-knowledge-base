---
id: "iss-devtools-1529"
type: "troubleshooting"
domain: "project"
title: "csolution: Layer rejected because the project provides a connection that no layer consumes"
summary: "The rule that a layer is unused when none of its provided connections are consumed was also applied to the project itself, so a project whose provides: entry had no consumer was skipped in layer detection."
status: "draft"
tool: "csolution"
symptoms: ["provided combined connections not consumed:"]
symptom_regex: "provided\\s+combined\\s+connections\\s+not\\s+consumed:"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1529"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1529"
resolution: "fixed-in-release"
versions: "CMSIS-Toolbox 2.4.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`provided combined connections not consumed:`

## Cause

The rule that a layer is unused when none of its provided connections are consumed was also applied to the project itself, so a project whose provides: entry had no consumer was skipped in layer detection.

## Fix

The implementation was changed so a project stays valid even if none of its provided connections are consumed; the rule remains for layers. The thread names no release with the change.

## Source

Resolution: fixed-in-release

Versions: CMSIS-Toolbox 2.4.0

From [Open-CMSIS-Pack/devtools #1529](https://github.com/Open-CMSIS-Pack/devtools/issues/1529), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
