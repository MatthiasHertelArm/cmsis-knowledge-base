---
id: "iss-pyocd-1026"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: ST-Link V3 connect to STM32F750 fails: 'AP wait' and no cores discovered"
summary: "A nominally identical second board worked, so the reporter put it down to a hardware fault on the first hand-soldered prototype; the maintainer notes Cortex-M7 STM32F7/H7 parts have been problematic and did not rule out an ST-Link V3 issue …"
status: "draft"
tool: "pyocd"
symptoms: ["Error attempting to probe CoreSight component referenced by ROM table entry #0: STLink error (16): AP wait", "No cores were discovered!"]
symptom_regex: "Error\\s+attempting\\s+to\\s+probe\\s+CoreSight\\s+component\\s+referenced\\s+by\\s+ROM\\s+table\\s+entry\\s+\\#\\S+:\\s+STLink\\s+error\\s+\\(\\S+\\):\\s+AP\\s+wait"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1026"
doc_source: "https://github.com/pyocd/pyOCD/issues/1026"
resolution: "not-a-bug"
versions: "ST-Link V3J7M2"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["STM32F750V8Tx"], "core": ["Cortex-M7"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Error attempting to probe CoreSight component referenced by ROM table entry #0: STLink error (16): AP wait`
`No cores were discovered!`

## Cause

A nominally identical second board worked, so the reporter put it down to a hardware fault on the first hand-soldered prototype; the maintainer notes Cortex-M7 STM32F7/H7 parts have been problematic and did not rule out an ST-Link V3 issue in pyOCD.

## Fix

Test with a second board or probe before suspecting pyOCD, and keep the ST-Link V3 firmware updated (early versions had bugs). Connecting under reset did not help here.

## Source

Resolution: not-a-bug

Versions: ST-Link V3J7M2

From [pyocd/pyOCD #1026](https://github.com/pyocd/pyOCD/issues/1026), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
