---
id: "drv-wifi-interface-arm-wifi-ping"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_Ping"
summary: "The function ARM_WIFI_Ping checks if the remote host is reachable. It does this by sending an echo request and waiting for an echo response. The function then returns the result of the operation."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_Ping (const uint8_t *ip, uint32_t ip_len)
```


The function **ARM_WIFI_Ping** checks if the remote host is reachable. It does this by sending 
an echo request and waiting for an echo response. The function then returns the result
of the operation. Check the ARM_WIFI_CAPABILITIES of the driver, if this function
is supported in the driver implementation.

The argument **ip** is a pointer to the buffer containing the IP address octets of the host to ping.

The argument **ip_len** specifies the length of the IP address. The length is `4` bytes
for the IPv4 address and `16` bytes for the IPv6 address.
 
**Note:**
The host availability check fails, if the remote host does not respond to echo requests,
or intermediate routers do not forward the echo requests or echo responses.

**Example:**
```
extern ARM_DRIVER_WIFI Driver_WiFi0;
static ARM_DRIVER_WIFI *wifi;
 
void ping_host (void) {
  uint8_t ip[4] = { 192U, 168U, 0U, 100U };
  int32_t res;
 
  wifi = &Driver_WiFi0;
  res = wifi->Ping ((uint8_t *)ip, sizeof(ip));
  if (res == ARM_DRIVER_OK) {
    // Host responded
  }
}
```
