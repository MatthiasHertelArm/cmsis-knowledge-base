---
id: "txmw-chapter-2-usbx-device-stack-instal-usbx-version-id"
type: "concept"
domain: "rtos"
title: "Chapter 2 - USBX Device Stack Installation: USBX Version ID"
summary: "The current version of USBX is available both to the user and the application software during run-time. The programmer can obtain the USBX version from examination of the ux_port.h file."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-device-stack-2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-device-stack-2.md#usbx-version-id"
license: "MIT"
mode: "V"
---

The current version of USBX is available both to the user and the application software during run-time. The programmer can obtain the USBX version from examination of the ***ux_port.h*** file. In addition, this file also contains a version history of the corresponding port. Application software can obtain the USBX version by examining the global string ***_ux_version_id***, which is defined in ***ux_port.h***.
