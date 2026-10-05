---
id: "drv-usb-device-interface-arm-usbd-initialize"
type: "concept"
domain: "drivers"
title: "USB Device Interface: ARM_USBD_Initialize"
summary: "The function ARMUSBDInitialize initializes the USB Device interface. It is called when the middleware component starts operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USBD_Initialize (ARM_USBD_SignalDeviceEvent_t cb_device_event, ARM_USBD_SignalEndpointEvent_t cb_endpoint_event)
```


The function **ARM_USBD_Initialize** initializes the USB Device interface. 
It is called when the middleware component starts operation.

The function performs the following operations:
  - Initializes the resources needed for the USBD interface.
  - Registers the ARM_USBD_SignalDeviceEvent callback function.
  - Registers the ARM_USBD_SignalEndpointEvent callback function.

The parameter **cb_device_event** is a pointer to the ARM_USBD_SignalDeviceEvent callback function; use a NULL pointer 
when no device callback signals are required. \n
The parameter **cb_endpoint_event** is a pointer to the ARM_USBD_SignalEndpointEvent callback function.

**Example:**
 - see usbd_interface_gr - Driver Functions

****************************************************************************************************************
