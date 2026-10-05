---
id: "iss-toolbox-69"
type: "troubleshooting"
domain: "project"
title: "cbuild: Build succeeds but no .axf produced when only a legacy armasm file exists"
summary: "The AS_ARM language used for legacy armasm files had no link rule in the AC6 CMake description, so linking produced no .axf and reported no error."
status: "draft"
tool: "cbuild"
symptoms: ["info cbuild: build finished successfully!"]
symptom_regex: "build\\s+finished\\s+successfully!"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/69"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/69"
resolution: "fixed-in-release"
versions: "uv2csolution 1.0.0"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`info cbuild: build finished successfully!`

## Cause

The AS_ARM language used for legacy armasm files had no link rule in the AC6 CMake description, so linking produced no .axf and reported no error.

## Fix

Fixed in devtools PR 1101; the workaround was appending a CMAKE_AS_ARM_LINK_EXECUTABLE armlink rule to the AC6.<version>.cmake file.

## Source

Resolution: fixed-in-release

Versions: uv2csolution 1.0.0

From [Open-CMSIS-Pack/cmsis-toolbox #69](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/69), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
