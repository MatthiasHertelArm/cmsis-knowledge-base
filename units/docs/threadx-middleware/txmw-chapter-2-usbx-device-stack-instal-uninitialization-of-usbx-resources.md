---
id: "txmw-chapter-2-usbx-device-stack-instal-uninitialization-of-usbx-resources"
type: "concept"
domain: "rtos"
title: "Chapter 2 - USBX Device Stack Installation: Uninitialization of USBX resources"
summary: "USBX can be terminated by releasing its resources. Prior to terminating usbx, all classes and controller resources need to be terminated properly. The following function uninitializes USBX memory resources:"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-device-stack-2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-device-stack-2.md#uninitialization-of-usbx-resources"
license: "MIT"
mode: "V"
---

USBX can be terminated by releasing its resources. Prior to terminating usbx, all classes and controller resources need to be terminated properly. The following function uninitializes USBX memory resources:

```c
/* Uninitialize USBX Resources */
ux_system_uninitialize();
```

The prototype for the ux_system_initialize is as follows:

```c
UINT ux_system_uninitialize(VOID);
```
