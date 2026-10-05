---
id: "drv-wifi-interface-arm-wifi-getnetinfo"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_GetNetInfo"
summary: "The function ARMWIFIGetNetInfo retrieves wireless network information of a connected station."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_GetNetInfo (ARM_WIFI_NET_INFO_t *net_info)
```


The function **ARM_WIFI_GetNetInfo** retrieves wireless network information of a connected station.

It can be used to retrieve network connection information for subsequent connections
after initially connecting using WPS.

**Example:**
```
ARM_WIFI_CONFIG_t wifi_config;
ARM_WIFI_NET_INFO_t net_info;
 
memset(&wifi_config, 0, sizeof(wifi_config));
 
wifi_config.wps_method = ARM_WIFI_WPS_METHOD_PBC;
 
// Connect to wireless network (WPS)
status = wifi->Activate (0U, &wifi_config);
if (status != ARM_DRIVER_OK) {
  // error handling
}
 
// Retrieve network information
if (wifi->IsConnected ()) {
  status = wifi->GetNetInfo (&net_info);
  if (status != ARM_DRIVER_OK) {
    // error handling
  }
  printf("SSID=%s, Password=%s",net_info.ssid, net_info.pass);
}
 
// Disconnect from wireless network
wifi->Deactivate (0U);
```
