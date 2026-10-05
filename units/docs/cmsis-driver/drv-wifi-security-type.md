---
id: "drv-wifi-security-type"
type: "concept"
domain: "drivers"
title: "WiFi Security Type"
summary: "Specifies WiFi security type for ARMWIFIActivate."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

Specifies WiFi security type for ARM_WIFI_Activate.

The WiFi security type defines the standard used to protect the wireless network from unauthorized access.

### ARM_WIFI_SECURITY_OPEN

```c
ARM_WIFI_SECURITY_OPEN
```

 This is an open system which provides **no** security.
\sa wifi_sec_type

### ARM_WIFI_SECURITY_WEP

```c
ARM_WIFI_SECURITY_WEP
```

 This security standard provides **weak** level of security.
\sa wifi_sec_type

### ARM_WIFI_SECURITY_WPA

```c
ARM_WIFI_SECURITY_WPA
```

 This security standard provides **medium** level of security.
\sa wifi_sec_type

### ARM_WIFI_SECURITY_WPA2

```c
ARM_WIFI_SECURITY_WPA2
```

 This security standard provides **strong** level of security.
\sa wifi_sec_type

### ARM_WIFI_SECURITY_UNKNOWN

```c
ARM_WIFI_SECURITY_UNKNOWN
```

 Unknown security standard (reported by ARM_WIFI_Scan).
\sa wifi_sec_type
