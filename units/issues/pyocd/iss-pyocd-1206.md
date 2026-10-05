---
id: "iss-pyocd-1206"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: LPC55S28 flash fails with 'No ACK received'"
summary: "The target was not responding on SWD because the application had muxed one of the SWD pins to another function (the maintainer notes 'No ACK received' usually means low-power sleep or muxed SWD pins)."
status: "draft"
tool: "pyocd"
symptoms: ["No ACK received"]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1206"
doc_source: "https://github.com/pyocd/pyOCD/issues/1206"
resolution: "user-error"
versions: "0.31.0, 0.30.3"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["LPC55S28"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No ACK received`

## Cause

The target was not responding on SWD because the application had muxed one of the SWD pins to another function (the maintainer notes 'No ACK received' usually means low-power sleep or muxed SWD pins).

## Fix

Remove the application's pin configuration that reassigns the SWD pin; then flashing works.

## Source

Resolution: user-error

Versions: 0.31.0, 0.30.3

From [pyocd/pyOCD #1206](https://github.com/pyocd/pyOCD/issues/1206), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
