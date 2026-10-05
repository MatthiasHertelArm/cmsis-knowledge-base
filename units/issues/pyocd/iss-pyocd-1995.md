---
id: "iss-pyocd-1995"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: RTT up channel bytes_available raises AttributeError on 'target'"
summary: "Typo in the RTT channel code: it used an attribute named target where the object stores it as _target."
status: "draft"
tool: "pyocd"
symptoms: ["'GenericRTTUpChannel' object has no attribute 'target'"]
symptom_regex: "'.*?'\\s+object\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1995"
doc_source: "https://github.com/pyocd/pyOCD/issues/1995"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`'GenericRTTUpChannel' object has no attribute 'target'`

## Cause

Typo in the RTT channel code: it used an attribute named target where the object stores it as _target.

## Fix

Fixed upstream; use a pyOCD release that includes the correction.

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #1995](https://github.com/pyocd/pyOCD/issues/1995), summarized in own words; confidence medium, not reviewed yet.
