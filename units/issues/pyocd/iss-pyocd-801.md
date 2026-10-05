---
id: "iss-pyocd-801"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: LPC55S69 is treated as generic cortex_m and flashing fails unless -t is given"
summary: "The on-board probe runs LPC-Link2 firmware, which is shared by many NXP boards and carries no board ID, so pyOCD cannot detect the target."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/801"
doc_source: "https://github.com/pyocd/pyOCD/issues/801"
resolution: "not-a-bug"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "device": ["LPC55S69"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The on-board probe runs LPC-Link2 firmware, which is shared by many NXP boards and carries no board ID, so pyOCD cannot detect the target.

## Fix

Pass `-t lpc55s69`, or flash DAPLink firmware to the probe so the board is auto-detected.

## Source

Resolution: not-a-bug

From [pyocd/pyOCD #801](https://github.com/pyocd/pyOCD/issues/801), summarized in own words; confidence high, checked against the thread, not reviewed yet.
