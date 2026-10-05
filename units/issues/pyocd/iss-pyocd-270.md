---
id: "iss-pyocd-270"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd lists no boards on Linux unless run with sudo"
summary: "Normal users have no permission on the USB device nodes of the debug probe, so enumeration finds nothing."
status: "draft"
tool: "pyocd"
symptoms: ["No available boards are connected"]
symptom_regex: "No\\s+available\\s+boards\\s+are\\s+connected"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/270"
doc_source: "https://github.com/pyocd/pyOCD/issues/270"
resolution: "configuration"
versions: "0.8"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No available boards are connected`

## Cause

Normal users have no permission on the USB device nodes of the debug probe, so enumeration finds nothing.

## Fix

Install a udev rule that grants access to the probe (the project ships udev/50-pyocd.rules), reload udev and replug; pyOCD logs a debug-level permission hint.

## Source

Resolution: configuration

Versions: 0.8

From [pyocd/pyOCD #270](https://github.com/pyocd/pyOCD/issues/270), summarized in own words; confidence high, not reviewed yet.
