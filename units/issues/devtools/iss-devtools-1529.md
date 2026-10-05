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
versions: "2.5.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`provided combined connections not consumed:`

## Cause

The rule that a layer is unused when none of its provided connections are consumed was also applied to the project itself, so a project whose provides: entry had no consumer was skipped in layer detection.

## Fix

Fixed in a toolbox release after 2.5.0: a project stays valid even if none of its provided connections are consumed; the rule remains for layers.

## Source

Resolution: fixed-in-release

Versions: 2.5.0

From [Open-CMSIS-Pack/devtools #1529](https://github.com/Open-CMSIS-Pack/devtools/issues/1529), summarized in own words; confidence high, not reviewed yet.
