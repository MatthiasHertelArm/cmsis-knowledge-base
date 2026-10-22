---
id: "iss-sol-550"
type: "troubleshooting"
domain: "project"
title: "csolution: CubeMX fails to open from VS Code on Linux/macOS with CMSIS Solution v1.72"
summary: "The generator launch in the extension ran the csolution command inside a pseudo terminal (PTY) that was terminated when the CubeMX bridge detached, before the generator finished loading."
status: "draft"
tool: "csolution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/550"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/550"
resolution: "workaround"
versions: "Regression in CMSIS Solution extension v1.72; v1.70 works; fix validated in nightly 1.72.1-3-20261005 (2026-10-05)."
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The generator launch in the extension ran the csolution command inside a pseudo terminal (PTY) that was terminated when the CubeMX bridge detached, before the generator finished loading. The regression was introduced by PR #450; the thread reports it on Linux/macOS and not on Windows.

## Fix

Upgrade to a build containing the fix (validated on macOS in the nightly 1.72.1-3-20261005 of 2026-10-05). As a workaround, copy the csolution run command shown in the CMSIS Solution Output channel and run it in a regular VS Code terminal, or reinstall extension v1.70.

## Source

Resolution: workaround

Versions: Regression in CMSIS Solution extension v1.72; v1.70 works; fix validated in nightly 1.72.1-3-20261005 (2026-10-05).

From [Open-CMSIS-Pack/vscode-cmsis-solution #550](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/550), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
