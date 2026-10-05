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
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: context 'gpio-toggle.GCC' was not found`

## Cause

-c needs the fully qualified context <project>.<build-type>+<target-type>; parts cannot be left out when types exist (it may be omitted only when the solution has a single context).

## Fix

List the valid names with csolution -s <file> list contexts and pass one in full. The help text was updated to say build-type and target-type are not optional.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/devtools #330](https://github.com/Open-CMSIS-Pack/devtools/issues/330), summarized in own words; confidence high, not reviewed yet.
