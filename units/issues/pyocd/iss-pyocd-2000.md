---
id: "iss-pyocd-2000"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: CMSIS-DAP v2 probe without USB serial number is listed but 'not found' when opening"
summary: "A probe with no USB serial string gets a generated unique ID in the probe list, but the open path compared that ID against the real (missing) serial number and failed to match the device."
status: "draft"
tool: "pyocd"
symptoms: ["Probe NKBA2RU557ZLCOPTYPWHIX3IZUQ5ZH7B not found [__main__]"]
symptom_regex: "Probe\\s+NKBA2RU557ZLCOPTYPWHIX3IZUQ5ZH7B\\s+not\\s+found"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/2000"
doc_source: "https://github.com/pyocd/pyOCD/issues/2000"
resolution: "fixed-in-release"
versions: "seen on 0.44.1"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Probe NKBA2RU557ZLCOPTYPWHIX3IZUQ5ZH7B not found [__main__]`

## Cause

A probe with no USB serial string gets a generated unique ID in the probe list, but the open path compared that ID against the real (missing) serial number and failed to match the device.

## Fix

Use a pyOCD version containing the fix for serial-less CMSIS-DAP v2 probes (change #2007), which the reporter confirmed.

## Source

Resolution: fixed-in-release

Versions: seen on 0.44.1

From [pyocd/pyOCD #2000](https://github.com/pyocd/pyOCD/issues/2000), summarized in own words; confidence high, not reviewed yet.
