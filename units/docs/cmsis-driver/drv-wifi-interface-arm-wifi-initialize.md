---
id: "drv-wifi-interface-arm-wifi-initialize"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_Initialize"
summary: "The function ARM_WIFI_Initialize initializes the WiFi module."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_Initialize (ARM_WIFI_SignalEvent_t cb_event)
```


The function **ARM_WIFI_Initialize** initializes the WiFi module.

It is called when the middleware component starts operation.

The ARM_WIFI_Initialize function performs the following operations:
  - Initializes the resources and peripherals required for the WiFi module.
  - Registers the ARM_WIFI_SignalEvent callback function.

The parameter **cb_event** is a pointer to the ARM_WIFI_SignalEvent callback function;
use a `NULL` pointer when no callback signals are required.

**Example:**
```
extern ARM_DRIVER_WIFI Driver_WiFi0;
static ARM_DRIVER_WIFI *wifi;
static ARM_ETH_MAC_ADDR own_mac_address;
 
void initialize_wifi (void) {
  wifi = &Driver_WiFi0;
 
  // Initialize and Power-on WiFi Module
  wifi->Initialize (NULL);
  wifi->PowerControl (ARM_POWER_FULL);
 
  // Populate own_mac_address with the address to use
  wifi->SetOption(ARM_WIFI_MAC, &own_mac_address, 6U);
}
```
