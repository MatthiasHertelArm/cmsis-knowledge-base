---
id: "iss-devtools-177"
type: "troubleshooting"
domain: "project"
title: "csolution: error: context was not specified for list dependencies on a solution with several contexts"
summary: "The solution has several build-type/target-type combinations (contexts), and the command needs exactly one."
status: "draft"
tool: "csolution"
symptoms: ["error csolution: context was not specified", "warning csolution: yaml schemas were not found, file cannot be validated"]
symptom_regex: "context\\s+was\\s+not\\s+specified"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/177"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/177"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
checked: "supported"
applies_to: {"tool": ["csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`error csolution: context was not specified`
`warning csolution: yaml schemas were not found, file cannot be validated`

## Cause

The solution has several build-type/target-type combinations (contexts), and the command needs exactly one.

## Fix

Pass -c <project>.<build-type>+<target-type>. The schema warning only means the schema files were not found on that installation.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/devtools #177](https://github.com/Open-CMSIS-Pack/devtools/issues/177), summarized in own words; confidence high, checked against the thread, not reviewed yet.
