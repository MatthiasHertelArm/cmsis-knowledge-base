---
id: "spec-debug-description-debug-description-elements"
type: "concept"
domain: "pack"
title: "Debug Description: Debug description elements"
summary: "A complete debug description for a device consists of the following elements: - <debug> with the child element <dbg_datapatch> contains settings for the debug connection and for fixing silicon issues in software."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/debug_description.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html"
license: "Apache-2.0"
mode: "V"
---

A complete debug description for a device consists of the following elements:
 - `<debug>` with the child element `<dbg_datapatch>` contains settings for the debug connection and for
   fixing silicon issues in software.
 - `<debugconfig>` provides the default debugger configuration for a target connection.
 - `<debugvars>` specifies global debug access variables. They can be used in addition to predefined variables to pass
 user settings to debug access sequences.
 - `<debugport>` with the child elements `<dp_jtag>`, `<dp_swd>`, and `<dp_cjtag>` describes the
   debug port in detail.
 - `<accessportV1>` describes an access port (APv1) in detail.
 - `<accessportV2>` describes an access port (APv2) in detail.
 - `<sequences>` with the child elements `<sequence>`, `<seq_control>`, and `<seq_block>` creates a
   configuration for debug access sequences.
 - `<trace>` with the child elements `<trace_serialwire>`, `<trace_traceport>`, and
   `<trace_tracebuffer>` sets up the trace connection.
