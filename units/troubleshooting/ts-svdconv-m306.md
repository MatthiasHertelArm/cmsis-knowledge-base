---
id: "ts-svdconv-m306"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M306: Schema Version not set for <device>."
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M306"
symptoms: ["M306", "Schema Version not set for <device>."]
symptom_regex: "^Schema Version not set for <device>\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:50", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:152", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:922", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdDevice.cpp:924", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:125", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:234"]
---

## Symptom

`M306`
`Schema Version not set for <device>.`

## Cause

The root <device> element has no schemaVersion attribute, which the SVD schema requires to tell which SVD version the file follows. Warning by default, error with --strict.

## Fix

Add the attribute to the root element, for example <device schemaVersion="1.3">.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdDevice.cpp:50`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:152`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:922`
- `tools/svdconv/SVDModel/src/SvdDevice.cpp:924`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:125`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:234`
