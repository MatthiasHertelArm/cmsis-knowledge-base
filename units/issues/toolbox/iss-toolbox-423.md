---
id: "iss-toolbox-423"
type: "troubleshooting"
domain: "project"
title: "csolution: cdefault.yml compiler option overrides the same option set in csolution or cproject"
summary: "The misc options of the different levels are additive and their order on the command line is implementation defined: cproject, then csolution, then cdefault, then build-type, then target-type."
status: "draft"
tool: "csolution"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/423"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/423"
resolution: "unresolved"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution", "cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The misc options of the different levels are additive and their order on the command line is implementation defined: cproject, then csolution, then cdefault, then build-type, then target-type. Because the last occurrence of a repeated option wins in AC6, Clang and GCC, a value from cdefault.yml (for example -gdwarf4) beats one from csolution.yml (-gdwarf5).

## Fix

No change yet: a reordering with cdefault first, so that csolution and cproject options override it, was proposed as a breaking change and put up for review. The generated compile_commands.json shows the effective order.

## Source

Resolution: unresolved

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/cmsis-toolbox #423](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/423), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
