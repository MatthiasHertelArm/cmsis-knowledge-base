---
id: "txmw-chapter-1-introduction-to-usbx-hos-usbx-features"
type: "concept"
domain: "rtos"
title: "Chapter 1 - Introduction to USBX Host Stack: USBX features"
summary: "USBX support the three existing USB specifications: 1.1, 2.0 and OTG. It is designed to be scalable and will accommodate simple USB topologies with only one connected device as well as complex topologies with multiple devices and cascading hubs."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-host-stack-1.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-host-stack-1.md#usbx-features"
license: "MIT"
mode: "V"
---

USBX support the three existing USB specifications: 1.1, 2.0 and OTG. It is designed to be scalable and will accommodate simple USB topologies with only one connected device as well as complex topologies with multiple devices and cascading hubs. USBX supports all the data transfer types of the USB protocols: control, bulk, interrupt, and isochronous.

USBX supports both the host side and the device side. Each side is
comprised of three layers.

- Controller layer
- Stack layer
- Class layer

The relationship between the USB layers is as follows.

(figure: USB Layers)
