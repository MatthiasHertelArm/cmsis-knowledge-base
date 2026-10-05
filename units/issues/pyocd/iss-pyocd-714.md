---
id: "iss-pyocd-714"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Intermittent 'STLink error (20): DP wait' on ST boards after power cycling"
summary: "After a power cycle the Mbed OS application starts and goes to sleep without the DBGMCU_CR debug-in-sleep bits set; pyOCD sets these bits only when it connects and cannot wake a target that is already sleeping."
status: "draft"
tool: "pyocd"
symptoms: ["CRITICAL:__main__:STLink error (20): DP wait"]
symptom_regex: "STLink\\s+error\\s+\\(\\S+\\):\\s+DP\\s+wait"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/714"
doc_source: "https://github.com/pyocd/pyOCD/issues/714"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`CRITICAL:__main__:STLink error (20): DP wait`

## Cause

After a power cycle the Mbed OS application starts and goes to sleep without the DBGMCU_CR debug-in-sleep bits set; pyOCD sets these bits only when it connects and cannot wake a target that is already sleeping.

## Fix

In debug builds keep the firmware from sleeping at all, or have it set the DBGMCU_CR bits (such as DBG_SLEEP) at startup. Connecting under reset (connect_mode=under-reset) allowed a connection, and updating the ST-Link firmware cleared the error on most of the boards.

## Source

Resolution: configuration

From [pyocd/pyOCD #714](https://github.com/pyocd/pyOCD/issues/714), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
