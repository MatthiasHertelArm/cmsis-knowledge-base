---
id: "iss-pyocd-1556"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: -Ocmsis_dap.prefer_v1 ignored by load/gdbserver; v2 open fails on Windows"
summary: "Probe enumeration reads cmsis_dap.prefer_v1 before command-line options are parsed, so it is ignored."
status: "draft"
tool: "pyocd"
symptoms: ["C Error: Operation not supported or unimplemented on this platform [__main__]"]
symptom_regex: "C\\s+Error:\\s+Operation\\s+not\\s+supported\\s+or\\s+unimplemented\\s+on\\s+this\\s+platform"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1556"
doc_source: "https://github.com/pyocd/pyOCD/issues/1556"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C Error: Operation not supported or unimplemented on this platform [__main__]`

## Cause

Probe enumeration reads cmsis_dap.prefer_v1 before command-line options are parsed, so it is ignored. The underlying v2 failure was a libusb bug: interface numbers of 10 or higher are mis-parsed on Windows.

## Fix

Give the probe's CMSIS-DAP v2 interface a number below 10 (the reporter planned to reorder the USB interfaces), or replace the libusb DLL in the installed libusb-package with a fixed build. The -O cmsis_dap.prefer_v1 option will not take effect for load or gdbserver until sessions are restructured.

## Source

Resolution: workaround

From [pyocd/pyOCD #1556](https://github.com/pyocd/pyOCD/issues/1556), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
