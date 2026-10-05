---
id: "iss-devtools-1401"
type: "troubleshooting"
domain: "project"
title: "csolution: Layer variable with relative path fails when the cproject is in a subdirectory"
summary: "A relative path assigned to a variable in the csolution.yml is evaluated relative to the cproject.yml that uses it, which sits in another directory."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1401"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1401"
resolution: "workaround"
versions: "2.3.0-dev0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A relative path assigned to a variable in the csolution.yml is evaluated relative to the cproject.yml that uses it, which sits in another directory.

## Fix

Workaround: prefix the variable in the layer node with the relative path to the solution folder, for example layer: ../$Board-Layer$. Access sequences were not yet accepted in layer: at the time of that report.

## Source

Resolution: workaround

Versions: 2.3.0-dev0

From [Open-CMSIS-Pack/devtools #1401](https://github.com/Open-CMSIS-Pack/devtools/issues/1401), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
