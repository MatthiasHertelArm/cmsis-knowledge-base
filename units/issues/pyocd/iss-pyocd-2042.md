---
id: "iss-pyocd-2042"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Silabs Series 2 packs missing from pack index; pyocd pack find shows no devices"
summary: "The pack index cache has no entries for the Silicon Labs Series 2 packs, though the vendor index lists them."
status: "draft"
tool: "pyocd"
symptoms: ["No matching devices"]
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/2042"
doc_source: "https://github.com/pyocd/pyOCD/issues/2042"
resolution: "workaround"
versions: "pyOCD 0.45.1; pack SiliconLabs.GeckoPlatform_EFR32FG22_DFP 2025.12.1"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["pyocd"], "device": ["EFR32FG22C121F512GM40"], "pack": ["SiliconLabs.GeckoPlatform_EFR32FG22_DFP"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`No matching devices`

## Cause

The pack index cache has no entries for the Silicon Labs Series 2 packs, though the vendor index lists them. The thread suspects the download from the vendor site is blocked for scripted clients, but this is not confirmed and the cause is still open.

## Fix

Download the Silicon Labs Series 2 .pack file manually in a browser and point pyOCD at it with --pack, for example: pyocd flash --pack <downloaded .pack> -t <device> ... The thread reports this works on pyOCD 0.45.1.

## Source

Resolution: workaround

Versions: pyOCD 0.45.1; pack SiliconLabs.GeckoPlatform_EFR32FG22_DFP 2025.12.1

The issue is still open: the fix is a workaround, a later release may change it.

From [pyocd/pyOCD #2042](https://github.com/pyocd/pyOCD/issues/2042), summarized in own words; confidence low, checked against the thread, not reviewed yet.
