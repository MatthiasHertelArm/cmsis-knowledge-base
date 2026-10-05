---
id: "iss-pyocd-313"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd-gdbserver AssertionError at start because another program holds the probe"
summary: "The probe is opened for exclusive access; the assertion fires when another process (an IDE, mbed tools, a serial tool) already has the CMSIS-DAP interface open."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception:", "AssertionError"]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/313"
doc_source: "https://github.com/pyocd/pyOCD/issues/313"
resolution: "user-error"
versions: "0.8.1"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["MK64FN1M0xxx12"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception:`
`AssertionError`

## Cause

The probe is opened for exclusive access; the assertion fires when another process (an IDE, mbed tools, a serial tool) already has the CMSIS-DAP interface open.

## Fix

Close other programs that use the board, replug it, and start pyOCD again.

## Source

Resolution: user-error

Versions: 0.8.1

From [pyocd/pyOCD #313](https://github.com/pyocd/pyOCD/issues/313), summarized in own words; confidence medium, not reviewed yet.
