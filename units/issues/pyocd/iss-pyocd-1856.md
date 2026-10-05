---
id: "iss-pyocd-1856"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flashing AIR001 fails with Memory transfer fault (write) after 0.36.0"
summary: "The built-in flash algorithm placed its data buffer at a RAM address that was wrong for the target when double buffering was not in use; this affected many internal targets, not only AIR001."
status: "draft"
tool: "pyocd"
symptoms: ["C Memory transfer fault (write) @ 0x20001000-0x2000107f [__main__]"]
symptom_regex: "C\\s+Memory\\s+transfer\\s+fault\\s+\\(write\\)\\s+@\\s+\\S+\\-\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1856"
doc_source: "https://github.com/pyocd/pyOCD/issues/1856"
resolution: "fixed-in-release"
versions: "worked 0.36.0, broken above"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["AIR001"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`C Memory transfer fault (write) @ 0x20001000-0x2000107f [__main__]`

## Cause

The built-in flash algorithm placed its data buffer at a RAM address that was wrong for the target when double buffering was not in use; this affected many internal targets, not only AIR001.

## Fix

Upgrade to a release containing change #1898 (generic fix for all internal targets). Workaround was moving the begin_data address in the target file to RAM start plus 0x270.

## Source

Resolution: fixed-in-release

Versions: worked 0.36.0, broken above

From [pyocd/pyOCD #1856](https://github.com/pyocd/pyOCD/issues/1856), summarized in own words; confidence high, not reviewed yet.
