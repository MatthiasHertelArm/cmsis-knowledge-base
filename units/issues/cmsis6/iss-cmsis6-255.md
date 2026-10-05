---
id: "iss-cmsis6-255"
type: "troubleshooting"
domain: "core"
title: "CMSIS-Core: __disable_irq() returns void in CMSIS 6, code relying on the old return value breaks"
summary: "Older Arm Compiler support (arm_compat.h) declared __disable_irq() as returning the previous mask state."
status: "draft"
tool: "cmsis-core"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/255"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/255"
resolution: "workaround"
versions: "changed after CMSIS 5.0.0 (exact version not named)"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-core"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Older Arm Compiler support (arm_compat.h) declared __disable_irq() as returning the previous mask state. When the include of arm_compat.h was dropped from the CMSIS toolchain headers, the CMSIS variant kept only the void signature, so code that saved the return value to restore interrupts later no longer builds.

## Fix

With Arm Compiler, include arm_compat.h explicitly to get the signature with the return value. The maintainer considers bringing the return value back in CMSIS and asked for a pull request; no change or release is shown.

## Source

Resolution: workaround

Versions: changed after CMSIS 5.0.0 (exact version not named)

The issue is still open: the fix is a workaround, a later release may change it.

From [ARM-software/CMSIS_6 #255](https://github.com/ARM-software/CMSIS_6/issues/255), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
