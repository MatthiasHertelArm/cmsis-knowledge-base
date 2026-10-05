---
id: "iss-toolbox-188"
type: "troubleshooting"
domain: "project"
title: "csolution: csolution list configs without a solution file crashes silently"
summary: "'csolution list configs' without an input *.csolution.yml crashed silently with a non-zero exit code instead of reporting the missing argument."
status: "draft"
tool: "csolution"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/188"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/188"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

'csolution list configs' without an input *.csolution.yml crashed silently with a non-zero exit code instead of reporting the missing argument.

## Fix

Pass the solution file, e.g. csolution list configs <name>.csolution.yml. Nightly builds from 2024-12-02 (csolution 2.6.0+p56) report 'input yml files were not specified' instead of crashing.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/cmsis-toolbox #188](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/188), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
