---
id: "ts-packchk-m609"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M609: Processor '…': Exact one memory with attribute \"startup=1\" must be configured, but found …"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M609"
symptoms: ["M609", "Processor '%NAME%': Exact one memory with attribute \"startup=1\" must be configured, but found %NUM%"]
symptom_regex: "^Processor '.+?': Exact one memory with attribute \"startup=1\" must be configured, but found .*$"
documented: false
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "Among the memories that apply to a processor of a device (including those inherited from family and subFamily), none or more than one has startup=\"1\"."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:244", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:197-296", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1133-1172", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/MemoryAttributes/TestVendor.MemoryAttributes.pdsc:65-66", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/MemoryAttributes/TestVendor.MemoryAttributes.pdsc:82"]
---

## Symptom

`M609`
`Processor '%NAME%': Exact one memory with attribute "startup=1" must be configured, but found %NUM%`

## Cause

Among the memories that apply to a processor of a device (including those inherited from family and subFamily), none or more than one has startup="1".

## Fix

Mark exactly one executable memory per processor with startup="1" and remove startup or set it to "0" on the others.

## Note

On multi-core devices the processor name printed in the message accumulates the names of earlier processors (devName is extended inside the loop, ValidateSemantic.cpp:199-208).

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:244`
- `tools/packchk/src/ValidateSemantic.cpp:197-296`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1133-1172`
- `tools/packchk/test/data/MemoryAttributes/TestVendor.MemoryAttributes.pdsc:65-66`
- `tools/packchk/test/data/MemoryAttributes/TestVendor.MemoryAttributes.pdsc:82`
