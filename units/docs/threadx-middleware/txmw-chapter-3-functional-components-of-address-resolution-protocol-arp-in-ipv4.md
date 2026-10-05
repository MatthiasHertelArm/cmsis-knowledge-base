---
id: "txmw-chapter-3-functional-components-of-address-resolution-protocol-arp-in-ipv4"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Address Resolution Protocol (ARP) in IPv4"
summary: "The Address Resolution Protocol (ARP) is responsible for dynamically mapping 32-bit IPv4 addresses to those of the underlying physical media (RFC 826). Ethernet is the most typical physical media, and it supports 48-bit addresses."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#address-resolution-protocol-arp-in-ipv4"
license: "MIT"
mode: "V"
---

The Address Resolution Protocol (ARP) is responsible for dynamically mapping 32-bit IPv4 addresses to those of the underlying physical media (RFC 826). Ethernet is the most typical physical media, and it
supports 48-bit addresses. The need for ARP is determined by the network driver supplied to the ***nx_ip_create*** service. If physical mapping is required, the network driver must use the ***nx_interface_address_mapping_needed*** service to configure the driver interface properly.

### ARP Enable

For ARP to function properly, it must first be enabled by the application with the ***nx_arp_enable*** service. This service sets up various data structures for ARP processing, including the creation of an ARP cache area from the memory supplied to the ARP enable service.

### ARP Cache

The ARP cache can be viewed as an array of internal ARP mapping data structures. Each internal structure is capable of maintaining the relationship between an IP address and a physical hardware address. In addition, each data structure has link pointers so it can be part of multiple linked lists.

Application can look up an IP address from the ARP cache by supplying hardware MAC address using the service ***nx_arp_ip_address_find*** if the mapping exists in the ARP table. Similarly, the service ***nx_arp_hardware_address_find*** returns the MAC address for a given IP address.

### ARP Dynamic Entries

By default, the ARP enable service places all entries in the ARP cache on the list of available dynamic ARP entries. A dynamic ARP entry is allocated from this list by NetX Duo when a send request to an unmapped IP address is detected. After allocation, the ARP entry is set up and an ARP request is sent to the physical media.

A dynamic entry can also be created by the service ***nx_arp_dynamic_entry_set***.

> **Important:** *If all dynamic ARP entries are in use, the least recently used ARP entry is replaced with a new mapping.*

### ARP Static Entries

The application can also set up static ARP mapping by using the ***nx_arp_static_entry_create***service. This service allocates an ARP entry from the dynamic ARP entry list and places it on the static list with the mapping information supplied by the application. Static ARP entries are not subject to reuse or aging. The application can delete a static entry by using the service ***nx_arp_static_entry_delete***. To remove all static entries in the ARP table, the application may use the service ***nx_arp_static_entries_delete***.

### Automatic ARP Entry

NetX Duo records the peer's IP/MAC mapping after the peer responses to the ARP request. NetX Duo also implements the automatic ARP entry feature where it records peer IP/MAC address mapping based on unsolicited ARP requests from the network. This feature allows the ARP table to be populated with peer information, reducing the delay needed to go through the ARP request/response cycle. However the downside with enabling automatic ARP is that the ARP table tend to fill up quickly on a busy network with many nodes on the local link, which would eventually lead to ARP entry replacement.

This feature is enabled by default. To disable it, the NetX Duo library must be compiled with the symbol ***NX_DISABLE_ARP_AUTO_ENTRY***defined.

### ARP Messages

As mentioned previously, an ARP request message is sent when the IP task detects that mapping is needed for an IP address. ARP requests are sent periodically (every ***NX_ARP_UPDATE_RATE*** seconds) until a corresponding ARP response is received. A total of ***NX_ARP_MAXIMUM_RETRIES*** ARP requests are made before the ARP attempt is abandoned. When an ARP response is received, the associated physical address information is stored in the ARP entry that is in the cache.

For multihome systems, NetX Duo determines which interface to send the ARP requests and responses based on destination address specified.

> **Note:** *Outgoing IP packets are queued while NetX Duo waits for the ARP response. The number of outgoing IP packets queued is defined by the constant **NX_ARP_MAX_QUEUE_DEPTH**.*

NetX Duo also responds to ARP requests from other nodes on the local IPv4 network. When an external ARP request is made that matches the current IP address of the interface that receives the ARP request, NetX Duo builds an ARP response message that contains the current physical address.

The formats of Ethernet ARP requests and responses are shown in Figure 6 and are described below.

| **Request/Response Field**         | **Purpose**            |
| ---------------------------------- | ---------------------- |
| ***Ethernet Destination Address*** | This 6-byte field contains the destination address for the ARP response and is a broadcast (all ones) for ARP requests. This field is setup by the network driver. 
| ***Ethernet Source Address***      | This 6-byte field contains the address of the sender of the ARP request or response and is set up by the network driver. |
| ***Frame Type*** | This 2-byte field contains the type of Ethernet frame present and, for ARP requests and responses, this is equal to 0x0806. This is the last field the network driver is responsible for setting up. |
| ***Hardware Type*** | This 2-byte field contains the hardware type, which is 0x0001 for Ethernet. |
| ***Protocol Type*** | This 2-byte field contains the protocol type, which is 0x0800 for IP addresses. |
| ***Hardware Size*** | This 1-byte field contains the hardware address size, which is 6 for Ethernet addresses. |

(figure: Diagram of the  ARP Packet Format.)

**FIGURE 6. ARP Packet Format**

| Request/Response Field | Purpose |
|---|---|
| ***Protocol Size*** | This 1-byte field contains the IP address size, which is 4 for IP addresses. |
| ***Operation Code*** | This 2-byte field contains the operation for this ARP packet. An ARP request is specified with the value of 0x0001, while an ARP response is represented by a value of 0x0002. |
| ***Sender Ethernet Address*** | This 6-byte field contains the sender's Ethernet address. |
| ***Sender IP Address*** | This 4-byte field contains the sender's IP address. |
| ***Target Ethernet Address*** | This 6-byte field contains the target's Ethernet address. |
| ***Target IP Address*** | This 4-byte field contains the target's IP address. |

> **Note:** *ARP requests and responses are Ethernet-level packets. All other TCP/IP packets are encapsulated by an IP packet header.*

> **Note:** *All ARP messages in the TCP/IP implementation are expected to be in **big endian** format. In this format, the most significant byte of the word resides at the lowest byte address.*

### ARP Aging

NetX Duo supports automatic dynamic ARP entry invalidation. ***NX_ARP_EXPIRATION_RATE*** specifies the number of seconds an established IP address to physical mapping stays valid. After expiration, the ARP entry is removed from the ARP cache. The next attempt to send to the corresponding IP address will result in a new ARP request. Setting ***NX_ARP_EXPIRATION_RATE*** to zero disables ARP aging, which is the default configuration.

### ARP Defend

When an ARP request or ARP response packet is received and the sender has the same IP address, which conflicts with the IP address of this node, NetX Duo sends an ARP request for that address as a defense. If the conflict ARP packet is received more than once in 10 seconds, NetX Duo does not send more defend packets. The default interval 10 seconds can be redefined by ***NX_ARP_DEFEND_INTERVAL***. This behavior follows the policy specified in 2.4(c) of RFC5227. Since Windows XP ignores ARP announcement as a response for its ARP probe, user can define ***NX_ARP_DEFEND_BY_REPLY*** to send ARP response as additional defense.

### ARP Statistics and Errors

If enabled, the NetX Duo ARP software keeps track of several statistics and errors that may be useful to the application. The following statistics and error reports are maintained for each IP's ARP processing:

- Total ARP Requests Sent
- Total ARP Requests Received
- Total ARP Responses Sent 
- Total ARP Responses Received 
- Total ARP Dynamic Entries 
- Total ARP Static Entries 
- Total ARP Aged Entries 
- Total ARP Invalid Messages 

All these statistics and error reports are available to the application with the ***nx_arp_info_get*** service.
