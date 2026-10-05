---
id: "txmw-chapter-3-functional-components-of-internet-group-management-protocol-igmp"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Internet Group Management Protocol (IGMP)"
summary: "The Internet Group Management Protocol (IGMP) provides a device to communicate with its neighbors and its routers that it intends to receive, or join, an IPv4 multicast group (RFC 1112 and RFC 2236)."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#internet-group-management-protocol-igmp"
license: "MIT"
mode: "V"
---

The Internet Group Management Protocol (IGMP) provides a device to communicate with its neighbors and its routers that it intends to receive, or join, an IPv4 multicast group (RFC 1112 and RFC 2236). A multicast group is basically a dynamic collection of network members and is represented by a Class D IP address. Members of the multicast group may leave at any time, and new members may join at any time. The coordination involved in joining and leaving the group is the responsibility of IGMP.

> **Note:** *IGMP is designed only for IPv4 multicast groups. It cannot be used on the IPv6 network.*

### IGMP Enable     
Before any multicasting activity can take place in NetX Duo, the application must call the ***nx_igmp_enable*** service. This service performs basic IGMP initialization in preparation for multicast requests.

### Multicast IPv4 Addressing  
As mentioned previously, multicast addresses are actually Class D IP addresses as shown in [Figure 4](#ipv4-addresses). The lower 28-bits of the Class D address correspond to the multicast group ID. There are a series of pre-defined multicast addresses; however, the *all hosts address* (244.0.0.1) is particularly important to IGMP processing. The *all hosts address* is used by routers to query all multicast members to report on which multicast groups they belong to.  

### Physical Address Mapping in IPv4
Class D multicast addresses map directly to physical Ethernet addresses ranging from 01.00.5e.00.00.00 through 01.00.5e.7f.ff.ff. The lower 23 bits of the IP multicast address map directly to the lower 23 bits of the Ethernet address.

### Multicast Group Join
Applications that need to join a particular multicast group may do so by calling the ***nx_igmp_multicast_join*** service. This service keeps track of the number of requests to join this multicast group. If this is the first application request to join the multicast group, an IGMP report is sent out on the primary network indicating this host's intention to join the group. Next, the
network driver is called to set up for listening for packets with the Ethernet address for this multicast group.

In a multihome system, if the multicast group is accessible via a specific interface, application shall use the service ***nx_igmp_multicast_interface_join*** instead of ***nx_igmp_multicast_join***, which is limited to multicast groups on the primary network.

### Multicast Group Leave   
Applications that need to leave a previously joined multicast group may do so by calling the ***nx_igmp_multicast_leave*** service. This service reduces the internal count associated with how many times the group was joined. If there are no outstanding join requests for a group, the network driver is called to disable listening for packets with this multicast group's Ethernet address.

### Multicast Loopback    
An application may wish to receive multicast traffic originated from one of the sources on the same node. This requires the IP multicast component to have loopback enabled by using the service ***nx_igmp_loopback_enable***.

### IGMP Report Message      
When the application joins a multicast group, an IGMP report message is sent via the network to indicate the host's intention to join a particular multicast group. The format of the IGMP report message is shown in Figure 8. The multicast group address is used for both the group message in the IGMP report message and the destination IP address.

In the figure above (Figure 8), the IGMP header contains a version/type field, maximum response

(figure: Diagram of a IGMP report message.)

**FIGURE 8. IGMP Report Message**

time, a checksum field, and a multicast group address field. For IGMPv1 messages, the Maximum Response Time field is always set to zero, as this is not part of the IGMPv1 protocol. The Maximum Response Time field is set when the host receives a Query type IGMP message and cleared when a host receives another host's Report type message as defined by the IGMPv2 protocol.

The following describes the IGMP header format:

|Header Field|Purpose|
|---|---|
|**Version** |This field specifies the IGMP version (bits 31- 28).|
|**Type** |This field specifies the type of IGMP message (bits 27 -24).|
|**Maximum Response Time** |Not used in IGMP v1. In IGMP v2 this field serves as the maximum response time.|
|**Checksum** |This field contains the 16-bit checksum of the one's complement sum of the IGMP message starting with the IGMP version (bits 0-15)|
|**Group Address** |32-bit class D group IP address|

IGMP report messages are also sent in response to IGMP query messages sent by a multicast router. Multicast routers periodically send query messages out to see which hosts still require group membership. Query messages have the same format as the IGMP Report message shown in Figure 8. The only differences are the IGMP type is equal to 1 and the group address field is set to 0. IGMP Query messages are sent to the *all hosts* IP address by the multicast router. A host that still wishes to maintain group membership responds by sending another IGMP Report message.

> **Note:** *All messages in the TCP/IP implementation are expected to be in **big endian** format. In this format, the most significant byte of the word resides at the lowest byte address.*

### IGMP Statistics and Errors    
If enabled, the NetX Duo IGMP software keeps track of several statistics and errors that may be useful to the application. The following statistics and error reports are maintained for each IP's IGMP processing: 

- Total IGMP Reports Sent 
- Total IGMP Queries Received 
- Total IGMP Checksum Errors 
- Total IGMP Current Groups Joined 

All these statistics and error reports are available to the application with the ***nx_igmp_info_get***service. 

### Multicast without IGMP  
Application expecting IPv4 multicast traffic can join a multicast group address without invoking IGMP messages by using the service ***nx_ipv4_multicast_interface_join***. This service instructs the IPv4 layer and the underlying interface driver to accept packets from the designated IPv4 multicast address. However there is no IGMP group management messages being sent or processed for this group.

Application no longer wish to receive traffic from the group can use the service ***nx_ipv4_multicast_interface_leave.***
