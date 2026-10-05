---
id: "iss-view-48"
type: "troubleshooting"
domain: "trace"
title: "CMSIS-View: Downloaded eventlist for Linux is not executable"
summary: "The CI zip artifact step removed Unix permissions before the tar.gz was assembled."
status: "draft"
tool: "cmsis-view"
collection: "issues-view"
source: "https://github.com/ARM-software/CMSIS-View/issues/48"
doc_source: "https://github.com/ARM-software/CMSIS-View/issues/48"
resolution: "fixed-in-release"
versions: "eventlist 1.1.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-view"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The CI zip artifact step removed Unix permissions before the tar.gz was assembled.

## Fix

chmod +x eventlist; fixed in later releases by changing the packaging (PR 50).

## Source

Resolution: fixed-in-release

Versions: eventlist 1.1.0

From [ARM-software/CMSIS-View #48](https://github.com/ARM-software/CMSIS-View/issues/48), summarized in own words; confidence medium, not reviewed yet.
