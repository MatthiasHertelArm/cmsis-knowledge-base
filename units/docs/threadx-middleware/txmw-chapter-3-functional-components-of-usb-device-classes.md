---
id: "txmw-chapter-3-functional-components-of-usb-device-classes"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of USBX Device Stack: usb_device_classes"
summary: "The Class APIs are very specific to each USB class. Most of the common APIs for USB classes provided services such as opening/closing a device and reading from or writing to a device."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-device-stack-3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-device-stack-3.md#usb-device-classes"
license: "MIT"
mode: "V"
---

The Class APIs are very specific to each USB class. Most of the common APIs for USB classes provided services such as opening/closing a device and reading from or writing to a device.

### Storage Class

The storage class is in charge of answering storage class specific control requests and handling storage class protocol commands. Refer to USB Device Storage Class in Chapter 5 for more information.

### CDC Class

The CDC class is in charge of answering CDC class specific control requests and offering ways to communicate with host through data pipes. Following functionalities are supported now:
* CDC-ACM: communicate with host as a serial device
* CDC-ECM: communicate with host as an ethernet device
Refer to USB Device CDC-ACM Class and USB Device CDC-ECM Class in Chapter 5 for more information.

### HID Class

The HID class is in charge of answering the HID class specific control requests and offering ways to communicate host with HID class specific reports. Refer to USB Device HID Class in Chapter 5 for more information.

### Custom Class

For advanced developers, it's possible to create more customized class, to answering customized control requests and handling customized protocol on data pipes. Note such class may also require specific customization on host side, too.
