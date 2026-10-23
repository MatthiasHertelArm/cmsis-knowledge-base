---
id: "iss-devtools-2623"
type: "troubleshooting"
domain: "project"
title: "csolution: Pack defined in an inactive layer is reported missing when an mlops target adds a target set"
summary: "The mlops simulator node names a target set that is not the active target."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2623"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2623"
resolution: "workaround"
versions: "csolution v1.68.0"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"], "board": ["Corstone-320"], "pack": ["ARM::SSE_320_BSP@1.1.0"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The mlops simulator node names a target set that is not the active target. Packs required by that context are not loaded, because only the selected contexts are loaded. So the missing-pack check, including csolution list packs -m, does not look at packs from that layer, and the build fails when the pack is not installed.

## Fix

Workaround: declare the missing pack in the top-level sds.csolution.yml so it is found. Selecting the target set that uses the layer also installs it. The maintainers agreed the issue is low priority, and the thread does not show a scheduled fix.

## Source

Resolution: workaround

Versions: csolution v1.68.0

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/devtools #2623](https://github.com/Open-CMSIS-Pack/devtools/issues/2623), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
