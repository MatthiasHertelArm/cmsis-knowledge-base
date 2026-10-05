---
id: "spec-debug-description-debug-access-sequences"
type: "concept"
domain: "pack"
title: "Debug Description: Debug access sequences"
summary: "Debug access sequences define the activities of development tools to connect to a device using the debug channel for debugging, tracing, or flash programming. Several debug access sequences are predefined and executed in specific context. Refer to <sequences> for details."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/debug_description.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html"
license: "Apache-2.0"
mode: "V"
---

Debug access sequences define the activities of development tools to connect to a device using the debug channel for
debugging, tracing, or flash programming. Several debug access sequences are predefined and executed in specific context. 
Refer to `<sequences>` for details.

Software development tools should implement default_sequences. These predefined sequences can be overwritten by device
specific sequences using the `<sequence>` element in the `<sequences>` section of the PDSC file. Additionally,
a PDSC file can contain user-defined sequences, for example to reuse access sequence fragments:
 - usage_of_sequences explains how the sequences are used from a development tool point of view.
 - default_sequences lists all debug access sequences that are predefined by the CMSIS-Pack standard and shows the details of the predefined debug access sequences.
 - writing_sequences explains how to write custom debug access sequences. These can be used to either override predefined sequences or to define device specific sequences.
