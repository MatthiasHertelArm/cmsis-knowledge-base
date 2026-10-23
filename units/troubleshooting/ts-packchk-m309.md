---
id: "ts-packchk-m309"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M309: Attribute '…' missing on '…' (when '…' is specified)"
status: "draft"
tool: "packchk"
severity: "error"
code: "M309"
symptoms: ["M309", "Attribute '%TAG%' missing on '%TAG2%' (when '%TAG3%' is specified)"]
symptom_regex: "^Attribute '.+?' missing on '.+?' \\(when '.+?' is specified\\)$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/src/PackChk_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/packchk/README.md"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "Add missing attribute _'TAG'_ or remove the attribute _'TAG3'_ in the element _'TAG2'_."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:123", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:248-257", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1133-1172", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/MemoryAttributes/TestVendor.MemoryAttributes.pdsc:90", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/README.md:158"]
---

## Symptom

`M309`
`Attribute '%TAG%' missing on '%TAG2%' (when '%TAG3%' is specified)`

## Cause

Add missing attribute _'TAG'_ or remove the attribute _'TAG3'_ in the element _'TAG2'_.

## Fix

Give the <memory> both name and access, e.g. name="SRAM" access="rwx", or use the legacy id form instead.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:123`
- `tools/packchk/src/ValidateSemantic.cpp:248-257`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1133-1172`
- `tools/packchk/test/data/MemoryAttributes/TestVendor.MemoryAttributes.pdsc:90`
- `tools/packchk/README.md:158`
