---
id: "iss-pyocd-294"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flash programming errors 102 on FRDM-KL28Z because old DAPLink reports a clashing board ID"
summary: "The board's old DAPLink reported board ID 0290, which pyOCD maps to the FRDM-KW40Z (the KL28Z's ID had been changed to 0205), so pyOCD treated the board as a KW40Z."
status: "draft"
tool: "pyocd"
symptoms: ["ERROR:root:programPage(0x0) error: 102", "ERROR:root:Too many page programming errors, aborting program operation"]
symptom_regex: "programPage\\(\\S+\\)\\s+error:\\s+\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/294"
doc_source: "https://github.com/pyocd/pyOCD/issues/294"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["MKL28Z512xxx7"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ERROR:root:programPage(0x0) error: 102`
`ERROR:root:Too many page programming errors, aborting program operation`

## Cause

The board's old DAPLink reported board ID 0290, which pyOCD maps to the FRDM-KW40Z (the KL28Z's ID had been changed to 0205), so pyOCD treated the board as a KW40Z.

## Fix

Update the DAPLink firmware (confirmed by the reporter), or force the target with `-t frdmkl28z`.

## Source

Resolution: configuration

From [pyocd/pyOCD #294](https://github.com/pyocd/pyOCD/issues/294), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
