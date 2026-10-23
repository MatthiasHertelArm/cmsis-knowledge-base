---
id: "drv-wifi-socket-option-definitions"
type: "concept"
domain: "drivers"
title: "WiFi Socket Option definitions"
summary: "WiFi Socket Option definitions. The WiFi Socket Option specifies the socket option for which the value is to be set or obtained."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

WiFi Socket Option definitions.
 The WiFi Socket Option specifies the socket option for which the value is to be set or obtained.

### ARM_SOCKET_IO_FIONBIO

```c
ARM_SOCKET_IO_FIONBIO
```

 Enables or disables the non-blocking mode for the WiFi socket.
\sa wifi_soc_opt

### ARM_SOCKET_SO_RCVTIMEO

```c
ARM_SOCKET_SO_RCVTIMEO
```

 Specifies the time limit for receiving in blocking mode. The time limit is in milliseconds.
\sa wifi_soc_opt

### ARM_SOCKET_SO_SNDTIMEO

```c
ARM_SOCKET_SO_SNDTIMEO
```

 Specifies the time limit for sending in blocking mode. The time limit is in milliseconds.
\sa wifi_soc_opt

### ARM_SOCKET_SO_KEEPALIVE

```c
ARM_SOCKET_SO_KEEPALIVE
```

 Enables or disables the keep-alive mode for the stream socket.
\sa wifi_soc_opt

### ARM_SOCKET_SO_TYPE

```c
ARM_SOCKET_SO_TYPE
```

 Obtains the type of the Wifi socket.
\sa wifi_soc_opt
