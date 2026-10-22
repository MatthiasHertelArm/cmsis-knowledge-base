---
id: "drv-wifi-interface-arm-wifi-ethreadframe"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_EthReadFrame"
summary: "The function ARM_WIFI_EthReadFrame reads an Ethernet frame from the WiFi interface in the bypass mode."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_EthReadFrame (uint32_t interface, uint8_t *frame, uint32_t len)
```


The function **ARM_WIFI_EthReadFrame** reads an **Ethernet frame** from the WiFi interface
in the bypass mode.

The **len** of the Ethernet frame can be checked using the function ARM_WIFI_EthGetRxFrameSize.

The frame data addressed by **frame** starts with MAC destination and ends with the last
Payload data byte. The frame data is read from the receive buffer of the WiFi interface and
the number of bytes written into the memory addressed by **frame** is returned.
A negative return value indicates an error whereby the status code is defined with 
driver common return codes.

The function ARM_WIFI_EthReadFrame may be called with **buf** = `NULL` and **len** = `0`
to discard or release a frame. This is useful when an incorrect frame has been received or
no memory is available to hold the Ethernet frame.
 
**Example:**
```
size = wifi->EthGetRxFrameSize ();
if ((size < 14) || (size > 1514)) {    // frame excludes CRC
  wifi->EthReadFrame (NULL, 0);        // Frame error, release it
}
len = wifi->ReadFrame (0U, &frame_data[0], size);
if (len < 0)  {
  // error handling
}
```
