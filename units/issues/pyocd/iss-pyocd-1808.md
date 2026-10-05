---
id: "iss-pyocd-1808"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: cbuild-run load rejects IAR .out ELF files"
summary: "CMSIS-Toolbox names IAR output with the .out extension, which pyOCD's file programmer did not recognise as ELF."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1808"
doc_source: "https://github.com/pyocd/pyOCD/issues/1808"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "toolchain": ["IAR"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

CMSIS-Toolbox names IAR output with the .out extension, which pyOCD's file programmer did not recognise as ELF.

## Fix

Fixed in a pyOCD commit that adds the extension; use a release containing it.

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #1808](https://github.com/pyocd/pyOCD/issues/1808), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
