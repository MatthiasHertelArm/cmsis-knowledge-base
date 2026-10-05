---
id: "iss-sol-394"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: CMSIS View and PROBLEMS do not update after a generator creates the cgen.yml file"
summary: "Regression: file watches are derived from cbuild-idx.yml, which did not list the not-yet-existing cgen.yml."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/394"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/394"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Regression: file watches are derived from cbuild-idx.yml, which did not list the not-yet-existing cgen.yml.

## Fix

Fixed with csolution listing the cgen file in cbuild-idx.yml and CMSIS Solution nightly of 2026-07-24; refresh manually on older versions.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-solution #394](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/394), summarized in own words; confidence high, not reviewed yet.
