---
id: "iss-pyocd-337"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd-gdbserver TransferError right after 'DAP SWD MODE initialized' on an LPC812 board"
summary: "pyOCD could not even read the DP IDCODE register, which is always readable while the SW-DP is powered and its pins are connected, so the maintainer judged it a hardware problem rather than a pyOCD one."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception:", "TransferError"]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/337"
doc_source: "https://github.com/pyocd/pyOCD/issues/337"
resolution: "not-a-bug"
versions: "pyOCD 0.8.1a2.dev66; DAPLink 0243"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["LPC812M101JDH20"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception:`
`TransferError`

## Cause

pyOCD could not even read the DP IDCODE register, which is always readable while the SW-DP is powered and its pins are connected, so the maintainer judged it a hardware problem rather than a pyOCD one.

## Fix

Check the SWD connection and the target's power before suspecting pyOCD.

## Source

Resolution: not-a-bug

Versions: pyOCD 0.8.1a2.dev66; DAPLink 0243

From [pyocd/pyOCD #337](https://github.com/pyocd/pyOCD/issues/337), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
