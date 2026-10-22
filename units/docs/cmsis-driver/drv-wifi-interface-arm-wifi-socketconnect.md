---
id: "drv-wifi-interface-arm-wifi-socketconnect"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_SocketConnect"
summary: "The function ARM_WIFI_SocketConnect assigns the address of the peer communication endpoint. The function behaves differently according to the type of socket:"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_SocketConnect (int32_t socket, const uint8_t *ip, uint32_t ip_len, uint16_t port)
```


The function **ARM_WIFI_SocketConnect** assigns the address of the peer communication endpoint. The function
behaves differently according to the type of socket:

- **ARM_SOCKET_SOCK_STREAM:** A connection is established between the endpoints.

  In blocking mode, which is enabled by default, this function waits for a connection to be established.

  In non blocking mode, the function returns the error code `ARM_SOCKET_EINPROGRESS` and the connection
  is established asynchronously. Subsequent calls to **ARM_WIFI_SocketConnect** for the same socket,
  before the connection is established, return the error code `ARM_SOCKET_EALREADY.`  When the connection
  is established, the call to **ARM_WIFI_SocketConnect** returns the error code `ARM_SOCKET_EISCONN.` 

- **ARM_SOCKET_SOCK_DGRAM:** An address filter is established between the endpoints.

  The address filter is changed with another **ARM_WIFI_SocketConnect** function call. If the socket
  is not yet bound, the system implicitly binds to a random dynamic port.

The argument **socket** specifies a socket identification number returned from a previous call
to ARM_WIFI_SocketCreate.

The argument **ip** is a pointer to the buffer containing the IP address octets of the endpoint node.

The argument **ip_len** specifies the length of the IP address. The length is `4` bytes
for the IPv4 address and `16` bytes for the IPv6 address.

The argument **port** specifies the port of the endpoint node. If the argument **port** is `0`, 
the function returns error, because this port is reserved.

**Example:**
```
extern ARM_DRIVER_WIFI Driver_WiFi0;
static ARM_DRIVER_WIFI *wifi;
 
static const char message[] = { "The quick brown fox jumps over the lazy dog." };
  
void Echo_Client_Thread (void *arg) {
  uint8_t ip[4] = { 192U, 168U, 0U, 100U };
  int32_t sock, res;
  char dbuf[120];
 
  while (1) {
    wifi = &Driver_WiFi0;
    sock = wifi->SocketCreate (ARM_SOCKET_AF_INET, ARM_SOCKET_SOCK_STREAM, ARM_SOCKET_IPPROTO_TCP);
 
    res = wifi->SocketConnect (sock, (uint8_t *)ip, sizeof(ip), 7U);
    if (res == 0) {
      wifi->SocketSend (sock, message, sizeof(message));
      res = wifi->SocketRecv (sock, dbuf, sizeof(dbuf));
      if (res < 0) {
        break;               // Error occurred
      }
      if (res > 0) {
        if (memcmp (dbuf, message, res) != 0) {
          // error handling, message is not the same as sent
        }
      }    
    }
    wifi->SocketClose (sock);
    osDelay (1000U);
  }
}
```
