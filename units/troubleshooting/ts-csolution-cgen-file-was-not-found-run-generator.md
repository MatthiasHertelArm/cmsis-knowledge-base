---
id: "ts-csolution-cgen-file-was-not-found-run-generator"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: cgen file was not found, run generator '…' for context '…'"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["cgen file was not found, run generator '<…>' for context '<…>'"]
symptom_regex: "^cgen file was not found, run generator '.+?' for context '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrExtGenerator.cpp:80"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrExtGenerator.cpp:70-88", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5684-5703", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/test/src/ProjMgrUnitTests.cpp:5944-5970"]
---

## Symptom

`cgen file was not found, run generator '<…>' for context '<…>'`

## Cause

A selected component uses a globally registered generator (for example STM32CubeMX), and the generator import file `<project-or-name>.cgen.yml` that this generator writes does not exist in its output folder. The generator has not been run for this context yet, or `generators: options:` (`path:`/`name:`) point elsewhere. The first `<…>` is the generator id, the second the context.

## Fix

Run the generator for the context, e.g. `csolution run <name>.csolution.yml -g <generator-id> -c <context>`, then convert/build again; if it was run, make `generators: options: - generator: <id>  path: ...` point to the folder that holds the .cgen.yml.

## Trigger in the source

```cpp
if (!m_parser->ParseClayer(options.name, m_checkSchema)) {
```

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrExtGenerator.cpp:70-88`
- `tools/projmgr/src/ProjMgrWorker.cpp:5684-5703`
- `tools/projmgr/test/src/ProjMgrUnitTests.cpp:5944-5970`
