---
id: "iss-devtools-927"
type: "troubleshooting"
domain: "project"
title: "csolution: Files silently missing because for-compiler: appears twice in one group mapping"
summary: "A YAML mapping with two for-compiler keys is invalid, but the yaml-cpp parser accepts duplicate keys, so csolution's schema check did not report it and the GCC files were silently not included."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/927"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/927"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A YAML mapping with two for-compiler keys is invalid, but the yaml-cpp parser accepts duplicate keys, so csolution's schema check did not report it and the GCC files were silently not included.

## Fix

Write one group per compiler, or put for-compiler on each file entry; the schema check in VS Code flags the error. Fixed in csolution by PR #1107; the thread names no release.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/devtools #927](https://github.com/Open-CMSIS-Pack/devtools/issues/927), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
