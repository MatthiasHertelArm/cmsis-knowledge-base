---
id: "iss-pyocd-337"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd-gdbserver TransferError right after 'DAP SWD MODE initialized' on an LPC812 board"
summary: "pyOCD could not even read the DP IDCODE register, which is always readable if SWD is wired and powered, so the cause is on the hardware or probe side rather than software."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception:", "TransferError"]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/337"
doc_source: "https://github.com/pyocd/pyOCD/issues/337"
resolution: "not-a-bug"
versions: "0.2x"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["LPC812M101JDH20"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception:`
`TransferError`

## Cause

pyOCD could not even read the DP IDCODE register, which is always readable if SWD is wired and powered, so the cause is on the hardware or probe side rather than software.

## Fix

Check wiring, target power and the debug interface firmware before suspecting pyOCD.

## Source

Resolution: not-a-bug

Versions: 0.2x

From [pyocd/pyOCD #337](https://github.com/pyocd/pyOCD/issues/337), summarized in own words; confidence medium, not reviewed yet.
