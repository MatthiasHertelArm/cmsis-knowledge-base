---
id: "txmw-chapter-2-usbx-host-stack-installa-definition-of-usb-host-controllers"
type: "concept"
domain: "rtos"
title: "Chapter 2 - USBX Host Stack Installation: Definition of USB Host Controllers"
summary: "It is required to define at least one USB host controller for USBX to operate in host mode. The application initialization file should contain this definition. The following line performs the definition of a generic host controller."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-host-stack-2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-host-stack-2.md#definition-of-usb-host-controllers"
license: "MIT"
mode: "V"
---

It is required to define at least one USB host controller for USBX to operate in host mode. The application initialization file should contain this definition. The following line performs the definition of a generic host controller.

```c
ux_host_stack_hcd_register("ux_hcd_controller",
        ux_hcd_controller_initialize, 0xd0000, 0x0a);
```

The ux_host_stack_hcd_register has the following prototype.

```c
UINT ux_host_stack_hcd_register(
    UCHAR *hcd_name,
    UINT (*hcd_initialize_function)(struct UX_HCD_STRUCT *),
    ULONG hcd_param1, ULONG hcd_param2);
```

The ux_host_stack_hcd_register function has the following parameters.

- **hcd_name**: string of the controller name
- **hcd_initialize_function**: initialization function of the controller
- **hcd_param1**: usually the IO value or Memory used by the controller
- **hcd_param2**: usually the IRQ used by the controller

In our previous example:

- "ux_hcd_controller" is the name of the controller
- "ux_hcd_controller_initialize" is the initialization routine for the host controller
- 0xd0000 is the address at which the host controller registers are visible in memory
- and 0x0a is the IRQ used by the host controller.

Following is an example of the initialization of USBX in host mode with one host controller and several classes.

```c
UINT status;

/* Initialize USBX. */
ux_system_initialize(memory_ptr, (128*1024),0,0);

/* The code below is required for installing the USBX host stack. */
status = ux_host_stack_initialize(UX_NULL);

/* If status equals UX_SUCCESS, host stack has been initialized. */

/* Register all the host classes for this USBX implementation. */
status = ux_host_class_register("ux_host_class_hub", ux_host_class_hub_entry);

/* If status equals UX_SUCCESS, host class has been registered. */
status = ux_host_class_register("ux_host_class_storage", ux_host_class_storage_entry);

/* If status equals UX_SUCCESS, host class has been registered. */
status = ux_host_class_register("ux_host_class_printer", ux_host_class_printer_entry);

/* If status equals UX_SUCCESS, host class has been registered. */
status = ux_host_class_register("ux_host_class_audio", ux_host_class_audio_entry);

/* If status equals UX_SUCCESS, host class has been registered. */

/* Register all the USB host controllers available in this system. */ 
status = ux_host_stack_hcd_register("ux_hcd_controller", ux_hcd_controller_initialize, 0x300000, 0x0a);

/* If status equals UX_SUCCESS, USB host controllers have been registered. */
```
