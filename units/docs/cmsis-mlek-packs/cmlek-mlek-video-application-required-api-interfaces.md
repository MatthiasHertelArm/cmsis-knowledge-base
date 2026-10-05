---
id: "cmlek-mlek-video-application-required-api-interfaces"
type: "concept"
domain: "edge-ai"
title: "MLEK Video Application: Required API Interfaces"
summary: "For hardware deployment, the Board-Layer should provide the following API interfaces:"
status: "draft"
collection: "cmsis-mlek-packs"
source: "Arm-Examples/cmsis-mlek@6d60f43:docs/templates_video.md"
doc_source: "https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/docs/templates_video.md#required-api-interfaces"
license: "Apache-2.0"
mode: "V"
---

For hardware deployment, the Board-Layer should provide the following API interfaces:

| Required API Interface | Description |
|:----------------------|:------------|
| **CMSIS_VIO** | Virtual I/O interface for LEDs, buttons, and basic I/O |
| **CMSIS_VSTREAM_VIDEO_IN** | Virtual Video Input / Camera Interface |
| **CMSIS_VSTREAM_VIDEO_OUT** | Virtual Video Output / Display |
| **STDOUT, STDERR** | Standard output for printf debugging and logging |

These interfaces ideally are supplied by the vendor of your evaluation board. For custom hardware, details on the implementation are 
found in the [CMSIS-Driver Manual](https://arm-software.github.io/CMSIS_6/latest/Driver/group__vstream__interface__gr.html)
