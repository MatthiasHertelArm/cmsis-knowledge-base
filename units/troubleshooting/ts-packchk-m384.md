---
id: "ts-packchk-m384"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M384: Condition '…': Direct or indirect recursion detected. Skipping condition while searching for '…'."
status: "draft"
tool: "packchk"
severity: "error"
code: "M384"
symptoms: ["M384", "Condition '%NAME%': Direct or indirect recursion detected. Skipping condition while searching for '%NAME2%'."]
symptom_regex: "^Condition '.+?': Direct or indirect recursion detected\\. Skipping condition while searching for '.+?'\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Resolve recursion in condition _'NAME'_."
summary: "Evaluating a <condition> while collecting the compilers named in the pack's conditions failed: it refers to itself directly or through condition=\"...\" references, or such a reference names a condition id that is not defined."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:203", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/GatherCompilers.cpp:76-87", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckConditions.cpp:42-55", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteCondition.cpp:501-506", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteCondition.cpp:889-904", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteCondition.cpp:955-956", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:222"]
---

## Symptom

`M384`
`Condition '%NAME%': Direct or indirect recursion detected. Skipping condition while searching for '%NAME2%'.`

## Cause

Evaluating a <condition> while collecting the compilers named in the pack's conditions failed: it refers to itself directly or through condition="..." references, or such a reference names a condition id that is not defined. M390 usually reports the same condition earlier.

## Fix

Follow the condition="..." references from the named condition, break the loop, and define every referenced condition id.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:203`
- `tools/packchk/src/GatherCompilers.cpp:76-87`
- `tools/packchk/src/CheckConditions.cpp:42-55`
- `libs/rtemodel/src/RteCondition.cpp:501-506`
- `libs/rtemodel/src/RteCondition.cpp:889-904`
- `libs/rtemodel/src/RteCondition.cpp:955-956`
- `tools/packchk/README.md:222`
