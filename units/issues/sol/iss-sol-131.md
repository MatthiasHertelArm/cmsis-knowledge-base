---
id: "iss-sol-131"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Changes to cmsis-csolution.environmentVariables are not seen by the running RPC server"
summary: "The RPC daemon kept the environment it was started with, so changes to cmsis-csolution.environmentVariables only reached processes started afterwards."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/131"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/131"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The RPC daemon kept the environment it was started with, so changes to cmsis-csolution.environmentVariables only reached processes started afterwards.

## Fix

Fixed (validated with CI artifacts): changing a value in cmsis-csolution.environmentVariables now restarts the RPC server.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-solution #131](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/131), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
