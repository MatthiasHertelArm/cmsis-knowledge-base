---
id: "iss-toolbox-195"
type: "troubleshooting"
domain: "project"
title: "cbuild: Files in nested groups are compiled without -g and -O options"
summary: "cbuild 2.6.1 did not pass the project-level compile options to files placed in sub-groups, so no debug info was produced and breakpoints failed."
status: "draft"
tool: "cbuild"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/195"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/195"
resolution: "fixed-in-release"
versions: "2.6.1"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

cbuild 2.6.1 did not pass the project-level compile options to files placed in sub-groups, so no debug info was produced and breakpoints failed.

## Fix

Use a toolbox newer than 2.6.1 (nightly of December 2024 and later); or temporarily avoid nested groups.

## Source

Resolution: fixed-in-release

Versions: 2.6.1

From [Open-CMSIS-Pack/cmsis-toolbox #195](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/195), summarized in own words; confidence high, not reviewed yet.
