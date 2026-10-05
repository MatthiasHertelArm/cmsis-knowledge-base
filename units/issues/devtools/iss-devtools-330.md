---
id: "iss-devtools-330"
type: "troubleshooting"
domain: "project"
title: "csolution: error: context was not found when -c gives only a project or an incomplete context"
summary: "-c needs the fully qualified context <project>.<build-type>+<target-type>; parts cannot be left out when types exist (it may be omitted only when the solution has a single context)."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: context 'gpio-toggle.GCC' was not found"]
symptom_regex: "context\\s+'.*?'\\s+was\\s+not\\s+found"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/330"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/330"
resolution: "user-error"
versions: "csolution 0.9.5"
confidence: "medium"
cause_origin: "issue-digest"
checked: "partly"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: context 'gpio-toggle.GCC' was not found`

## Cause

-c needs the fully qualified context <project>.<build-type>+<target-type>; parts cannot be left out when types exist (it may be omitted only when the solution has a single context).

## Fix

List the valid names with csolution -s <file> list contexts and pass one in full. A help text saying build-type and target-type are not optional was proposed.

## Source

Resolution: user-error

Versions: csolution 0.9.5

From [Open-CMSIS-Pack/devtools #330](https://github.com/Open-CMSIS-Pack/devtools/issues/330), summarized in own words; confidence medium, corrected against the thread, not reviewed yet.
