---
id: "ts-csolution-invalid-pattern"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: invalid pattern '…': …"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["invalid pattern '<…>': <…>"]
symptom_regex: "^invalid pattern '.+?': .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrYamlParser.cpp:719"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "A `for-context:` or `not-for-context:` entry starts with `^` or `\\`, so csolution treats it as a regular expression, but the expression does not compile; the first `<…>` is the entry, the second the regex library's error text."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:684", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:710", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:715", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/ForContextRegex/regex-fail.csolution.yml:19", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/ForContextRegex/regex.cproject.yml:13", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:6764"]
---

## Symptom

`invalid pattern '<…>': <…>`

## Cause

A `for-context:` or `not-for-context:` entry starts with `^` or `\`, so csolution treats it as a regular expression, but the expression does not compile; the first `<…>` is the entry, the second the regex library's error text. Example: `for-context: ^.Debug+(CM0` has an unclosed parenthesis.

## Fix

Correct the regular expression, escaping the literal `.` and `+` of context names, e.g. `for-context: ^\.Debug\+(CM0|CM3)`. If no pattern is meant, use the plain form `.Debug+CM0` without a leading `^` or `\`.

## Trigger in the source

```cpp
if (regexDelimiter == 0) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:684`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:710`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:715`
- `tools/projmgr/test/data/TestSolution/ForContextRegex/regex-fail.csolution.yml:19`
- `tools/projmgr/test/data/TestSolution/ForContextRegex/regex.cproject.yml:13`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:6764`
