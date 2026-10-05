---
id: "drv-wifi-socket-type-definitions"
type: "concept"
domain: "drivers"
title: "WiFi Socket Type definitions"
summary: "WiFi Socket Type definitions. The WiFi Socket Type specifies the type of the WiFi socket."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

WiFi Socket Type definitions.
 The WiFi Socket Type specifies the type of the WiFi socket.

### ARM_SOCKET_SOCK_STREAM

```c
ARM_SOCKET_SOCK_STREAM
```

 Stream Socket is connection-oriented, sequenced and reliable, implemented on top of the TCP protocol.

### ARM_SOCKET_SOCK_DGRAM

```c
ARM_SOCKET_SOCK_DGRAM
```

 Datagram Socket is connectionless, unreliable, using the UDP protocol.
