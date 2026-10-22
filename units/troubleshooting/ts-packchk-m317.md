---
id: "ts-packchk-m317"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M317: Condition '…': No component found for '…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M317"
symptoms: ["M317", "Condition '%NAME%': No component found for '%NAME2%'"]
symptom_regex: "^Condition '.+?': No component found for '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "An expression inside a <condition> names a component (Cclass, Cgroup, Csub, Cvendor, Cversion ...) that no loaded pack provides. packchk only knows the components of the PDSC under test and of PDSC files passed with -i; %NAME% is the …"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:133", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckConditions.cpp:63-70", "Open-CMSIS-Pack/devtools@30f5e817:libs/rtemodel/src/RteCondition.cpp:52-55", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1249-1281", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1315-1345"]
---

## Symptom

`M317`
`Condition '%NAME%': No component found for '%NAME2%'`

## Cause

An expression inside a <condition> names a component (Cclass, Cgroup, Csub, Cvendor, Cversion ...) that no loaded pack provides. packchk only knows the components of the PDSC under test and of PDSC files passed with -i; %NAME% is the condition id, %NAME2% the expression.

## Fix

Correct the component attributes in the expression, or pass the PDSC of the pack that provides the component with -i, e.g. packchk MyVendor.MyPack.pdsc -i ARM.CMSIS.pdsc.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:133`
- `tools/packchk/src/CheckConditions.cpp:63-70`
- `libs/rtemodel/src/RteCondition.cpp:52-55`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1249-1281`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1315-1345`
