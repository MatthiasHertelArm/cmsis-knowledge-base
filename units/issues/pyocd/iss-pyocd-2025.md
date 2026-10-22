---
id: "iss-pyocd-2025"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Sparse HEX holes filled with 0xFF instead of the FLM empty value on single-range flash"
summary: "Per the reporter's analysis, when the FLM describes one sector range covering the whole flash region, pyOCD creates no subregions and does not copy FlashDevice.valEmpty to the parent region's erased_byte_value, which stays at the default 0xFF; the image builder …"
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/2025"
doc_source: "https://github.com/pyocd/pyOCD/issues/2025"
resolution: "fixed-in-release"
versions: "Reported on pyOCD 0.44.1; 0.45.1 was inspected with logic appearing unchanged. Fix is PR #2032; release not named."
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["SC32F12TC7"], "pack": ["SinOne.SC32xxxxx_DFP"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Per the reporter's analysis, when the FLM describes one sector range covering the whole flash region, pyOCD creates no subregions and does not copy FlashDevice.valEmpty to the parent region's erased_byte_value, which stays at the default 0xFF; the image builder then pads sparse HEX holes with 0xFF.

## Fix

Suggested fix: propagate FlashDevice.valEmpty to the parent flash region's erased_byte_value, including when no subregion is created. A comment says the issue was fixed by PR #2032; no release containing it is named. Local workaround in the thread: a project pyocd_user.py did_connect hook setting erased_byte_value to 0x00 on the IROM1 region.

## Source

Resolution: fixed-in-release

Versions: Reported on pyOCD 0.44.1; 0.45.1 was inspected with logic appearing unchanged. Fix is PR #2032; release not named.

From [pyocd/pyOCD #2025](https://github.com/pyocd/pyOCD/issues/2025), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
