---
id: "iss-pyocd-239"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: DAP TransferError when flashing a K64F with blank flash"
summary: "On a Kinetis device whose flash was erased and left blank, the target executes an erased reset vector and the debug access fails, so pyOCD cannot reconnect."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/239"
doc_source: "https://github.com/pyocd/pyOCD/issues/239"
resolution: "fixed-in-release"
versions: "0.7.1"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["MK64FN1M0xxx12"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

On a Kinetis device whose flash was erased and left blank, the target executes an erased reset vector and the debug access fails, so pyOCD cannot reconnect.

## Fix

Recover by copying a valid image over the mass-storage interface, then use pyOCD; fixed later by handling blank flash on Kinetis parts.

## Source

Resolution: fixed-in-release

Versions: 0.7.1

From [pyocd/pyOCD #239](https://github.com/pyocd/pyOCD/issues/239), summarized in own words; confidence medium, not reviewed yet.
