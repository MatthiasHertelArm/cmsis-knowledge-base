---
id: "iss-pyocd-335"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: K64F via Raspberry Pi: 'read thread exited' errors during reset or flashing"
summary: "USB instability on the Raspberry Pi 3 (and some VMs such as VirtualBox) loses packets between host and CMSIS-DAP probe."
status: "draft"
tool: "pyocd"
symptoms: ["DeviceError: ... read thread exited"]
symptom_regex: "DeviceError:\\s+\\.\\.\\.\\s+read\\s+thread\\s+exited"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/335"
doc_source: "https://github.com/pyocd/pyOCD/issues/335"
resolution: "workaround"
versions: "0.2x"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["MK66FN2M0xxx18"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`DeviceError: ... read thread exited`

## Cause

USB instability on the Raspberry Pi 3 (and some VMs such as VirtualBox) loses packets between host and CMSIS-DAP probe.

## Fix

Lower the SWD clock with `-f`, or pass `--daparg limit_packets=True`; alternatively reset the target by sending a BREAK over the DAPLink serial port.

## Source

Resolution: workaround

Versions: 0.2x

From [pyocd/pyOCD #335](https://github.com/pyocd/pyOCD/issues/335), summarized in own words; confidence medium, not reviewed yet.
