---
id: "iss-pyocd-995"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: PSoC6: gdb 'monitor reset' fails with TransferError and kills the connection"
summary: "After a reset PSoC6 drops back to JTAG mode and loses DAP state, so the DAP must be fully re-initialised; since 0.28.0 dp.init() goes through the shared probe proxy, which increments its connect count and then turns the SWJ …"
status: "draft"
tool: "pyocd"
symptoms: ["TransferError: No ACK received"]
symptom_regex: "TransferError:\\s+No\\s+ACK\\s+received"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/995"
doc_source: "https://github.com/pyocd/pyOCD/issues/995"
resolution: "workaround"
versions: "0.28.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "family": ["PSoC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`TransferError: No ACK received`

## Cause

After a reset PSoC6 drops back to JTAG mode and loses DAP state, so the DAP must be fully re-initialised; since 0.28.0 dp.init() goes through the shared probe proxy, which increments its connect count and then turns the SWJ switch sequence into a no-op.

## Fix

Pull request #1018 is meant to fix reconnecting; the maintainer asked the reporter to verify it. The reporter's tested workaround in the PSoC6 target code re-initialises the DAP after reset (SWJ sequence, reset_did_occur on the APs, read DP IDR, clear sticky errors, power up debug).

## Source

Resolution: workaround

Versions: 0.28.0

From [pyocd/pyOCD #995](https://github.com/pyocd/pyOCD/issues/995), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
