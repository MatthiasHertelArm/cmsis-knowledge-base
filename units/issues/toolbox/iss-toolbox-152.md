---
id: "iss-toolbox-152"
type: "troubleshooting"
domain: "pack"
title: "svdconv: svdconv writes __VTOR_PRESENT 0 when vtorPresent is missing in the SVD"
summary: "The SVD specification says a missing vtorPresent means VTOR is present, but svdconv assumed false."
status: "draft"
tool: "svdconv"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/152"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/152"
resolution: "fixed-in-release"
versions: "fixed in svdconv 3.3.51"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["svdconv"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The SVD specification says a missing vtorPresent means VTOR is present, but svdconv assumed false.

## Fix

Use svdconv 3.3.51 or later, or set vtorPresent explicitly in the SVD.

## Source

Resolution: fixed-in-release

Versions: fixed in svdconv 3.3.51

From [Open-CMSIS-Pack/cmsis-toolbox #152](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/152), summarized in own words; confidence high, not reviewed yet.
