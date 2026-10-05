---
id: "iss-pyocd-647"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd cmd W32 to a flash address fails with NameError flashPtr"
summary: "program_phrase() in pyOCD's flash code tested an undefined variable flashPtr in its alignment check instead of the address, so a W32 to a flash address raised NameError."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: name 'flashPtr' is not defined"]
symptom_regex: "uncaught\\s+exception:\\s+name\\s+'.*?'\\s+is\\s+not\\s+defined"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/647"
doc_source: "https://github.com/pyocd/pyOCD/issues/647"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "family": ["nRF51 Series"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: name 'flashPtr' is not defined`

## Cause

program_phrase() in pyOCD's flash code tested an undefined variable flashPtr in its alignment check instead of the address, so a W32 to a flash address raised NameError.

## Fix

The maintainers took the bug on; the reporter's correction is to check address % min_len in program_phrase(). Use a pyOCD version that carries the correction.

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #647](https://github.com/pyocd/pyOCD/issues/647), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
