---
id: "iss-cmsis6-192"
type: "troubleshooting"
domain: "trace"
title: "CMSIS-View: Program fails before main with Event Recorder when heap size is 0 on AC6"
summary: "Event Recorder uses no heap."
status: "draft"
tool: "cmsis-view"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/192"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/192"
resolution: "user-error"
confidence: "low"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-view"], "toolchain": ["AC6"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Event Recorder uses no heap. The heap-using C/C++ library functions (stdio, C++ library) require heap, and zero heap breaks startup; here the project implicitly used malloc/free through its library setup.

## Fix

Give the library a heap or avoid heap-using library functions per the Arm C library heap documentation.

## Source

Resolution: user-error

From [ARM-software/CMSIS_6 #192](https://github.com/ARM-software/CMSIS_6/issues/192), summarized in own words; confidence low, not reviewed yet.
