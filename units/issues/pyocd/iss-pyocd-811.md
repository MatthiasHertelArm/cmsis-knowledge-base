---
id: "iss-pyocd-811"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Chip erase on STM32WB55 fails: flash algorithm runs on the wrong core"
summary: "STM32WB is dual-core and a mass erase issued from the application core (CPU1) is restricted; pyOCD always used the first core for flash operations and ignored the Pname attribute of the pack's algorithm element."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/811"
doc_source: "https://github.com/pyocd/pyOCD/issues/811"
resolution: "workaround"
versions: "seen with 0.24.1"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["STM32WB55RGVx"], "core": ["Cortex-M4", "Cortex-M0+"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

STM32WB is dual-core and a mass erase issued from the application core (CPU1) is restricted; pyOCD always used the first core for flash operations and ignored the Pname attribute of the pack's algorithm element. The same limitation appears with Keil MDK and that pack.

## Fix

Use a pyOCD release that honours the Pname of the flash algorithm; until then prefer sector erase over --chip on this part.

## Source

Resolution: workaround

Versions: seen with 0.24.1

From [pyocd/pyOCD #811](https://github.com/pyocd/pyOCD/issues/811), summarized in own words; confidence low, not reviewed yet.
