---
id: "spec-debug-setup-with-cmsis-pack"
type: "concept"
domain: "pack"
title: "Debug Setup with CMSIS-Pack"
summary: "CMSIS-Pack offers two ways to simplify the debug setup: - A debugdescription declares a set of standardized debug and trace methods are automatically executed by the debugger. Implementation-specific steps can be described using an XML syntax."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/debug_description.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/coresight_setup.html"
license: "Apache-2.0"
mode: "V"
---

CMSIS-Pack offers two ways to simplify the debug setup:
- A debug_description declares a set of standardized debug and trace methods are automatically executed by the
  debugger. Implementation-specific steps can be described using an XML syntax. This concept is easy to implement for basic
  chip configurations that mostly rely on a standard implementation of the CoreSight architecture. Most single-core devices
  should be able to be specified completely with debug descriptions.
  
- For more complex topologies and multi-core devices, a System Description File helps debuggers to connect to
  the target and access all available cores via trace. An SDF file is more complex (although also specified in XML), but is
  also more flexible with regards to the underlying debug architecture.
  
- dbg_setup_tutorial provides a guide on how to implement the debug descriptions for a microcontroller device. It explains the options for configuring debug connection. Gives examples on implementing debug access sequences in specific scenarios such as trace support, bootloader handling, multi-core systems and others. And finally shows how debug descriptions can be used in various IDE debuggers.
