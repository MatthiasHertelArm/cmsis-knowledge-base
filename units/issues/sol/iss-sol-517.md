---
id: "iss-sol-517"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Solution is not converted after a generator creates the cgen.yml file"
summary: "The extension had no file watch for the missing cgen.yml because cbuild-idx.yml did not list it."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/517"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/517"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The extension had no file watch for the missing cgen.yml because cbuild-idx.yml did not list it.

## Fix

Use CMSIS Solution nightly of 2026-09-09 or later (csolution now lists the cgen file before it exists).

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-solution #517](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/517), summarized in own words; confidence medium, not reviewed yet.
