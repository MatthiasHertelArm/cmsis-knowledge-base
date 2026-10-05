---
id: "iss-pyocd-802"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Flashing via gdb fails: type object 'Target' has no attribute 'CATCH_CORE_RESET'"
summary: "A regression after the constant CATCH_CORE_RESET was renamed left one use of the old name in the flash loader."
status: "draft"
tool: "pyocd"
symptoms: ["Unhandled exception in handle_message: type object 'Target' has no attribute 'CATCH_CORE_RESET'"]
symptom_regex: "Unhandled\\s+exception\\s+in\\s+handle_message:\\s+type\\s+object\\s+'.*?'\\s+has\\s+no\\s+attribute\\s+'.*?'"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/802"
doc_source: "https://github.com/pyocd/pyOCD/issues/802"
resolution: "fixed-in-release"
versions: "affected 0.24.1"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["LPC1768"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`Unhandled exception in handle_message: type object 'Target' has no attribute 'CATCH_CORE_RESET'`

## Cause

A regression after the constant CATCH_CORE_RESET was renamed left one use of the old name in the flash loader.

## Fix

Use a release after 0.24.1 (fix merged as PR #821).

## Source

Resolution: fixed-in-release

Versions: affected 0.24.1

From [pyocd/pyOCD #802](https://github.com/pyocd/pyOCD/issues/802), summarized in own words; confidence high, not reviewed yet.
