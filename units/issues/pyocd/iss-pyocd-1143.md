---
id: "iss-pyocd-1143"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: CMSIS-DAP probe open fails with ValueError parsing the firmware version string"
summary: "Some probe firmwares (Microchip EDBG, Particle DAPLink) put a vendor firmware revision in the DAP_Info field that pre-2.1 CMSIS-DAP specs loosely called firmware version but that means protocol version; pyOCD tried to parse it as numbers."
status: "draft"
tool: "pyocd"
symptoms: ["ValueError: invalid literal for int() with base 10: '01B6'"]
symptom_regex: "ValueError:\\s+invalid\\s+literal\\s+for\\s+int\\(\\)\\s+with\\s+base\\s+\\S+:\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1143"
doc_source: "https://github.com/pyocd/pyOCD/issues/1143"
resolution: "fixed-in-release"
versions: "fixed in 0.32.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["ATSAMV71Q21B"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ValueError: invalid literal for int() with base 10: '01B6'`

## Cause

Some probe firmwares (Microchip EDBG, Particle DAPLink) put a vendor firmware revision in the DAP_Info field that pre-2.1 CMSIS-DAP specs loosely called firmware version but that means protocol version; pyOCD tried to parse it as numbers.

## Fix

Upgrade to pyOCD 0.32.0 or later, where the maintainer says this is resolved (the change discussed was to handle the parse error and default to CMSIS-DAP protocol 1.0.0 for unknown values).

## Source

Resolution: fixed-in-release

Versions: fixed in 0.32.0

From [pyocd/pyOCD #1143](https://github.com/pyocd/pyOCD/issues/1143), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
