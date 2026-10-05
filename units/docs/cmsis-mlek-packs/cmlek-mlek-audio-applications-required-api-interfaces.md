---
id: "cmlek-mlek-audio-applications-required-api-interfaces"
type: "concept"
domain: "edge-ai"
title: "MLEK - Audio Applications: Required API Interfaces"
summary: "For hardware deployment, the Board-Layer should provide the following API interfaces:"
status: "draft"
collection: "cmsis-mlek-packs"
source: "Arm-Examples/cmsis-mlek@6d60f43:docs/templates_audio.md"
doc_source: "https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/docs/templates_audio.md#required-api-interfaces"
license: "Apache-2.0"
mode: "V"
---

For hardware deployment, the Board-Layer should provide the following API interfaces:

| Required API Interface | Description |
|:----------------------|:------------|
| **CMSIS_VIO** | Virtual I/O interface for LEDs, buttons, and basic I/O |
| **CMSIS_VSTREAM_AUDIO_IN** | Virtual Audio Input / Audio Interface |
| **STDOUT, STDERR** | Standard output for printf debugging and logging |

These interfaces ideally are supplied by the vendor of your evaluation board. For custom hardware, details on the implementation are 
found in the [CMSIS-Driver Manual](https://arm-software.github.io/CMSIS_6/latest/Driver/group__vstream__interface__gr.html)
