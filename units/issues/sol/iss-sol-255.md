---
id: "iss-sol-255"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: Pack lock cannot be removed after switching from a local to a released pack"
summary: "After a local repository was used for ARM::SDS@3.0.0-dev (which created its entry in cbuild-pack.yml) and the released pack was then installed, the pack lock could not be removed and the installed pack was shown incorrectly; the thread names no …"
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/255"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/255"
resolution: "fixed-in-release"
versions: "1.67.2"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

After a local repository was used for ARM::SDS@3.0.0-dev (which created its entry in cbuild-pack.yml) and the released pack was then installed, the pack lock could not be removed and the installed pack was shown incorrectly; the thread names no root cause and suspects it was fixed along with #250.

## Fix

Use CMSIS Solution nightly of 2026-06-10 or later; then the lock can be resolved and the installed version selected.

## Source

Resolution: fixed-in-release

Versions: 1.67.2

From [Open-CMSIS-Pack/vscode-cmsis-solution #255](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/255), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
