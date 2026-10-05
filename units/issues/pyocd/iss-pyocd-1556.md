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
versions: "0.35"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C Error: Operation not supported or unimplemented on this platform [__main__]`

## Cause

Probe enumeration reads cmsis_dap.prefer_v1 before command-line options are parsed, so it is ignored. The underlying v2 failure was a libusb bug: interface numbers of 10 or higher are mis-parsed on Windows.

## Fix

Renumber the probe's USB interfaces so the v2 interface is below 10, or use a different libusb build. Use a config file for prefer_v1.

## Source

Resolution: workaround

Versions: 0.35

From [pyocd/pyOCD #1556](https://github.com/pyocd/pyOCD/issues/1556), summarized in own words; confidence medium, not reviewed yet.
