---
id: "ts-csolution-number-must-be-integer-or-hexadecimal-prefixed-b"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: number must be integer or hexadecimal prefixed by 0x"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["number must be integer or hexadecimal prefixed by 0x"]
symptom_regex: "^number must be integer or hexadecimal prefixed by 0x$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrYamlParser.cpp:392"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "ProjMgrYamlParser::ParseNumber reads a numeric csolution YAML field as a string and checks it against the pattern ^(0x[0-9a-fA-F]+)$ or ^([0-9]*)$."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:387-395", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:390-392"]
---

## Symptom

`number must be integer or hexadecimal prefixed by 0x`

## Cause

ProjMgrYamlParser::ParseNumber reads a numeric csolution YAML field as a string and checks it against the pattern ^(0x[0-9a-fA-F]+)$ or ^([0-9]*)$. The warning is printed when the value in the YAML is neither a run of decimal digits nor a 0x-prefixed hexadecimal number, for example a negative number, a decimal fraction, a value with a suffix or spaces, or a non-hex value after 0x. The warning gives the location of the value in the file, but not the key or the value itself, so the user has to find the offending entry at that line and column.

## Fix

Open the YAML file at the line and column given in the warning and rewrite the value as a plain decimal integer (for example 4096) or as a hexadecimal number with the 0x prefix and hex digits only (for example 0x1000). Remove any sign, decimal point, unit suffix, or surrounding text from the value.

## Trigger in the source

```cpp
if (!regex_match(value, regex("^(0x[0-9a-fA-F]+)$|^([0-9]*)$"))) {
```

## Note

The message does not name the key or the value, so a reviewer should know the user must locate the entry from the reported line and column. The regex also accepts an empty value, so an empty number produces no warning. The value is kept as a string and parsing continues after the warning; the source here does not show what happens to the non-matching value downstream, and the callers of ParseNumber are not in the lines given. The README has no entry for this message.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:387-395`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:390-392`
