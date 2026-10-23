---
id: "drv-wifi-interface-arm-wifi-scan"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_Scan"
summary: "The function ARM_WIFI_Scan searches for available WiFi networks. Using this function, you can determine which wireless networks are available for the connection. If the network is secured, you must also know the password to connect."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_Scan (ARM_WIFI_SCAN_INFO_t scan_info[], uint32_t max_num)
```


The function **ARM_WIFI_Scan** searches for available WiFi networks. Using this function,
you can determine which wireless networks are available for the connection. If the network is
secured, you must also know the password to connect.
 
The argument **scan_info** is a pointer to an array of network information structures, where 
the available network information will be returned.

The argument **max_num** specifies maximum number of network information structures,
that can be stored to the **scan_info.**

**Example:**
```
ARM_WIFI_SCAN_INFO_t scan_info[8];
 
num = wifi->Scan (scan_info, 8U);
 
// Print SSIDs of available WiFi networks
for (i = 0; i < num; i++) {
  printf ("%d. ssid=%s\n", i, scan_info[i].ssid);
}
```
