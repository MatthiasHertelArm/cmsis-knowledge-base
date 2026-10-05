---
id: "iss-devtools-1430"
type: "troubleshooting"
domain: "project"
title: "csolution: Local repository packs handled inconsistently by list packs and convert"
summary: "Local repository packs were added to the pack list without version filtering and ignored when the cbuild-pack requirements were established, so an older installed pack could win over a newer local one."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1430"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1430"
resolution: "fixed-in-release"
versions: "2.2.1 to 2.3.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Local repository packs were added to the pack list without version filtering and ignored when the cbuild-pack requirements were established, so an older installed pack could win over a newer local one.

## Fix

Fixed in CMSIS-Toolbox 2.4: local packs are visible wherever installed packs are used and take precedence when their version is equal or larger within the requested range.

## Source

Resolution: fixed-in-release

Versions: 2.2.1 to 2.3.0

From [Open-CMSIS-Pack/devtools #1430](https://github.com/Open-CMSIS-Pack/devtools/issues/1430), summarized in own words; confidence high, not reviewed yet.
