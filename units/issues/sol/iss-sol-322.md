---
id: "iss-sol-322"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: CMSIS View stuck on 'Loading' when a VS Code workspace has additional folders"
summary: "Activation of the extension failed when its solution roots watcher tried to read a workspace folder it had no permission for (EPERM on a .pytest_cache folder), so the CMSIS View stayed on Loading."
status: "draft"
tool: "cmsis-solution"
symptoms: ["NoPermissions (FileSystemError): Error: EPERM: operation not permitted, scandir 'c:\\GitRepos\\REPO_NAME\\.pytest_cache'"]
symptom_regex: "NoPermissions\\s+\\(FileSystemError\\):\\s+Error:\\s+EPERM:\\s+operation\\s+not\\s+permitted,\\s+scandir\\s+'.*?'"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/322"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/322"
resolution: "fixed-in-release"
versions: "1.66.0, 1.67.2 and 1.68.0 affected"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`NoPermissions (FileSystemError): Error: EPERM: operation not permitted, scandir 'c:\GitRepos\REPO_NAME\.pytest_cache'`

## Cause

Activation of the extension failed when its solution roots watcher tried to read a workspace folder it had no permission for (EPERM on a .pytest_cache folder), so the CMSIS View stayed on Loading.

## Fix

Use the CMSIS Solution nightly of 2026-07-01 or later, which the reporter confirmed resolves it.

## Source

Resolution: fixed-in-release

Versions: 1.66.0, 1.67.2 and 1.68.0 affected

From [Open-CMSIS-Pack/vscode-cmsis-solution #322](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/322), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
