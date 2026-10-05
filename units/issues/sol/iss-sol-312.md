---
id: "iss-sol-312"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Outline view shows no files for a Zephyr/West project when first opened"
summary: "For Zephyr/West projects the *.cbuild.yml file list is completed only during cbuild setup from compile_commands.json, but the Outline view was refreshed right after solution conversion."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/312"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/312"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

For Zephyr/West projects the *.cbuild.yml file list is completed only during cbuild setup from compile_commands.json, but the Outline view was refreshed right after solution conversion.

## Fix

The extension now refreshes the Outline after cbuild setup for Zephyr/West projects; validated with CI artifacts, no release named.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-solution #312](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/312), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
