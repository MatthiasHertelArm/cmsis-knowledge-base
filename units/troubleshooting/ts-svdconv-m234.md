---
id: "ts-svdconv-m234"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M234: No valid items found for … '…'"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M234"
symptoms: ["M234", "No valid items found for %LEVEL% '%NAME%'"]
symptom_regex: "^No valid items found for .+? '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
doc_cause: "Correct SVD."
summary: "After the checks, a <peripheral> or a <cluster> directly inside a peripheral has no valid register left, because all its registers and clusters were dropped by earlier errors. svdconv then ignores the whole peripheral or cluster."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:843-905", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:101", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:228"]
---

## Symptom

`M234`
`No valid items found for %LEVEL% '%NAME%'`

## Cause

After the checks, a <peripheral> or a <cluster> directly inside a peripheral has no valid register left, because all its registers and clusters were dropped by earlier errors. svdconv then ignores the whole peripheral or cluster.

## Fix

Fix the errors reported earlier for the registers and clusters inside it; the message goes away once at least one register is valid.

## Note

Error under --strict. A peripheral with no registers at all gets M328 instead.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDevice.cpp:843-905`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:101`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:228`
