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
resolution: "not-a-bug"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution", "cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The misc options of the different levels are additive and their order on the command line is implementation defined: cproject, then csolution, then cdefault, then build-type, then target-type. Because the last occurrence of a repeated option wins in AC6, Clang and GCC, a value from cdefault.yml (for example -gdwarf4) beats one from csolution.yml (-gdwarf5). Maintainers see this as a possible future change, which would be a breaking one.

## Fix

To override a cdefault.yml option today, put the replacement option in a level that is emitted later, i.e. under build-types or target-types, or remove the conflicting option from cdefault.yml. Check the generated compile_commands.json to see the final order.

## Source

Resolution: not-a-bug

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/cmsis-toolbox #423](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/423), summarized in own words; confidence medium, not reviewed yet.
