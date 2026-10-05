---
id: "iss-toolbox-458"
type: "troubleshooting"
domain: "project"
title: "cbuild: $SolutionDir()$ and $ProjectDir()$ in execute steps expand with extra ../ when -O is used"
summary: "cbuild2cmake computed the paths relative to the redirected output folder, so the expanded values contained a parent-directory component."
status: "draft"
tool: "cbuild"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/458"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/458"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

cbuild2cmake computed the paths relative to the redirected output folder, so the expanded values contained a parent-directory component.

## Fix

Use a toolbox nightly after November 2025 with the cbuild2cmake fix (confirmed by the reporter).

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/cmsis-toolbox #458](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/458), summarized in own words; confidence high, not reviewed yet.
