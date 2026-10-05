---
id: "iss-sol-517"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Solution is not converted after a generator creates the cgen.yml file"
summary: "The extension did not react when a generator created the missing .cgen.yml, so no solution convert followed."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/517"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/517"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The extension did not react when a generator created the missing .cgen.yml, so no solution convert followed.

## Fix

Use the CMSIS Solution nightly of 2026-09-09 or later; there cbuild setup runs once the generator has finished.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-solution #517](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/517), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
