---
id: "iss-pyocd-1206"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: LPC55S28 flash fails with 'No ACK received'"
summary: "The target was not responding to SWD; here one SWD pin had been reconfigured to another function in the application."
status: "draft"
tool: "pyocd"
symptoms: ["No ACK received"]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1206"
doc_source: "https://github.com/pyocd/pyOCD/issues/1206"
resolution: "user-error"
versions: "0.31.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["LPC55S28"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No ACK received`

## Cause

The target was not responding to SWD; here one SWD pin had been reconfigured to another function in the application.

## Fix

Remove the pin mux for the SWD pins or recover the device (reset or erase) so the debug port is reachable.

## Source

Resolution: user-error

Versions: 0.31.0

From [pyocd/pyOCD #1206](https://github.com/pyocd/pyOCD/issues/1206), summarized in own words; confidence medium, not reviewed yet.
