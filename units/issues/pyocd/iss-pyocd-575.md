---
id: "iss-pyocd-575"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: STLink probe appears and disappears with 'The device has no langid' on Windows"
summary: "On Windows, STLink discovery through the custom USB match function intermittently failed to read the STLink's USB device fields ('The device has no langid'), so the probe list alternated between found and empty."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/575"
doc_source: "https://github.com/pyocd/pyOCD/issues/575"
resolution: "fixed-in-release"
versions: "STLink V2-1 firmware v2J32"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

On Windows, STLink discovery through the custom USB match function intermittently failed to read the STLink's USB device fields ('The device has no langid'), so the probe list alternated between found and empty.

## Fix

Use a pyOCD version with the maintainer's permanent fix, which the reporter confirmed (no release named). The reporter's workaround was to find the STLink by VID 0x0483 / PID 0x374b in get_all_connected_devices instead of the custom match.

## Source

Resolution: fixed-in-release

Versions: STLink V2-1 firmware v2J32

From [pyocd/pyOCD #575](https://github.com/pyocd/pyOCD/issues/575), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
