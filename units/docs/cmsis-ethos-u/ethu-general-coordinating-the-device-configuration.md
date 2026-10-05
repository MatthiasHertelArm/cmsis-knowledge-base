---
id: "ethu-general-coordinating-the-device-configuration"
type: "concept"
domain: "edge-ai"
title: "General: Coordinating the device configuration"
summary: "An Edge AI MCU has a fixed Cortex-M, Ethos-U, interconnect, and memory integration. The software descriptions used to build an application must match that finished device:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/general/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/general/src/main.md#coordinating-the-device-configuration"
license: "Apache-2.0"
mode: "V"
---

An Edge AI MCU has a fixed Cortex-M, Ethos-U, interconnect, and memory
integration. The software descriptions used to build an application must match
that finished device:

1. The device description identifies the processor, Ethos-U configuration, and
   available memory regions.
2. The `vela.ini` configuration models the device's memory performance and
   defines its supported memory modes.
3. The linker and MPU/SAU configuration place code and data in the device's
   physical memory regions with suitable CPU attributes.
4. The driver configuration assigns the command stream and model regions to the
   matching NPU memory-access paths and attributes.

A DFP can provide these related configuration artifacts, and CMSIS-Toolbox can
resolve them for the selected device and build context. The artifacts must be
consistent. The full mapping, examples, and consistency checklist are in
Integration. The meaning and syntax of `vela.ini`
are in Vela.
