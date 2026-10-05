---
id: "txmw-chapter-3-functional-components-of-tcp-ip-offload"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: TCP/IP Offload"
summary: "This feature enables NetX Duo to support network interface card that offers TCP/IP service on the hardware."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#tcp-ip-offload"
license: "MIT"
mode: "V"
---

This feature enables NetX Duo to support network interface card that offers TCP/IP service on the hardware. Certain WiFi modules offer TCP/IP processing on the module, and the applications on MCU send and receive packets through APIs to access its TCP/IP stack. With this feature enabled, developers can run native NetX Duo applications directly.

To enable TCP/IP offload feature, NetX Duo must be built with `NX_ENABLE_TCPIP_OFFLOAD` and `NX_ENABLE_INTERFACE_CAPABILITY` defined.

### TCP/IP Offload Handler
NetX Duo communicates with network driver through a callback function to handle TCP or UDP socket operations. The callback function is defined in the `NX_INTERFACE_STRUCT`. Network driver needs to set the TCP/IP callback function during `NX_LINK_ENABLE` driver command. The prototype of TCP/IP callback function is as below.

``` C
UINT (*nx_interface_tcpip_offload_handler)(struct NX_IP_STRUCT *ip_ptr,
                                           struct NX_INTERFACE_STRUCT *interface_ptr,
                                           VOID *socket_ptr, UINT operation, NX_PACKET *packet_ptr,
                                           NXD_ADDRESS *local_ip, NXD_ADDRESS *remote_ip,
                                           UINT local_port, UINT *remote_port, UINT wait_option);
```
Description of parameters.
* `ip_ptr` - Pointer to IP instance
* `interface_ptr` - Pointer to interface
* `socket_ptr` - Pointer to `NX_TCP_SOCKET` or `NX_UDP_SOCKET`, depends on the value of `operation`
* `operation` - Operation of current function call. Values are defined as below
``` C
#define NX_TCPIP_OFFLOAD_TCP_CLIENT_SOCKET_CONNECT  0
#define NX_TCPIP_OFFLOAD_TCP_SERVER_SOCKET_LISTEN   1
#define NX_TCPIP_OFFLOAD_TCP_SERVER_SOCKET_ACCEPT   2
#define NX_TCPIP_OFFLOAD_TCP_SERVER_SOCKET_UNLISTEN 3
#define NX_TCPIP_OFFLOAD_TCP_SOCKET_DISCONNECT      4
#define NX_TCPIP_OFFLOAD_TCP_SOCKET_SEND            5
#define NX_TCPIP_OFFLOAD_UDP_SOCKET_BIND            6
#define NX_TCPIP_OFFLOAD_UDP_SOCKET_UNBIND          7
#define NX_TCPIP_OFFLOAD_UDP_SOCKET_SEND            8
```
* `packet_ptr` - Pointer to packet. The value is set when `operation` is `TCP_SOCKET_SEND` or `UDP_SOCKET_SEND`
* `local_ip` - Pointer to local IP address. The value is set when `operation` is `UDP_SOCKET_SEND`
* `remote_ip` - Pointer to remote IP address. The value is set when `operation` is `TCP_CLIENT_SOCKET_CONNECT` or `UDP_SOCKET_SEND`. When the operation is `TCP_SERVER_SOCKET_ACCEPT`, this value must be returned by callback function
* `local_port` - Local port. The value is set when `operation` is `TCP_CLIENT_SOCKET_CONNECT`, `TCP_SERVER_SOCKET_LISTEN`, `TCP_SERVER_SOCKET_ACCEPT`, `TCP_SERVER_SOCKET_UNLISTEN` or UDP
* `remote_port` - Remote port. The value is set when `operation` is `TCP_CLIENT_SOCKET_CONNECT` or `UDP_SOCKET_SEND`. When the operation is `TCP_SERVER_SOCKET_ACCEPT`, this value must be returned by callback function
* `wait_option` - Wait option in ticks. The value is set for all operations

### TCP/IP Offload Context
A pointer is added to `NX_TCP_SOCKET` structure to be used by TCP/IP offload driver.
```
typedef struct NX_TCP_SOCKET_STRUCT
{
    // ...

    /* This pointer is designed to be accessed by TCP/IP offload directly.  */
    VOID *nx_tcp_socket_tcpip_offload_context;
} NX_TCP_SOCKET;
```

A pointer is added to `NX_UDP_SOCKET` structure to be used by TCP/IP offload driver.
```
typedef struct NX_UDP_SOCKET_STRUCT
{
    // ...

    /* This pointer is designed to be accessed by TCP/IP offload directly.  */
    VOID *nx_udp_socket_tcpip_offload_context;
} NX_UDP_SOCKET;
```

### APIs for TCP/IP Offload Network Driver
``` C
/* Invoked when TCP packet is receive or connection error.  */
VOID _nx_tcp_socket_driver_packet_receive(NX_TCP_SOCKET *socket_ptr, NX_PACKET *packet_ptr);

/* Invoked when TCP connection is establish.  */
UINT _nx_tcp_socket_driver_establish(NX_TCP_SOCKET *socket_ptr, NX_INTERFACE *interface_ptr, UINT remote_port);

/* Invoked when UDP packet is receive.  */
VOID _nx_udp_socket_driver_packet_receive(NX_UDP_SOCKET *socket_ptr, NX_PACKET *packet_ptr,
                                          NXD_ADDRESS *local_ip, NXD_ADDRESS *remote_ip, UINT remote_port);
```
### TCP/IP Offload Driver
A driver function is needed for each IP interface. Refer to [Chapter 5](https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#tcpip-offload-driver-guidance) for more details on how to develop NetX Duo driver functions.

### TCP/IP Offload Known Limitations
- Only TCP and UDP sockets are supported
- DHCP is usually done by underlayer TCP/IP stack not NetX Duo
- Other limitations from underlayer TCP/IP stack
