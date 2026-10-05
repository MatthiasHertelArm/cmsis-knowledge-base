---
id: "iss-devtools-2363"
type: "troubleshooting"
domain: "pack"
title: "packchk: packchk M371 for unknown device feature type such as LGA"
summary: "The PDSC schema now accepts any string as device feature type, but packchk still validated against the old fixed enumeration."
status: "draft"
tool: "packchk"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2363"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2363"
resolution: "fixed-in-release"
versions: "fixed in toolbox builds after 2026-04-07"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The PDSC schema now accepts any string as device feature type, but packchk still validated against the old fixed enumeration.

## Fix

Fixed in packchk shipped with toolbox nightlies after 2026-04-07; update the toolbox.

## Source

Resolution: fixed-in-release

Versions: fixed in toolbox builds after 2026-04-07

From [Open-CMSIS-Pack/devtools #2363](https://github.com/Open-CMSIS-Pack/devtools/issues/2363), summarized in own words; confidence high, not reviewed yet.
