---
id: "iss-pyocd-1026"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: ST-Link V3 connect to STM32F750 fails: 'AP wait' and no cores discovered"
summary: "In this thread the same firmware worked on a second, nominally identical board, so a hardware fault on the first prototype board was the cause; Cortex-M7 STM32F7/H7 parts are known to be touchy to connect to."
status: "draft"
tool: "pyocd"
symptoms: ["Error attempting to probe CoreSight component referenced by ROM table entry #0: STLink error (16): AP wait", "No cores were discovered!"]
symptom_regex: "Error\\s+attempting\\s+to\\s+probe\\s+CoreSight\\s+component\\s+referenced\\s+by\\s+ROM\\s+table\\s+entry\\s+\\#\\S+:\\s+STLink\\s+error\\s+\\(\\S+\\):\\s+AP\\s+wait"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1026"
doc_source: "https://github.com/pyocd/pyOCD/issues/1026"
resolution: "not-a-bug"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["STM32F750V8Tx"], "core": ["Cortex-M7"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Error attempting to probe CoreSight component referenced by ROM table entry #0: STLink error (16): AP wait`
`No cores were discovered!`

## Cause

In this thread the same firmware worked on a second, nominally identical board, so a hardware fault on the first prototype board was the cause; Cortex-M7 STM32F7/H7 parts are known to be touchy to connect to.

## Fix

Try `--connect=under-reset`, update the ST-Link V3 firmware (early versions had bugs), and test a second board or probe before suspecting pyOCD.

## Source

Resolution: not-a-bug

From [pyocd/pyOCD #1026](https://github.com/pyocd/pyOCD/issues/1026), summarized in own words; confidence low, not reviewed yet.
