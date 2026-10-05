---
id: "iss-pyocd-161"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: gdb 'load' fails on a custom W7500 target until the flash analyzer is enabled"
summary: "The new W7500 target's flash algorithm definition had analyzer_supported off and a begin_data RAM address that did not work, so gdb 'load' failed."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/161"
doc_source: "https://github.com/pyocd/pyOCD/issues/161"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The new W7500 target's flash algorithm definition had analyzer_supported off and a begin_data RAM address that did not work, so gdb 'load' failed.

## Fix

In the target's flash algorithm definition set analyzer_supported to true and begin_data to a usable RAM address (0x20002000 on the W7500).

## Source

Resolution: configuration

From [pyocd/pyOCD #161](https://github.com/pyocd/pyOCD/issues/161), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
