---
id: "iss-pyocd-1222"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: DAPLink probe: DP IDCODE read failed or No ACK, board not auto-detected"
summary: "Maintainers said 'No ACK' and 'DP IDCODE read failed' usually mean the probe cannot talk to the target, most often because the target is in a low-power mode."
status: "draft"
tool: "pyocd"
symptoms: ["DP IDCODE read failed; resending SWJ sequence (use dormant=False)"]
symptom_regex: "DP\\s+IDCODE\\s+read\\s+failed;\\s+resending\\s+SWJ\\s+sequence\\s+\\(use\\s+dormant=False\\)"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1222"
doc_source: "https://github.com/pyocd/pyOCD/issues/1222"
resolution: "unresolved"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["pyocd"], "device": ["STM32WB55RG"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`DP IDCODE read failed; resending SWJ sequence (use dormant=False)`

## Cause

Maintainers said 'No ACK' and 'DP IDCODE read failed' usually mean the probe cannot talk to the target, most often because the target is in a low-power mode. Board auto-detection needs a DAPLink build with a built-in target; standalone HIC builds report an all-zero board ID.

## Fix

Suggested, not confirmed: connect under reset (pyocd erase --connect=under-reset; the option is --connect, not --connect-mode), and check wiring, target power and the probe. For auto-detection use a DAPLink build made for the board.

## Source

Resolution: unresolved

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1222](https://github.com/pyocd/pyOCD/issues/1222), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
