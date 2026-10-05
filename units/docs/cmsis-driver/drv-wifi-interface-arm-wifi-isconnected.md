---
id: "drv-wifi-interface-arm-wifi-isconnected"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_IsConnected"
summary: "The function ARM_WIFI_IsConnected checks if the station is connected to a wireless network and returns the connection status."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
uint32_t ARM_WIFI_IsConnected (void)
```


The function **ARM_WIFI_IsConnected** checks if the station is connected to a wireless network
and returns the connection status.

The function returns a `non-zero` value, if the station is connected. If the station
is not connected, the function returns `0`.

**Example:**
 - see ARM_WIFI_GetNetInfo
