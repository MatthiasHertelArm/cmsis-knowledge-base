---
id: "iss-toolbox-458"
type: "troubleshooting"
domain: "project"
title: "cbuild: $SolutionDir()$ and $ProjectDir()$ in execute steps expand with extra ../ when -O is used"
summary: "A bug in cbuild2cmake made $SolutionDir()$ and $ProjectDir()$ in execute steps expand with an extra ../ component when cbuild's -O option was used."
status: "draft"
tool: "cbuild"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/458"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/458"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A bug in cbuild2cmake made $SolutionDir()$ and $ProjectDir()$ in execute steps expand with an extra ../ component when cbuild's -O option was used.

## Fix

Use a toolbox nightly that contains the cbuild2cmake fix (PR #381), which the reporter confirmed; no release is named.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/cmsis-toolbox #458](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/458), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
