---
id: "drv-wifi-interface-arm-wifi-ethgetrxframesize"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_EthGetRxFrameSize"
summary: "The function ARM_WIFI_EthGetRxFrameSize returns the size of a received Ethernet frame in the bypass mode. This function can be called before ARM_WIFI_EthReadFrame and retrieves the value len."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t ARM_WIFI_EthGetRxFrameSize (uint32_t interface)
```


The function **ARM_WIFI_EthGetRxFrameSize** returns the size of a received **Ethernet frame**
in the bypass mode. This function can be called before ARM_WIFI_EthReadFrame and retrieves 
the value **len.**

The frame size includes MAC destination and ends with the last Payload data byte.
Value `0` indicates that no Ethernet frame is available in the receive buffer.
Values smaller than minimum size of Ethernet frame or larger than maximum size of Ethernet frame
indicate an invalid frame which needs to be discarded by calling ARM_WIFI_EthReadFrame.
 
**Example:**
 - see ARM_WIFI_EthReadFrame
