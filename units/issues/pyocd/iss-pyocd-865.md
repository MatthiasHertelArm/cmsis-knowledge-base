---
id: "iss-pyocd-865"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: gdb 'load' after a chip erase fails on Kinetis with FlashFailure init error"
summary: "Initialising the flash algorithm in verify mode failed on K22F/K66F boards after the chip erase; both built-in and pack algorithms fail."
status: "draft"
tool: "pyocd"
symptoms: ["FlashFailure: init error: 536870913"]
symptom_regex: "FlashFailure:\\s+init\\s+error:\\s+\\S+"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/865"
doc_source: "https://github.com/pyocd/pyOCD/issues/865"
resolution: "fixed-in-release"
versions: "affected 0.26.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "family": ["Kinetis"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`FlashFailure: init error: 536870913`

## Cause

Initialising the flash algorithm in verify mode failed on K22F/K66F boards after the chip erase; both built-in and pack algorithms fail.

## Fix

Upgrade to a release after 0.26: pyOCD now retries the init in erase mode when verify init raises. Connecting under reset also improves stability.

## Source

Resolution: fixed-in-release

Versions: affected 0.26.0

From [pyocd/pyOCD #865](https://github.com/pyocd/pyOCD/issues/865), summarized in own words; confidence medium, not reviewed yet.
