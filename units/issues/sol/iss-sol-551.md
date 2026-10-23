---
id: "iss-sol-551"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Automatic cbuild setup runs too often; disable autoConvertOnFileChange to stop them"
summary: "The extension runs cbuild setup automatically on many file events, such as saving the VS Code tasks file, a Git checkout or AI-driven edits to cproject files, and after pack updates."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/551"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/551"
resolution: "configuration"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The extension runs cbuild setup automatically on many file events, such as saving the VS Code tasks file, a Git checkout or AI-driven edits to cproject files, and after pack updates. Each run adds delay and may modify the development environment unexpectedly.

## Fix

The thread points to the cmsis-csolution.autoConvertOnFileChange setting, which is on by default and can be turned off to stop setup running on file changes. A manual Refresh Build Information button is proposed and reported as implemented in a PR, with a dirty flag still needing build handling; no release is named.

## Source

Resolution: configuration

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-solution #551](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/551), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
