---
id: "iss-pyocd-1222"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: DAPLink probe: DP IDCODE read failed or No ACK, board not auto-detected"
summary: "These errors mean the probe cannot talk to the target, often because the target is in a low-power mode."
status: "draft"
tool: "pyocd"
symptoms: ["DP IDCODE read failed; resending SWJ sequence (use dormant=False)"]
symptom_regex: "DP\\s+IDCODE\\s+read\\s+failed;\\s+resending\\s+SWJ\\s+sequence\\s+\\(use\\s+dormant=False\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1222"
doc_source: "https://github.com/pyocd/pyOCD/issues/1222"
resolution: "workaround"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["STM32WB55RG"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`DP IDCODE read failed; resending SWJ sequence (use dormant=False)`

## Cause

These errors mean the probe cannot talk to the target, often because the target is in a low-power mode. Board auto-detection needs a DAPLink build that has a built-in target ID.

## Fix

Connect under reset: pyocd erase --connect=under-reset (the option is --connect, not --connect-mode). Check wiring, power and probe. Use a DAPLink build that names its board for auto-detection.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1222](https://github.com/pyocd/pyOCD/issues/1222), summarized in own words; confidence low, not reviewed yet.
