---
id: "drv-wifi-interface-arm-wifi-ethsendframe"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_EthSendFrame"
summary: "The function ARMWIFIEthSendFrame writes an Ethernet frame to the WiFi transmit buffer."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_EthSendFrame (uint32_t interface, const uint8_t *frame, uint32_t len)
```


The function **ARM_WIFI_EthSendFrame** writes an **Ethernet frame** to the WiFi transmit buffer.

The WiFi bypass mode must be enabled by using the function ARM_WIFI_BypassControl
before a call to this function.

The frame data addressed by **frame** starts with MAC destination and ends with the last
Payload data byte. The frame data is copied into the transmit buffer of the WiFi interface.

The maximum value for **len** is implied by the size restrictions of the Ethernet frame
but is not verified. Using an invalid value for **len** may generate unpredicted results.

**Example:**
```
status = wifi->EthSendFrame (0U, &frame_data[0], frame_length);
if (status != ARM_DRIVER_OK)  {
  // error handling
}
```
