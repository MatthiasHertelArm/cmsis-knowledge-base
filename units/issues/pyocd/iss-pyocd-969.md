---
id: "iss-pyocd-969"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pyocd commander --elf crashes with 'name os is not defined'"
summary: "A missing import of os in commands/commander.py (regression in a 0.28.1 development build) broke the --elf option."
status: "draft"
tool: "pyocd"
symptoms: ["uncaught exception: name 'os' is not defined"]
symptom_regex: "uncaught\\s+exception:\\s+name\\s+'.*?'\\s+is\\s+not\\s+defined"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/969"
doc_source: "https://github.com/pyocd/pyOCD/issues/969"
resolution: "fixed-in-release"
versions: "affected 0.28.1.dev builds"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`uncaught exception: name 'os' is not defined`

## Cause

A missing import of os in commands/commander.py (regression in a 0.28.1 development build) broke the --elf option.

## Fix

Update to a release that contains the maintainer's patch; avoid --elf on the affected dev build.

## Source

Resolution: fixed-in-release

Versions: affected 0.28.1.dev builds

From [pyocd/pyOCD #969](https://github.com/pyocd/pyOCD/issues/969), summarized in own words; confidence medium, not reviewed yet.
