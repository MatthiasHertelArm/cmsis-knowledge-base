---
id: "iss-sol-265"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Build after a target change in Manage Solution produces no output files"
summary: "With an unsaved target change from Manage Solution, Build saved the changes and started cbuild and cbuild setup concurrently (the database generation had been split off from cbuild setup); when cbuild finished first, the later setup removed its outputs."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/265"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/265"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

With an unsaved target change from Manage Solution, Build saved the changes and started cbuild and cbuild setup concurrently (the database generation had been split off from cbuild setup); when cbuild finished first, the later setup removed its outputs.

## Fix

Use CMSIS Solution nightly of 2026-06-10 or later; with VS Code set to save files before running a task, Build now saves the files and runs csolution convert before building. On older versions save explicitly before building.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-solution #265](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/265), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
