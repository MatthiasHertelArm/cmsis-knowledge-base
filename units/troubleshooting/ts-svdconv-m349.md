---
id: "ts-svdconv-m349"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M349: Alternate … '…' is equal to … name '…'"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M349"
symptoms: ["M349", "Alternate %LEVEL% '%NAME%' is equal to %LEVEL% name '%NAME2%'"]
symptom_regex: "^Alternate .+? '.+?' is equal to .+? name '.+?'$"
documented: true
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@5f04db7:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "svdconv found an alternate name in the SVD that is identical to the name of its own level, such as an alternateRegister or alternateCluster whose name equals the register or cluster it is meant to alias."
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"]
---

## Symptom

`M349`
`Alternate %LEVEL% '%NAME%' is equal to %LEVEL% name '%NAME2%'`

## Cause

svdconv found an alternate name in the SVD that is identical to the name of its own level, such as an alternateRegister or alternateCluster whose name equals the register or cluster it is meant to alias. The %LEVEL% and %NAME% placeholders hold the element kind and the duplicated name. Since the source lines were not available, this reading is taken from the message text and the usual meaning of alternate names in SVD, not from the code.

## Fix

Open the SVD file at the element named in the message and rename the alternate entry so its name differs from the name of the base element it refers to, or remove the alternate entry if it is not needed. Then run svdconv again and check that M349 no longer appears.

## Note

Source lines were not available, so the trigger condition is inferred from the message text only; the README cause and fix were not checked against the code.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp`
