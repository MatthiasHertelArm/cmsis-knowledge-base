---
id: "iss-cmsis6-255"
type: "troubleshooting"
domain: "core"
title: "CMSIS-Core: __disable_irq() returns void in CMSIS 6, code relying on the old return value breaks"
summary: "Older Arm Compiler support headers declared __disable_irq() as returning the previous mask state."
status: "draft"
tool: "cmsis-core"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/255"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/255"
resolution: "workaround"
versions: "Behaviour changed between CMSIS 5.0.0 and later versions; the thread does not name a fixed release."
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-core"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Older Arm Compiler support headers declared __disable_irq() as returning the previous mask state. When the compat header was dropped from the CMSIS toolchain headers, the CMSIS variant kept only the void signature, so code that saved the return value to restore interrupts later no longer works.

## Fix

Do not use the return value. Save the state explicitly before disabling, for example read it with __get_PRIMASK() (Cortex-M) first, then call __disable_irq(), and restore with __set_PRIMASK(saved) afterwards. Maintainers agreed the signature should be brought back but no release containing that is named in the thread.

## Source

Resolution: workaround

Versions: Behaviour changed between CMSIS 5.0.0 and later versions; the thread does not name a fixed release.

The issue is still open: the fix is a workaround, a later release may change it.

From [ARM-software/CMSIS_6 #255](https://github.com/ARM-software/CMSIS_6/issues/255), summarized in own words; confidence medium, not reviewed yet.
