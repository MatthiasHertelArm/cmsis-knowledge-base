---
id: "iss-pyocd-270"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd lists no boards on Linux unless run with sudo"
summary: "On Linux a normal user lacked the access rights to the probe's USB device, so pyOCD found no boards while mbedls did; running with sudo worked."
status: "draft"
tool: "pyocd"
symptoms: ["No available boards are connected"]
symptom_regex: "No\\s+available\\s+boards\\s+are\\s+connected"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/270"
doc_source: "https://github.com/pyocd/pyOCD/issues/270"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No available boards are connected`

## Cause

On Linux a normal user lacked the access rights to the probe's USB device, so pyOCD found no boards while mbedls did; running with sudo worked.

## Fix

Run pyOCD with sudo; the reporter asked for documentation on how to run without sudo, and the issue was closed as a duplicate of #267.

## Source

Resolution: configuration

From [pyocd/pyOCD #270](https://github.com/pyocd/pyOCD/issues/270), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
