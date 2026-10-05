---
id: "txmw-chapter-3-functional-components-of-application-interface-calls"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of NetX Duo: Execution Overview / Application Interface Calls"
summary: "Calls from the application are largely made from application threads running under the ThreadX RTOS. However, some initialization, create, and enable services may be called from tx_application_define."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter3.md#application-interface-calls"
license: "MIT"
mode: "V"
---

_Part of: Execution Overview_

Calls from the application are largely made from application threads running under the ThreadX RTOS. However, some initialization, create, and enable services may be called from ***tx_application_define***. The "Allowed From" sections in [Chapter 4 - Description of NetX Duo Services](https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter4.md) indicate from which each NetX Duo service can be called.

For the most part, processing intensive activities such as computing checksums is done within the calling thread's context—without blocking access of other threads to the IP instance. For example, on transmission, the UDP checksum calculation is performed inside the ***nx_udp_socket_send*** service, prior to calling the underlying IP send function. On a received packet, the UDP checksum is calculated in the ***nx_udp_socket_receive*** service, executed in the  of the application thread. This helps prevent stalling network requests of higher-priority threads because of processing intensive checksum computation in lower-priority threads.

Values, such as IP addresses and port numbers, are passed to APIs in host byte order. Internally these values are stored in host byte order as well. This allows developers to easily view the values via a debugger. When these values are programmed into a frame for transmission, they are converted to network byte order.
