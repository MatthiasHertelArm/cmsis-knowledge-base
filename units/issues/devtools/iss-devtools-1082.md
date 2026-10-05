---
id: "iss-devtools-1082"
type: "troubleshooting"
domain: "pack"
title: "svdconv: svdconv --generate partition loops endlessly when the SVD has no sauNumRegions"
summary: "Without sauNumRegions the internal default (an unset marker, all bits set) was used as region count, so the generated partition header ran SAU_INIT_REGION far beyond any sensible number."
status: "draft"
tool: "svdconv"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1082"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1082"
resolution: "fixed-in-release"
versions: "3.3.45, fixed in 3.3.46"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["svdconv"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Without sauNumRegions the internal default (an unset marker, all bits set) was used as region count, so the generated partition header ran SAU_INIT_REGION far beyond any sensible number.

## Fix

Fixed in SVDConv 3.3.46: the count is checked and the header contains an #error that the number of SAU regions is not set. Add sauNumRegions under cpu in the SVD.

## Source

Resolution: fixed-in-release

Versions: 3.3.45, fixed in 3.3.46

From [Open-CMSIS-Pack/devtools #1082](https://github.com/Open-CMSIS-Pack/devtools/issues/1082), summarized in own words; confidence high, not reviewed yet.
