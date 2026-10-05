---
id: "iss-devtools-1809"
type: "troubleshooting"
domain: "project"
title: "cbuild: cbuild clean fails with missing RTE files on a multi-target project"
summary: "Cleaning relied on files of all targets, including RTE files of targets that were never set up, so it errored and left out and tmp in place."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1809"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1809"
resolution: "fixed-in-release"
versions: "2.6.0 and 2.6.1, fixed in 2.7.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Cleaning relied on files of all targets, including RTE files of targets that were never set up, so it errored and left out and tmp in place. RTE files should also be kept in version control.

## Fix

Cleanup strategy changed in cbuild (released with CMSIS-Toolbox 2.7.0): tmp is deleted, and out files only for the selected contexts. Also commit the RTE folder and run cbuild setup --packs.

## Source

Resolution: fixed-in-release

Versions: 2.6.0 and 2.6.1, fixed in 2.7.0

From [Open-CMSIS-Pack/devtools #1809](https://github.com/Open-CMSIS-Pack/devtools/issues/1809), summarized in own words; confidence medium, not reviewed yet.
