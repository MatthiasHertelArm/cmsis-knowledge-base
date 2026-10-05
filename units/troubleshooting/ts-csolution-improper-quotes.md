---
id: "ts-csolution-improper-quotes"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: invalid define: …, improper quotes"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["invalid define: <…>, improper quotes"]
symptom_regex: "^invalid define: .+?, improper quotes$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:450"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:420", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:449", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1073", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestSolution/test_invalid_defines.csolution.yml:19", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:7407"]
---

## Symptom

`invalid define: <…>, improper quotes`

## Cause

An entry under `define:`, `define-asm:`, `west-defs:` or `linker:` - `define:` has a value with misplaced double quotes; `<…>` is that value. csolution accepts a value with no `"` at all, or one quoted completely: exactly two quotes, either as `"..."` at both ends or as escaped `\"...\"` at both ends. A quote in the middle, a missing closing quote or a mix of `"` and `\"` is rejected. Quotes that are YAML syntax (`- KEY: "value"`) are removed by YAML and do not count.

## Fix

Quote the whole value or not at all. To pass a C string literal write the escaped form, e.g. `- KEY3: \"valid\"` or `- \"Test 3\"`; for a plain token write `- KEY: value`.

## Trigger in the source

```cpp
if (!isValid) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:420`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:449`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:1073`
- `tools/projmgr/test/data/TestSolution/test_invalid_defines.csolution.yml:19`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:7407`
