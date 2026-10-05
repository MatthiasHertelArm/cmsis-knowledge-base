---
id: "txmw-chapter-3-functional-components-of-initialization-2"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of USBX Device Stack: initialization"
summary: "In order to activate USBX, the function ux_system_initialize must be called. This function initializes the memory resources of USBX."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-device-stack-3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-device-stack-3.md#initialization"
license: "MIT"
mode: "V"
---

In order to activate USBX, the function ***ux_system_initialize*** must be called. This function initializes the memory resources of USBX.

In order to activate USBX device facilities, the function ***ux_device_stack_initialize*** must be called. This function will in turn initialize all the resources used by the USBX device stack such as ThreadX threads, mutexes, and semaphores.

It is up to the application initialization to activate the USB device controller and one or more USB classes. Contrary to the USB host side, the device side can have only one USB controller driver running at any time. When the classes have been registered to the stack and the device controller(s) initialization function has been called, the bus is active and the stack will reply to bus reset and host enumeration commands.
