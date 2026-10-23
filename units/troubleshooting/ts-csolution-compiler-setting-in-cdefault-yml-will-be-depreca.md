---
id: "ts-csolution-compiler-setting-in-cdefault-yml-will-be-depreca"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: 'compiler' setting in cdefault.yml will be deprecated in CMSIS-Toolbox 3.0.0"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["'compiler' setting in cdefault.yml will be deprecated in CMSIS-Toolbox 3.0.0"]
symptom_regex: "^'compiler' setting in cdefault\\.yml will be deprecated in CMSIS\\-Toolbox 3\\.0\\.0$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/projmgr/src/ProjMgrYamlParser.cpp:45"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The cdefault.yml used by the solution (enabled with `cdefault:` in the csolution.yml) sets `compiler:` under `default:`."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrYamlParser.cpp:42-46", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgr.cpp:497-501", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/schemas/common.schema.json:1193-1199", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/schemas/common.schema.json:1216", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/data/TestDefault/cdefault.yml:5"]
---

## Symptom

`'compiler' setting in cdefault.yml will be deprecated in CMSIS-Toolbox 3.0.0`

## Cause

The cdefault.yml used by the solution (enabled with `cdefault:` in the csolution.yml) sets `compiler:` under `default:`. The setting still works but is announced to be dropped in CMSIS-Toolbox 3.0.0.

## Fix

Move the compiler selection into the csolution.yml, e.g. `solution: compiler: GCC` (or per build-type/target-type `compiler:`), and delete `compiler:` from cdefault.yml. `select-compiler:` in cdefault.yml carries the same deprecation note in the schema, so move it to the csolution.yml as well.

## Trigger in the source

```cpp
if (!cdefault.compiler.empty()) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrYamlParser.cpp:42-46`
- `tools/projmgr/src/ProjMgr.cpp:497-501`
- `tools/projmgr/schemas/common.schema.json:1193-1199`
- `tools/projmgr/schemas/common.schema.json:1216`
- `tools/projmgr/test/data/TestDefault/cdefault.yml:5`
