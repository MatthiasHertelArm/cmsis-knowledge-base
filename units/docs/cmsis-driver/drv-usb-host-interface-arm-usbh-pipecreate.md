---
id: "drv-usb-host-interface-arm-usbh-pipecreate"
type: "concept"
domain: "drivers"
title: "USB Host Interface: ARM_USBH_PipeCreate"
summary: "The function ARMUSBHPipeCreate creates a pipe for transfers (allocates required resources and configures the pipe)."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_USBH.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_USBH_PIPE_HANDLE ARM_USBH_PipeCreate (uint8_t dev_addr, uint8_t dev_speed, uint8_t hub_addr, uint8_t hub_port, uint8_t ep_addr, uint8_t ep_type, uint16_t ep_max_packet_size, uint8_t ep_interval)
```


The function **ARM_USBH_PipeCreate** creates a pipe for transfers (allocates required resources and configures the pipe).

The parameters specify pipe information (connection between host and device endpoint):
 - device: address and speed
 - hub (optional): hub address and number of the hub port to which the device is connected 
 - endpoint: address, type, maximum packet size and polling interval

The function returns an pipe handle that is used for all subsequent operations on that pipe.
In case of errors an invalid handle (**NULL)** is returned.   
****************************************************************************************************************
