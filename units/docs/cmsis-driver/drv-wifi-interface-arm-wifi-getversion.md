---
id: "drv-wifi-interface-arm-wifi-getversion"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_GetVersion"
summary: "The function ARM_WIFI_GetVersion returns version information of the driver implementation in ARM_DRIVER_VERSION."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
ARM_DRIVER_VERSION ARM_WIFI_GetVersion (void)
```


The function **ARM_WIFI_GetVersion** returns version information of the driver implementation in ARM_DRIVER_VERSION.

API version is the version of the CMSIS-Driver specification used to implement this driver.
Driver version is source code version of the actual driver implementation.

**Example:**
```
extern ARM_DRIVER_WIFI Driver_WiFi0;
static ARM_DRIVER_WIFI *wifi;
 
void get_wifi_version (void)  {
  ARM_DRIVER_VERSION version;
 
  wifi= &Driver_WiFi0;  
  version = wifi->GetVersion ();
  if (version.api < 0x100U) {        // requires at minimum API version 1.0 or higher
    // error handling
    return;
  }
}
```
