---
id: "ts-packchk-m610"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M610: File category '…': '…' redefined in component '…', see Line …"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M610"
symptoms: ["M610", "File category '%CAT%': '%NAME%' redefined in component '%NAME2%', see Line %LINE%"]
symptom_regex: "^File category '.+?': '.+?' redefined in component '.+?', see Line .+?$"
documented: false
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:245", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/CheckComponents.cpp:35-77", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1174-1199", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/ConcurrentComponentFiles/ARM.ConcurrentComponentFiles.pdsc:65-78"]
---

## Symptom

`M610`
`File category '%CAT%': '%NAME%' redefined in component '%NAME2%', see Line %LINE%`

## Cause

The same source, library or object file (category library, object, source, sourceC, sourceCpp, sourceAsm or genSource) is listed in two components with the same file condition, component condition, Cvariant and Cbundle, so selecting both would add the file twice. %NAME% shows packchk's internal key (file name and those values joined by ':').

## Fix

List the file in one component only; if several components need it, move it into a common component that the others require.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:245`
- `tools/packchk/src/CheckComponents.cpp:35-77`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1174-1199`
- `tools/packchk/test/data/ConcurrentComponentFiles/ARM.ConcurrentComponentFiles.pdsc:65-78`
