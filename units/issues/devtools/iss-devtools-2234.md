---
id: "iss-devtools-2234"
type: "troubleshooting"
domain: "project"
title: "csolution: Error that the solution requires a newer CMSIS-Toolbox version"
summary: "The created-for: node of the solution names a minimum CMSIS-Toolbox version that is higher than the version of the CMSIS-Toolbox manifest in use (not the csolution executable version)."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: solution requires newer CMSIS-Toolbox version 2.12.0"]
symptom_regex: "solution\\s+requires\\s+newer\\s+CMSIS\\-Toolbox\\s+version\\s+\\S+"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2234"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2234"
resolution: "configuration"
versions: "new message in csolution 2.11.0+p28"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: solution requires newer CMSIS-Toolbox version 2.12.0`

## Cause

The created-for: node of the solution names a minimum CMSIS-Toolbox version that is higher than the version of the CMSIS-Toolbox manifest in use (not the csolution executable version).

## Fix

Use a CMSIS-Toolbox at least as new as created-for. Newer csolution builds name the file, the required and the current version; the message stays an error on the command line but is a warning in RPC mode (VS Code), where a schema error still stops processing.

## Source

Resolution: configuration

Versions: new message in csolution 2.11.0+p28

From [Open-CMSIS-Pack/devtools #2234](https://github.com/Open-CMSIS-Pack/devtools/issues/2234), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
