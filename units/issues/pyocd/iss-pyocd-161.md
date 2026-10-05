---
id: "iss-pyocd-161"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: gdb 'load' fails on a custom W7500 target until the flash analyzer is enabled"
summary: "The new target's flash definition had analyzer support off and a wrong RAM buffer address, so loads from gdb failed."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/161"
doc_source: "https://github.com/pyocd/pyOCD/issues/161"
resolution: "configuration"
versions: "0.4"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The new target's flash definition had analyzer support off and a wrong RAM buffer address, so loads from gdb failed.

## Fix

In the target's flash algo definition set analyzer_supported to true and put begin_data at a valid RAM address (0x20002000 for that device).

## Source

Resolution: configuration

Versions: 0.4

From [pyocd/pyOCD #161](https://github.com/pyocd/pyOCD/issues/161), summarized in own words; confidence medium, not reviewed yet.
