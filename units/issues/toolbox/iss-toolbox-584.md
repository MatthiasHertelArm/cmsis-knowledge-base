---
id: "iss-toolbox-584"
type: "troubleshooting"
domain: "project"
title: "cbuild: Startup/linker files in RTE are not replaced after changing compiler in csolution.yml"
summary: "The tools never delete configuration files from the RTE folder."
status: "draft"
tool: "cbuild"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/584"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/584"
resolution: "not-a-bug"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The tools never delete configuration files from the RTE folder. If a pack offers compiler-specific config files under the same component, the file names or extensions must differ per compiler; here the pack description did not do that.

## Fix

Fix the pack description so compiler variants have mutually exclusive file names. As a workaround delete the stale RTE files, switch the compiler and run Update RTE.

## Source

Resolution: not-a-bug

From [Open-CMSIS-Pack/cmsis-toolbox #584](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/584), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
