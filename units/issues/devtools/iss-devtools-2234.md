---
id: "iss-devtools-2234"
type: "troubleshooting"
domain: "project"
title: "csolution: Error that the solution requires a newer CMSIS-Toolbox version"
summary: "The created-for: node of the solution names a minimum CMSIS-Toolbox version that is higher than the version of the installed toolbox manifest."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: solution requires newer CMSIS-Toolbox version 2.12.0"]
symptom_regex: "solution\\s+requires\\s+newer\\s+CMSIS\\-Toolbox\\s+version\\s+\\S+"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2234"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2234"
resolution: "configuration"
versions: "message reworded after 2.11.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: solution requires newer CMSIS-Toolbox version 2.12.0`

## Cause

The created-for: node of the solution names a minimum CMSIS-Toolbox version that is higher than the version of the installed toolbox manifest.

## Fix

Install a CMSIS-Toolbox at least as new as created-for, or lower created-for if the solution does not need it. Newer builds print the file, required and current version; in RPC mode (VS Code) it is only a warning.

## Source

Resolution: configuration

Versions: message reworded after 2.11.0

From [Open-CMSIS-Pack/devtools #2234](https://github.com/Open-CMSIS-Pack/devtools/issues/2234), summarized in own words; confidence high, not reviewed yet.
