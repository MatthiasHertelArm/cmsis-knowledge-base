---
id: "intr-connecting-matter-over-thread-devi-a-brief-introduction-to-matter"
type: "concept"
domain: "debug"
title: "Connecting Matter-over-Thread Devices to the Internet: A Brief Introduction to Matter"
summary: "Matter[^matter_spec] is an application-layer protocol for smart home devices. It was developed by the Connectivity Standards Alliance (CSA), with backing from Apple, Google, Amazon, and others."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-03-24-matter-internet-connectivity.md"
doc_source: "https://interrupt.memfault.com/blog/matter-internet-connectivity#a-brief-introduction-to-matter"
license: "CC-BY-SA-4.0"
mode: "V"
---

Matter[^matter_spec] is an application-layer protocol for smart home devices. It
was developed by the Connectivity Standards Alliance (CSA), with backing from
Apple, Google, Amazon, and others. The goal is interoperability: a Matter light
bulb works with any Matter controller, regardless of the ecosystem.

(figure: Matter components)

Matter defines a data model (clusters, attributes, commands) and the
networking stack to carry it. Devices are commissioned into a fabric (a logical
network of controllers and devices), and from that point on, controllers can read attributes, send commands, and subscribe to changes.

### Matter's Networking Stack

Under the hood, Matter runs on IPv6 over either Wi-Fi or Thread. For
battery-powered and low-power devices, Thread is the typical choice.

Thread[^thread_spec] is a low-power mesh networking protocol built on top of
IEEE 802.15.4 (the same radio layer as Zigbee). It provides IPv6 addressing,
mesh routing, and secure commissioning. Crucially, Thread networks include a
Border Router, a device that bridges traffic between the Thread mesh and the
wider IP network (typically your home Wi-Fi/Ethernet).

(figure: Matter network topologies)

Matter does not use TCP. Instead, it runs on UDP and adds its own reliability and encryption on top through the Matter Reliable Protocol (MRP) and a custom
security layer (CASE/PASE sessions with AES-CCM encryption).

> **Note**: Matter 1.5 adds TCP support to the standard, but it remains to be seen how this will be implemented in practice.
