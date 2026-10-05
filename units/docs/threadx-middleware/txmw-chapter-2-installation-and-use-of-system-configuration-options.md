---
id: "txmw-chapter-2-installation-and-use-of-system-configuration-options"
type: "concept"
domain: "rtos"
title: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / System Configuration Options"
summary: "Chapter 2 - Installation and Use of NetX Duo: Configuration Options / System Configuration Options"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter2.md#system-configuration-options"
license: "MIT"
mode: "V"
---

_Part of: Configuration Options_

| Option  | Description  |
|---|---|
| NX_ASSERT_FAIL    | Symbol that defines the debug statement to use when an assertion fails.                               |
| NX_DEBUG           | Defined, enables the optional print debug information available from the RAM Ethernet network driver. |
| NX_DEBUG_PACKET   | Defined, enables the optional debug packet dumping available in the RAM Ethernet network driver.      |
| NX_DISABLE_ASSERT | Defined, disables ASSERT checks in the source code. By default this option is not defined.            |
|NX_DISABLE_ERROR_CHECKING | Defined, removes the basic NetX Duo error checking API and improves performance. API return codes not affected by disabling error checking are listed in bold typeface in the API definition. This define is typically used after the application is debugged sufficiently and its use improves performance and decreases code size.|
|NX_DRIVER_DEFERRED_PROCESSING | Defined, enables deferred network driver packet handling. This allows the network driver to place a packet on the IP instance and have the real processing routine called from the NetX Duo internal IP helper thread.|
|NX_DUAL_PACKET_POOL_ENABLE | Renamed to  ***NX_ENABLE_DUAL_PACKET_POOL***. Although it is still being supported, new designs are encouraged to use ***NX_ENABLE_DUAL_PACKET_POOL***.|
|NX_ENABLE_DUAL_PACKET_POOL | Defined, allows the stack to use two packet pools, one with large payload size and one with smaller payload size. By default this option is not enabled.|
|NX_ENABLE_EXTENDED_NOTIFY_SUPPORT| Defined, enables more callback hooks in the stack. These callback functions are used by the BSD wrapper layer. By default this option is not defined.|
|NX_ENABLE_INTERFACE_CAPABILITY| Defined, allows the interface device driver to specify extra capability information, such as checksum off-loading. By default this option is not defined.|
|NX_ENABLE_SOURCE_ADDRESS_CHECK| Defined, enables the source address of incoming packet to be checked. By default this option is disabled.|
| NX_IPSEC_ENABLE  | Defined, enables the NetX Duo library to support IPsec operations. This feature requires the optional NetX Duo IPsec module. By default this feature is not enabled.            |
| NX_LITTLE_ENDIAN | Defined, performs the necessary byte swapping on little endian environments to ensure the protocol headers are in proper big endian format. Note the default is typically setup in ***nx_port.h***.|
|NX_MAX_PHYSICAL_INTERFACES | Specifies the total number of physical network interfaces on the device. The default value is 1 and is defined in ***nx_api.h***; a device must have at least one physical interface. Note this does not include the loopback interface.|
| NX_NAT_ENABLE | Defined, NetX Duo is built with NAT process. By default this option is not defined.|
| NX_PHYSICAL_HEADER  | Specifies the size in bytes of the physical header of the frame. The default value is 16 (based on a typical 14-byte Ethernet frame aligned to 32-bit boundary) and is defined in ***nx_api.h***. The application can override the default by defining the value before ***nx_api.h*** is included, such as in ***nx_user.h**.* |
| NX_PHYSICAL_TRAILER | Specifies the size in bytes of the physical packet trailer and is typically used to reserve storage for things like Ethernet CRCs, etc. The default value is 4 and is defined in ***nx_api.h***.|
