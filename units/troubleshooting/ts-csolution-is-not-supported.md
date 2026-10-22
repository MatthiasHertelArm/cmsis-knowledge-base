---
id: "ts-csolution-is-not-supported"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: 'for-compiler: …' is not supported"
status: "draft"
tool: "csolution"
severity: "warning"
symptoms: ["'for-compiler: <…>' is not supported"]
symptom_regex: "^'for\\-compiler: .+?' is not supported$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:4103"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution run collected a for-compiler value that the tool does not recognise as a supported toolchain, and PrintMissingFilters() reports each such value as a warning."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:4102-4103"]
---

## Symptom

`'for-compiler: <…>' is not supported`

## Cause

The csolution run collected a for-compiler value that the tool does not recognise as a supported toolchain, and PrintMissingFilters() reports each such value as a warning. The bracketed text is the for-compiler value as written in the input, for example in a build-type or target-type selection of the csolution YAML. The lines given show only the print, not where m_missingToolchains is filled, so the exact input that populates it is inferred.

## Fix

Find the for-compiler entry in the csolution YAML that names the value shown in the message and correct it to a supported compiler or toolchain name, or remove the entry if it is not needed. Then rerun the csolution command and confirm the warning is gone. The lines given do not list the supported names, so check them in the CMSIS-Toolbox documentation.

## Note

The README has no entry for this message. The population of m_missingToolchains and the list of supported compilers are outside the lines provided, so the cause is inferred from the print site and the message text.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:4102-4103`
