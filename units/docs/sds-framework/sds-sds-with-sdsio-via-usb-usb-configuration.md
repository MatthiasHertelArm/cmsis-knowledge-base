---
id: "sds-sds-with-sdsio-via-usb-usb-configuration"
type: "concept"
domain: "test"
title: "SDS with SDSIO via USB: USB Configuration"
summary: "The following MDK-Middleware USB software components are required:"
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:layer/sdsio/usb/README.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/layer/sdsio/usb/README.md#usb-configuration"
license: "Apache-2.0"
mode: "V"
---

The following MDK-Middleware USB software components are required:

```yml
  - component: USB&MDK:CORE
  - component: USB&MDK:Device
  - component: USB&MDK:Device:Custom Class
```

### USB Vendor ID and Product ID

The default `USBD_Config_0.h` contains placeholder Vendor ID (VID) and Product ID (PID) values:

```c
#define USBD0_DEV_DESC_IDVENDOR         0xC251   // replace with your own VID
#define USBD0_DEV_DESC_IDPRODUCT        0x8007   // replace with your own PID
```

The Vendor ID **0xC251 (Keil)** and Product ID **0x8007** can be used for internal testing environments with limited access.
For production, the Vendor ID (VID) and Product ID (PID) should be vendor-specific.
The Vendor ID must be assigned by the [USB Implementers Forum (USB-IF)](https://www.usb.org/) following the procedure for
[Getting a Vendor ID](https://www.usb.org/getting-vendor-id).
