---
id: "drv-wifi-interface-arm-wifi-uninitialize"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_Uninitialize"
summary: "The function ARMWIFIUninitialize de-initializes the resources of the WiFi module."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_Uninitialize (void)
```


The function **ARM_WIFI_Uninitialize** de-initializes the resources of the WiFi module.

It is called when the middleware component stops operation and releases the software resources 
used by the module.

**Example:**
```
extern ARM_DRIVER_WIFI Driver_WiFi0;
static ARM_DRIVER_WIFI *wifi;
 
void uninitialize_wifi (void) {
  wifi = &Driver_WiFi0;
 
  // Power off and De-initialize WiFi Module
  wifi->PowerControl (ARM_POWER_OFF);
  wifi->Uninitialize ();
}
```
