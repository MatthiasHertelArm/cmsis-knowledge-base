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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlParser.cpp:712"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "GetTypes parses one entry of a forContext or notForContext list (ParseTypeFilter, ParseTypePair)."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:707-713", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:699", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:686-687"]
---

## Symptom

`type '<…>': it must start with '.' or '+' for normal strings and with '^' or '\' for regex patterns`

## Cause

GetTypes parses one entry of a forContext or notForContext list (ParseTypeFilter, ParseTypePair). It finds the first '.', the first '+' and the first '^' or '\' in the entry, and rejects the entry when none of the three sits at position 0. An entry such as 'Debug' with no prefix, or one where the delimiter is not the first character, matches this case. The '<…>' in the message is that entry as written in the project YAML.

## Fix

Edit the entry so it starts with the marker for its kind: '.' followed by the build type (for example '.Debug'), '+' followed by the target type (for example '+CM4'), or '^' or '\' followed by a regex pattern. Apply this to each item in the forContext or notForContext list that the message names. Example: forContext: [".Debug", "+CM4"]

## Trigger in the source

```cpp
if (((buildDelimiter > 0) && (targetDelimiter > 0) && (regexDelimiter > 0))) {
```

## Note

The condition tests '> 0' on the find results, so std::string::npos (not found) also passes it. An entry that contains no marker at all therefore fails, which is the usual way to hit this message. The message says 'for normal strings' and the README does not document it, so the wording is only a hint. Parsing of a normal string starting with '.' or '+' continues at lines 725-738, which is not shown here.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:707-713`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:699`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:686-687`
