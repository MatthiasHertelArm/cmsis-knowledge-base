---
id: "iss-pyocd-1637"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: pack target crashes at session init on multi-AP Cortex-M33 devices like EFR32BG22/24"
summary: "pyOCD's pack target looks up each discovered core's access port in the pack's processor-to-AP map."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/1637"
doc_source: "https://github.com/pyocd/pyOCD/issues/1637"
resolution: "workaround"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["pyocd"], "device": ["EFR32BG22", "EFR32BG24"], "core": ["Cortex-M33"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

pyOCD's pack target looks up each discovered core's access port in the pack's processor-to-AP map. On these devices some discovered AP has no entry in the map (the pack does not describe it), so the lookup fails during session initialisation. A fix landed through pull request 1865.

## Fix

Use a release containing the fix from PR 1865. Interim options: add a check in pack_target.py so cores whose AP address is missing from processors_ap_map are skipped, or create a built-in target from the pack's flash algorithm (docs/adding_new_targets.md), which made 0.36.0 work with the EFR32BG24.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #1637](https://github.com/pyocd/pyOCD/issues/1637), summarized in own words; confidence medium, not reviewed yet.
