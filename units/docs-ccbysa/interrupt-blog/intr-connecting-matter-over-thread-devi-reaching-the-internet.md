---
id: "intr-connecting-matter-over-thread-devi-reaching-the-internet"
type: "concept"
domain: "debug"
title: "Connecting Matter-over-Thread Devices to the Internet: Reaching the Internet"
summary: "But sometimes local-only communication is not enough. You may want to:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2026-03-24-matter-internet-connectivity.md"
doc_source: "https://interrupt.memfault.com/blog/matter-internet-connectivity#reaching-the-internet"
license: "CC-BY-SA-4.0"
mode: "V"
---

But sometimes local-only communication is not enough. You may want to:

- Send telemetry data to a cloud backend
- Pull a firmware update directly from your backend rather than the DCL
- Reach a custom server for functionality outside the Matter spec

In theory, Matter hubs are full-fledged Thread Border Routers and
should be able to bridge traffic from the Thread mesh to the internet.

### One does not simply send IPv6 packets

Since Thread is an IPv6 network, you might wonder: why not just send packets to
the server's IPv6 address directly?

The short answer is that Thread devices typically do not have globally routable
IPv6 addresses. The addresses assigned within a Thread mesh are either
link-local (`fe80::`) or mesh-local (`fd::`), neither of which is routable on
the public internet. For a device to send IPv6 traffic directly to an internet
server, it would need a Global Unicast Address (GUA), and the Border Router
would need to route that prefix into the mesh.

Most Thread Border Routers do not enable this. Apple's HomePod, for example,
does not assign GUAs to Thread devices. Some other Border Router implementations
might, but it is not common today.

We need a different solution.

### Enter NAT64

Thread 1.4 introduced NAT64, a network address translation mechanism that allows IPv6-only clients to communicate with IPv4-only servers.

Here is how it works:

1. The device resolves a hostname using the Thread network's DNS server (provided
   by the Border Router). When resolving an A record (IPv4), the DNS client
   synthesizes an IPv6 address by embedding the IPv4 address within a well-known
   NAT64 prefix.
2. The device sends its UDP packet to that synthesized IPv6 address.
3. The Border Router recognizes the NAT64 prefix, extracts the IPv4 address, and
   forwards the packet to the IPv4 destination on the internet.
4. The reply comes back through the same path in reverse.

From the device's perspective, it is sending data to an IPv6 address. The NAT64
translation is transparent.

> **Note:** Not every Thread Border Router supports NAT64. Apple devices (HomePod
> mini, Apple TV 4K) do support it. NAT64 is a requirement in the Thread 1.4
> specification[^thread_1_4], so support will improve as more hubs receive
> updates.

### Sending data over UDP

Since Matter runs on UDP over Thread, there are a few constraints to keep in
mind:

- **UDP only.** Since TCP is not compatible with Matter, we get no HTTP,
  no HTTPS, no WebSockets.
- **Small effective payload.** Thread runs IPv6 over IEEE 802.15.4, which has
  very small MAC frames (127 bytes) and relies on 6LoWPAN fragmentation to carry
  the IPv6 minimum MTU of 1280 bytes. In practice, after headers and considering
  fragmentation overhead, you should assume your reliable UDP payload budget per
  message is well under 1200 bytes.
- **No TLS.** TLS requires TCP. For encrypted communication, you need DTLS
  (Datagram TLS), which is the UDP equivalent.

This complicates our life a bit, as it means we cannot simply talk to our backend over HTTP (which depends on TCP). We'll get to that in a bit.

### End-to-end data path

Putting everything we've learned together, here's how a UDP packet from a Matter device gets to a server on the internet:

```
┌─────────────┐    802.15.4    ┌───────────────────┐    Wi-Fi/Ethernet  ┌──────────┐
│ Matter      │ ─── Thread ──> │ Border Router     │ ──── NAT64 ──────> │  Cloud   │
│ Device      │    (IPv6/UDP)  │ (e.g. HomePod)    │   (IPv6 to IPv4)   │  Server  │
│ (nRF54LM20) │                │                   │                    │          │
└─────────────┘                └───────────────────┘                    └──────────┘
```

1. The application builds a UDP packet and hands it to the OpenThread stack.
2. OpenThread encapsulates it for 802.15.4, which encrypts each frame at the
   MAC layer (AES-128-CCM) before transmitting over the air.
3. The Border Router receives the 802.15.4 frame, decapsulates it, and sees a
   UDP/IPv6 packet destined for a NAT64 address.
4. The Border Router performs NAT64 translation and forwards the packet as
   UDP/IPv4 to the destination server.
5. The server replies, and the process reverses.
