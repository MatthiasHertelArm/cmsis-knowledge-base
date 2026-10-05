---
id: "drv-wifi-interface-arm-wifi-powercontrol"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_PowerControl"
summary: "The function ARM_WIFI_PowerControl allows you to configure the power modes of the WiFi module."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_PowerControl (ARM_POWER_STATE state)
```


The function **ARM_WIFI_PowerControl** allows you to configure the power modes of the WiFi module.

The parameter **state** specifies the ARM_POWER_STATE.

Low-power mode depends on additional options set by ARM_WIFI_SetOption :
 - Deep-sleep mode is entered when ARM_WIFI_LP_TIMER option is set to a value different than 0
 - Sleep mode is entered otherwise

**Deep-sleep** mode (only for station):
Module turns off the radio and also internal CPU thus reducing power consumption to minimum,
only the timer is running that wakes-up the module after specified time.
When timer expires the module reconnects to the access point.

This mode is used when power consumption is a priority (battery powered devices) and when WiFi
is used in short intervals that do not occur very often
(example: sending a temperature from a sensor to a cloud every 10 seconds).

**Sleep** mode (only for station):
Module reduces power consumption by going into sleep and waking up periodically to listen for beacons.

Delivery Traffic Indication Message (DTIM) interval can be configured with option ARM_WIFI_DTIM
(station and access point) and beacon interval with option ARM_WIFI_BEACON (only for access point).

Default module intervals are used when those options are not explicitly set.

If power **state** specifies an unsupported mode, the function returns ARM_DRIVER_ERROR_UNSUPPORTED as
status information and the previous power state of the peripheral is unchanged. Multiple calls with the same
**state** generate no error.

**Example:**
 - see ARM_WIFI_Initialize
 - see ARM_WIFI_Uninitialize
