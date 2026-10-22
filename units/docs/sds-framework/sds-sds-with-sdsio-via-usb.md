---
id: "sds-sds-with-sdsio-via-usb"
type: "concept"
domain: "test"
title: "SDS with SDSIO via USB"
summary: "This layer provides SDS with SDSIO using the USB communication. It is implemented with the MDK-Middleware USB component. It is based on the following components:"
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@c18efee:layer/sdsio/usb/README.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/c18efee/layer/sdsio/usb/README.md"
license: "Apache-2.0"
mode: "V"
---

This layer provides SDS with SDSIO using the USB communication.
It is implemented with the MDK-Middleware USB component.
It is based on the following components:

- [SDS](https://arm-software.github.io/SDS-Framework/main/SDS_API/group__SDS__Stream__Interface.html) data streaming,
- [SDSIO](https://arm-software.github.io/SDS-Framework/main/SDS_API/group__SDSIO__Interface.html) SDSIO interface,
- [MDK-Middleware USB](https://arm-software.github.io/MDK-Middleware/latest/USB/USB_Device.html) communication stack,
- [CMSIS-Driver USB Device](https://arm-software.github.io/CMSIS_6/latest/Driver/group__usbd__interface__gr.html) physical interface.
