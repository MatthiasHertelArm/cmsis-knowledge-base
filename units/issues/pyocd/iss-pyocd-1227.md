---
id: "iss-pyocd-1227"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: RP2040 over DAPLink probe: requires a probe with SWD sequence capability"
summary: "RP2040 needs CMSIS-DAP commands added in protocol version 1.2.0; the probe runs older DAPLink firmware."
status: "draft"
tool: "pyocd"
symptoms: ["pyocd.core.exceptions.TargetSupportError: RP2040 requires a debug probe with SWD sequence capability"]
symptom_regex: "pyocd\\.core\\.exceptions\\.TargetSupportError:\\s+RP2040\\s+requires\\s+a\\s+debug\\s+probe\\s+with\\s+SWD\\s+sequence\\s+capability"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1227"
doc_source: "https://github.com/pyocd/pyOCD/issues/1227"
resolution: "configuration"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["RP2040"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`pyocd.core.exceptions.TargetSupportError: RP2040 requires a debug probe with SWD sequence capability`

## Cause

RP2040 needs CMSIS-DAP commands added in protocol version 1.2.0; the probe runs older DAPLink firmware.

## Fix

Update the probe's DAPLink firmware to release 0254 or later.

## Source

Resolution: configuration

From [pyocd/pyOCD #1227](https://github.com/pyocd/pyOCD/issues/1227), summarized in own words; confidence high, not reviewed yet.
