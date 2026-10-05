---
id: "iss-pyocd-811"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Chip erase on STM32WB55 fails: flash algorithm runs on the wrong core"
summary: "STM32WB is dual-core with shared flash, and its reference manual says a mass erase issued by CPU1 (the Cortex-M4) is ignored with a bus error. pyOCD always ran flash operations on the first core and ignored the Pname of …"
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/811"
doc_source: "https://github.com/pyocd/pyOCD/issues/811"
resolution: "workaround"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["pyocd"], "device": ["STM32WB55RGVx"], "core": ["Cortex-M4", "Cortex-M0+"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

STM32WB is dual-core with shared flash, and its reference manual says a mass erase issued by CPU1 (the Cortex-M4) is ignored with a bus error. pyOCD always ran flash operations on the first core and ignored the Pname of the pack's algorithm element, although the maintainer noted the failure was reported by EraseChip() rather than as a bus error. A full chip erase with that pack also failed in Keil MDK.

## Fix

No fix in the thread; the maintainer said pyOCD would have to run the flash algorithm on the core named by the algorithm's Pname attribute.

## Source

Resolution: workaround

From [pyocd/pyOCD #811](https://github.com/pyocd/pyOCD/issues/811), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
