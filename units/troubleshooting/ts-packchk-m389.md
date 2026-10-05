---
id: "ts-packchk-m389"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M389: The component '…' (Line …) has dependency '…' : '…' that is resolved by the component itself."
status: "draft"
tool: "packchk"
severity: "warning"
code: "M389"
symptoms: ["M389", "The component '%NAME%' (Line %LINE%) has dependency '%EXPR%' : '%NAME2%' that is resolved by the component itself."]
symptom_regex: "^The component '.+?' \\(Line .+?\\) has dependency '.+?' : '.+?' that is resolved by the component itself\\.$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "A component's condition (directly or through a referenced condition) contains a component dependency that the component itself satisfies, e.g. the component Cclass=\"C\" Cgroup=\"G\" uses a condition with <require Cclass=\"C\" Cgroup=\"G\"/>. %NAME% is the component, %EXPR% the condition and %NAME2% …"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:208", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:976-1020", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:528-554", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/CompResolvedByItself/ARM.CompResolvedByItself.pdsc:16-33"]
---

## Symptom

`M389`
`The component '%NAME%' (Line %LINE%) has dependency '%EXPR%' : '%NAME2%' that is resolved by the component itself.`

## Cause

A component's condition (directly or through a referenced condition) contains a component dependency that the component itself satisfies, e.g. the component Cclass="C" Cgroup="G" uses a condition with <require Cclass="C" Cgroup="G"/>. %NAME% is the component, %EXPR% the condition and %NAME2% the expression.

## Fix

Remove the self-matching <require> or <accept> from that condition, or give the component its own condition without it, e.g. split a shared condition into a hardware part and a software part.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:208`
- `tools/packchk/src/ValidateSemantic.cpp:976-1020`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:528-554`
- `tools/packchk/test/data/CompResolvedByItself/ARM.CompResolvedByItself.pdsc:16-33`
