---
id: "drv-wifi-interface-arm-wifi-getoption"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_GetOption"
summary: "The function ARM_WIFI_GetOption retrieves the current value of the specified option of the WiFi module."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_GetOption (uint32_t interface, uint32_t option, void *data, uint32_t *len)
```


The function **ARM_WIFI_GetOption** retrieves the current value of the specified option of
the WiFi module.

The argument **interface** specifies the interface (0 = Station, 1 = Access Point).

The argument **option** specifies the option that is to be retrieved (see ARM_WIFI_SetOption).

The argument **data** points to a buffer that will be used to store the value of 
the **option** and must be aligned to the data type of the corresponding option.

The argument **len** is a pointer to the length of the buffer at input and returns the length
of the option information on the output.

**Example:**
```
uint8_t ip[4];          // IP address
uint8_t mask[4];        // Subnet mask
uint8_t gateway[4];     // Gateway address
 
// Get IP address, Subnet mask and Gateway address of the Station
wifi->GetOption (0U, ARM_WIFI_IP, &ip, sizeof(ip));
wifi->GetOption (0U, ARM_WIFI_IP_SUBNET_MASK, &mask, sizeof(mask));
wifi->GetOption (0U, ARM_WIFI_IP_GATEWAY, &gateway, sizeof(gateway));
```
