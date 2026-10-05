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
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:392"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:387", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:647", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1141", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:1219"]
---

## Symptom

`number must be integer or hexadecimal prefixed by 0x`

## Cause

A numeric node holds a value that is neither a plain decimal integer nor a hexadecimal number written with a lowercase `0x` prefix; the message carries file, line and column. The nodes checked are `debugger:` - `clock:`, the `memory:` entries' `start:`, `size:`, `ram-start:` and `ram-size:`, and the `images:` entries' `load-offset:`. Values like `1.5`, `-4`, `1e6`, `64K` or `0X1000` are rejected.

## Fix

Write the value as a decimal integer (`clock: 10000000`) or as `0x`-prefixed hex (`start: 0x20000000`).

## Trigger in the source

```cpp
if (!regex_match(value, regex("^(0x[0-9a-fA-F]+)$|^([0-9]*)$"))) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:387`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:647`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:1141`
- `tools/projmgr/src/ProjMgrYamlParser.cpp:1219`
