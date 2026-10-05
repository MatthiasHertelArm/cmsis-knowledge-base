---
id: "iss-pyocd-1846"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: CMSIS-DAP v1 probe 'not found' on Windows/macOS after upgrading from 0.36 to 0.40"
summary: "After upgrading from 0.36.0 to 0.40.0, opening a CMSIS-DAP v1 probe through the hidapi backend on Windows failed with 'Probe ... not found' although pyocd list showed it; the thread does not state the root cause."
status: "draft"
tool: "pyocd"
symptoms: ["Probe 0226000005d968d700000000000000000000000097969905 not found"]
symptom_regex: "Probe\\s+0226000005d968d700000000000000000000000097969905\\s+not\\s+found"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1846"
doc_source: "https://github.com/pyocd/pyOCD/issues/1846"
resolution: "fixed-in-release"
versions: "0.36.0 worked; broken in 0.40.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Probe 0226000005d968d700000000000000000000000097969905 not found`

## Cause

After upgrading from 0.36.0 to 0.40.0, opening a CMSIS-DAP v1 probe through the hidapi backend on Windows failed with 'Probe ... not found' although pyocd list showed it; the thread does not state the root cause.

## Fix

Use a pyOCD version containing change #1854 (hidapi backend changes), which the reporter confirmed works on Windows.

## Source

Resolution: fixed-in-release

Versions: 0.36.0 worked; broken in 0.40.0

From [pyocd/pyOCD #1846](https://github.com/pyocd/pyOCD/issues/1846), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
