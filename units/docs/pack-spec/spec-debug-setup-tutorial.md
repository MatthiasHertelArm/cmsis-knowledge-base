---
id: "spec-debug-setup-tutorial"
type: "concept"
domain: "pack"
title: "Debug Setup Tutorial"
summary: "debugdescription сhapter extensively documents the methods available in CMSIS-Pack for implementing device-specific debugger behavior."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_dbg_setup_tutorial.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_setup_tutorial.html"
license: "Apache-2.0"
mode: "V"
---

debug_description сhapter extensively documents the methods available in CMSIS-Pack for implementing device-specific debugger behavior.

This chapter guides you through the key use cases that require implementation of debug descriptions. It is structured as follows:
  - dbg_setup_access explains commonly used debug configuration options that can be specified in CMSIS-Pack
  - dbg_debug_sqns demonstrates the implementation of debug sequences in typical scenarios such as trace configuration, bootloader support and multi-core system
  - dbg_sqns_ide describes how debug descriptions work in IDE debuggers
