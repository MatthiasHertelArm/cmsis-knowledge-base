---
id: "ts-svdconv-m368"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M368: … '…' (@…) has same address as '…' …"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M368"
symptoms: ["M368", "%LEVEL% '%NAME%' (@%ADDR%) has same address as '%NAME2%' %LINE%"]
symptom_regex: "^.+? '.+?' \\(@.+?\\) has same address as '.+?' .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "Two clusters in the same peripheral or cluster start at the same address, and the later one has no <alternateCluster> naming a cluster already at that address."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:757", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:769", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:779", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:789", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:187"]
---

## Symptom

`M368`
`%LEVEL% '%NAME%' (@%ADDR%) has same address as '%NAME2%' %LINE%`

## Cause

Two clusters in the same peripheral or cluster start at the same address, and the later one has no <alternateCluster> naming a cluster already at that address.

## Fix

Correct the later cluster's <addressOffset>, or, if both clusters are alternative views of the same registers, add <alternateCluster>NAME2</alternateCluster> to the later one.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:757`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:769`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:779`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:789`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:187`
