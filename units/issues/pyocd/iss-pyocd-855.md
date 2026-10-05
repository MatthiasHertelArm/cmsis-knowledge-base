---
id: "iss-pyocd-855"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: gdb and SWV together on a CMSIS-DAP probe corrupt each other's responses"
summary: "The SWO polling thread (DAP_SWO_Data) and the transfer thread used the same probe endpoint without synchronisation, so their DAP responses were mixed up on probes without a separate SWO streaming endpoint."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/855"
doc_source: "https://github.com/pyocd/pyOCD/issues/855"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The SWO polling thread (DAP_SWO_Data) and the transfer thread used the same probe endpoint without synchronisation, so their DAP responses were mixed up on probes without a separate SWO streaming endpoint.

## Fix

The maintainer reported it fixed; the thread names no version or change.

## Source

Resolution: fixed-in-release

From [pyocd/pyOCD #855](https://github.com/pyocd/pyOCD/issues/855), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
