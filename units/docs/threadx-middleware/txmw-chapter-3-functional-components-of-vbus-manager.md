---
id: "txmw-chapter-3-functional-components-of-vbus-manager"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of USBX Device Stack: vbus_manager"
summary: "In most USB device designs, VBUS is not part of the USB Device core but rather connected to an external GPIO, which monitors the line signal."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-device-stack-3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-device-stack-3.md#vbus-manager"
license: "MIT"
mode: "V"
---

In most USB device designs, VBUS is not part of the USB Device core but rather connected to an external GPIO, which monitors the line signal.

As a result, VBUS has to be managed separately from the device controller driver.

It is up to the application to provide the device controller with the address of the VBUS IO. VBUS must be initialized prior to the device controller initialization.

Depending on the platform specification for monitoring VBUS, it is possible to let the controller driver handle VBUS signals after the VBUS IO is initialized or if this is not possible, the application has to provide the code for handling VBUS.

If the application wishes to handle VBUS by itself, its only requirement is to call the function ***ux_device_stack_disconnect*** when it detects that a device has been extracted. It is not necessary to inform the controller when a device is inserted because the controller will wake up when the BUS RESET assert/deassert signal is detected.
