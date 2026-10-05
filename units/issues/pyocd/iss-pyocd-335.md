---
id: "iss-pyocd-335"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: K64F via Raspberry Pi: 'read thread exited' errors during reset or flashing"
summary: "USB instability on the Raspberry Pi 3; the maintainer closed the issue as a Raspberry Pi USB problem."
status: "draft"
tool: "pyocd"
symptoms: ["DeviceError: ... read thread exited"]
symptom_regex: "DeviceError:\\s+\\.\\.\\.\\s+read\\s+thread\\s+exited"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/335"
doc_source: "https://github.com/pyocd/pyOCD/issues/335"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["MK66FN2M0xxx18"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`DeviceError: ... read thread exited`

## Cause

USB instability on the Raspberry Pi 3; the maintainer closed the issue as a Raspberry Pi USB problem.

## Fix

Suggestions, none confirmed: lower the DAP frequency, pass `--daparg limit_packets=True` (also needed under some VMs such as VirtualBox on Windows), or reset the target by sending a break over DAPLink's virtual COM port.

## Source

Resolution: workaround

From [pyocd/pyOCD #335](https://github.com/pyocd/pyOCD/issues/335), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
