---
id: "intr-connecting-matter-over-thread-devi-doing-something-useful"
type: "concept"
domain: "debug"
title: "Connecting Matter-over-Thread Devices to the Internet: Doing something useful"
summary: "A plain UDP echo is a good proof of concept, but a real application needs two things on top of raw UDP: a standard communication protocol, and encryption."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-03-24-matter-internet-connectivity.md"
doc_source: "https://interrupt.memfault.com/blog/matter-internet-connectivity#doing-something-useful"
license: "CC-BY-SA-4.0"
mode: "V"
---

A plain UDP echo is a good proof of concept, but a real application needs two
things on top of raw UDP: a standard communication protocol, and encryption.

**CoAP** (Constrained Application Protocol)[^coap_rfc] is a good fit for the
protocol layer. It was designed specifically for constrained devices and
low-power networks. Like HTTP, it uses methods (GET, POST, PUT, DELETE) and
status codes, so the programming model is familiar. Unlike HTTP, it runs over
UDP, uses compact binary headers (typically 4 bytes plus options), and supports
confirmable messages with built-in retransmission. It also supports observe
(server push) and block-wise transfers for payloads larger than a single MTU.

**DTLS** (Datagram TLS) handles encryption. It is the UDP equivalent of TLS,
providing the same authentication and confidentiality guarantees but designed for
datagram transports. The OpenThread stack already includes mbedTLS, so adding
DTLS to a Thread application does not require pulling in a new crypto library.
In most cases, you'll want to use DTLS 1.2 with Connection ID (RFC 9146): it lets you resume sessions without a full handshake, which is useful for devices that send data periodically and sleep in between.

Together, CoAP over DTLS gives you a lightweight, encrypted, request/response
channel over UDP. This is the same pattern used by LwM2M and other IoT
protocols, so there is good tooling and server-side support.

We are big fans of CoAP at nRF Cloud[^nrfcloud], and have built support for the
protocol across our cloud platform. Device-to-cloud message routing,
observability, and location services all support CoAP over DTLS. If you are looking to connect your Thread devices to the internet and want a backend that speaks their language, check it out.
