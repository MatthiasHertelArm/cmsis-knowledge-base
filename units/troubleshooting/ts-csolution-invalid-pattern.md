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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlParser.cpp:719"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution parser handles a type filter string (a for-context or not-for-context entry, from a YAML value such as a build or target type list) as a regex when it starts with '^' or '\\' (the first '^' or …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:715-721", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:707-711", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:695-703"]
---

## Symptom

`invalid pattern '<…>': <…>`

## Cause

The csolution parser handles a type filter string (a for-context or not-for-context entry, from a YAML value such as a build or target type list) as a regex when it starts with '^' or '\' (the first '^' or '\' is at position 0). It compiles the whole string with std::regex, and the C++ regex engine rejected it. The '<…>' in the message is the offending filter string as written in the YAML, and the appended text is the regex engine's error description (e.g. an unbalanced parenthesis or invalid escape).

## Fix

Correct the regular expression in the reported filter so that it compiles as an ECMAScript regex. Check for unbalanced parentheses or brackets, and for backslash escapes that are not valid regex syntax; a literal backslash must be written as '\\' in the YAML. If a plain name was intended rather than a pattern, remove the leading '^' or '\' and use the '.' (build) or '+' (target) prefix form instead.

## Trigger in the source

```cpp
if (regexDelimiter == 0) {
```

## Note

The message text is 'invalid pattern' followed by the regex_error what() string, so the exact regex problem is only known from that suffix. The README does not document this message. The cause is inferred from the trigger; the lines given do not show which regex dialect the std::regex default uses.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:715-721`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:707-711`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:695-703`
