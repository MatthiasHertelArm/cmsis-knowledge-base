---
id: "iss-sol-452"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Generator start floods output with 'Input redirection is not supported'"
summary: "The generator's Windows launch script contained TIMEOUT commands that fail when stdin is redirected, as done when started from the extension."
status: "draft"
tool: "cmsis-solution"
symptoms: ["ERROR: Input redirection is not supported, exiting the process immediately."]
symptom_regex: "Input\\s+redirection\\s+is\\s+not\\s+supported,\\s+exiting\\s+the\\s+process\\s+immediately\\."
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/452"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/452"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`ERROR: Input redirection is not supported, exiting the process immediately.`

## Cause

The generator's Windows launch script contained TIMEOUT commands that fail when stdin is redirected, as done when started from the extension. The cgen.yml was still written.

## Fix

Use the updated generator launch script in a CMSIS-Toolbox nightly after 2026-06-09.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-solution #452](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/452), summarized in own words; confidence medium, not reviewed yet.
