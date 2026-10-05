---
id: "iss-pyocd-294"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flash programming errors 102 on FRDM-KL28Z because old DAPLink reports a clashing board ID"
summary: "A pre-production DAPLink image on the board used board ID 0290, which pyOCD maps to the FRDM-KW40Z, so the wrong flash algorithm was loaded."
status: "draft"
tool: "pyocd"
symptoms: ["ERROR:root:programPage(0x0) error: 102", "ERROR:root:Too many page programming errors, aborting program operation"]
symptom_regex: "programPage\\(\\S+\\)\\s+error:\\s+\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/294"
doc_source: "https://github.com/pyocd/pyOCD/issues/294"
resolution: "workaround"
versions: "0.8"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["MKL28Z512xxx7"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ERROR:root:programPage(0x0) error: 102`
`ERROR:root:Too many page programming errors, aborting program operation`

## Cause

A pre-production DAPLink image on the board used board ID 0290, which pyOCD maps to the FRDM-KW40Z, so the wrong flash algorithm was loaded.

## Fix

Update the DAPLink firmware (the KL28Z ID became 0205), or force the target with `-t frdmkl28z`.

## Source

Resolution: workaround

Versions: 0.8

From [pyocd/pyOCD #294](https://github.com/pyocd/pyOCD/issues/294), summarized in own words; confidence high, not reviewed yet.
