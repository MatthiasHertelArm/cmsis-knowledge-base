---
id: "iss-devtools-21"
type: "troubleshooting"
domain: "general"
title: "other: Building devtools fails with fatal error: filesystem: No such file or directory"
summary: "The sources use std::filesystem, which needs GCC 8 or newer; GCC 7.5 does not provide the header."
status: "draft"
tool: "other"
symptoms: ["fatal error: filesystem: No such file or directory"]
symptom_regex: "fatal\\s+error:\\s+filesystem:\\s+No\\s+such\\s+file\\s+or\\s+directory"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/21"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/21"
resolution: "configuration"
versions: "GCC 7.5.0 fails, GCC 8.3.0 works"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`fatal error: filesystem: No such file or directory`

## Cause

The sources use std::filesystem, which needs GCC 8 or newer; GCC 7.5 does not provide the header.

## Fix

Build with GCC 8 or later (a README change, PR #27, was proposed to state this).

## Source

Resolution: configuration

Versions: GCC 7.5.0 fails, GCC 8.3.0 works

From [Open-CMSIS-Pack/devtools #21](https://github.com/Open-CMSIS-Pack/devtools/issues/21), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
