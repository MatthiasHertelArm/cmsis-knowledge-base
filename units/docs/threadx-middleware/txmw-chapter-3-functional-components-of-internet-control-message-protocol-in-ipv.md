---
id: "txmw-chapter-3-functional-components-of-internet-control-message-protocol-in-ipv"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Internet Control Message Protocol in IPv6 (ICMPv6)"
summary: "The role of ICMPv6 in IPv6 has been greatly expanded to support IPv6 address mapping and router discovery. In addition, NetX Duo ICMPv6 supports echo request and response, ICMPv6 error reports, and ICMPv6 redirect messages."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#internet-control-message-protocol-in-ipv6-icmpv6"
license: "MIT"
mode: "V"
---

The role of ICMPv6 in IPv6 has been greatly expanded to support IPv6 address mapping and router discovery. In addition, NetX Duo ICMPv6 supports echo request and response, ICMPv6 error reports, and ICMPv6 redirect messages.

### ICMPv6 Enable    
Before ICMPv6 messages can be processed by NetX Duo, the application must call the ***nxd_icmp_enable*** service to enable ICMPv6 processing as explained previously. 

### ICMPv6 Messages     
The ICMPv6 header structure is similar to the ICMPv4 header structure. As shown below, the basic ICMPv6 header contains the three fields, type, code, and checksum, plus variable length of ICMPv6 option data. 

(figure: Diagram of a basic ICMPv6 header.)

**FIGURE 10. Basic ICMPv6 Header**

|Field |Size(bytes) |Description |
|-----|-----|-----|
|     | 1   |Identifies the ICMPv6 message type; |
|     |     |1 Destination Unreachable |
|     |     |2 Packet Too Big |
|     |     |3 Time Exceeded |
|     |     |4 Parameter Problem |
|     |     |128 Echo Request |
|     |     |129 Echo Reply |
|     |     |133 Router Solicitation |
|     |     |134 Router Advertisement |
|     |     |135 Neighbor Solicitation |
|     |     |136 Neighbor Advertisement |
|     |     |137 Redirect Message |
|Code | 1   |Further qualifies the ICMPv6 message type. Generally used with error messages. If not used, it is set to zero. Echo request/reply and NS messages do not use it.|
|Checksum | 2 |16-bit checksum field for the ICMP Header. This is a 16-bit complement of the entire ICMPv6 message, including the ICMPv6 header. It also includes a pseudo-header of the IPv6 source address, destination address, and packet payload length. |

An example Neighbor Solicitation header is shown below.

(figure: Diagram of an example Neighbor Solicitation header.)

**FIGURE 11. ICMPv6 Header for a Neighbor Solicitation Message**

|Field |Size(bytes) |Description |
|-----|-----|-----|
|Type | 1   |Identifies the ICMPv6 message type for neighbor solicitation messages. Value is 135. |
|Code | 1   |Not used. Set to 0. |
|Checksum | 2  |16-bit checksum field for the ICMPv6 header. |
|Reserved | 4  |4 reserved bytes set to 0. |
|Target Address | 16  |IPv6 address of target of the solicitation. For IPv6 address resolution, this is the actual unicast IP address of the device whose link layer address needs to be resolved. |
|Options | Variable |Optional information specified by the Neighbor Discovery Protocol. |

### ICMPv6 Ping Request
In NetX Duo applications use ***nxd_icmp_ping*** to issue either IPv6 or IPv4 ping requests, based on the destination IP address specified in the parameters.  

### ICMPv6 Ping Response
An ICMPv6 ping response is another type of ICMPv6 message that is generated internally by the ICMPv6 component in response to an external ICMPv6 ping request. In additional to acknowledgement, the ICMPv6 ping response also contains a copy of the user data supplied in the ICMPv6 ping request.  

### Thread Suspension
Application threads can suspend while attempting to ping another network member. After a ping response is received, the ping response message is given to the first thread suspended and that thread is resumed. Like all NetX Duo services, suspending on a ping request has an optional timeout.  

### Other ICMPv6 Messages
ICMPv6 messages are required for the following features:  

- Neighbor Discovery  
- Stateless Address Autoconfiguration 
- Router Discovery 
- Neighbor Unreachability Detection  

### Neighbor Unreachability, Router and Prefix Discovery    
Neighbor Unreachability Detection, Router Discovery, and Prefix Discovery are based on the Neighbor Discovery protocol and are described below. 

***Neighbor Unreachability Detection:*** An IPv6 device searches its Neighbor Discovery (ND) Cache for the destination link layer address when it wishes to send a packet. The immediate destination, sometimes referred to as the 'next hop,' may be the actual destination on the same link or it may be a router if the destination is off link. An ND cache entry contains the status on a neighbor's reachability.

A REACHABLE status indicates the neighbor is considered reachable. A neighbor is reachable if it has recently received confirmation that packets sent to the neighbor have been received. Confirmation in NetX Duo take the form of receiving an NA message from the neighbor in response to an NS message sent by the NetX Duo device. NetX Duo will also change the state of the neighbor status to REACHABLE if the
application calls the NetX Duo service ***nxd_nd_cache_entry_set*** to manually enter a cache record.

***Router Discovery:*** An IPv6 device uses a router to forward all packets intended for off link destinations. It may also use information sent by the router, such as router advertisement (RA) messages, to configure its global IPv6 addresses.

A device on the network may initiate the Router Discovery process by sending a router solicitation (RS) message to the all-router multicast address (FF01::2). Or it can wait on the all-node multicast address (FF::1) for a periodic RA from the routers.

An RA message contains the prefix information for configuring an IPv6 address for that network. In NetX Duo, router solicitation is by default enabled and can be disabled by setting the configuration option ***NX_DISABLE_ICMPV6_ROUTER_SOLICITATION*** in ***nx_user.h***. See Configuration Options in the "Installation and Use of NetX Duo" chapter for more details on setting Router Solicitation parameters. 

***Prefix Discovery***: An IPv6 device uses prefix discovery to learn which target hosts are accessible directly without going through a router. This information is made available to the IPv6 device from RA messages from the router. The IPv6 device stores the prefix information in a prefix table. Prefix discovery is matching a prefix from the IPv6 device prefix table to a target address. A prefix matches a target address if all the bits in the prefix match the most significant bits of the target address. If more than one prefix covers an address, the longest prefix is selected.

### ICMPv6 Error Messages    
The following ICMPv6 error messages are supported in NetX Duo:  

- Destination Unreachable  
- Packet Too Big  
- Time Exceed  
- Parameter Problem
