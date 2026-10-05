---
id: "drv-usb-host-interface-arm-usbh-initialize"
type: "concept"
domain: "drivers"
title: "USB Host Interface: ARM_USBH_Initialize"
summary: "The function ARM_USBH_Initialize initializes the USB Host interface. It is called when the middleware component starts operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_USBH_Initialize (ARM_USBH_SignalPortEvent_t cb_port_event, ARM_USBH_SignalPipeEvent_t cb_pipe_event)
```


The function **ARM_USBH_Initialize** initializes the USB Host interface. 
It is called when the middleware component starts operation.

The function performs the following operations:
  - Initializes the resources needed for the USBH interface.
  - Registers the ARM_USBH_SignalPortEvent callback function.
  - Registers the ARM_USBH_SignalPipeEvent callback function.

The parameter **cb_port_event** is a pointer to the ARM_USBH_SignalPortEvent callback function; use a NULL pointer 
when no port callback signals are required.

The parameter **cb_pipe_event** is a pointer to the ARM_USBH_SignalPipeEvent callback function.

**Example:**
 - see usbh_interface_gr - Driver Functions

****************************************************************************************************************
