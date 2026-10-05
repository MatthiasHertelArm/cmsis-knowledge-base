---
id: "iss-devtools-1889"
type: "troubleshooting"
domain: "project"
title: "cbuild: CMake error that the cache source does not match after switching the target type"
summary: "After the active target type changed, the shared tmp CMake directory still held a cache of the previous context."
status: "draft"
tool: "cbuild"
symptoms: ["CMake Error: The source \"<tmp>/Demo.Debug+MyBoard/CMakeLists.txt\" does not match the source \"<tmp>/Demo.Debug+AVH/CMakeLists.txt\" used to generate cache."]
symptom_regex: "CMake\\s+Error:\\s+The\\s+source\\s+\".*?\"\\s+does\\s+not\\s+match\\s+the\\s+source\\s+\".*?\"\\s+used\\s+to\\s+generate\\s+cache\\."
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1889"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/1889"
resolution: "fixed-in-release"
versions: "2.6.1"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`CMake Error: The source "<tmp>/Demo.Debug+MyBoard/CMakeLists.txt" does not match the source "<tmp>/Demo.Debug+AVH/CMakeLists.txt" used to generate cache.`

## Cause

After the active target type changed, the shared tmp CMake directory still held a cache of the previous context.

## Fix

Fixed in CMSIS-Toolbox nightlies from December 2024 (released in 2.7.0): switching the target type cleans and sets up the new context. Workaround on older versions: delete the tmp directory of the solution.

## Source

Resolution: fixed-in-release

Versions: 2.6.1

From [Open-CMSIS-Pack/devtools #1889](https://github.com/Open-CMSIS-Pack/devtools/issues/1889), summarized in own words; confidence high, not reviewed yet.
