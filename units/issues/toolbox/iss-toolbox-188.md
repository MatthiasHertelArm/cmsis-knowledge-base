---
id: "iss-toolbox-188"
type: "troubleshooting"
domain: "project"
title: "csolution: csolution list configs without a solution file crashes silently"
summary: "Calling the command without an input yml file crashed (non-zero exit with no message) on Windows and macOS Arm64."
status: "draft"
tool: "csolution"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/188"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/188"
resolution: "fixed-in-release"
versions: "2.6.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Calling the command without an input yml file crashed (non-zero exit with no message) on Windows and macOS Arm64.

## Fix

Pass the solution file, for example csolution list configs <name>.csolution.yml. Later builds print an error about missing input files instead of crashing.

## Source

Resolution: fixed-in-release

Versions: 2.6.0

From [Open-CMSIS-Pack/cmsis-toolbox #188](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/188), summarized in own words; confidence medium, not reviewed yet.
