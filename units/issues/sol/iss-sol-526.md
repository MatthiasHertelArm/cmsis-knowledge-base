---
id: "iss-sol-526"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Create Solution from a reference app with several csolution files edits the wrong solution"
summary: "The reference application contains three *.csolution.yml files in one folder; the create flow copies the app and takes 'the' solution file, which was not the selected one."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/526"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/526"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The reference application contains three *.csolution.yml files in one folder; the create flow copies the app and takes 'the' solution file, which was not the selected one.

## Fix

Fixed in the CMSIS Solution nightly of 2026-09-18 by using the load value of the pack description. Note the new target must be selected in Manage Solution before compiler and layer selection starts.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-solution #526](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/526), summarized in own words; confidence high, not reviewed yet.
