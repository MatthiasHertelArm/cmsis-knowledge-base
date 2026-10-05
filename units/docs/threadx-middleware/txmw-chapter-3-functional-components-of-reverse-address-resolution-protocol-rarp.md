---
id: "txmw-chapter-3-functional-components-of-reverse-address-resolution-protocol-rarp"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Reverse Address Resolution Protocol (RARP) in IPv4"
summary: "The Reverse Address Resolution Protocol (RARP) is the protocol for requesting network assignment of the host's 32-bit IP addresses (RFC 903)."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#reverse-address-resolution-protocol-rarp-in-ipv4"
license: "MIT"
mode: "V"
---

The Reverse Address Resolution Protocol (RARP) is the protocol for requesting network assignment of the host's 32-bit IP addresses (RFC 903). This is done through an RARP request and continues periodically until a network member assigns an IP address to the host network interface in an RARP response. The application creates an IP instance by the service ***nx_ip_create*** with a zero IP address. If RARP is enabled by the application, it can use the RARP protocol to request an IP address from the network server accessible through the interface that has a zero IP address.

### RARP Enable

To use RARP, the application must create the IP instance with an IP address of zero, then enable RARP using the service ***nx_rarp_enable***. For multihome systems, at least one network device associated with the IP instance must have an IP address of zero. The RARP processing periodically sends RARP request messages for the NetX Duo system requiring an IP address until a valid RARP reply with the network designated IP address is received. At this point, RARP processing is complete.

After RARP has been enabled, it is disabled automatically after all interface addresses are resolved. The application may force RARP to terminate by using the service ***nx_rarp_disable***.

### RARP Request

The format of an RARP request packet is almost identical to the ARP packet shown in [Figure 6](#arp-messages).The only difference is the frame type field is 0x8035 and the *Operation Code* field is 3, designating an RARP request. As mentioned previously, RARP requests will be sent periodically (every ***NX_RARP_UPDATE_RATE*** seconds) until a RARP reply with the network assigned IP address is received.

> **Note:** *All RARP messages in the TCP/IP implementation are expected to be in **big endian** format. In this format, the most significant byte of the word resides at the lowest byte address.*

### RARP Reply

RARP reply messages are received from the network and contain the network assigned IP address for this host. The format of an RARP reply packet is almost identical to the ARP packet shown in Figure 6. The only difference is the frame type field is 0x8035 and the *Operation Code* field is 4, which designates an RARP reply. After received, the IP address is setup in the IP instance, the periodic RARP request is disabled, and the IP instance is now ready for normal network operation.

For multihome hosts, the IP address is applied to the requesting network interface. If there are other network interfaces still requesting an IP address assignment, the periodic RARP service continues until all interface IP address requests are resolved.

> **Note:** *The application should not use the IP instance until the RARP processing is complete. The **nx_ip_status_check** may be used by applications to wait for the RARP completion. For multihome systems, the application should not use the requesting interface until the RARP processing is complete on that interface. Status of the IP address on the secondary device can be checked with the **nx_ip_interface_status_check** service.*

### RARP Statistics and Errors

If enabled, the NetX Duo RARP software keeps track of several statistics and errors that may be useful to the application. The following statistics and error reports are maintained for each IP's RARP processing:

- Total RARP Requests Sent
- Total RARP Responses Received
- Total RARP Invalid Messages

All these statistics and error reports are available to the application with the ***nx_rarp_info_get*** service.
