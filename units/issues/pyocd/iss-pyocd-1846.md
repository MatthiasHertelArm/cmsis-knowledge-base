---
id: "iss-pyocd-1846"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: CMSIS-DAP v1 probe 'not found' on Windows/macOS after upgrading from 0.36 to 0.40"
summary: "A rework of the hidapi backend in 0.40 mishandled report sizes for some HID-based CMSIS-DAP v1 probes."
status: "draft"
tool: "pyocd"
symptoms: ["Probe 0226000005d968d700000000000000000000000097969905 not found"]
symptom_regex: "Probe\\s+0226000005d968d700000000000000000000000097969905\\s+not\\s+found"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1846"
doc_source: "https://github.com/pyocd/pyOCD/issues/1846"
resolution: "fixed-in-release"
versions: "broken 0.40.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Probe 0226000005d968d700000000000000000000000097969905 not found`

## Cause

A rework of the hidapi backend in 0.40 mishandled report sizes for some HID-based CMSIS-DAP v1 probes.

## Fix

Use a release including change #1854, which fixes the hidapi backend by reading the HID report descriptor.

## Source

Resolution: fixed-in-release

Versions: broken 0.40.0

From [pyocd/pyOCD #1846](https://github.com/pyocd/pyOCD/issues/1846), summarized in own words; confidence high, not reviewed yet.
