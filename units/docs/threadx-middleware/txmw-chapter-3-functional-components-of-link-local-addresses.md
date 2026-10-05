---
id: "txmw-chapter-3-functional-components-of-link-local-addresses"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: IPv6 in NetX Duo / Link Local Addresses"
summary: "A link-local address is only valid on the local network. A device can send and receive packets to another device on the same network after a valid link local address is assigned to it."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#link-local-addresses"
license: "MIT"
mode: "V"
---

_Part of: IPv6 in NetX Duo_

A link-local address is only valid on the local network. A device can send and receive packets to another device on the same network after a valid link local address is assigned to it. An application assigns a link-local address by calling the NetX Duo service ***nxd_ipv6_address_set***, with the prefix length parameter set to 10. The application may supply a link-local address to the service, or it may simply use NX_NULL as the link-local address and allow NetX Duo to construct a link-local address based on the device's MAC address.

The following example instructs NetX Duo to configure the link-local address with a prefix length of 10 on the primary device (index 0) using its MAC address:

```c
nxd_ipv6_address_set(ip_ptr, 0, NX_NULL, 10, NX_NULL);
```
In the example above, if the MAC address of the interface is 54:32:10:1A:BC:67, the corresponding link-local address would be:

```c
FE80::5632:10FF:FE1A:BC67
```
Note that the host ID portion of the IPv6 address (**5632:10FF:FE1A:BC67**) is made up of the 6-byte MAC address, with the following modifications:

- **0xFFFE** inserted between byte 3 and byte 4 of the MAC address
- Second lowest bit of the first byte of the MAC address (U/L bit) is set to 1

Refer to RFC 2464 (Transmission of IPv6 Packets over Ethernet Network) for more information on how to construct the host portion of an IPv6 address from its interface MAC address.

There are a few special multicast addresses for sending multicast messages to one or more hosts in IPv6:

| Group  | Address   | Description  |
|---|---|---|
|All nodes group |**FF02::1** |All hosts on the local network|
|All routers group |**FF02::2** |All routers on the local network|
|Solicited-node |**FF02::1:FF00:0/104** |Explained below|

A solicited-node multicast address targets specific hosts on the local link rather than all the IPv6 hosts. It consists of the prefix **FF02::1:FF00:0/104**, which is 104 bits and the last 24-bits of the target IPv6 address. For example, an IPv6 address **205B:209D:D028::F058:D1C8:1024** has a solicited-node multicast address of address **FF02::1:FFC8:1024**.

> **Important:** *The double colon notation indicates the intervening bits are all zeroes. **FF02::1:FF00:0/104** fully expanded looks like* **FF02:0000:0000:0000:0000:0001:FF00:0000**
