---
id: "iss-pyocd-1212"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: new micro:bit V2 fails to flash with chip or sector erase until mass erase"
summary: "Factory micro:bit V2 units have access-port protection set."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1212"
doc_source: "https://github.com/pyocd/pyOCD/issues/1212"
resolution: "workaround"
versions: "pyocd 0.32"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["nRF52833"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Factory micro:bit V2 units have access-port protection set. Only a mass erase removes it.

## Fix

Once: pyocd erase --mass -t nrf52833, then flash as usual. Dragging a file to the MSD also works.

## Source

Resolution: workaround

Versions: pyocd 0.32

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1212](https://github.com/pyocd/pyOCD/issues/1212), summarized in own words; confidence medium, not reviewed yet.
