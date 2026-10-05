---
id: "iss-sol-312"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Outline view shows no files for a Zephyr/West project when first opened"
summary: "The cbuild.yml file list is completed only after cbuild setup, but the view refreshed after convert."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/312"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/312"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The cbuild.yml file list is completed only after cbuild setup, but the view refreshed after convert.

## Fix

Fixed: the Outline now refreshes after cbuild setup for Zephyr/West projects (CI build of June 2026).

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-solution #312](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/312), summarized in own words; confidence medium, not reviewed yet.
