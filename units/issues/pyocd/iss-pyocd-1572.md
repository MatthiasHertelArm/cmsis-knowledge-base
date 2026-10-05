---
id: "iss-pyocd-1572"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd list shows target n/a for standalone ST-Link"
summary: "Automatic target detection only works for on-board probes whose firmware reports the board type; a standalone ST-Link cannot identify the MCU."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1572"
doc_source: "https://github.com/pyocd/pyOCD/issues/1572"
resolution: "not-a-bug"
versions: "0.35.1"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Automatic target detection only works for on-board probes whose firmware reports the board type; a standalone ST-Link cannot identify the MCU.

## Fix

Map the probe unique ID to a target in pyocd.yaml under 'probes:' with 'target_override', or pass -t.

## Source

Resolution: not-a-bug

Versions: 0.35.1

From [pyocd/pyOCD #1572](https://github.com/pyocd/pyOCD/issues/1572), summarized in own words; confidence high, not reviewed yet.
