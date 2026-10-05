---
id: "iss-cmsis6-118"
type: "troubleshooting"
domain: "core"
title: "CMSIS-Core: CoreDebug_Type is gone in CMSIS 6, breaking vendor SDK code"
summary: "CMSIS 6 renamed the CoreDebug_Type structure to DCB_Type, which breaks vendor code such as NXP's fsl_common.c."
status: "draft"
tool: "cmsis-core"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/118"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/118"
resolution: "fixed-in-release"
versions: "CMSIS 5.9 defines CoreDebug_Type; CMSIS 6.0 renamed it"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-core"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

CMSIS 6 renamed the CoreDebug_Type structure to DCB_Type, which breaks vendor code such as NXP's fsl_common.c.

## Fix

Use DCB_Type; the issue was marked as addressed by PR #122 without saying what it changes or which release has it.

## Source

Resolution: fixed-in-release

Versions: CMSIS 5.9 defines CoreDebug_Type; CMSIS 6.0 renamed it

From [ARM-software/CMSIS_6 #118](https://github.com/ARM-software/CMSIS_6/issues/118), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
