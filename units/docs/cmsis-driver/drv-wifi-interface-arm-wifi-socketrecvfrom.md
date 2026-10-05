---
id: "drv-wifi-interface-arm-wifi-socketrecvfrom"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_SocketRecvFrom"
summary: "The function ARMWIFISocketRecvFrom is used to receive data that has been queued for a socket."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_SocketRecvFrom (int32_t socket, void *buf, uint32_t len, uint8_t *ip, uint32_t *ip_len, uint16_t *port)
```


The function **ARM_WIFI_SocketRecvFrom** is used to receive data that has been queued for a socket.
It is normally used to receive messages on datagram sockets, but can also be used to receive a reliable,
ordered stream of data on a connected stream sockets. It reads as much information as currently available
up to the size of the buffer specified.

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

The argument **ip** is a pointer to the buffer that will receive the IP address of the sender.
If the **ip** is `NULL`, the IP address is not returned.

The argument **ip_len** is a pointer to the IP address length. It should initially contain the amount of
space pointed to by **ip.** On return it contains the actual length of the address returned in bytes.

The argument **port** is a pointer to the buffer, that will receive the port number of the sender.
If the **port** is `NULL`, the port number is not returned.

**Note:**
The function can also be used to check if the socket has data available to read by specifying `0`
for argument **len** (arguments **buf,** **ip,** **ip_len** and **port** are ignored).
The function returns `0` if data is available or error code otherwise.
In blocking mode, the function waits until data is available, in non blocking mode the function returns instantly.

**Example:**
```
extern ARM_DRIVER_WIFI Driver_WiFi0;
static ARM_DRIVER_WIFI *wifi;
 
void Echo_Server_Thread (void *arg) {
  uint8_t ip[4];
  uint16_t port;
  int32_t sock, res;
  uint32_t ip_len;
  char dbuf[120];
 
  while (1) {
    wifi = &Driver_WiFi0;
    sock = wifi->SocketCreate (ARM_SOCKET_AF_INET, ARM_SOCKET_SOCK_DGRAM, ARM_SOCKET_IPPROTO_UDP);
 
    ip[0] = 0U;                 // Unspecified address
    ip[1] = 0U;
    ip[2] = 0U;
    ip[3] = 0U;
    port  = 7U;                 // Standard port for Echo service
 
    wifi->SocketBind (sock, (uint8_t *)ip, sizeof(ip), port);
 
    while (1) {
      ip_len = sizeof(ip);
      res = wifi->SocketRecvFrom (sock, dbuf, sizeof(dbuf), (uint8_t *)ip, &ip_len, &port);
      if (res < 0) {
        break;                  // Error occurred
      }
      if (res > 0) {            // Echo the data
        wifi->SocketSendTo (sock, dbuf, res, (uint8_t *)ip, ip_len, port);
      }    
    }
    wifi->SocketClose (sock);
  }
}
```
