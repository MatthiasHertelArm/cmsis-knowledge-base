---
id: "iss-sol-550"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Opening the CubeMX generator does nothing with CMSIS Solution 1.72 on macOS and Linux"
summary: "A regression in version 1.72: the generator is started in a pseudo terminal, and on Linux and macOS that terminal ends when cbridge detaches, before the generator has loaded."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/550"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/550"
resolution: "workaround"
versions: "Broken in 1.72, working in 1.70, fixed in nightly 2026-10-02"
issue_state: "open"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-solution", "csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A regression in version 1.72: the generator is started in a pseudo terminal, and on Linux and macOS that terminal ends when cbridge detaches, before the generator has loaded.

## Fix

Copy the launch command from the CMSIS Solution output channel (csolution run <solution>.csolution.yml -g CubeMX -a <target>) and run it in a normal VS Code terminal; or go back to version 1.70. The fix was included in the nightly build of 2 October 2026.

## Source

Resolution: workaround

Versions: Broken in 1.72, working in 1.70, fixed in nightly 2026-10-02

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-solution #550](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/550), summarized in own words; confidence high, not reviewed yet.
