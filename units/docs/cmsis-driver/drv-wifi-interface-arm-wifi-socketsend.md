---
id: "drv-wifi-interface-arm-wifi-socketsend"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_SocketSend"
summary: "The function ARM_WIFI_SocketSend is used to send data on an already connected socket. This function is normally used to send a reliable, ordered stream of data bytes on a stream sockets."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_SocketSend (int32_t socket, const void *buf, uint32_t len)
```


The function **ARM_WIFI_SocketSend** is used to send data on an already connected socket. This function is
normally used to send a reliable, ordered stream of data bytes on a stream sockets. It can also be used
to send messages on datagram sockets.

The argument **socket** specifies a socket identification number returned from a previous call
to ARM_WIFI_SocketCreate.

The argument _buf_ is a pointer to the application data buffer containing data to transmit. The buffer
data length is not limited in size. If the data length is too large for one packet, the **ARM_WIFI_SocketSend** function
will fragment the data and send it in several successive data packets:
- In blocking mode, which is enabled by default, this function returns after the data has been successfully queued for transmission.
- In non blocking mode, the function returns immediately without blocking the system.

The argument _len_ specifies the length of data in bytes.

Return value, when positive, represents the number of bytes sent, which can be less than _len._

**Note:**
The function can also be used to check if the socket is ready to send data by specifying `0` 
for argument **len** (argument **buf** is ignored).
The function returns `0` if the socket is writable or error code otherwise.

**Example:**
 - see ARM_WIFI_SocketListen
