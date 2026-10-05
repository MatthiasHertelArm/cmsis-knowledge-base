---
id: "iss-devtools-1809"
type: "troubleshooting"
domain: "project"
title: "cbuild: cbuild clean fails with missing RTE files on a multi-target project"
summary: "Clean with cmsis-toolbox 2.6.0/2.6.1 depended on the files of all targets, so RTE files missing for a target that was never built caused errors and out and tmp were not cleaned."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1809"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1809"
resolution: "fixed-in-release"
versions: "cmsis-toolbox 2.6.0 and 2.6.1 affected; 2.4.0 works"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Clean with cmsis-toolbox 2.6.0/2.6.1 depended on the files of all targets, so RTE files missing for a target that was never built caused errors and out and tmp were not cleaned. RTE files are meant to be kept in version control.

## Fix

A fix was provided in cbuild PR #343 (CMSIS-Toolbox nightly of 05.12.2024; proposed behaviour: delete tmpdir, and outdir only for the selected contexts), not confirmed by the reporter. Commit the RTE folder and run cbuild setup <solution> --packs; the reporter's own template change to the new compiler-selection format also made clean work.

## Source

Resolution: fixed-in-release

Versions: cmsis-toolbox 2.6.0 and 2.6.1 affected; 2.4.0 works

From [Open-CMSIS-Pack/devtools #1809](https://github.com/Open-CMSIS-Pack/devtools/issues/1809), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
