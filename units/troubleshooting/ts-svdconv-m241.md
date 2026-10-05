---
id: "ts-svdconv-m241"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M241: Parse Error: '…' invalid for Array generation"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M241"
symptoms: ["M241", "Parse Error: '%VALUE%' invalid for Array generation"]
symptom_regex: "^Parse Error: '.+?' invalid for Array generation$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
cause_origin: "source-analysis"
confidence: "low"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDimension.cpp:350-358", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdUtils.cpp:136-143", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:108", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:231"]
---

## Symptom

`M241`
`Parse Error: '%VALUE%' invalid for Array generation`

## Cause

Meant for a dim element whose <name>, <displayName> or <description> has [%s] somewhere other than at the end. In svdconv 30f5e81 the expression parser never returns that result, so such a name surfaces as M239 instead.

## Fix

Put [%s] at the very end of the name (REG[%s]), or use %s for a list.

## Note

Unreachable at 30f5e81: ARRAYINVALID is commented out in SvdUtils::ParseExpression (SvdUtils.cpp:140).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence low, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDimension.cpp:350-358`
- `tools/svdconv/SVDModel/src/SvdUtils.cpp:136-143`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:108`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:231`
