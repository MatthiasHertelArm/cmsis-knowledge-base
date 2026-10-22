---
id: "drv-wifi-interface-arm-wifi-socketaccept"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_SocketAccept"
summary: "The function ARM_WIFI_SocketAccept accepts a connection request queued for a listening socket. If a connection request is pending, ARM_WIFI_SocketAccept removes the request from the queue, and creates a new socket for the connection."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_SocketAccept (int32_t socket, uint8_t *ip, uint32_t *ip_len, uint16_t *port)
```


The function **ARM_WIFI_SocketAccept** accepts a connection request queued for a listening socket.
If a connection request is pending, **ARM_WIFI_SocketAccept** removes the request from the queue,
and creates a new socket for the connection. The original listening socket remains open and continues
to queue new connection requests. The **socket** must be a socket of type **ARM_SOCKET_SOCK_STREAM.**

In blocking mode, which is enabled by default, this function waits for a connection request. In
non blocking mode, you must call the **ARM_WIFI_SocketAccept** function again if the error code
`ARM_SOCKET_EAGAIN` is returned.

The argument **socket** specifies a socket identification number returned from a previous call
to ARM_WIFI_SocketCreate.

The argument **ip** is a pointer to the buffer that will receive the IP address of the connection node.
If the **ip** is `NULL`, the IP address is not returned.

The argument **ip_len** is a pointer to the IP address length. It should initially contain the amount of
space pointed to by **ip.** On return it contains the actual length of the address returned in bytes.

The argument **port** is a pointer to the buffer, that will receive the port number of the connection node.
If the **port** is `NULL`, the port number is not returned.

**Example:**
 - see ARM_WIFI_SocketListen
