---
id: "iss-sol-273"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Create Solution view shows no devices when Web Services is enabled"
summary: "The device search service returned an error because the number of devices (about 13,041) exceeded the search result window configured on the server (13,000)."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/273"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/273"
resolution: "workaround"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The device search service returned an error because the number of devices (about 13,041) exceeded the search result window configured on the server (13,000). The server limit was raised to 15,000 afterwards; a client-side change was still pending.

## Fix

Server side already patched. If the list is still empty, disable Web Services, install the BSP and DFP packs for the board or device (copy the cpackget command from the board or device page on keil.arm.com and run it in a VS Code terminal) and pick the board from the installed packs.

## Source

Resolution: workaround

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-solution #273](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/273), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
