---
id: "txmw-chapter-3-functional-components-of-user-datagram-protocol-udp"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: User Datagram Protocol (UDP)"
summary: "The User Datagram Protocol (UDP) provides the simplest form of data transfer between network members (RFC 768)."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#user-datagram-protocol-udp"
license: "MIT"
mode: "V"
---

The User Datagram Protocol (UDP) provides the simplest form of data transfer between network members (RFC 768). UDP data packets are sent from one network member to another in a best effort fashion; i.e., there is no built-in mechanism for acknowledgement by the packet recipient. In addition, sending a UDP packet does not require any connection to be established in advance. Because of this, UDP packet transmission is very efficient.

For developers migrating their NetX applications to NetX Duo there are only a few basic changes in UDP functionality between NetX and NetX Duo. This is because IPv6 is primarily concerned with the underlying
IP layer. All NetX Duo UDP services can be used for either IPv4 or IPv6 connectivity.

### UDP Header       
UDP places a simple packet header in front of the application's data on transmission, and removes a 
similar UDP header from the packet on reception before delivering a received UDP packet to the application. UDP utilizes the IP protocol for sending and receiving packets, which means there is an IP header in front of the UDP header when the packet is on the network. Figure 12 shows the format of the
UDP header.

(figure: Diagram of the UDP header format.)

**FIGURE 12. UDP Header**

> **Note:** *All headers in the UDP/IP implementation are expected to be in **big endian** format. In this format, the most significant byte of the word resides at the lowest byte address.*

The following describes the UDP header format:

|Header Field |Purpose |
|---|---|
|**16-bit source port number** |This field contains the port on which the UDP packet is being sent from. Valid UDP ports range from 1 through 0xFFFF. |
|**16-bit destination port number** |This field contains the UDP port to which the packet is being sent to. Valid UDP ports range from 1 through 0xFFFF. |
|**16-bit UDP length** |This field contains the number of bytes in the UDP packet, including the size of the UDP header. |
|**16-bit UDP checksum** |This field contains the 16-bit checksum for the packet, including the UDP header, the packet data area, and the pseudo IP header. |

### UDP Enable   
Before UDP packet transmission is possible, the application must first enable UDP by calling the ***nx_udp_enable*** service. After enabled, the application is free to send and receive UDP packets.  

### UDP Socket Create    
UDP sockets are created either during initialization or during runtime by application threads. The initial type of service, time to live, and receive queue depth are defined by the ***nx_udp_socket_create*** service. There are no limits on the number of UDP sockets in an application.

### UDP Checksum   
IPv6 protocol requires a UDP header checksum computation on packet data, whereas in the IPv4 protocol it is optional.  

UDP specifies a one's complement 16-bit checksum that covers the IP pseudo header (consisting of the source IP address, destination IP address, and the protocol/length IP word), the UDP header, and the UDP packet data. The only differences between IPv4 and IPv6 UDP packet header checksums is that the source and destination IP addresses are 32 bit in IPv4 while in IPv6 they are 128 bit. If the calculated UDP checksum is 0, it is stored as all ones (0xFFFF). If the sending socket has the UDP checksum logic disabled, a zero is placed in the UDP checksum field to indicate the checksum was not calculated.

If the UDP checksum does not match the computed checksum by the receiver, the UDP packet is simply discarded.

On the IPv4 network, UDP checksum is optional. NetX Duo allows an application to enable or disable UDP checksum calculation on a per-socket basis. By default, the UDP socket checksum logic is enabled. The application can disable checksum logic for a particular UDP socket by calling the ***nx_udp_socket_checksum_disable*** service. On the IPv6 network, however, UDP checksum is mandatory. Therefore, the service ***nx_udp_socket_checksum_disable*** would not disable UDP checksum logic when sending a packet through the IPv6 network.

Certain Ethernet controllers are able to generate the UDP checksum on the fly. If the system is able to use hardware checksum computation feature, the NetX Duo library can be built without the checksum logic. To disable UDP software checksum, the NetX Duo library must be built with the following symbols defined: ***NX_DISABLE_UDP_TX_CHECKSUM*** and ***NX_DISABLE_UDP_RX_CHECKSUM*** (described in Chapter two). The configuration options remove UDP checksum logic from NetX Duo entirely, while calling the ***nx_udp_socket_checksum_disable*** service allows the application to disable IPv4 UDP checksum processing on a per socket basis.

### UDP Ports and Binding      
A UDP port is a logical end point in the UDP protocol. There are 65,535 valid ports in the UDP component of NetX Duo, ranging from 1 through 0xFFFF. To send or receive UDP data, the application must first create a UDP socket, then bind it to a desired port. After binding a UDP socket to a port, the application may send and receive data on that socket.

### UDP Fast Path
The UDP Fast Path is the name for a low packet overhead path through the NetX Duo UDP implementation. Sending a UDP packet requires just a few function calls: ***nx_udp_socket_send***, ***nx_ip_packet_send***, and the eventual call to the network driver. ***nx_udp_socket_send*** is available in NetX Duo for existing NetX applications and is only applicable for IPv4 packets. The preferred method, however, is to use ***nxd_udp_socket_send*** service discussed below. On UDP packet reception, the UDP packet is either placed on the appropriate UDP socket receive queue or delivered to a suspended application thread in a single function call from the network driver's receive interrupt processing. This highly optimized logic for sending and receiving UDP packets is the essence of UDP Fast Path technology.  

### UDP Packet Send    
Sending UDP data over IPv6 or IPv4 networks is easily accomplished by calling the ***nxd_udp_socket_send*** function. The caller must set the IP version in the *nx_ip_version* field of the NXD_ADDRESS pointer parameter. NetX Duo will determine the best source address for transmitted UDP packets based on the destination IPv4/IPv6 address. This service places a UDP header in front of the packet data and sends it out onto the network using an internal IP send routine. There is no thread suspension on sending UDP packets because all UDP packet transmissions are processed immediately. 

For multicast or broadcast destinations, the application should specify the source IP address to use if the NetX Duo device has multiple IP addresses to choose from. This can be done with the services ***nxd_udp_socket_source_send.***

> **Important:** *If **nx_udp_socket_send** is used for transmitting multicast or broadcast packets, the IP address of the first enabled interface is used as source address*.

> **Note:** *If UDP checksum logic is enabled for this socket, the checksum operation is performed in the context of the calling thread, without blocking access to the UDP or IP data structures*. 

> **Warning:** *The UDP payload data residing in the NX_PACKET structure should reside on a long-word boundary. The application needs to leave sufficient space between the prepend pointer and the data start pointer for NetX Duo to place the UDP, IP, and physical media headers*.

### UDP Packet Receive    
Application threads may receive UDP packets from a particular socket by calling ***nx_udp_socket_receive***. The socket receive function delivers the oldest packet on the socket's receive queue. If there are no packets on the receive queue, the calling thread can suspend (with an optional timeout) until a packet arrives.

The UDP receive packet processing (usually called from the network driver's receive interrupt handler) is responsible for either placing the packet on the UDP socket's receive queue or delivering it to the first suspended thread waiting for a packet. If the packet is queued, the receive processing also checks the maximum receive queue depth associated with the socket. If this newly queued packet exceeds the queue depth, the oldest packet in the queue is discarded.

### UDP Receive Notify   
If the application thread needs to process received data from more than one socket, the ***nx_udp_socket_receive_notify*** function should be used. This function registers a receive packet callback function for the socket. Whenever a packet is received on the socket, the callback function is executed.

The contents of the callback function is application specific; however, it would most likely contain logic to inform the processing thread that a packet is now available on the corresponding socket.

### Peer Address and Port   
On receiving a UDP packet, application may find the sender's IP address and port number by using the service ***nx_udp_packet_info_extract***. On successful return, this service provides information on the sender's IP address, sender's port number, and the local interface through which the packet was received.  

### Thread Suspension   
As mentioned previously, application threads can suspend while attempting to receive a UDP packet on a particular UDP port. After a packet is received on that port, it is given to the first thread suspended and that thread is then resumed. An optional timeout is available when suspending on a UDP receive packet, a feature available for most NetX Duo services.  

### UDP Socket Statistics and Errors     
If enabled, the NetX Duo UDP socket software keeps track of several statistics and errors that may be useful to the application. The following statistics and error reports are maintained for each IP/UDP instance:

- Total UDP Packets Sent  
- Total UDP Bytes Sent  
- Total UDP Packets Received   
- Total UDP Bytes Received  
- Total UDP Invalid Packets  
- Total UDP Receive Packets Dropped  
- Total UDP Receive Checksum Errors  
- UDP Socket Packets Sent  
- UDP Socket Bytes Sent  
- UDP Socket Packets Received   
- UDP Socket Bytes Received  
- UDP Socket Packets Queued  
- UDP Socket Receive Packets Dropped  
- UDP Socket Checksum Errors  

All these statistics and error reports are available to the application with the ***nx_udp_info_get*** service for UDP statistics amassed over all UDP sockets, and the ***nx_udp_socket_info_get*** service for UDP statistics on the specified UDP socket.

### UDP Socket Control Block NX_UDP_SOCKET
The characteristics of each UDP socket are found in the associated NX_UDP_SOCKET control block. It contains useful information such as the link to the IP data structure, the network interface for the sending and receiving paths, the bound port, and the receive packet queue. This structure is defined in the ***nx_api.h*** file.
