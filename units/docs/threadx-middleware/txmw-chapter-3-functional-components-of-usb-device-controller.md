---
id: "txmw-chapter-3-functional-components-of-usb-device-controller"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of USBX Device Stack: usb_device_controller"
summary: "The device controller driver (DCD) interoperates USB Device Stack operations to hardware actions. Normally, a USBX application should not have to call device controller APIs, except initialization function."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-device-stack-3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-device-stack-3.md#usb-device-controller"
license: "MIT"
mode: "V"
---

The device controller driver (DCD) interoperates USB Device Stack operations to hardware actions. Normally, a USBX application should not have to call device controller APIs, except initialization function. When the device controller initialization function is called, the bus is active and the stack will reply to bus reset and host enumeration commands through device controller driver.

Here are some possible hardware which USB Device Stack can operate on:
* STMicroelectronics chip with USB device controller
* Microchip chip with USB device controller
* NXP chip with USB device controller
* Reneses chip with USB device controller
* Other chip with USB device controller, etc.
