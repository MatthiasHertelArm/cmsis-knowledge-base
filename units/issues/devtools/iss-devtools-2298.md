---
id: "iss-devtools-2298"
type: "troubleshooting"
domain: "project"
title: "cbuild: JLink server cannot find SVD files listed with relative paths in cbuild-run from local packs"
summary: "The cbuild-run file lists SVD files with paths relative to its own location, but the J-Link server resolves them against the current working directory, which depends on actions the user performed."
status: "draft"
tool: "cbuild"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2298"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2298"
resolution: "unresolved"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["J-Link server"], "core": ["Cortex-M55"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The cbuild-run file lists SVD files with paths relative to its own location, but the J-Link server resolves them against the current working directory, which depends on actions the user performed. Local pack repositories are where this has been reported, in some cases with the M55_HP core.

## Fix

The issue proposes using absolute SVD paths in the cbuild-run file for local pack repositories, and a comment suggests resolving the SVD path in the debugger extension when building the J-Link command line. A related pull request in vscode-cmsis-debugger (#815) is reported as possibly addressing this and was awaiting review. No confirmed workaround or fix is recorded; the issue is open.

## Source

Resolution: unresolved

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/devtools #2298](https://github.com/Open-CMSIS-Pack/devtools/issues/2298), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
