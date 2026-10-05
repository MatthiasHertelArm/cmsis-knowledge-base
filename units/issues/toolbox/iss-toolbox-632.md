---
id: "iss-toolbox-632"
type: "troubleshooting"
domain: "project"
title: "cbuild: cbuild cleans and rebuilds every time when CMSIS_COMPILER_ROOT is set and -c is used"
summary: "A change of the compiler registration root deliberately forces a rebuild, because generated CMake files from another toolbox installation may hold stale paths."
status: "draft"
tool: "cbuild"
symptoms: ["(1/1) Cleaning context: \"Hello.Debug+CS300\""]
symptom_regex: "\\(\\S+/\\S+\\)\\s+Cleaning\\s+context:\\s+\".*?\""
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/632"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/632"
resolution: "fixed-in-release"
versions: "seen in 2.14.0; gone in 2.14.1 nightly"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`(1/1) Cleaning context: "Hello.Debug+CS300"`

## Cause

A change of the compiler registration root deliberately forces a rebuild, because generated CMake files from another toolbox installation may hold stale paths. With the context given by -c the check fired on every run.

## Fix

Build with --active (what the VS Code extension does) and the second run reports no work to do. The repeated clean was no longer seen in toolbox 2.14.1 nightlies.

## Source

Resolution: fixed-in-release

Versions: seen in 2.14.0; gone in 2.14.1 nightly

From [Open-CMSIS-Pack/cmsis-toolbox #632](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/632), summarized in own words; confidence medium, not reviewed yet.
