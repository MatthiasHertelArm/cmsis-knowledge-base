---
id: "ts-svdconv-m244"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M244: C Expression: Referenced item '…' not found from: '…'"
status: "draft"
tool: "svdconv"
severity: "error"
code: "M244"
symptoms: ["M244", "C Expression: Referenced item '%NAME%' not found from: '%MSG%'"]
symptom_regex: "^C Expression: Referenced item '.+?' not found from: '.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCExpression.cpp:59", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCExpression.cpp:85", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCExpression.cpp:87", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/include/SvdItem.h:256", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdCExpressionParser.cpp:110", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:147", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/data/disablecondition/DisableCondTest.svd:32", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/test/data/disablecondition/DisableCondTest.svd:85"]
---

## Symptom

`M244`
`C Expression: Referenced item '%NAME%' not found from: '%MSG%'`

## Cause

A peripheral's <disableCondition> uses a name svdconv cannot resolve. Each operand is looked up as a path that starts with a peripheral name and goes down through clusters to a register and field (separated by '->' or '.'); NAME is the first part of the path that does not exist and MSG is the expression read so far. The disable condition is then dropped.

## Fix

Write each operand as a full path to an existing register or field using the <name>s of peripheral, cluster, register and field, for example <disableCondition>DCB-&gt;DSCSR-&gt;CDS == 0</disableCondition> ('->' must be escaped as '-&gt;' in XML). Check the spelling of each part.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdCExpression.cpp:59`
- `tools/svdconv/SVDModel/src/SvdCExpression.cpp:85`
- `tools/svdconv/SVDModel/src/SvdCExpression.cpp:87`
- `tools/svdconv/SVDModel/include/SvdItem.h:256`
- `tools/svdconv/SVDModel/src/SvdCExpressionParser.cpp:110`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:147`
- `tools/svdconv/test/data/disablecondition/DisableCondTest.svd:32`
- `tools/svdconv/test/data/disablecondition/DisableCondTest.svd:85`
