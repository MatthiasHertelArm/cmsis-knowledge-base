---
id: "iss-devtools-791"
type: "troubleshooting"
domain: "pack"
title: "packchk: Building packchk on Linux fails: attempted static link of dynamic object libcurl.so"
summary: "Xerces-C picks up libcurl when it is installed, but packchk is linked with -static and libcurl.so cannot be linked statically."
status: "draft"
tool: "packchk"
symptoms: ["attempted static link of dynamic object libcurl.so"]
symptom_regex: "attempted\\s+static\\s+link\\s+of\\s+dynamic\\s+object\\s+libcurl\\.so"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/791"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/791"
resolution: "configuration"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["packchk"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`attempted static link of dynamic object libcurl.so`

## Cause

Xerces-C picks up libcurl when it is installed, but packchk is linked with -static and libcurl.so cannot be linked statically.

## Fix

Build Xerces with its option network=OFF; packchk is agreed to need no network support.

## Source

Resolution: configuration

From [Open-CMSIS-Pack/devtools #791](https://github.com/Open-CMSIS-Pack/devtools/issues/791), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
