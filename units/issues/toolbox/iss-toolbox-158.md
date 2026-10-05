---
id: "iss-toolbox-158"
type: "troubleshooting"
domain: "project"
title: "cbuild: .clangd points to out/ but compile_commands.json is in tmp/"
summary: "The compilation database is only copied to the output folder by the database target (cbuild setup), and the copy failed when the out folder structure did not exist yet."
status: "draft"
tool: "cbuild"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/158"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/158"
resolution: "fixed-in-release"
versions: "2.5.0"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The compilation database is only copied to the output folder by the database target (cbuild setup), and the copy failed when the out folder structure did not exist yet.

## Fix

Run cbuild setup <solution> --context-set or a normal build first. A cbuild2cmake fix creates the folders. Do not edit tmp manually.

## Source

Resolution: fixed-in-release

Versions: 2.5.0

From [Open-CMSIS-Pack/cmsis-toolbox #158](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/158), summarized in own words; confidence medium, not reviewed yet.
