---
id: "iss-cmsis6-195"
type: "troubleshooting"
domain: "core"
title: "CMSIS-Core: NVIC_SystemReset on Cortex-M55 may return without resetting"
summary: "On M55 the SYSRESETREQ bit is cleared on entry to WARM_RST; if the power controller denies the transition, no reset happens and nobody sets the bit again."
status: "draft"
tool: "cmsis-core"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/195"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/195"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-core"], "core": ["Cortex-M55"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

On M55 the SYSRESETREQ bit is cleared on entry to WARM_RST; if the power controller denies the transition, no reset happens and nobody sets the bit again. Arm errata 3776408.

## Fix

Re-assert AIRCR.SYSRESETREQ inside the wait loop of NVIC_SystemReset; maintainers asked for a PR with this change.

## Source

Resolution: workaround

From [ARM-software/CMSIS_6 #195](https://github.com/ARM-software/CMSIS_6/issues/195), summarized in own words; confidence medium, not reviewed yet.
