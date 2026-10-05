---
id: "txmw-chapter-5-netx-duo-network-drivers-tcp-ip-offload-driver-guidance"
type: "concept"
domain: "rtos"
title: "Chapter 5 - NetX Duo Network Drivers: TCP/IP Offload Driver Guidance"
summary: "For TCP/IP offload feature, a driver function is needed for each IP interface. Here is a list of additional tasks for network driver."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter5.md#tcp-ip-offload-driver-guidance"
license: "MIT"
mode: "V"
---

For TCP/IP offload feature, a driver function is needed for each IP interface. Here is a list of additional tasks for network driver.

* For command `NX_LINK_INITIALIZE`,
  * Create a driver thread to handle TCP/IP offload receive events.
* For command `NX_LINK_INTERFACE_ATTACH`,
  * Set the capability of to driver interface. See sample code below.
``` C
driver_req_ptr -> nx_ip_driver_interface -> nx_interface_capability_flag = NX_INTERFACE_CAPABILITY_TCPIP_OFFLOAD;
```
* For command `NX_LINK_ENABLE`,
  * Start the driver thread.
  * Set TCP/IP callback function to driver interface. See sample code below.
``` C
driver_req_ptr -> nx_ip_driver_interface -> nx_interface_tcpip_offload_handler = _nx_driver_tcpip_handler;
```
* For command `NX_LINK_DISABLE`,
  * Stop the driver thread
  * Clear TCP/IP callback function of driver interface.
* For command `NX_LINK_UNINITIALIZE`,
  * Delete the driver thread

### TCP/IP Offload Driver Thread
The purpose of driver thread is to receive incoming TCP or UDP packets. In driver thread, there is typically a while loop to check whether there is incoming TCP or UDP packet available or connection established. When data are available, pass the TCP or UDP packet to NetX Duo. The room between `nx_packet_data_start` and `nx_packet_prepend_ptr` must be sufficient to insert TCP/IP header. For TCP socket, allocate packet with type `NX_TCP_PACKET`. For UDP socket, allocate packet with type `NX_UDP_PACKET`. Fill in incoming data from `nx_packet_append_ptr` to `nx_packet_data_end`. The data in `nx_packet_append_ptr` must contain TCP or UDP payload only. TCP/IP header **MUST** not be filled in packet. Adjust the packet length and set receive interface, then call `_nx_tcp_socket_driver_packet_receive` for TCP packet and `_nx_udp_socket_driver_packet_receive` for UDP packet. If a TCP connection is shutdown, call `_nx_tcp_socket_driver_packet_receive` with packet set to NULL. When connection is established, call `_nx_tcp_socket_driver_establish`.

### TCP/IP Offload Driver Handler
The following driver commands are required for network interfaces with TCP/IP services. 
* For operation `NX_TCPIP_OFFLOAD_TCP_CLIENT_SOCKET_CONNECT`,
  * Allocate resource if needed.
  * Bind to local TCP port and connect to server.
  * Return success on connection established. When the connection is in progress, return `NX_IN_PROGRESS`. Or else, return failure.
* For operation `NX_TCPIP_OFFLOAD_TCP_SERVER_SOCKET_LISTEN`,
  * Check for duplicate listen first. It can be called multiple time on same port. First time from `nx_tcp_server_socket_listen` and then `nx_tcp_server_socket_relisten`.
  * Allocate resource if needed.
  * Listen to local TCP port.
* For operation `NX_TCPIP_OFFLOAD_TCP_SERVER_SOCKET_ACCEPT`,
  * Allocate resource if needed.
  * Accept connection.
* For operation `NX_TCPIP_OFFLOAD_TCP_SERVER_SOCKET_UNLISTEN`,
  * Find TCP socket listening on local port.
  * Close the listening socket if found.
* For operation `NX_TCPIP_OFFLOAD_TCP_SOCKET_DISCONNECT`,
  * Close the TCP/IP offload connection.
  * Unbind local TCP port.
  * Cleanup resources created during connect.
* For operation `NX_TCPIP_OFFLOAD_TCP_SOCKET_SEND`,
  * Send data through TCP/IP offload. Be prepare to handle packet length larger than MSS or packet chain situation.
* For operation `NX_TCPIP_OFFLOAD_UDP_SOCKET_BIND`,
  * Allocate resource if needed.
  * Bind to local UDP port.
* For operation `NX_TCPIP_OFFLOAD_UDP_SOCKET_UNBIND`,
  * Unbind local UDP port.
  * Cleanup resources created during bind.
* For operation `NX_TCPIP_OFFLOAD_UDP_SOCKET_SEND`,
  * Send data through TCP/IP offload. Be prepare to handle packet length larger than MTU or packet chain situation.
