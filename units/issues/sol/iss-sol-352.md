---
id: "iss-sol-352"
type: "troubleshooting"
domain: "project"
title: "CMSIS Solution: CMake source mismatch error after changing which projects are selected in a solution"
summary: "Adding or removing projects changes the list of contexts and hence the generated CMakeLists files at solution and context level, so the existing CMake cache of the earlier selection no longer matches."
status: "draft"
tool: "cmsis-solution"
symptoms: ["CMake Error: The source \".../AlgorithmTest.Debug+AppKit-E7-U55/CMakeLists.txt\" does not match the source \".../DataTest.Debug+AppKit-E7-U55/CMakeLists.txt\" used to generate cache."]
symptom_regex: "CMake\\s+Error:\\s+The\\s+source\\s+\".*?\"\\s+does\\s+not\\s+match\\s+the\\s+source\\s+\".*?\"\\s+used\\s+to\\s+generate\\s+cache\\."
collection: "issues-sol"
source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/352"
doc_source: "https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/352"
resolution: "configuration"
versions: "csolution 1.68.1"
issue_state: "open"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cmsis-solution", "cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`CMake Error: The source ".../AlgorithmTest.Debug+AppKit-E7-U55/CMakeLists.txt" does not match the source ".../DataTest.Debug+AppKit-E7-U55/CMakeLists.txt" used to generate cache.`

## Cause

Adding or removing projects changes the list of contexts and hence the generated CMakeLists files at solution and context level, so the existing CMake cache of the earlier selection no longer matches.

## Fix

Rebuild (clean build) after changing the project selection. To switch between sets of projects without rebuilding, define a separate target-set for each set; each target-set uses its own tmp folder.

## Source

Resolution: configuration

Versions: csolution 1.68.1

The issue is still open: the fix is a workaround, a later release may change it.

From [Open-CMSIS-Pack/vscode-cmsis-solution #352](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution/issues/352), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
