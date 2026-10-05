---
id: "intr-connecting-matter-over-thread-devi"
type: "concept"
domain: "debug"
title: "Connecting Matter-over-Thread Devices to the Internet"
summary: "While it has taken longer than some people expected, Matter is finally going mainstream. Brands including Ikea, Kwikset, and Bosch have shipped matter devices, and matter hubs can increasingly be found in people's homes."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-03-24-matter-internet-connectivity.md"
doc_source: "https://interrupt.memfault.com/blog/matter-internet-connectivity"
license: "CC-BY-SA-4.0"
mode: "V"
---

While it has taken longer than some people expected, Matter is finally going mainstream. Brands including Ikea, Kwikset, and Bosch have shipped matter devices, and matter hubs can increasingly be found in people's homes.

Many dev kits out there are matter compatible, and if you want to build a simple application you can find good example code and get started quickly. This is fine if your use case fits neatly within existing Matter clusters, but direct internet communication is not straightforward.



In this post, we look at how a Matter-over-Thread device can reach the internet
through a Thread Border Router. We will cover the key networking concepts (Thread, NAT64, and UDP) and walk through a working example that sends a UDP
message from an nRF54LM20 DK to an echo server on the public internet.
