---
id: "txmw-overview-of-usbx-usbx-apis"
type: "concept"
domain: "rtos"
title: "Overview of USBX: USBX APIs"
summary: "The USBX Host API is an intuitive and consistent API, following a noun-verb naming convention. All APIs have leading ux_host to easily identify as USBX. Any blocking APIs have optional thread timeout."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/overview-usbx.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/overview-usbx.md#usbx-apis"
license: "MIT"
mode: "V"
---

### USBX Host API

The USBX Host API is an intuitive and consistent API, following a noun-verb naming convention. All APIs have leading ux_host_* to easily identify as USBX. Any blocking APIs have optional thread timeout. Please see [USBX Host User Guide](https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-host-stack-about.md) for more details.

* ASIX
    - Minimal 0.3 KB FLASH, 4 KB RAM
    - Automatic scaling
    - System-level trace via TraceX
    - Intuitive USBX host APIs in this form: *ux_host_class_asix_**
* AUDIO (1.0/2.0)
    - Minimal 1.2 KB FLASH, 4 KB RAM
    - Automatic scaling
    - System-level trace via TraceX
    - Intuitive USBX host APIs in this form: *ux_host_class_audio_**
* CDC/ACM
    - Minimal 1.4 KB FLASH, 4 KB RAM
    - Automatic scaling
    - Support of standalone mode
    - System-level trace via TraceX
    - Intuitive USBX host APIs in this form: *ux_host_class_cdc_acm_**
* HID
    - Minimal 0.3 KB FLASH, 4 KB RAM
    - Keyboard, mouse, and remote support
    - Automatic scaling
    - Support of standalone mode
    - System-level trace via TraceX
    - Intuitive USBX host APIs in this form: *ux_host_class_hid_** 
* HUB
    - Minimal 1.7 KB FLASH, 2 KB RAM
    - Automatic scaling
    - Support of standalone mode
    - System-level trace via TraceX
    - Intuitive USBX host APIs in this form: *ux_host_class_hub_**
* PIMA (PTP/MTP)
    - Minimal 0.9 KB FLASH, 8 KB RAM
    - Automatic scaling
    - System-level trace via TraceX
    - Intuitive USBX host APIs in this form: *ux_host_class_pima_**
* PRINTER
    - Minimal 0.8 KB FLASH, 8 KB RAM
    - Automatic scaling
    - Support of standalone mode
    - System-level trace via TraceX
    - Intuitive USBX host APIs in this form: *ux_host_class_printer_**
* PROLIFIC
    - Minimal 1.5 KB FLASH, 4 KB RAM
    - Automatic scaling
    - System-level trace via TraceX
    - Intuitive USBX host APIs in this form: *ux_host_class_prolific_**
* STORAGE
    - Minimal 5.6 KB FLASH, 4 KB RAM
    - Automatic scaling
    - Support of standalone mode
    - Integrated with FileX
    - System-level trace via TraceX
    - Intuitive USBX host APIs in this form: *ux_host_class_storage_**
* VIDEO
    - Minimal 0.8 KB FLASH, 8 KB RAM
    - Automatic scaling
    - System-level trace via TraceX
    - Intuitive USBX host APIs in this form: *ux_host_class_video_**
* USB Host STACK
    - Supports many host controllers
    - Minimal 18 KB FLASH, 25 KB RAM
    - Automatic scaling
    - Support for multiple host controllers on same platform
    - USB low, full, and high-speed support
    - System-level trace via TraceX
    - Intuitive USBX host APIs in this form: *ux_host_stack_** 
* OHCI, EHCI, PROPRIETARY Host CONTROLLERS 

### USBX Device API

The USBX Device API is an intuitive and consistent API following a noun-verb naming convention. All APIs have leading ux_device_* to easily identify as USBX. Blocking APIs have optional thread timeout. Please see [USBX Device User Guide](https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-device-stack-about.md) for more details.

* AUDIO (1.0/2.0)
    - Minimal xx KB FLASH, x KB RAM
    - Automatic scaling
    - Support of standalone mode
    - System-level trace via TraceX
    - Intuitive USBX host APIs in this form: *ux_device_class_audio_**
* CDC/ACM
    - Minimal 0.8 KB FLASH, 2 KB RAM
    - Automatic scaling
    - Support of standalone mode
    - System-level trace via TraceX
    - Intuitive USBX device APIs in this form: *ux_device_class_cdc_acm_**
* CDC/ECM
    - Minimal 1.5 KB FLASH, 4 KB to 8 KB RAM
    - Automatic scaling
    - System-level trace via TraceX
    - Intuitive USBX device APIs in this form: *ux_device_class_cdc_ecm_**
* DFU
    - Minimal 1.1 KB FLASH, 2 KB RAM
    - Automatic scaling
    - Support of standalone mode
    - System-level trace via TraceX
    - Intuitive USBX device APIs in this form: *ux_device_class_dfu_** 
* HID
    - Minimal 0.9 KB FLASH, 2 KB RAM
    - Automatic scaling
    - Support of standalone mode
    - System-level trace via TraceX
    - Intuitive USBX device APIs in this form: *ux_device_class_hid_** 
* PIMA (PTP/MTP)
    - Minimal 5.2 KB FLASH, 8 KB RAM
    - Automatic scaling
    - System-level trace via TraceX
    - Intuitive USBX device APIs in this form: *ux_device_class_pima_** 
* STORAGE
    - Minimal 2.3 KB FLASH, 4 KB RAM
    - Automatic scaling
    - Support of standalone mode
    - System-level trace via TraceX
    - Intuitive USBX device APIs in this form: *ux_device_class_storage_**
* RNDIS
    - Minimal 2.3 KB FLASH, 4 KB to 8 KB RAM
    - Automatic scaling
    - Integrated with NetX Duo
    - System-level trace via TraceX
    - Intuitive USBX device APIs in this form: *ux_device_class_rndis_**
* PRINTER
    - Minimal xx KB FLASH, x KB RAM
    - Automatic scaling
    - Support of standalone mode
    - System-level trace via TraceX
    - Intuitive USBX host APIs in this form: *ux_device_class_printer_**
* VIDEO
    - Minimal xx KB FLASH, x KB RAM
    - Automatic scaling
    - Support of standalone mode
    - System-level trace via TraceX
    - Intuitive USBX host APIs in this form: *ux_device_class_video_**
* CCID
    - Minimal xx KB FLASH, x KB RAM
    - Automatic scaling
    - Support of standalone mode
    - System-level trace via TraceX
    - Intuitive USBX host APIs in this form: *ux_device_class_ccid_**
* USBX Device STACK
    - Minimal 2.3 KB FLASH, 4 KB RAM
    - Automatic scaling
    - System-level trace via TraceX
    - Intuitive USBX device APIs in this form: *ux_device_stack_**
* PROPRIETARY Device CONTROLLERS
