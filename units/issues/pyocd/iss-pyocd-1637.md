---
id: "iss-pyocd-1637"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pack target crashes at session init on multi-AP Cortex-M33 devices like EFR32BG22/24"
summary: "The error log in the thread is cut off before the failure."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1637"
doc_source: "https://github.com/pyocd/pyOCD/issues/1637"
resolution: "workaround"
versions: "0.34.3 (partly working), 0.36.0"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["EFR32BG22", "EFR32BG24"], "core": ["Cortex-M33"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The error log in the thread is cut off before the failure. A suggested patch points at pack_target.py, where each discovered core's AP address is looked up in the pack's processors_ap_map; on these multi-AP Cortex-M33 devices that lookup can fail for a core whose AP is not in the map. The maintainer said it should be fixed by #1865.

## Fix

Create a built-in target from the pack's flash algorithm (docs/adding_new_targets.md), which made 0.36.0 work with an EFR32BG24. Skipping cores whose AP address is missing from processors_ap_map in pack_target.py was suggested, but did not solve it for the reporter. #1865 was named as the fix.

## Source

Resolution: workaround

Versions: 0.34.3 (partly working), 0.36.0

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1637](https://github.com/pyocd/pyOCD/issues/1637), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
