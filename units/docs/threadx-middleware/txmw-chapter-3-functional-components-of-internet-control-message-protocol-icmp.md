---
id: "txmw-chapter-3-functional-components-of-internet-control-message-protocol-icmp"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Internet Control Message Protocol (ICMP)"
summary: "Internet Control Message Protocol for IPv4 (ICMP) is limited to passing error and control information between IP network members."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#internet-control-message-protocol-icmp"
license: "MIT"
mode: "V"
---

Internet Control Message Protocol for IPv4 (ICMP) is limited to passing error and control information between IP network members. Internet Control Message Protocol for IPv6 (ICMPv6) also handles error
and control information and is required for address resolution protocols such as Duplicate Address Detection (DAD) and stateless address autoconfiguration.

Like most other application layer (e.g., TCP/IP) messages, ICMP and ICMPv6 messages are encapsulated by an IP header with the ICMP (or ICMPv6) protocol designation.

### ICMP Statistics and Errors

If enabled, NetX Duo keeps track of several ICMP statistics and errors that may be useful to the application. The following statistics and error reports are maintained for each IP's ICMP processing: 

- Total ICMP Pings Sent  
- Total ICMP Ping Timeouts 
- Total ICMP Ping Threads Suspended 
- Total ICMP Ping Responses Received 
- Total ICMP Checksum Errors 
- Total ICMP Unhandled Messages 

All these statistics and error reports are available to the application with the ***nx_icmp_info_get*** service.
