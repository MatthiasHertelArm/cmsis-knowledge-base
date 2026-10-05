---
id: "txmw-chapter-1-introduction-to-netx-duo-netx-duo-unique-features"
type: "concept"
domain: "rtos"
title: "Chapter 1 - Introduction to NetX Duo: NetX Duo Unique Features"
summary: "Unlike other TCP/IP implementations, NetX Duo is designed to be versatile—easily scaling from small micro-controller-based applications to those that use powerful RISC and DSP processors."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/chapter1.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/chapter1.md#netx-duo-unique-features"
license: "MIT"
mode: "V"
---

Unlike other TCP/IP implementations, NetX Duo is designed to be versatile—easily scaling from small micro-controller-based applications to those that use powerful RISC and DSP processors. This is in sharp contrast to public domain or other commercial implementations originally intended for workstation environments but then squeezed into embedded designs.

### Piconet Architecture

Underlying the superior scalability and performance of NetX Duo is _Piconet_, a software architecture especially designed for embedded systems. Piconet architecture maximizes scalability by implementing NetX Duo services as a C library. In this way, only those services used by the application are brought into the final runtime image. Hence, the actual size of NetX Duo is determined by the application. For most applications, the instruction image requirements of NetX Duo ranges between 5 KBytes and 30 KBytes in size. With IPv6 and ICMPv6 enabled for IPv6 address configuration and neighbor discovery protocols, NetX Duo ranges in size from 30 kbytes to 45 kbytes.

NetX Duo achieves superior network performance by layering internal component function calls only when it is necessary. In addition, much of NetX Duo processing is done directly in-line, resulting in outstanding performance advantages over the workstation network software used in embedded designs in the past.

### Zero-copy Implementation

NetX Duo provides a packet-based, zero-copy implementation of TCP/IP. Zero copy means that data in the application's packet buffer are never copied inside NetX Duo. This greatly improves performance and frees up valuable processor cycles to the application, which is important in embedded applications.

### UDP Fast Path Technology

With _UDP Fast Path Technology_, NetX Duo provides the fastest possible UDP processing. On the sending side, UDP processing—including the optional UDP checksum—is contained within the _**nx_udp_socket_send**_ service. No additional function calls are made until the packet is ready to be sent via the internal NetX Duo IP send routine. This routine is also flat (that is, its function call nesting is minimal) so the packet is quickly dispatched to the application's network driver. When the UDP packet is received, the NetX Duo packet-receive processing places the packet directly on the appropriate UDP socket's receive queue or gives it to the first thread suspended waiting for a receive packet from the UDP socket's receive queue. No additional ThreadX context switches are necessary.

### ANSI C Source Code

NetX Duo is written completely in ANSI C and is portable immediately to virtually any processor architecture that has an ANSI C compiler and ThreadX support.

### Not A Black Box

Most distributions of NetX Duo include the complete C source code. This eliminates the "black-box" problems that occur with many commercial network stacks. By using NetX Duo, applications developers can see exactly what the network stack is doing—there are no mysteries!

Having the source code also allows for application-specific modifications. Although not recommended, it is beneficial to have the ability to modify the network stack if it is required.

These features are especially comforting to developers accustomed to working with in-house or public domain network stacks. They expect to have source code and the ability to modify it. NetX Duo is the ultimate network software for such developers.

### BSD-Compatible Socket API

For legacy applications, NetX Duo also provides a BSD-compatible socket interface that makes calls to the high-performance NetX Duo API underneath. This helps in migrating existing network application code to NetX Duo.
