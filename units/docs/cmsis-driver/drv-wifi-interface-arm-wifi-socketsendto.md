---
id: "drv-wifi-interface-arm-wifi-socketsendto"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_SocketSendTo"
summary: "The function ARM_WIFI_SocketSendTo is used to send data. It is normally used to send messages on a datagram sockets, but can also be used to send data on a connected stream sockets."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_SocketSendTo (int32_t socket, const void *buf, uint32_t len, const uint8_t *ip, uint32_t ip_len, uint16_t port)
```


The function **ARM_WIFI_SocketSendTo** is used to send data. It is normally used to send messages
on a datagram sockets, but can also be used to send data on a connected stream sockets.

If the datagram socket is not yet bound, the system implicitly binds to a random dynamic port.

The argument **socket** specifies a socket identification number returned from a previous call
to ARM_WIFI_SocketCreate.

The argument _buf_ is a pointer to the application data buffer containing data to transmit. The buffer
data length is not limited in size. If the data length is too large for one packet, the **ARM_WIFI_SocketSend** function
will fragment the data and send it in several successive data packets:
- In blocking mode, which is enabled by default, this function returns after the data has been successfully queued for transmission.
- In non blocking mode, the function returns immediately without blocking the system.

The argument _len_ specifies the length of data in bytes.

The argument **ip** is a pointer to the buffer containing the IP address octets of the endpoint node.

The argument **ip_len** specifies the length of the IP address. The length is `4` bytes
for the IPv4 address and `16` bytes for the IPv6 address.

The argument **port** specifies the port of the endpoint node. If the argument **port** is `0`, 
the function returns error, because this port is reserved.

For the stream sockets, arguments **ip,** **ip_len** and **port** are ignored.

Return value, when positive, represents the number of bytes sent, which can be less than _len._

**Note:**
The function can also be used to check if the socket is ready to send data by specifying `0` 
for argument **len** (arguments **buf,** **ip,** **ip_len** and **port** are ignored).
The function returns `0` if the socket is writable or error code otherwise.

**Example:**
 - see ARM_WIFI_SocketRecvFrom
