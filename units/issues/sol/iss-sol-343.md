---
id: "iss-sol-343"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Software Components stuck on 'Saving changes...' for layers outside solution folder"
summary: "The active solution tracker ignored changes in files outside the solution directory, so saving a clayer there never completed."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/343"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/343"
resolution: "fixed-in-release"
versions: "1.68.x"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The active solution tracker ignored changes in files outside the solution directory, so saving a clayer there never completed.

## Fix

Use CMSIS Solution nightly of 2026-07-03 or later.

## Source

Resolution: fixed-in-release

Versions: 1.68.x

From [Open-CMSIS-Pack/vscode-cmsis-solution #343](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/343), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
