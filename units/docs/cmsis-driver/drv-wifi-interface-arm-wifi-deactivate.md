---
id: "drv-wifi-interface-arm-wifi-deactivate"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_Deactivate"
summary: "The function ARM_WIFI_Deactivate deactivates the specified interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_Deactivate (uint32_t interface)
```


The function **ARM_WIFI_Deactivate** deactivates the specified interface.

The argument **interface** specifies the interface (0 = Station, 1 = Access Point).

When station interface is specified, the WiFi module disconnects from the wireless network.

When access point interface is specified, the WiFi module deactivates the access point.

**Example:**
 - see ARM_WIFI_GetNetInfo
