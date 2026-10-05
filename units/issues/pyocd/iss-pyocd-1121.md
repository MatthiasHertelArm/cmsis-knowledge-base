---
id: "iss-pyocd-1121"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: WCH-Link CMSIS-DAP probe is not listed by pyocd on macOS"
summary: "pyOCD recognises HID CMSIS-DAP probes by 'CMSIS-DAP' in the product name; the WCH-Link's product string lacks it, hidapi does not report interface names, and the WCH-Link's HID interface string descriptor is broken, so the probe was ignored on macOS …"
status: "draft"
tool: "pyocd"
symptoms: ["No available debug probes are connected"]
symptom_regex: "No\\s+available\\s+debug\\s+probes\\s+are\\s+connected"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1121"
doc_source: "https://github.com/pyocd/pyOCD/issues/1121"
resolution: "workaround"
versions: "0.30.3.dev0 (macOS), 0.29.0 (Windows)"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No available debug probes are connected`

## Cause

pyOCD recognises HID CMSIS-DAP probes by 'CMSIS-DAP' in the product name; the WCH-Link's product string lacks it, hidapi does not report interface names, and the WCH-Link's HID interface string descriptor is broken, so the probe was ignored on macOS (Windows with pyocd 0.29.0 listed it).

## Fix

Install the maintainer's branch that also looks for 'CMSIS-DAP' in the hidapi device path (pip install -U git+https://github.com/flit/pyOCD@bugfix/hidapi_uid_and_if_name); the reporter confirmed the probe is then found.

## Source

Resolution: workaround

Versions: 0.30.3.dev0 (macOS), 0.29.0 (Windows)

From [pyocd/pyOCD #1121](https://github.com/pyocd/pyOCD/issues/1121), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
