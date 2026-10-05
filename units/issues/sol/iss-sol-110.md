---
id: "iss-sol-110"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Outline: removing a file from a layer leaves the clayer.yml entry"
summary: "File items in the outline tree did not get the layerUri attribute, so removing a file from a layer deleted the file but left its reference in the clayer.yml."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/110"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/110"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

File items in the outline tree did not get the layerUri attribute, so removing a file from a layer deleted the file but left its reference in the clayer.yml.

## Fix

Fixed (verified in the thread): removing a file from the Solution Outline also removes its .clayer.yml entry; no build or release is named.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-solution #110](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/110), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
