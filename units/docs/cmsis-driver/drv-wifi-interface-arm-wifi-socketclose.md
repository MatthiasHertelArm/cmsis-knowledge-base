---
id: "drv-wifi-interface-arm-wifi-socketclose"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_SocketClose"
summary: "The function ARM_WIFI_SocketClose closes an existing socket and releases the socket descriptor. Further references to socket fail with ARM_SOCKET_EINVAL error code."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_SocketClose (int32_t socket)
```


The function **ARM_WIFI_SocketClose** closes an existing socket and releases the socket descriptor.
Further references to **socket** fail with `ARM_SOCKET_EINVAL` error code.

The argument **socket** specifies a socket identification number returned from a previous call
to ARM_WIFI_SocketCreate.

In blocking mode, which is enabled by default, this function will wait until a socket is closed.
In non blocking mode, you must call the **ARM_WIFI_SocketClose** function again if the error code
`ARM_SOCKET_EAGAIN` is returned.

**Example:**
 - see ARM_WIFI_SocketListen
