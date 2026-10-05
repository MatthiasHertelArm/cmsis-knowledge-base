---
id: "iss-devtools-216"
type: "troubleshooting"
domain: "pack"
title: "packchk: WARNING M379 No example(s) found for Board"
summary: "packchk expects a board support pack to ship at least one example for each board."
status: "draft"
tool: "packchk"
symptoms: ["*** WARNING M379: <pack>.pdsc (Line 52)\n  No example(s) found for Board '[STMicroelectronics] B-U585I-IOT02A'."]
symptom_regex: "<pack>\\.pdsc\\s+\\(Line\\s+\\S+\\)\\\\s+No\\s+example\\(s\\)\\s+found\\s+for\\s+Board\\s+'.*?'\\."
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/216"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/216"
resolution: "configuration"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`*** WARNING M379: <pack>.pdsc (Line 52)
  No example(s) found for Board '[STMicroelectronics] B-U585I-IOT02A'.`

## Cause

packchk expects a board support pack to ship at least one example for each board.

## Fix

Add an example, or suppress the message with packchk -x M379.

## Source

Resolution: configuration

From [Open-CMSIS-Pack/devtools #216](https://github.com/Open-CMSIS-Pack/devtools/issues/216), summarized in own words; confidence high, checked against the thread, not reviewed yet.
