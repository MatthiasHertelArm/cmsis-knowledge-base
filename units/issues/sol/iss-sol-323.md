---
id: "iss-sol-323"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Stuck on 'Loading Solution...' with empty key in environmentVariables setting"
summary: "A setting with an empty name caused an unhandled error that blocked solution loading."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/323"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/323"
resolution: "fixed-in-release"
versions: "1.68.0"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A setting with an empty name caused an unhandled error that blocked solution loading.

## Fix

Remove the empty "": "" entry from settings.json; fixed in nightly of 2026-06-25 where settings are validated.

## Source

Resolution: fixed-in-release

Versions: 1.68.0

From [Open-CMSIS-Pack/vscode-cmsis-solution #323](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/323), summarized in own words; confidence high, checked against the thread, not reviewed yet.
