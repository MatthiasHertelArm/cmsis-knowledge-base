---
id: "iss-sol-131"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Changes to cmsis-csolution.environmentVariables are not seen by the running RPC server"
summary: "The RPC daemon kept the environment it was started with."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/131"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/131"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The RPC daemon kept the environment it was started with.

## Fix

Fixed: changing the setting restarts the RPC server; on older versions reload the window.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-solution #131](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/131), summarized in own words; confidence medium, not reviewed yet.
