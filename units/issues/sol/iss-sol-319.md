---
id: "iss-sol-319"
type: "troubleshooting"
domain: "project"
title: "csolution: Broken pack description file blocks loading unrelated solutions in the extension"
summary: "csolution appears to load installed packs rather than only those selected by the open solution (a guess in the thread, not confirmed)."
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

csolution appears to load installed packs rather than only those selected by the open solution (a guess in the thread, not confirmed). A malformed PDSC in an installed pack makes that pack's load fail, and RteKernel::LoadAndInsertPacks returns immediately on the failure, so an unrelated solution also shows the error and the debug button stays disabled.

## Fix

The thread gives no confirmed fix.

## Source

Resolution: unresolved

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-solution #319](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/319), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
