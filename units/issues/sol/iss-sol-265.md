---
id: "iss-sol-265"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Build after a target change in Manage Solution produces no output files"
summary: "Build saved the changes and started cbuild and cbuild setup concurrently; when cbuild finished first, the later setup removed its outputs."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/265"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/265"
resolution: "fixed-in-release"
versions: "1.67.2"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Build saved the changes and started cbuild and cbuild setup concurrently; when cbuild finished first, the later setup removed its outputs.

## Fix

Use CMSIS Solution nightly of 2026-06-10 or later; the build now saves files first and converts before building. Save explicitly before building on older versions.

## Source

Resolution: fixed-in-release

Versions: 1.67.2

From [Open-CMSIS-Pack/vscode-cmsis-solution #265](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/265), summarized in own words; confidence high, not reviewed yet.
