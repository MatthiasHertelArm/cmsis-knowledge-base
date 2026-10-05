---
id: "iss-pyocd-995"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: PSoC6: gdb 'monitor reset' fails with TransferError and kills the connection"
summary: "After a reset PSoC6 drops back to JTAG mode and loses DAP state, so the DAP must be fully re-initialised; the shared probe proxy turned the SWJ switch sequence into a no-op once the connect count was above one."
status: "draft"
tool: "pyocd"
symptoms: ["TransferError: No ACK received"]
symptom_regex: "TransferError:\\s+No\\s+ACK\\s+received"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/995"
doc_source: "https://github.com/pyocd/pyOCD/issues/995"
resolution: "fixed-in-release"
versions: "regression from 0.28.0; fixed by #1018"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["PSoC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`TransferError: No ACK received`

## Cause

After a reset PSoC6 drops back to JTAG mode and loses DAP state, so the DAP must be fully re-initialised; the shared probe proxy turned the SWJ switch sequence into a no-op once the connect count was above one.

## Fix

Use a pyOCD release that includes the reconnect rework from PR #1018 (after 0.28).

## Source

Resolution: fixed-in-release

Versions: regression from 0.28.0; fixed by #1018

From [pyocd/pyOCD #995](https://github.com/pyocd/pyOCD/issues/995), summarized in own words; confidence medium, not reviewed yet.
