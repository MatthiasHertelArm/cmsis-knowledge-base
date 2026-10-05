---
id: "iss-toolbox-98"
type: "troubleshooting"
domain: "project"
title: "cbuild: cbuild exits with status 0xc0000409 when run from Cygwin on Windows"
summary: "Cygwin versions of cmake and ninja combined with MDK-generated RTE files cause the crash."
status: "draft"
tool: "cbuild"
symptoms: ["error cbuild: exit status 0xc0000409"]
collection: "issues-toolbox"
source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/98"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/98"
resolution: "not-a-bug"
versions: "toolbox 2.2.1"
confidence: "medium"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["cbuild"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error cbuild: exit status 0xc0000409`

## Cause

Cygwin versions of cmake and ninja combined with MDK-generated RTE files cause the crash. Cygwin is not a supported environment.

## Fix

Use the Windows installation of cmake and ninja or build from a native shell.

## Source

Resolution: not-a-bug

Versions: toolbox 2.2.1

From [Open-CMSIS-Pack/cmsis-toolbox #98](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues/98), summarized in own words; confidence medium, checked against the thread, not reviewed yet.
