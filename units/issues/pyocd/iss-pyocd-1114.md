---
id: "iss-pyocd-1114"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: CMSIS-DAP connect raises AttributeError on a None protocol in v0.30"
summary: "A trace log statement in the CMSIS-DAP probe connect() accesses protocol.name while the protocol is None."
status: "draft"
tool: "pyocd"
symptoms: ["AttributeError: 'NoneType' object has no attribute 'name'"]
symptom_regex: "AttributeError:\\s+'.*?'\\s+object\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1114"
doc_source: "https://github.com/pyocd/pyOCD/issues/1114"
resolution: "unresolved"
versions: "0.30"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`AttributeError: 'NoneType' object has no attribute 'name'`

## Cause

A trace log statement in the CMSIS-DAP probe connect() accesses protocol.name while the protocol is None.

## Fix

The thread gives no confirmed fix.

## Source

Resolution: unresolved

Versions: 0.30

From [pyocd/pyOCD #1114](https://github.com/pyocd/pyOCD/issues/1114), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
