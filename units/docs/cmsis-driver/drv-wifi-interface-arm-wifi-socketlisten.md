---
id: "drv-wifi-interface-arm-wifi-socketlisten"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_SocketListen"
summary: "The function ARM_WIFI_SocketListen sets the specified socket to listening mode, that is to the server mode of operation. Before calling the ARM_WIFI_SocketListen function, the ARM_WIFI_SocketBind function must be called."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_SocketListen (int32_t socket, int32_t backlog)
```


The function **ARM_WIFI_SocketListen** sets the specified socket to listening mode, that is to the
server mode of operation. Before calling the **ARM_WIFI_SocketListen** function, the ARM_WIFI_SocketBind
function must be called.

The argument **socket** specifies a socket identification number returned from a previous call
to ARM_WIFI_SocketCreate.

The argument **backlog** specifies a maximum number of connection requests that can be queued.
 
**Example:**
```
extern ARM_DRIVER_WIFI Driver_WiFi0;
static ARM_DRIVER_WIFI *wifi;
 
void Echo_Server_Thread (void *arg) {
  uint8_t ip[4] = { 0U, 0U, 0U, 0U };
  int32_t sock, sd, res;
  char dbuf[120];
 
  while (1) {
    wifi = &Driver_WiFi0;
    sock = wifi->SocketCreate (ARM_SOCKET_AF_INET, ARM_SOCKET_SOCK_STREAM, ARM_SOCKET_IPPROTO_TCP);
 
    wifi->SocketBind (sock, (uint8_t *)ip, sizeof(ip), 7U);
    wifi->SocketListen (sock, 1);
    sd = wifi->SocketAccept (sock, NULL, NULL, NULL);
    wifi->SocketClose (sock);
    sock = sd;
 
    while (1) {
      res = wifi->SocketRecv (sock, dbuf, sizeof(dbuf));
      if (res < 0) {
        break;                                      // Error occurred
      }
      if (res > 0) {
        wifi->SocketSend (sock, dbuf, res);         // Echo the data
      }
    }
    wifi->SocketClose (sock);
  }
}
```
