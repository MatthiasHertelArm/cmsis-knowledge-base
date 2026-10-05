---
id: "iss-pyocd-812"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: NUCLEO-H743ZI2 flash fails with STLink error (5) No device connected"
summary: "The ST-Link read the AP IDRs once and then failed on the second read with 'No device connected'; ST suggested the target may be running and going into a sleep mode after the initial connect."
status: "draft"
tool: "pyocd"
symptoms: ["STLink error (5): No device connected"]
symptom_regex: "STLink\\s+error\\s+\\(\\S+\\):\\s+No\\s+device\\s+connected"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/812"
doc_source: "https://github.com/pyocd/pyOCD/issues/812"
resolution: "workaround"
versions: "0.24.1 and 0.25.0"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "family": ["STM32H7 Series"], "device": ["STM32H743ZITx"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`STLink error (5): No device connected`

## Cause

The ST-Link read the AP IDRs once and then failed on the second read with 'No device connected'; ST suggested the target may be running and going into a sleep mode after the initial connect.

## Fix

Retry with -Oconnect_mode=under-reset (or set connect_mode in pyocd.yaml); one participant reported this solved it, while the reporter still saw the failure with it on 0.25.0.

## Source

Resolution: workaround

Versions: 0.24.1 and 0.25.0

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #812](https://github.com/pyocd/pyOCD/issues/812), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
