---
id: "iss-devtools-2286"
type: "troubleshooting"
domain: "project"
title: "csolution: cbuild-pack.yml contains only an empty resolved-packs entry"
summary: "The for-context value was written as +AVH* without escaping; the leading plus is a special character, which broke pack resolution."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2286"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2286"
resolution: "user-error"
versions: "2.12"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The for-context value was written as +AVH* without escaping; the leading plus is a special character, which broke pack resolution.

## Fix

Escape it as \+AVH* in for-context:. Later toolbox builds also clean up when switching target sets, and the report could no longer be reproduced.

## Source

Resolution: user-error

Versions: 2.12

From [Open-CMSIS-Pack/devtools #2286](https://github.com/Open-CMSIS-Pack/devtools/issues/2286), summarized in own words; confidence medium, not reviewed yet.
