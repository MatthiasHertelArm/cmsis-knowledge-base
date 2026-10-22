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
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrExtGenerator.cpp:80"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "During csolution's generator import, the tool looks for the .cgen file named in the generator's options for a context."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrExtGenerator.cpp:72-80", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrExtGenerator.cpp:74-75"]
---

## Symptom

`cgen file was not found, run generator '<…>' for context '<…>'`

## Cause

During csolution's generator import, the tool looks for the .cgen file named in the generator's options for a context. If that file does not exist on disk, it prints this error, with '<…>' filled by the generator id (options.id) and the context id. The cgen file is produced by running the generator, so it has not been generated yet for that context.

## Fix

Run the generator for the named context so the .cgen file is created, then run the csolution command again. Check that the generator id and context shown in the message match a generator in your project's configuration.

## Trigger in the source

```cpp
if (!m_parser->ParseClayer(options.name, m_checkSchema)) {
```

## Note

The message names the generator and context, but the source does not show which command runs the generator; the fix relies on the message wording. The code also stores the missing cgen path and returns a non-null clayer with success=false, so the failure is reported to the caller through the success flag.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrExtGenerator.cpp:72-80`
- `tools/projmgr/src/ProjMgrExtGenerator.cpp:74-75`
