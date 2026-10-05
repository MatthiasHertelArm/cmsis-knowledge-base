---
id: "iss-pyocd-1696"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STM32H753 firmware hard-faults after pyOCD flashing with the pack target"
summary: "The flash algorithm from the Keil STM32H7 pack can corrupt flash on these parts, so the programmed image is bad even though pyOCD reports success."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1696"
doc_source: "https://github.com/pyocd/pyOCD/issues/1696"
resolution: "workaround"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "family": ["STM32H7 Series"], "device": ["STM32H753ZI"], "core": ["Cortex-M7"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The flash algorithm from the Keil STM32H7 pack can corrupt flash on these parts, so the programmed image is bad even though pyOCD reports success. A built-in target for the same die programs correctly.

## Fix

Use the built-in target stm32h743xx (or stm32h750xx) instead of the pack-provided H753 target, e.g. -t stm32h750xx. A pull request also corrected sector sizes and a wrong RDP security-lock detection on that built-in target.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1696](https://github.com/pyocd/pyOCD/issues/1696), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
