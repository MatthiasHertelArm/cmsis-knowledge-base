---
id: "iss-devtools-2286"
type: "troubleshooting"
domain: "project"
title: "csolution: cbuild-pack.yml contains only an empty resolved-packs entry"
summary: "The reporter traced the corrupted cbuild-pack.yml (resolved-packs: - {}) to for-context: +AVH* written without escaping the leading plus; the maintainer could not reproduce the problem."
status: "draft"
tool: "csolution"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2286"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/2286"
resolution: "workaround"
versions: "2.12"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

The reporter traced the corrupted cbuild-pack.yml (resolved-packs: - {}) to for-context: +AVH* written without escaping the leading plus; the maintainer could not reproduce the problem.

## Fix

Write the value as \+AVH* in for-context:. The report could no longer be reproduced with nightly CMSIS Solution extension builds, which clean up when switching between target sets.

## Source

Resolution: workaround

Versions: 2.12

From [Open-CMSIS-Pack/devtools #2286](https://github.com/Open-CMSIS-Pack/devtools/issues/2286), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
