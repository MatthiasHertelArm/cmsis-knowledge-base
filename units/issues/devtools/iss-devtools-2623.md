---
id: "iss-devtools-2623"
type: "troubleshooting"
domain: "project"
title: "csolution: Pack required only by an inactive target's mlops context is not reported as missing"
summary: "The mlops target line adds a target set outside the active target selection. csolution loads packs only for the selected contexts, and the missing-pack listing does not extend to target sets named under mlops, so a pack needed only …"
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
applies_to: {"tool": ["csolution"], "pack": ["ARM::SSE_320_BSP@1.1.0"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The mlops target line adds a target set outside the active target selection. csolution loads packs only for the selected contexts, and the missing-pack listing does not extend to target sets named under mlops, so a pack needed only by that set is not reported or installed until that target is selected.

## Fix

Workaround: declare the missing pack in the top-level solution file (the thread adds ARM::SSE_320_BSP@1.1.0 to sds.csolution.yml) so it is always loaded, or select the mlops target set so the pack is installed.

## Source

Resolution: workaround

Versions: csolution v1.68.0

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/devtools #2623](https://github.com/Open-CMSIS-Pack/devtools/issues/2623), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
