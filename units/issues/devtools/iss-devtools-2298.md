---
id: "iss-devtools-2298"
type: "troubleshooting"
domain: "debug"
title: "CMSIS Debugger: SVD path in cbuild-run is relative, so debug servers fail to find it for local packs"
summary: "For SVD files from a local pack repository, the cbuild-run file stores a path relative to the current directory rather than an absolute path."
status: "draft"
tool: "cmsis-debugger"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2298"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2298"
resolution: "unresolved"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-debugger"], "device": ["AE822FA0E5597BS0"], "core": ["Cortex-M55"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

For SVD files from a local pack repository, the cbuild-run file stores a path relative to the current directory rather than an absolute path. A launcher such as JLINK_Server that resolves that path against its working directory can fail to find the file when the working directory changes. pyOCD already resolves relative paths against the cbuild-run file's own location, so only the other consumer is affected.

## Fix

No confirmed fix. Proposed: resolve SVD paths against the cbuild-run location where the J-Link server command line is built (for example around getSvdFilePaths in vscode-cmsis-debugger). A vscode-cmsis-debugger pull request (PR 815) is believed by one commenter to address this, but review was still pending. Absolute paths for local SVD files were proposed in the report but questioned by maintainers.

## Source

Resolution: unresolved

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/devtools #2298](https://github.com/Open-CMSIS-Pack/devtools/issues/2298), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
