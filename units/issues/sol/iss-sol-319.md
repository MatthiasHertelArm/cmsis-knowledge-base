---
id: "iss-sol-319"
type: "troubleshooting"
domain: "project"
title: "csolution: Broken installed PDSC blocks unrelated solutions from loading and disables debug"
summary: "csolution loads installed packs rather than only those selected by the active solution."
status: "draft"
tool: "csolution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/319"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/319"
resolution: "unresolved"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

csolution loads installed packs rather than only those selected by the active solution. The RTE kernel's LoadAndInsertPacks returns immediately when loading one pack fails, so a malformed installed PDSC produces an error even for solutions that do not need that pack. The reporter guesses this is the cause.

## Fix

The thread gives no confirmed fix.

## Source

Resolution: unresolved

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-solution #319](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/319), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
