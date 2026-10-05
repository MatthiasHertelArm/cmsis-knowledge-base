---
id: "drv-wifi-interface-arm-wifi-getmoduleinfo"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_GetModuleInfo"
summary: "The function ARM_WIFI_GetModuleInfo retrieves string containing information about the WiFi module."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_GetModuleInfo (char *module_info, uint32_t max_len)
```


The function **ARM_WIFI_GetModuleInfo** retrieves string containing information about the WiFi module.

The information might include module name, firmware version, ...

**Note:** Module must be initialized and powered before module information can be retrieved.

**Example:**
```
extern ARM_DRIVER_WIFI Driver_WiFi0;
static ARM_DRIVER_WIFI *wifi;
 
void initialize_wifi (void) {
  char info[32];
 
  wifi = &Driver_WiFi0;
 
  // Initialize and Power-on WiFi Module
  wifi->Initialize (NULL);
  wifi->PowerControl (ARM_POWER_FULL);
 
  // Retrieve module information
  wifi->GetModuleInfo(&info, sizeof(info));
}
```
