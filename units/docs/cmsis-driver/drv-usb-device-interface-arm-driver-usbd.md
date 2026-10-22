---
id: "drv-usb-device-interface-arm-driver-usbd"
type: "concept"
domain: "drivers"
title: "USB Device Interface: ARM_DRIVER_USBD"
summary: "The functions of the USB Device driver are accessed by function pointers. Refer to DriverFunctions for overview information."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBD.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_DRIVER_USBD
```


The functions of the USB Device driver are accessed by function pointers. Refer to DriverFunctions for 
overview information.

Each instance of an USBD provides such an access struct. The instance is indicated by
a postfix in the symbol name of the access struct, for example:
 - **Driver_USBD0** is the name of the access struct of the first instance (no. 0).
 - **Driver_USBD1** is the name of the access struct of the second instance (no. 1).


A configuration setting in the middleware allows connecting the middleware to a specific driver instance **Driver_USBD_n_**.
The default is `0`, which connects a middleware to the first instance of a driver.

**Note:**    The struct must remain unchanged.
****************************************************************************************************************
