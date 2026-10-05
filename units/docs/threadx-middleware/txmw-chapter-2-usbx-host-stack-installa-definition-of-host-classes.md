---
id: "txmw-chapter-2-usbx-host-stack-installa-definition-of-host-classes"
type: "concept"
domain: "rtos"
title: "Chapter 2 - USBX Host Stack Installation: Definition of Host Classes"
summary: "It is required to define one or more host classes with USBX. A USB class is required to drive a USB device after the USB stack has configured the USB device. A USB class is specific to the device."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-host-stack-2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-host-stack-2.md#definition-of-host-classes"
license: "MIT"
mode: "V"
---

It is required to define one or more host classes with USBX. A USB class is required to drive a USB device after the USB stack has configured the USB device. A USB class is specific to the device. One or more classes may be required to drive a USB device depending on the number of interfaces contained in the USB device descriptors.

This is an example of the registration of the HUB class.

```c
status = ux_host_stack_class_register("ux_host_class_hub", ux_host_class_hub_entry);
```

The function ux_host_class_register has the following prototype.

```c
UINT ux_host_stack_class_register(
    UCHAR *class_name, 
    UINT (*class_entry_address) (struct UX_HOST_CLASS_COMMAND_STRUCT *));
```

- **class_name** is the name of the class
- **class_entry_address** is the entry point of the class

In the example of the HUB class initialization:

- "ux_host_class_hub" is the name of the hub class
- ux_host_class_hub_entry is the entry point of the HUB class.
