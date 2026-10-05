---
id: "iss-sol-542"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: ${env:AVH_FVP_PLUGINS} empty in tasks and launch.json until window reload"
summary: "The Arm Tools Environment Manager activates the variable after VS Code has built the environment used by its ${env:...} resolver, and the resolver is not refreshed afterwards. process.env in the extension host already has the value."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/542"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/542"
resolution: "workaround"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The Arm Tools Environment Manager activates the variable after VS Code has built the environment used by its ${env:...} resolver, and the resolver is not refreshed afterwards. process.env in the extension host already has the value.

## Fix

Run Developer: Reload Window after the environment was activated; this makes ${env:AVH_FVP_PLUGINS} available for Load & Debug. It is documented in the CMSIS Solution tips and tricks.

## Source

Resolution: workaround

From [Open-CMSIS-Pack/vscode-cmsis-solution #542](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/542), summarized in own words; confidence high, checked against the thread, not reviewed yet.
