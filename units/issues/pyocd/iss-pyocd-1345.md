---
id: "iss-pyocd-1345"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Session open fails: 'SYS_AP_PSoC64' object has no attribute 'core'"
summary: "GenericMemAPTarget lost its CoreSightCoreComponent base class in a refactor."
status: "draft"
tool: "pyocd"
symptoms: ["'SYS_AP_PSoC64' object has no attribute 'core'"]
symptom_regex: "'.*?'\\s+object\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1345"
doc_source: "https://github.com/pyocd/pyOCD/issues/1345"
resolution: "fixed-in-release"
versions: "0.33"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`'SYS_AP_PSoC64' object has no attribute 'core'`

## Cause

GenericMemAPTarget lost its CoreSightCoreComponent base class in a refactor.

## Fix

Fixed by change #1350; update pyOCD.

## Source

Resolution: fixed-in-release

Versions: 0.33

From [pyocd/pyOCD #1345](https://github.com/pyocd/pyOCD/issues/1345), summarized in own words; confidence medium, not reviewed yet.
