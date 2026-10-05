---
id: "iss-sol-186"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Error for a non-existent pack version stays in PROBLEMS after correcting it"
summary: "The invalid version was still referenced in another file (for example the csolution.yml) when a valid one was added to the cproject.yml."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/186"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/186"
resolution: "fixed-in-release"
versions: "1.67.2"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The invalid version was still referenced in another file (for example the csolution.yml) when a valid one was added to the cproject.yml.

## Fix

Use Find in Files from the problem to remove the stale reference; the underlying fix is in devtools PR 2463 (nightly 2026-04-05).

## Source

Resolution: fixed-in-release

Versions: 1.67.2

From [Open-CMSIS-Pack/vscode-cmsis-solution #186](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/186), summarized in own words; confidence medium, not reviewed yet.
