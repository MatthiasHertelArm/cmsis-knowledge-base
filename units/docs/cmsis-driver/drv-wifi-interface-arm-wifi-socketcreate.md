---
id: "drv-wifi-interface-arm-wifi-socketcreate"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_SocketCreate"
summary: "The function ARM_WIFI_SocketCreate creates a communication endpoint called a socket."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_SocketCreate (int32_t af, int32_t type, int32_t protocol)
```


The function **ARM_WIFI_SocketCreate** creates a communication endpoint called a socket.

The argument **af** specifies the address family. The following values are supported:
Family                       | Description
:----------------------------|:-------------------------------------------------
ARM_SOCKET_AF_INET      | Address Family Internet
ARM_SOCKET_AF_INET6     | Address Family Internet version 6

The argument **type** specifies the communication semantics. The following are the currently supported types:
Type                         | Description
:----------------------------|:-------------------------------------------------
ARM_SOCKET_SOCK_STREAM  | Provides a reliable connection based data stream that is full-duplex
ARM_SOCKET_SOCK_DGRAM   | Provides connectionless communication that is unreliable

The argument **protocol** specifies the protocol that must be used with the socket type:
Protocol                     | Description
:----------------------------|:-------------------------------------------------
ARM_SOCKET_IPPROTO_TCP  | Must be used with ARM_SOCKET_SOCK_STREAM socket type
ARM_SOCKET_IPPROTO_UDP  | Must be used with ARM_SOCKET_SOCK_DGRAM socket type
`0`                    | The system selects a matching protocol for the socket type

**Example:**
 - see ARM_WIFI_SocketListen, ARM_WIFI_SocketConnect
