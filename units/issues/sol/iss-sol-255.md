---
id: "iss-sol-255"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Pack lock cannot be removed after switching from a local to a released pack"
summary: "Stale local-pack information after installing the released pack while cbuild-pack.yml still pinned the local one."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/255"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/255"
resolution: "fixed-in-release"
versions: "1.67.2"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Stale local-pack information after installing the released pack while cbuild-pack.yml still pinned the local one.

## Fix

Fixed in nightly of 2026-06-10; then the lock can be resolved and the installed version selected.

## Source

Resolution: fixed-in-release

Versions: 1.67.2

From [Open-CMSIS-Pack/vscode-cmsis-solution #255](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/255), summarized in own words; confidence medium, not reviewed yet.
