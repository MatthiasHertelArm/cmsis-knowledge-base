---
id: "txmw-chapter-3-functional-components-of-initialization"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Execution Overview / Initialization"
summary: "The service nx_system_initialize must be called before any other NetX Duo service is called. System initialization can be called either from the ThreadX tx_application_define function or from application threads."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#initialization"
license: "MIT"
mode: "V"
---

_Part of: Execution Overview_

The service ***nx_system_initialize*** must be called before any other NetX Duo service is called. System initialization can be called either from the ThreadX ***tx_application_define*** function or from application threads.

After ***nx_system_initialize*** returns, the system is ready to create packet pools and IP instances. Because creating an IP instance requires a default packet pool, at least one NetX Duo packet pool must exist prior to creating an IP instance. Creating packet pools and IP instances are allowed from the ThreadX initialization function ***tx_application_define*** and from application threads.

Internally, creating an IP instance is accomplished in two parts: The first part is done within the context of the caller, either from ***tx_application_define*** or from an application thread's context. This includes setting up the IP data structure and creating various IP resources, including the internal IP thread. The second part is performed during the initial execution from the internal IP thread. This is where the network driver, supplied during the first part of IP creation, is first called. Calling the network driver from the internal IP thread enables the driver to perform I/O and suspend during its initialization processing.

When the network driver returns from its initialization processing, the IP creation is complete.

Initialization of IPv6 in NetX Duo requires a few additional NetX Duo services. These are described in greater detail in the section [IPv6 in NetX Duo](#ipv6-in-netx-duo) later in this chapter.

> **Note:** *The NetX Duo service **nx_ip_status_check** is available to obtain information on the IP instance and its primary interface status. Such status information includes whether or not the link is initialized, enabled and IP address is resolved. This information is used to synchronize application threads needing to use a newly created IP instance. For multihome systems, see [Multihome Support](#multihome-support). **nx_ip_interface_status_check** is available to obtain 3information on the specified interface.*
