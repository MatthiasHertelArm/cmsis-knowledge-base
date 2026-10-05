---
id: "drv-wifi-interface-arm-wifi-socketsetopt"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_SocketSetOpt"
summary: "The function ARM_WIFI_SocketSetOpt sets options for a socket."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_SocketSetOpt (int32_t socket, int32_t opt_id, const void *opt_val, uint32_t opt_len)
```


The function **ARM_WIFI_SocketSetOpt** sets options for a socket.

The argument **socket** specifies a socket identification number returned from a previous call
to ARM_WIFI_SocketCreate.

The argument **opt_id** is the socket option for which the value is to be set. The following
socket options are supported:
Option                       | Description
:----------------------------|:-------------------------------------------------
ARM_SOCKET_IO_FIONBIO   | Non-blocking mode for the socket
ARM_SOCKET_SO_RCVTIMEO  | Timeout for receiving in blocking mode
ARM_SOCKET_SO_SNDTIMEO  | Timeout for sending in blocking mode
ARM_SOCKET_SO_KEEPALIVE | Keep-alive mode for the stream socket

The argument **opt_val** points to the buffer containing the value of the **opt_id.**

The argument **opt_len** tells the exact length of the option.
 
**Example:**
```
uint32_t nonblocking = 0U;    // Blocking mode
uint32_t timeout = 10000U;    // Timeout 10 seconds
 
wifi->SocketSetOpt (sock, ARM_SOCKET_IO_FIONBIO, &nonblocking, sizeof(nonblocking));
wifi->SocketSetOpt (sock, ARM_SOCKET_SO_RCVTIMEO, &timeout, sizeof(timeout)); 
wifi->SocketSetOpt (sock, ARM_SOCKET_SO_SNDTIMEO, &timeout, sizeof(timeout));
```
