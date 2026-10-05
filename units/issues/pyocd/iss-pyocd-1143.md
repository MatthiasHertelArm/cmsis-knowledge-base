---
id: "iss-pyocd-1143"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: CMSIS-DAP probe open fails with ValueError parsing the firmware version string"
summary: "Some probe firmwares (Microchip EDBG, Particle DAPLink) put a vendor firmware revision in the DAP_Info field that older CMSIS-DAP specs described loosely as firmware version but is really the protocol version; pyOCD tried to parse it as numbers."
status: "draft"
tool: "pyocd"
symptoms: ["ValueError: invalid literal for int() with base 10: '01B6'"]
symptom_regex: "ValueError:\\s+invalid\\s+literal\\s+for\\s+int\\(\\)\\s+with\\s+base\\s+\\S+:\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1143"
doc_source: "https://github.com/pyocd/pyOCD/issues/1143"
resolution: "fixed-in-release"
versions: "fixed in 0.32.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["ATSAMV71Q21B"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ValueError: invalid literal for int() with base 10: '01B6'`

## Cause

Some probe firmwares (Microchip EDBG, Particle DAPLink) put a vendor firmware revision in the DAP_Info field that older CMSIS-DAP specs described loosely as firmware version but is really the protocol version; pyOCD tried to parse it as numbers.

## Fix

Upgrade to pyOCD 0.32.0 or later, which tolerates non-conforming strings and falls back to protocol version 1.0.0.

## Source

Resolution: fixed-in-release

Versions: fixed in 0.32.0

From [pyocd/pyOCD #1143](https://github.com/pyocd/pyOCD/issues/1143), summarized in own words; confidence high, not reviewed yet.
