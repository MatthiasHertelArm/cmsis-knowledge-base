---
id: "iss-pyocd-1114"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: CMSIS-DAP connect raises AttributeError on a None protocol in v0.30"
summary: "A trace log statement in the CMSIS-DAP probe connect path accessed the protocol name even when no protocol had been chosen."
status: "draft"
tool: "pyocd"
symptoms: ["AttributeError: 'NoneType' object has no attribute 'name'"]
symptom_regex: "AttributeError:\\s+'.*?'\\s+object\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1114"
doc_source: "https://github.com/pyocd/pyOCD/issues/1114"
resolution: "fixed-in-release"
versions: "affected 0.30.0"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`AttributeError: 'NoneType' object has no attribute 'name'`

## Cause

A trace log statement in the CMSIS-DAP probe connect path accessed the protocol name even when no protocol had been chosen.

## Fix

Fixed by the maintainers shortly after 0.30.0; upgrade to a later 0.30.x or newer release.

## Source

Resolution: fixed-in-release

Versions: affected 0.30.0

From [pyocd/pyOCD #1114](https://github.com/pyocd/pyOCD/issues/1114), summarized in own words; confidence low, not reviewed yet.
