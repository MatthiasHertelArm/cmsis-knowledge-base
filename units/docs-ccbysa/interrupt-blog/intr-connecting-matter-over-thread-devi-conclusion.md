---
id: "intr-connecting-matter-over-thread-devi-conclusion"
type: "concept"
domain: "debug"
title: "Connecting Matter-over-Thread Devices to the Internet: Conclusion"
summary: "Matter devices are designed to operate within the local network, and the hub handles most internet-facing communication."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-03-24-matter-internet-connectivity.md"
doc_source: "https://interrupt.memfault.com/blog/matter-internet-connectivity#conclusion"
license: "CC-BY-SA-4.0"
mode: "V"
---

Matter devices are designed to operate within the local network, and the hub
handles most internet-facing communication. But when you need to reach the
internet directly for telemetry, diagnostics, or custom cloud integration,
the Thread Border Router can bridge your traffic.

The recipe we came up with is simple: use the OpenThread DNS client to resolve
hostnames via the Border Router's DNS proxy, NAT64 to reach IPv4 servers, and
UDP as the transport. For security, layer DTLS on top and use CoAP as the
application protocol.

NAT64 support is not universal today, but it is required in Thread 1.4 and
already available on Apple Border Routers. As more hubs get updated, this
pattern will become increasingly reliable.

I hope this post gives you a starting point for adding internet connectivity to
your Matter devices. As always, we would love to hear about your experience in
the comments.







{:.no_toc}
