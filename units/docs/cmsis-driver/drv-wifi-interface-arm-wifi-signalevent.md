---
id: "drv-wifi-interface-arm-wifi-signalevent"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_SignalEvent"
summary: "The function ARM_WIFI_SignalEvent is a callback function registered by the function ARM_WIFI_Initialize. It is called by the WiFi driver to notify the application about WiFi Events occurred during operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
void ARM_WIFI_SignalEvent (uint32_t event, void *arg)
```


The function **ARM_WIFI_SignalEvent** is a callback function registered by the function ARM_WIFI_Initialize.
It is called by the WiFi driver to notify the application about WiFi Events occurred during operation.

The parameter **event** indicates the event that occurred during driver operation.

The parameter **arg** provides additional information about the event.

The following events can be generated:

Parameter **event**                  | Description
:------------------------------------|:------------------------------------------
ARM_WIFI_EVENT_AP_CONNECT       | Occurs in access point mode when a station has connected to the access point.
ARM_WIFI_EVENT_AP_DISCONNECT    | Occurs in access point mode when a station has disconnected from the access point.
ARM_WIFI_EVENT_ETH_RX_FRAME     | Occurs in wifi_bypass_gr when an ethernet frame is received.
