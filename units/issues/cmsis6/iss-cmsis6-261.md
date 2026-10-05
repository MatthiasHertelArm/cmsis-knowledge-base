---
id: "iss-cmsis6-261"
type: "troubleshooting"
domain: "general"
title: "other: Devcontainer postCreate fails with \"vcpkg: command not found\""
summary: "vcpkg changed its activation command: 'vcpkg activate' no longer works and 'vcpkg-shell activate' takes its place, so the postCreate script fails."
status: "draft"
tool: "other"
symptoms: ["/home/postCreateCommand.sh: line 12: vcpkg: command not found"]
symptom_regex: "\\S+:\\s+line\\s+\\S+:\\s+vcpkg:\\s+command\\s+not\\s+found"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/261"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/261"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["other"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`/home/postCreateCommand.sh: line 12: vcpkg: command not found`

## Cause

vcpkg changed its activation command: 'vcpkg activate' no longer works and 'vcpkg-shell activate' takes its place, so the postCreate script fails.

## Fix

Call vcpkg-shell activate in the postCreate script (proposed in PR #262). Separately, the devcontainer build can fail when the .armlm or .iarlm folders mounted by devcontainer.json do not exist; creating them was suggested by the reporter.

## Source

Resolution: fixed-in-release

From [ARM-software/CMSIS_6 #261](https://github.com/ARM-software/CMSIS_6/issues/261), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
