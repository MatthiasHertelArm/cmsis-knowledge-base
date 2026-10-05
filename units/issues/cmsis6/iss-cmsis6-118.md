---
id: "iss-cmsis6-118"
type: "troubleshooting"
domain: "core"
title: "CMSIS-Core: CoreDebug_Type is gone in CMSIS 6, breaking vendor SDK code"
summary: "CMSIS 6 renamed the CoreDebug structure to DCB_Type."
status: "draft"
tool: "cmsis-core"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/118"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/118"
resolution: "fixed-in-release"
versions: "6.0.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-core"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

CMSIS 6 renamed the CoreDebug structure to DCB_Type.

## Fix

Use DCB_Type, or the compatibility change tracked in PR 122 that keeps the old name for existing code.

## Source

Resolution: fixed-in-release

Versions: 6.0.0

From [ARM-software/CMSIS_6 #118](https://github.com/ARM-software/CMSIS_6/issues/118), summarized in own words; confidence medium, not reviewed yet.
