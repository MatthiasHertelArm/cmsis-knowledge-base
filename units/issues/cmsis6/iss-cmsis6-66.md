---
id: "iss-cmsis6-66"
type: "troubleshooting"
domain: "general"
title: "other: Devcontainer postCreate fails with \"vcpkg: command not found\""
summary: "The activation command of vcpkg changed to vcpkg-shell activate."
status: "draft"
tool: "other"
symptoms: ["/home/postCreateCommand.sh: line 12: vcpkg: command not found"]
symptom_regex: "\\S+:\\s+line\\s+\\S+:\\s+vcpkg:\\s+command\\s+not\\s+found"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/66"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/66"
resolution: "fixed-in-release"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["other"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`/home/postCreateCommand.sh: line 12: vcpkg: command not found`

## Cause

The activation command of vcpkg changed to vcpkg-shell activate.

## Fix

Use vcpkg-shell activate in the script; ensure the .armlm and .iarlm mount folders exist.

## Source

Resolution: fixed-in-release

From [ARM-software/CMSIS_6 #66](https://github.com/ARM-software/CMSIS_6/issues/66), summarized in own words; confidence medium, not reviewed yet.
