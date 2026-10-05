---
id: "drv-wifi-interface-arm-wifi-getcapabilities"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_GetCapabilities"
summary: "The function ARM_WIFI_GetCapabilities retrieves information about capabilities in this driver implementation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_WIFI_CAPABILITIES ARM_WIFI_GetCapabilities (void)
```


The function **ARM_WIFI_GetCapabilities** retrieves information about capabilities in this driver implementation.
The data fields of the struct ARM_WIFI_CAPABILITIES encode various capabilities, for example
if a WiFi module supports the Access Point mode or the bypass mode, or is capable to signal events using
the ARM_WIFI_SignalEvent callback function.

**Example:**
```
extern ARM_DRIVER_WIFI Driver_WiFi0;
static ARM_DRIVER_WIFI *wifi;
  
void get_wifi_capabilities (void)  {
  ARM_WIFI_CAPABILITIES capabilities;
 
  wifi = &Driver_WiFi0;  
  capabilities = wifi->GetCapabilities ();
  // interrogate capabilities
   :
}
```
