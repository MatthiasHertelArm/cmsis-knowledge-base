---
id: "iss-sol-319"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Broken installed pack PDSC blocks loading unrelated solution and disables debug"
summary: "The csolution RTE model loads installed packs, not only the packs the open solution uses."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/319"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/319"
resolution: "unresolved"
issue_state: "open"
confidence: "low"
cause_origin: "issue-digest"
checked: "unsupported"
applies_to: {"tool": ["cmsis-solution", "csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The csolution RTE model loads installed packs, not only the packs the open solution uses. When one installed PDSC is malformed, the pack load fails and the error is raised for the whole workspace, even though the solution does not need that pack. The failing path in RteKernel::LoadAndInsertPacks returns immediately when a pack fails to load.

## Fix

No fix is given in the thread. A code change that ignores pack load failures for packs the active solution does not require is feasible but has not been made, and a failure must still be distinguished from a missing pack.

## Source

Resolution: unresolved

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-solution #319](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/319), summarized in own words; confidence low, corrected against the thread, not reviewed yet.
