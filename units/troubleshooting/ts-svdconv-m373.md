---
id: "ts-svdconv-m373"
type: "troubleshooting"
domain: "error-catalog"
title: "svdconv M373: … <…> '…' already defined …"
status: "draft"
tool: "svdconv"
severity: "warning"
code: "M373"
symptoms: ["M373", "%LEVEL% <%TAG%> '%NAME%' already defined %LINE%"]
symptom_regex: "^.+? <.+?> '.+?' already defined .+?$"
documented: true
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp"
doc_source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
applies_to: {"tool": ["svdconv"]}
license: "Apache-2.0"
mode: "V"
summary: "Two registers or clusters at the same level of a peripheral or cluster end up with the same display name. svdconv compares each register's <displayName> and, where a register has none (and for clusters, which have no <displayName>), its …"
cause_origin: "source-analysis"
confidence: "medium"
evidence: ["Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:843-866", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:800-827", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1028-1030", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1049-1051", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1157-1158", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:404-423", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDModel/src/SvdItem.cpp:514-518", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:192", "Open-CMSIS-Pack/devtools@30f5e817:tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:255"]
---

## Symptom

`M373`
`%LEVEL% <%TAG%> '%NAME%' already defined %LINE%`

## Cause

Two registers or clusters at the same level of a peripheral or cluster end up with the same display name. svdconv compares each register's <displayName> and, where a register has none (and for clusters, which have no <displayName>), its <name>; so registers that share a <name> in different <alternateGroup>s collide here even though the name check accepts them.

## Fix

Give each register at that level a unique <displayName>, or drop a copied <displayName> so the distinct <name> is used. For registers with the same <name> in different <alternateGroup>s, add a distinct <displayName> to each, e.g. <displayName>CTRL_ALT</displayName>. The line in the message points to the first definition.

## Note

Error under --strict. The name check appends <alternateGroup> to the name (SvdPeripheral.cpp:806-809) but the displayName check does not, so equal names in different alternate groups without explicit <displayName> look like a false positive.

## Evidence

Read from the source of Open-CMSIS-Pack/devtools@30f5e817, confidence medium, not reviewed yet:

- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:843-866`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:800-827`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1028-1030`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1049-1051`
- `tools/svdconv/SVDModel/src/SvdPeripheral.cpp:1157-1158`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:404-423`
- `tools/svdconv/SVDModel/src/SvdItem.cpp:514-518`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:192`
- `tools/svdconv/SVDConv/src/SVDConv_Msgs.cpp:255`
