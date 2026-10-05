---
id: "drv-wifi-interface-arm-wifi-socketgetpeername"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_SocketGetPeerName"
summary: "The function ARMWIFISocketGetPeerName retrieves the IP address and port of the peer to which a socket is connected."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_SocketGetPeerName (int32_t socket, uint8_t *ip, uint32_t *ip_len, uint16_t *port)
```


The function **ARM_WIFI_SocketGetPeerName** retrieves the IP address and port of the peer to which
a socket is connected.

The argument **socket** specifies a socket identification number returned from a previous call
to ARM_WIFI_SocketCreate.

The argument **ip** is a pointer to the buffer that will receive the IP address of the peer.
If the **ip** is `NULL`, the IP address is not returned.

The argument **ip_len** is a pointer to the IP address length. It should initially contain the amount of
space pointed to by **ip.** On return it contains the actual length of the address returned in bytes.

The argument **port** is a pointer to the buffer, that will receive the port number of the peer.
If the **port** is `NULL`, the port number is not returned.

**Example:**
```
static uint8_t  peer_ip[4];    // Socket address and port
static uint16_t peer_port;
 
static void get_socket_peer_info (void) {
  uint32_t ip_len;
 
  ip_len = sizeof(peer_ip);
  wifi->SocketGetPeerName (sock, (uint8_t *)peer_ip, &ip_len, &peer_port);
}
```
