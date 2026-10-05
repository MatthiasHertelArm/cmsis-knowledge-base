---
id: "iss-toolbox-69"
type: "troubleshooting"
domain: "project"
title: "cbuild: Build succeeds but no .axf produced when only a legacy armasm file exists"
summary: "The AS_ARM language used for legacy armasm files had no link rule in the AC6 CMake description, so linking did nothing."
status: "draft"
tool: "cbuild"
symptoms: ["info cbuild: build finished successfully!"]
symptom_regex: "build\\s+finished\\s+successfully!"
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/69"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/69"
resolution: "fixed-in-release"
versions: "2023 toolbox"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`info cbuild: build finished successfully!`

## Cause

The AS_ARM language used for legacy armasm files had no link rule in the AC6 CMake description, so linking did nothing.

## Fix

Fixed in devtools PR 1101; workaround was setting CMAKE_AS_ARM_LINK_EXECUTABLE to an armlink command in the AC6 cmake file.

## Source

Resolution: fixed-in-release

Versions: 2023 toolbox

From [Open-CMSIS-Pack/cmsis-toolbox #69](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/69), summarized in own words; confidence high, not reviewed yet.
