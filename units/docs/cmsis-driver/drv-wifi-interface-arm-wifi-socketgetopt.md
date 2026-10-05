---
id: "drv-wifi-interface-arm-wifi-socketgetopt"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_SocketGetOpt"
summary: "The function ARMWIFISocketGetOpt retrieves options for a socket."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_SocketGetOpt (int32_t socket, int32_t opt_id, void *opt_val, uint32_t *opt_len)
```


The function **ARM_WIFI_SocketGetOpt** retrieves options for a socket.

The argument **socket** specifies a socket identification number returned from a previous call
to ARM_WIFI_SocketCreate.

The argument **opt_id** is the socket option for which the value is to be retrieved. The following
socket options are supported:
Option                       | Description
:----------------------------|:-------------------------------------------------
ARM_SOCKET_SO_RCVTIMEO  | Timeout for receiving in blocking mode
ARM_SOCKET_SO_SNDTIMEO  | Timeout for sending in blocking mode
ARM_SOCKET_SO_KEEPALIVE | Keep-alive mode for the stream socket
ARM_SOCKET_SO_TYPE      | Type of the socket (stream or datagram)

The argument **opt_val** points to the buffer that will receive the value of the **opt_id.**

The argument **opt_len** contains the length of the buffer at the input and returns the length
of the option information on the output.

**Example:**
```
uint32_t type;
 
wifi->SocketGetOpt (sock, ARM_SOCKET_SO_TYPE, &type, sizeof(type));
if (type == ARM_SOCKET_SOCK_STREAM) {
  // Stream socket
}
if (type == ARM_SOCKET_SOCK_DGRAM) {
  // Datagram socket
}
```
