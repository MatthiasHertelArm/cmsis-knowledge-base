---
id: "mbedtls-mbed-tls-over-low-bandwidth-unreli-configuring-mbed-tls-in-networks-with-lo"
type: "concept"
domain: "security"
title: "Mbed TLS over low-bandwidth, unreliable datagram networks: Configuring Mbed TLS in networks with low MTU"
summary: "The maximum size of packets that a specific network connection is able to handle is commonly called the maximum transmission unit, or MTU for short."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/controlling_package_size.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/controlling_package_size.md#configuring-mbed-tls-in-networks-with-low-mtu"
license: "Apache-2.0"
mode: "V"
---

### Background: The Maximum Transmission Unit (MTU)

The maximum size of packets that a specific network connection is able to handle is commonly called the _maximum transmission unit_, or _MTU_ for short. If a message needs to be sent whose size exceeds the MTU, this requires a higher layer protocol in the networking stack. This protocol is aware of the MTU limitation, and is able to split the message into sufficiently small fragments on the sender side, then reassemble those fragments on the receiving side. For example, if an [IPv4](https://en.wikipedia.org/wiki/IPv4) router finds an IPv4 packet too large for the link layer, which transports it to its destination, the router may fragment the packet (or refine existing fragmentation) before passing it to the link layer. In contrast, [IPv6](https://en.wikipedia.org/wiki/IPv6) fragmentation during routing is not allowed, and an IPv6 router will drop a packet that is too large to be passed to the underlying link layer; instead, IPv6 fragmentation must happen at the endpoints or be handled by an upper layer protocol. The minimum requirement for implementation is an MTU of 576 bytes for IPv4 and 1280 bytes for IPv6. In that regard, note that even though the IPv4 and IPv6 specifications provide methods for fragmentation at the endpoints, constrained devices might use implementations that do not support those, and only provide these minimal MTU requirements.

We must therefore consider that DTLS may use a handshake message of a size larger than the MTU of the datagram transport it is based on. For example, the `Certificate` and `NewSessionTicket` messages can be larger than the IPv4 / IPv6 MTUs mentioned in the previous paragraph. To still allow the use of DTLS over such datagram links, [DTLS RFC 6347, Section 4.2.3](https://tools.ietf.org/html/rfc6347#section-4.2.3) specifies a mechanism for fragmentation and reassembly of handshake messages. This allows reducing the size of datagrams passed to the underlying datagram link to below the link's MTU. This assumes, though, that the DTLS implementation is aware of the MTU limitation of the underlying datagram link, so the next section explains how the user can inform Mbed TLS about it.

### Setting the MTU of the underlying datagram link

The value of the underlying datagram link's MTU - or a safe under-approximation of it - may be configured through the API call:

```
mbedtls_ssl_set_mtu()
```

This function may be called at any point during the lifetime of an SSL context, depending on when information about the underlying datagram link's MTU becomes available or gets updated (for example, when the rate of package loss indicates that your MTU configuration is too large). It takes effect immediately, ensuring that no datagram of a size exceeding the MTU is sent, and fragmenting handshake messages if necessary to guarantee this.


For example, to set the initial MTU value used for the handshake, the function should be called after the SSL context has been set up using `mbedtls_ssl_setup()`, but before performing the handshake using `mbedtls_ssl_handshake()`. This is exemplified in the [ssl_server2](https://github.com/Mbed-TLS/mbedtls/blob/development/programs/ssl/ssl_server2.c) and [ssl_client2](https://github.com/Mbed-TLS/mbedtls/blob/development/programs/ssl/ssl_client2.c) example programs.

### Getting the maximum application data size

The API call `mbedtls_ssl_set_mtu()` informs Mbed TLS about the MTU of the underlying datagram link, but a natural question from the perspective of the user is what the 'outgoing' MTU of the DTLS connection itself is; that is, what is the maximum size of (unprotected) application datagrams that the DTLS connection can send.

In that regard, it is important to note that the DTLS fragmentation mechanism referred to above applies to the DTLS-internal handshake messages only. In contrast, no fragmentation mechanism for application datagrams sent and received by the user is built into DTLS. An MTU restriction on the underlying datagram link directly restricts the MTU of the DTLS connection from the perspective of the application layer: The MTU of the DTLS connection is smaller than the datagram link's MTU by at least the overhead for DTLS headers and encryption as determined by `mbedtls_ssl_get_record_expansion()` (However, note that it can be larger, for example due to the use of the maximum fragment length configuration discussed below).

The maximum application data size of a DTLS connection can be queried using the API call:

```
mbedtls_ssl_get_max_out_record_payload()
```

The library guarantees that application datagrams of a size not exceeding this value can be sent through the DTLS connection to reach the peer's DTLS stack (provided the MTU value configured through `mbedtls_ssl_set_mtu()` is valid). In contrast, if the user attempts to send larger application datagrams, the corresponding call to `mbedtls_ssl_write()` fails.

It is the responsibility of the application layer protocol to implement fragmentation of application data, if necessary, to ensure that the data it passes to `mbedtls_ssl_write()` is within the bounds set by `mbedtls_ssl_get_max_out_record_payload()`.
