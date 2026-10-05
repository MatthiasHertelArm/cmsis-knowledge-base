---
id: "drv-wifi-interface-arm-wifi-socketbind"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_SocketBind"
summary: "The function ARM_WIFI_SocketBind assigns a name to an unnamed socket. The name represents the local address and port of the communication endpoint."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_SocketBind (int32_t socket, const uint8_t *ip, uint32_t ip_len, uint16_t port)
```


The function **ARM_WIFI_SocketBind** assigns a name to an unnamed socket. The name represents the local address
and port of the communication endpoint.

The argument **socket** specifies a socket identification number returned from a previous call
to ARM_WIFI_SocketCreate.

The argument **ip** is a pointer to the buffer containing the IP address octets of the local IP address.

The argument **ip_len** specifies the length of the local IP address. The length is `4` bytes
for the IPv4 address and `16` bytes for the IPv6 address.

The argument **port** specifies the local port. If the argument **port** is `0`, the function returns error,
because this port is reserved.
 
**Example:**
 - see ARM_WIFI_SocketListen
