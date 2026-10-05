---
id: "iss-pyocd-647"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd cmd W32 to a flash address fails with NameError flashPtr"
summary: "A coding bug in the flash write path used an undefined variable in the alignment check (the check should have tested the address against the minimum write length)."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: name 'flashPtr' is not defined"]
symptom_regex: "uncaught\\s+exception:\\s+name\\s+'.*?'\\s+is\\s+not\\s+defined"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/647"
doc_source: "https://github.com/pyocd/pyOCD/issues/647"
resolution: "fixed-in-release"
versions: "early 2019 builds"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["nRF51 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: name 'flashPtr' is not defined`

## Cause

A coding bug in the flash write path used an undefined variable in the alignment check (the check should have tested the address against the minimum write length).

## Fix

Use a pyOCD release containing the fix; to program flash use `pyocd flash` or the flash loader rather than raw memory writes.

## Source

Resolution: fixed-in-release

Versions: early 2019 builds

From [pyocd/pyOCD #647](https://github.com/pyocd/pyOCD/issues/647), summarized in own words; confidence medium, not reviewed yet.
