---
id: "iss-sol-332"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: tasks.json keeps old image or target arguments after a target change and Build"
summary: "Debug tasks and launch configuration were not updated when csolution convert regenerated cbuild-run.yml during build."
status: "draft"
tool: "cmsis-solution"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/332"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/332"
resolution: "fixed-in-release"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Debug tasks and launch configuration were not updated when csolution convert regenerated cbuild-run.yml during build.

## Fix

Use CMSIS Solution nightly of 2026-07-14 or later; it saves pending changes per task.saveBeforeRun and refreshes tasks.json. Workaround: press Save in Manage Solution.

## Source

Resolution: fixed-in-release

From [Open-CMSIS-Pack/vscode-cmsis-solution #332](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/332), summarized in own words; confidence high, checked against the thread, not reviewed yet.
