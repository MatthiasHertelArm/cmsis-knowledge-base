---
id: "iss-sol-404"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: CMake error 'Command failed: 1' for the database target after a successful build"
summary: "A user-set CMSIS_COMPILER_ROOT pointed to a toolbox etc folder that did not match the extension's CMSIS-Toolbox version, so the compile-database step failed."
status: "draft"
tool: "cmsis-solution"
symptoms: ["CMake Error at <build>/<context>-stamp/<context>-database-.cmake:37 (message):", "Command failed: 1"]
symptom_regex: "CMake\\s+Error\\s+at\\s+<build>/<context>\\-stamp/<context>\\-database\\-\\.cmake:\\S+\\s+\\(message\\):"
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/404"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/404"
resolution: "user-error"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-solution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`CMake Error at <build>/<context>-stamp/<context>-database-.cmake:37 (message):`
`Command failed: 1`

## Cause

A user-set CMSIS_COMPILER_ROOT pointed to a toolbox etc folder that did not match the extension's CMSIS-Toolbox version, so the compile-database step failed.

## Fix

Unset CMSIS_COMPILER_ROOT or point it at the folder of the toolbox the extension uses.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/vscode-cmsis-solution #404](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/404), summarized in own words; confidence medium, not reviewed yet.
