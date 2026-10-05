---
id: "iss-cmsis6-235"
type: "troubleshooting"
domain: "core"
title: "CMSIS-Core: __PROGRAM_START not found at link time when startup.c is compiled as C++"
summary: "Name mangling when a .c file is built in C++ mode."
status: "draft"
tool: "cmsis-core"
collection: "issues-cmsis6"
source: "https://github.com/ARM-software/CMSIS_6/issues/235"
doc_source: "https://github.com/ARM-software/CMSIS_6/issues/235"
resolution: "user-error"
confidence: "medium"
cause_origin: "issue-digest"
applies_to: {"tool": ["cmsis-core"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Cause

Name mangling when a .c file is built in C++ mode.

## Fix

Build .c files as C; CMSIS does not support compiling them as C++ even with extern "C".

## Source

Resolution: user-error

From [ARM-software/CMSIS_6 #235](https://github.com/ARM-software/CMSIS_6/issues/235), summarized in own words; confidence medium, not reviewed yet.
