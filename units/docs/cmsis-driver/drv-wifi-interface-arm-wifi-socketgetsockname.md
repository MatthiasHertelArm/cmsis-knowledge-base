---
id: "drv-wifi-interface-arm-wifi-socketgetsockname"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_SocketGetSockName"
summary: "The function ARM_WIFI_SocketGetSockName retrieves the local IP address and port for a socket."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_SocketGetSockName (int32_t socket, uint8_t *ip, uint32_t *ip_len, uint16_t *port)
```


The function **ARM_WIFI_SocketGetSockName** retrieves the local IP address and port for a socket.

The argument **socket** specifies a socket identification number returned from a previous call
to ARM_WIFI_SocketCreate.

The argument **ip** is a pointer to the buffer that will receive the local IP address.
If the **ip** is `NULL`, the local IP address is not returned.

The argument **ip_len** is a pointer to the IP address length. It should initially contain the amount of
space pointed to by **ip.** On return it contains the actual length of the address returned in bytes.

The argument **port** is a pointer to the buffer, that will receive the local port number.
If the **port** is `NULL`, the local port number is not returned.

**Example:**
```
static uint8_t  local_ip[4];    // Socket address and port
static uint16_t local_port;
 
static void get_socket_local_info (void) {
  uint32_t ip_len;
 
  ip_len = sizeof(local_ip);
  wifi->SocketGetSockName (sock, (uint8_t *)local_ip, &ip_len, &local_port);
}
```
