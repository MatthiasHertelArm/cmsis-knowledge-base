---
id: "ts-packchk-m608"
type: "troubleshooting"
domain: "error-catalog"
title: "packchk M608: Memory '…' with '…'='…' must have '…'='…'"
status: "draft"
tool: "packchk"
severity: "warning"
code: "M608"
symptoms: ["M608", "Memory '%NAME%' with '%ATTR%'='%VALUE%' must have '%ATTR2%'='%VALUE2%'"]
symptom_regex: "^Memory '.+?' with '.+?'='.+?' must have '.+?'='.+?'$"
documented: false
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/packchk/src/PackChk_Msgs.cpp"
applies_to: {"tool": ["packchk"]}
license: "Apache-2.0"
mode: "V"
summary: "A <memory> has startup=\"1\" but its access attribute does not contain 'x' (execute); a startup memory without access is reported too."
cause_origin: "source-analysis"
confidence: "high"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/PackChk_Msgs.cpp:243", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/src/ValidateSemantic.cpp:280-288", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1133-1172", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/MemoryAttributes/TestVendor.MemoryAttributes.pdsc:74", "Open-CMSIS-Pack/devtools@30f5e817:tools/packchk/test/data/MemoryAttributes/TestVendor.MemoryAttributes.pdsc:90"]
---

## Symptom

`M608`
`Memory '%NAME%' with '%ATTR%'='%VALUE%' must have '%ATTR2%'='%VALUE2%'`

## Cause

A <memory> has startup="1" but its access attribute does not contain 'x' (execute); a startup memory without access is reported too. Memories with id IROM*/IRAM* are exempt.

## Fix

Add x to the access of the startup memory or move startup="1" to the executable region, e.g. <memory name="Flash" access="rx" start="0x08000000" size="0x00080000" startup="1"/>.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence high, not reviewed yet:

- `tools/packchk/src/PackChk_Msgs.cpp:243`
- `tools/packchk/src/ValidateSemantic.cpp:280-288`
- `tools/packchk/test/integtests/src/PackChkIntegTests.cpp:1133-1172`
- `tools/packchk/test/data/MemoryAttributes/TestVendor.MemoryAttributes.pdsc:74`
- `tools/packchk/test/data/MemoryAttributes/TestVendor.MemoryAttributes.pdsc:90`
