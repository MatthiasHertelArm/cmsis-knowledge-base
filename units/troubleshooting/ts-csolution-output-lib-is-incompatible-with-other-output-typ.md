---
id: "ts-csolution-output-lib-is-incompatible-with-other-output-typ"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: output 'lib' is incompatible with other output types"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["output 'lib' is incompatible with other output types"]
symptom_regex: "^output 'lib' is incompatible with other output types$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:5611"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The project's output types, collected from the output type entries of the project and its matching setups and from cmake image types, include lib together with at least one of elf, hex or bin."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5609-5613", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5580-5582", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5587-5589", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:5599-5601"]
---

## Symptom

`output 'lib' is incompatible with other output types`

## Cause

The project's output types, collected from the output type entries of the project and its matching setups and from cmake image types, include lib together with at least one of elf, hex or bin. The source checks this combination in ProcessOutputFilenames and refuses it, because a library output cannot be combined with an executable-style output in the same context. The 'output' type list in the csolution YAML (project or setup level) or the image types supplied through cmake are the inputs that produce the conflict.

## Fix

Keep only one output family for the context: either set the output type to lib alone, or remove lib and keep elf, hex and/or bin. Check the output type entries of the project and of every setup whose filters match the current context, and the cmake image types if cmake images are used, since any of them can add an output type. Re-run the csolution command after editing.

## Trigger in the source

```cpp
if (context.outputTypes.lib.on &&
```

## Note

The README does not document this message. The check runs after setup and cmake output types are merged, so the conflicting type may come from a setup or a cmake image rather than the top-level output list. The default elf output is only added later and does not cause this error.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:5609-5613`
- `tools/projmgr/src/ProjMgrWorker.cpp:5580-5582`
- `tools/projmgr/src/ProjMgrWorker.cpp:5587-5589`
- `tools/projmgr/src/ProjMgrWorker.cpp:5599-5601`
