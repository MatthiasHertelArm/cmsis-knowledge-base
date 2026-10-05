---
id: "iss-toolbox-119"
type: "troubleshooting"
domain: "project"
title: "cbuild: misc options on a single file are missing in compile_commands.json"
summary: "The cbuildgen backend did not honor file-level misc: options in the compile command."
status: "draft"
tool: "cbuild"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/119"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/119"
resolution: "fixed-in-release"
versions: "before 2.4.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The cbuildgen backend did not honor file-level misc: options in the compile command.

## Fix

Use the cbuild2cmake backend (--cbuild2cmake) or upgrade to toolbox 2.4.0 where it is fixed.

## Source

Resolution: fixed-in-release

Versions: before 2.4.0

From [Open-CMSIS-Pack/cmsis-toolbox #119](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/119), summarized in own words; confidence high, checked against the thread, not reviewed yet.
