---
id: "ts-csolution-it-must-start-with-or-for-normal-strings-and-wit"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: type '…': it must start with '.' or '+' for normal strings and with '^' or '\\' for regex patterns"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["type '<…>': it must start with '.' or '+' for normal strings and with '^' or '\\' for regex patterns"]
symptom_regex: "^type '.+?': it must start with '\\.' or '\\+' for normal strings and with '\\^' or '\\\\' for regex patterns$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrYamlParser.cpp:712"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A `for-context:` or `not-for-context:` entry does not begin with `.` (build type), `+` (target type), `^` or `\\` (regular expression); `<…>` is the entry, e.g."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:707", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:684", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/schemas/common.schema.json:14"]
---

## Symptom

`type '<…>': it must start with '.' or '+' for normal strings and with '^' or '\' for regex patterns`

## Cause

A `for-context:` or `not-for-context:` entry does not begin with `.` (build type), `+` (target type), `^` or `\` (regular expression); `<…>` is the entry, e.g. `Debug` or `CM0+Debug`. The schema rejects such values too, so this message appears mainly with `-n`.

## Fix

Start the entry with the right prefix: `.Debug`, `+CM0`, `.Debug+CM0`, or a regex such as `^\.Debug\+.*`.

## Trigger in the source

```cpp
if (((buildDelimiter > 0) && (targetDelimiter > 0) && (regexDelimiter > 0))) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:707`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:684`
- `tools/projmgr/schemas/common.schema.json:14`
