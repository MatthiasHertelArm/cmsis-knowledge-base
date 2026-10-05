---
id: "iss-devtools-1889"
type: "troubleshooting"
domain: "project"
title: "cbuild: CMake error that the cache source does not match after switching the target type"
summary: "After the active target type changed, the CMake cache in tmp still belonged to the previous context, so CMake refused the new source directory."
status: "draft"
tool: "cbuild"
symptoms: ["CMake Error: The source \"<tmp>/Demo.Debug+MyBoard/CMakeLists.txt\" does not match the source \"<tmp>/Demo.Debug+AVH/CMakeLists.txt\" used to generate cache."]
symptom_regex: "CMake\\s+Error:\\s+The\\s+source\\s+\".*?\"\\s+does\\s+not\\s+match\\s+the\\s+source\\s+\".*?\"\\s+used\\s+to\\s+generate\\s+cache\\."
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1889"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1889"
resolution: "fixed-in-release"
versions: "cbuild 2.6.1-25-g3f083c7 affected"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`CMake Error: The source "<tmp>/Demo.Debug+MyBoard/CMakeLists.txt" does not match the source "<tmp>/Demo.Debug+AVH/CMakeLists.txt" used to generate cache.`

## Cause

After the active target type changed, the CMake cache in tmp still belonged to the previous context, so CMake refused the new source directory.

## Fix

Use a CMSIS-Toolbox nightly from 2024-12-09 or later: switching the target type now cleans the context and sets it up again.

## Source

Resolution: fixed-in-release

Versions: cbuild 2.6.1-25-g3f083c7 affected

From [Open-CMSIS-Pack/devtools #1889](https://github.com/Open-CMSIS-Pack/devtools/issues/1889), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
