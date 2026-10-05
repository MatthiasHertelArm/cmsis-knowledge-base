---
id: "drv-wifi-protected-setup-wps-method"
type: "concept"
domain: "drivers"
title: "WiFi Protected Setup (WPS) Method"
summary: "Specifies WiFi WPS method for ARM_WIFI_Activate."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

Specifies WiFi WPS method for ARM_WIFI_Activate.

The WiFi WPS method defines which WPS method is used.

### ARM_WIFI_WPS_METHOD_NONE

```c
ARM_WIFI_WPS_METHOD_NONE
```

 WPS not used.
\sa wifi_wps_method

### ARM_WIFI_WPS_METHOD_PBC

```c
ARM_WIFI_WPS_METHOD_PBC
```

 WPS with Push Button Configuration.
\sa wifi_wps_method

### ARM_WIFI_WPS_METHOD_PIN

```c
ARM_WIFI_WPS_METHOD_PIN
```

 WPS with PIN.
\sa wifi_wps_method
