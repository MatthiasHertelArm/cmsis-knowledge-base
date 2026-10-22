---
id: "iss-devtools-2623"
type: "troubleshooting"
domain: "project"
title: "csolution: Pack required only by an unselected mlops target set is reported missing and blocks the build"
summary: "The missing-pack check only looks at the active target set."
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
applies_to: {"tool": ["csolution"], "pack": ["ARM::SSE_320_BSP"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The missing-pack check only looks at the active target set. Packs required by an mlops target set that is not active are not loaded, so csolution convert fails when such a pack is not installed, even though the build does not use it. Selecting that target set makes the pack install immediately.

## Fix

Defining the pack (ARM::SSE_320_BSP@1.1.0) in the top-level sds.csolution.yml works as a workaround. Listing missing packs with csolution list packs -m without an active target set does not yet cover mlops target sets.

## Source

Resolution: workaround

Versions: csolution v1.68.0

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/devtools #2623](https://github.com/Open-CMSIS-Pack/devtools/issues/2623), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
