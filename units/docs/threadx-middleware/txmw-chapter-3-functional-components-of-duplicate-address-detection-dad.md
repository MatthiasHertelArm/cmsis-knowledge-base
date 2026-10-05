---
id: "txmw-chapter-3-functional-components-of-duplicate-address-detection-dad"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: IPv6 in NetX Duo / Duplicate Address Detection (DAD)"
summary: "After a system configures its IPv6 address, the address is marked as TENTATIVE. If Duplicate Address Detection (DAD), described in RFC 4862, is enabled, NetX Duo automatically sends neighbor solicitation (NS) messages with this tentative address as the destination."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#duplicate-address-detection-dad"
license: "MIT"
mode: "V"
---

_Part of: IPv6 in NetX Duo_

After a system configures its IPv6 address, the address is marked as *TENTATIVE*. If Duplicate Address Detection (DAD), described in RFC 4862, is enabled, NetX Duo automatically sends neighbor solicitation (NS) messages with this tentative address as the destination. If no hosts on the network respond to these NS messages within a given period of time, the address is assumed to be unique on the local link, and its state transits to the VALID state. At this point the application may start using this IP address for communication.  

The DAD functionality is part of the ICMPv6 module. Therefore, the application must enable ICMPv6 services before a newly configured address can go through the DAD process. Alternatively, the DAD 
process may be turned off by defining ***NX_DISABLE_IPV6_DAD*** option in the NetX Duo library build environment (defined as ***nx_user.h***). During the DAD process, the ***NX_IPV6_DAD_TRANSMITS*** parameter determines the number of NS messages sent by NetX Duo without receiving a response to determine that the address is unique. By default and recommended by RFC 4862, ***NX_IPV6_DAD_TRANSMITS*** is set at 3. Setting this symbol to zero effectively disables DAD.

If ICMPv6 or DAD is not enabled at the time the application assigns an IPv6 address, DAD is not performed and NetX Duo sets the state of the IPv6 address to VALID immediately.

NetX Duo cannot communicate on the IPv6 network until its link local and/or global address is valid. After a valid address is obtained, NetX Duo attempts to match the destination address of an incoming packet against one of its configured IPv6 address or an enabled multicast address. If no matches are found, the packet is dropped. 

**Warning:** *During the DAD process, the number of DAD NS packets to be transmitted is defined by ***NX_IPV6_DAD_TRANSMITS***, which defaults to 3, and by default there is a one second delay between each DAD NS message is sent. Therefore, in a system with DAD enabled, after an IPv6 address is assigned (and assuming this is not a duplicated address), there is approximately 3 seconds delay before the IP address is in a VALID state and is ready for communication.*

Applications may want to receive notifications when IPv6 addresses in the system are changed. To enable the IPv6 address change notification feature, the NetX Duo library must be built with the symbol **NX_ENABLE_IPV6_ADDRESS_CHANGE_NOTIFY** defined. Once the feature is enabled, applications may install the callback function by using the ***nxd_ipv6_address_change_notify*** service.

Once an IPv6 address is changed, or becomes invalid, the user-supplied callback function is invoked with the following information:

| Function  | Description  |
|---|---|
|ip_ptr |Pointer to the IP instance|
|interface_index |Index to the network interface that this IPv6 address is associated with
|ipv6_addr_index |Index to the IPv6 address table|
|ipv6_address |Pointer to the IPv6 address, in the form of an array of four ULONG integers. Pv6 addresses are presented in host byte order.|
