---
id: "iss-devtools-2298"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: J-Link server cannot find SVD files listed with relative paths in cbuild-run"
summary: "The cbuild-run file lists SVD files with paths relative to the cbuild-run file itself. pyOCD resolves them that way, but the J-Link server can depend on the current working directory, so the SVD file may not be found when …"
status: "draft"
tool: "cmsis-debugger"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2298"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2298"
resolution: "unresolved"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["cbuild-run", "jlink_server"], "core": ["Cortex-M55"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The cbuild-run file lists SVD files with paths relative to the cbuild-run file itself. pyOCD resolves them that way, but the J-Link server can depend on the current working directory, so the SVD file may not be found when the tool runs from elsewhere.

## Fix

Not confirmed in the thread. The reporter proposed writing absolute SVD paths into cbuild-run for local packs; maintainers argued for resolving SVD paths in vscode-cmsis-debugger when building the J-Link server command line instead. A later comment says vscode-cmsis-debugger PR 815 already addresses this and asks for review; no confirmation is given.

## Source

Resolution: unresolved

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/devtools #2298](https://github.com/Open-CMSIS-Pack/devtools/issues/2298), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
