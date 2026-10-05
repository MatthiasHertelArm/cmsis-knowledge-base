---
id: "iss-sol-310"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: uVision opens only the secure project for TrustZone solutions"
summary: "uVision still relies on the context-set while CMSIS Solution uses target-set."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/310"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/310"
resolution: "workaround"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

uVision still relies on the context-set while CMSIS Solution uses target-set.

## Fix

Generate a cbuild-set containing both contexts: cbuild setup <solution>.csolution.yml -S -c *.Debug.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-solution #310](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/310), summarized in own words; confidence high, checked against the thread, not reviewed yet.
