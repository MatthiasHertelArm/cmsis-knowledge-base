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
versions: "csolution 2.2.1, 2.3.0+p1"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Local repository packs were added to the pack list without version filtering and ignored when the cbuild-pack requirements were established, so an older installed pack could win over a newer local one.

## Fix

Fixed in csolution: local packs are visible wherever installed packs are used and take precedence when their version is equal or larger within the requested range. The thread names no release.

## Source

Resolution: fixed-in-release

Versions: csolution 2.2.1, 2.3.0+p1

From [Open-CMSIS-Pack/devtools #1430](https://github.com/Open-CMSIS-Pack/devtools/issues/1430), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
