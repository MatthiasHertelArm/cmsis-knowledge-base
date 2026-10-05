---
id: "iss-devtools-347"
type: "troubleshooting"
domain: "project"
title: "cbuild: for-type with a comma list on one line is not a YAML list; file silently not compiled"
summary: "for-type: .GCC, .GCC_STATUS written on one line is a single YAML string, not a list, so the filter matched neither type and the source file was left out."
status: "draft"
tool: "cbuild"
symptoms: ["exit.c:(.text.exit+0x16): undefined reference to `_exit'"]
symptom_regex: "exit\\.c:\\(\\.text\\.exit\\+\\S+\\):\\s+undefined\\s+reference\\s+to\\s+`_exit'"
collection: "issues-devtools"
source: "https://github.com/Open-CMSIS-Pack/devtools/issues/347"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/issues/347"
resolution: "user-error"
confidence: "high"
cause_origin: "issue-digest"
applies_to: {"tool": ["cbuild", "csolution"]}
license: "own summary of a GitHub issue"
mode: "S"
---

## Symptom

`exit.c:(.text.exit+0x16): undefined reference to `_exit'`

## Cause

for-type: .GCC, .GCC_STATUS written on one line is a single YAML string, not a list, so the filter matched neither type and the source file was left out.

## Fix

Write the type list as a YAML sequence: for-type: [.GCC, .GCC_STATUS] or one entry per line. The documentation example was corrected.

## Source

Resolution: user-error

From [Open-CMSIS-Pack/devtools #347](https://github.com/Open-CMSIS-Pack/devtools/issues/347), summarized in own words; confidence high, not reviewed yet.
