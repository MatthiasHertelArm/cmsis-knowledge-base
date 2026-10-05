---
id: "iss-devtools-927"
type: "troubleshooting"
domain: "project"
title: "csolution: Files silently missing because for-compiler: appears twice in one group mapping"
summary: "A YAML mapping with two for-compiler keys is invalid, but the yaml-cpp parser accepts duplicate keys, so the schema check did not report it and only the last value and files section took effect."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/927"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/927"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

A YAML mapping with two for-compiler keys is invalid, but the yaml-cpp parser accepts duplicate keys, so the schema check did not report it and only the last value and files section took effect.

## Fix

Write one group per compiler, or put for-compiler on each file entry. csolution was patched to reject duplicate keys (devtools PR 1107, CMSIS-Toolbox 2.0 era); an editor with YAML schema support also flags the error.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/devtools #927](https://github.com/Open-CMSIS-Pack/devtools/issues/927), summarized in own words; confidence high, not reviewed yet.
