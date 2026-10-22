---
id: "ts-svdconv-m340"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M340: No Devices found."
status: "draft"
tool: "svdconv"
severity: "error"
code: "M340"
symptoms: ["M340", "No Devices found."]
symptom_regex: "^No Devices found\\.$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv parsed the input SVD file but found no <device> element to convert, so there is nothing to generate output from."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M340`
`No Devices found.`

## Cause

svdconv parsed the input SVD file but found no <device> element to convert, so there is nothing to generate output from. This usually means the SVD file is empty, truncated, or its root structure does not contain a device description.

## Fix

Open the SVD file named in the build log and confirm it contains a <device> element with peripherals under it; if the file is truncated or was generated incorrectly, regenerate or re-download it, then run svdconv again.

## Note

Source lines were not available, so the trigger location is unverified and the cause is inferred from the message text and the README entry. Verify against the source before relying on the specific wording.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
