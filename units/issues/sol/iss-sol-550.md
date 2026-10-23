---
id: "iss-sol-550"
type: "troubleshooting"
domain: "project"
title: "csolution: CubeMX generator fails to open on Linux/macOS with CMSIS Solution extension 1.72"
summary: "The extension launched the CubeMX generator inside a pseudo terminal (observed on macOS), and cbridge detach terminated that terminal before the generator was loaded; the regression was introduced by PR #450."
status: "draft"
tool: "csolution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/550"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/550"
resolution: "unresolved"
versions: "Affected: 1.72. Works in 1.70. Fix validated in nightly 1.72.1-3-20261005; nightly build 2026-10-02 is noted as including the change."
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"], "component": ["CubeMX integration"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The extension launched the CubeMX generator inside a pseudo terminal (observed on macOS), and cbridge detach terminated that terminal before the generator was loaded; the regression was introduced by PR #450.

## Fix

Use a build containing the fix (validated on macOS in nightly 1.72.1-3-20261005). Until a release with the fix is confirmed, copy the csolution run command from the CMSIS Solution Output channel and run it in a regular VS Code terminal, or reinstall extension 1.70.

## Source

Resolution: unresolved

Versions: Affected: 1.72. Works in 1.70. Fix validated in nightly 1.72.1-3-20261005; nightly build 2026-10-02 is noted as including the change.

From [Open-CMSIS-Pack/vscode-cmsis-solution #550](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/550), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
