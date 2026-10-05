---
id: "iss-sol-336"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Saving Software Components strips packs/components from other contexts' clayer files"
summary: "Saving for one context rewrote packs: and components: nodes in layer files used only by other contexts."
status: "draft"
tool: "cmsis-solution"
symptoms: ["board 'KIT_T2G-B-H_LITE:V1' was not found"]
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/336"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/336"
resolution: "fixed-in-release"
versions: "1.68.0"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`board 'KIT_T2G-B-H_LITE:V1' was not found`

## Cause

Saving for one context rewrote packs: and components: nodes in layer files used only by other contexts.

## Fix

Fixed after 1.68.0 (CI build of 2026-06-30); restore the removed nodes from version control.

## Source

Resolution: fixed-in-release

Versions: 1.68.0

From [Open-CMSIS-Pack/vscode-cmsis-solution #336](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/336), summarized in own words; confidence high, not reviewed yet.
