---
id: "iss-pyocd-2025"
type: "troubleshooting"
domain: "debug"
title: "pyOCD: Sparse HEX holes filled with 0xFF instead of the FLM valEmpty erased value"
summary: "When the FLM sector range covers the whole parent memory region, pyOCD creates no subregions and never copies the FLM valEmpty value to the parent flash region's erased_byte_value."
status: "draft"
tool: "pyocd"
collection: "issues-pyocd"
source: "https://github.com/pyocd/pyOCD/issues/2025"
doc_source: "https://github.com/pyocd/pyOCD/issues/2025"
resolution: "workaround"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["pyocd"], "device": ["SC32F12TC7"], "pack": ["SinOne.SC32xxxxx_DFP"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

When the FLM sector range covers the whole parent memory region, pyOCD creates no subregions and never copies the FLM valEmpty value to the parent flash region's erased_byte_value. The region keeps the default 0xFF, so the flash builder pads sparse image holes with 0xFF even though the device erases to 0x00.

## Fix

The thread points to PR #2032, which propagates FlashDevice.valEmpty to the parent FlashRegion.erased_byte_value; the thread does not name a release containing it. Until a release includes the fix, a project-local pyocd_user.py hook can set erased_byte_value to 0x00 on the flash region.

## Source

Resolution: workaround

From [pyocd/pyOCD #2025](https://github.com/pyocd/pyOCD/issues/2025), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
