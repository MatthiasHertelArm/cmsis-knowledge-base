---
id: "iss-devtools-1460"
type: "troubleshooting"
domain: "pack"
title: "svdconv: SVDConv 3.3.46 reports error M364 for sauNumRegions equal to 0"
summary: "A value of 0 is valid by the SVD schema, but the new check rejected it."
status: "draft"
tool: "svdconv"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1460"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1460"
resolution: "fixed-in-release"
versions: "3.3.46 (MDK 5.39), fixed in 3.3.47"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["svdconv"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A value of 0 is valid by the SVD schema, but the new check rejected it.

## Fix

Fixed in SVDConv 3.3.47, which compares sauNumRegions with the configured SAU regions: warning M391 when regions exceed the number, error M387 when it is 0 but regions exist.

## Source

Resolution: fixed-in-release

Versions: 3.3.46 (MDK 5.39), fixed in 3.3.47

From [Open-CMSIS-Pack/devtools #1460](https://github.com/Open-CMSIS-Pack/devtools/issues/1460), summarized in own words; confidence high, checked against the thread, not reviewed yet.
