---
id: "txmw-chapter-3-functional-components-of-icmpv4-services-in-netx-duo"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: ICMPv4 Services in NetX Duo"
summary: "Before ICMPv4 messages can be processed by NetX Duo, the application must call the nx_icmp_enable service to enable ICMPv4 processing. After this is done, the application can issue ping requests and field incoming ping packets."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#icmpv4-services-in-netx-duo"
license: "MIT"
mode: "V"
---

### ICMPv4 Enable

Before ICMPv4 messages can be processed by NetX Duo, the application must call the ***nx_icmp_enable*** service to enable ICMPv4 processing. After this is done, the application can issue ping requests and field incoming ping packets.  

### ICMPv4 Echo Request

An echo request is one type of ICMPv4 message that is typically used to check for the existence of a specific node on the network, as identified by its host IP address. The popular ping command is implemented using ICMP echo request/echo reply messages. If the specific host is present, its network stack processes the ping request and responses with a ping response. Figure 7 details the ICMPv4 ping message format.

(figure: ICMPv4 Ping Message)  

**FIGURE 7. ICMPv4 Ping Message**

> **Note:** *All ICMPv4 messages in the TCP/IP implementation are expected to be in **big endian** format. In this format, the most significant byte of the word resides at the lowest byte address.*

The following describes the ICMPv4 header format:

|Header Field |Purpose |
|---|---|
|**Type** |This field specifies the ICMPv4 message (bits 31-24). The most common are:
-  0: Echo Reply
- 3: Destination Unreachable
- 8: Echo Request
- 11: Time Exceeded
- 12: Parameter Problem |
|**Code** |This field is context specific on the type field (bits 23-16). For an echo request or reply the code is set to zero.|
|**Checksum** |This field contains the 16-bit checksum of the one's complement sum of the ICMPv4 message including the entire the ICMPv4 header starting with the Type field. Before generating the checksum, the checksum field is cleared.|
|**Identification** | This field contains an ID value identifying the host; a host should use the ID extracted from an ECHO request in the ECHO REPLY (bits 31-16).|
|**Sequence number** |This field contains an ID value; a host should use the ID extracted from an ECHO request in the ECHO REPLY (bits 31-16). Unlike the identifier field, this value will change in a subsequent Echo request from the same host (bits 15-0).|

### ICMPv4 Echo Response    
A ping response is another type of ICMP message that is generated internally by the ICMP component in response to an external ping request. In addition to acknowledgement, the ping response also contains a copy of the user data supplied in the ping request.

### ICMPv4 Error Messages   
The following ICMPv4 error messages are supported in NetX Duo: 
- Destination Unreachable 
- Time Exceed 
- Parameter Problem
