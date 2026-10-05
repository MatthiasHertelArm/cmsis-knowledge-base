---
id: "spec-use-of-debug-descriptions-in-mu-vi"
type: "concept"
domain: "pack"
title: "Use of debug descriptions in &mu;Vision"
summary: "debugdescription elements and access sequences are defined as IDE-independent. However the debug IDE can use this information to provide settings and to use sequences where applicable in its debug flow."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_dbg_setup_tutorial.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_sqns_uvision.html"
license: "Apache-2.0"
mode: "V"
---

debug_description elements and access sequences are defined as IDE-independent. However the debug IDE can use this information to provide settings and to use sequences where applicable in its debug flow.

**Arm &mu;Vision debugger ** (part of Keil MDK)  supports CMSIS debug descriptions. If any of the debug description elements or debug access sequences are defined in a DFP for the target MCU the &mu;Vision automatically detects that and provides user with the configuration options described in this chapter.
