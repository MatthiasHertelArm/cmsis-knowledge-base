---
id: "drv-wifi-interface-arm-wifi-socketrecv"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_SocketRecv"
summary: "The function ARM_WIFI_SocketRecv receives incoming data that has been queued for the socket. You can use this function with both, the stream and the datagram socket."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_SocketRecv (int32_t socket, void *buf, uint32_t len)
```


The function **ARM_WIFI_SocketRecv** receives incoming data that has been queued for the socket.
You can use this function with both, the stream and the datagram socket. It reads as much
information as currently available up to the size of the buffer specified.

In blocking mode, which is enabled by default, this function waits for received data. In non
blocking mode, you must call the **ARM_WIFI_SocketRecv** function again if the error code 
`ARM_SOCKET_EAGAIN` is returned.

The argument **socket** specifies a socket identification number returned from a previous call
to ARM_WIFI_SocketCreate.

The argument **buf** is a pointer to the application data buffer for storing the data to.
If the available data is too large to fit in the supplied application buffer **buf,** excess bytes
are discarded in case of a datagram sockets. For stream sockets, the data is buffered internally
so the application can retrieve all data by multiple calls of **ARM_WIFI_SocketRecv** function.

The argument **len** specifies the size of the application data buffer.

**Note:**
The function can also be used to check if the socket has data available to read by specifying `0`
for argument **len** (argument **buf** is ignored).
The function returns `0` if data is available or error code otherwise.
In blocking mode, the function waits until data is available, in non blocking mode the function returns instantly.


**Example:**
 - see ARM_WIFI_SocketListen
