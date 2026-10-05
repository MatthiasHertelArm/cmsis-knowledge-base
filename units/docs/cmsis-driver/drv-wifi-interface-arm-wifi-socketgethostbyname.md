---
id: "drv-wifi-interface-arm-wifi-socketgethostbyname"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_SocketGetHostByName"
summary: "The function ARMWIFISocketGetHostByName retrieves host information corresponding to a host name from a host database. It does this by sending DNS requests to the DNS server."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_SocketGetHostByName (const char *name, int32_t af, uint8_t *ip, uint32_t *ip_len)
```


The function **ARM_WIFI_SocketGetHostByName** retrieves host information corresponding to
a host name from a host database. It does this by sending DNS requests to the DNS server.
The IP address of the DNS server is specified in the network interface configuration or can be
obtained from the DHCP server for the local area network.

The argument _name_ is a pointer to the `null`-terminated name of the host to resolve.

The argument **af** specifies the address family, that is, which type of IP address you want
to resolve. The following values are supported:
Family                       | Description
:----------------------------|:-------------------------------------------------
ARM_SOCKET_AF_INET      | Resolve the IPv4 address
ARM_SOCKET_AF_INET6     | Resolve the IPv6 address

The argument **ip** is a pointer to the buffer that will receive the resolved IP address of the host.
If the argument **ip** is `NULL`, the function returns error.

The argument **ip_len** is a pointer to the IP address length. It should initially contain the amount of
space pointed to by **ip.** On return it contains the actual length of the address returned in bytes.

**Example:**
```
extern ARM_DRIVER_WIFI Driver_WiFi0;
static ARM_DRIVER_WIFI *wifi;
 
void ping_arm_com (void) {
  uint8_t ip[4];
  uint32_t ip_len;
  int32_t res;
 
  wifi = &Driver_WiFi0;
  ip_len = sizeof(ip);
  res = wifi->SocketGetHostByName ("www.arm.com", ARM_SOCKET_AF_INET, (uint8_t *)ip, &ip_len);
  if (res == ARM_DRIVER_OK) {
    res = wifi->Ping ((uint8_t *)ip, sizeof(ip));
    if (res == ARM_DRIVER_OK) {
      // "www.arm.com" responded to ping  
    }
  }
  else {
    // "www.arm.com" not resolved
  }
}
```
