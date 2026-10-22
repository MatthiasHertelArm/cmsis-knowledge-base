---
id: "ts-csolution-malformed-access-sequence"
type: "troubleshooting"
domain: "error-catalog"
title: "csolution: malformed access sequence: '…"
status: "draft"
tool: "csolution"
severity: "error"
symptoms: ["malformed access sequence: '<…>"]
symptom_regex: "^malformed access sequence: '.+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/projmgr/src/ProjMgrWorker.cpp:3722"
applies_to: {"tool": ["csolution"]}
license: "Apache-2.0"
mode: "V"
summary: "The csolution tool scans the item string for access sequences delimited by '$' (for example $Pack(vendor::name)$ or $OutDir(context)$)."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3716", "Open-CMSIS-Pack/devtools@30f5e817:tools/projmgr/src/ProjMgrWorker.cpp:3721-3722"]
---

## Symptom

`malformed access sequence: '<…>`

## Cause

The csolution tool scans the item string for access sequences delimited by '$' (for example $Pack(vendor::name)$ or $OutDir(context)$). When RteUtils::GetAccessSequence cannot find a complete sequence while it walks the string, it prints this error and aborts processing of that item. The text after the quote is the whole item as it was passed in (the variable-expanded value when the item is not solution-level), so the unpaired or unterminated '$' is somewhere in that value.

## Fix

Find the value shown after the quote in the csolution YAML or the PDSC/project setting that produced it. Check that every access sequence opens and closes with '$' and has balanced parentheses, for example $Pack(Vendor::Name)$, and remove or escape any stray '$' that is not meant as a sequence delimiter. Then rerun the csolution command.

## Trigger in the source

```cpp
if (!RteUtils::GetAccessSequence(offset, input, sequence, '$', '$')) {
```

## Note

The message has no closing quote, so the printed value is the full item and may be long. The exact delimiter rules live in RteUtils::GetAccessSequence, which is not among the lines given, so the cause is inferred from the call site. The message has no code and the README does not document it.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/projmgr/src/ProjMgrWorker.cpp:3716`
- `tools/projmgr/src/ProjMgrWorker.cpp:3721-3722`
