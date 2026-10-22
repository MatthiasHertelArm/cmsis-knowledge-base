---
id: "mbedtls-mbed-tls-over-low-bandwidth-unreli-configuring-mbed-tls-in-lossy-networks"
type: "concept"
domain: "security"
title: "Mbed TLS over low-bandwidth, unreliable datagram networks: Configuring Mbed TLS in lossy networks"
summary: "In DTLS, Mbed TLS offers packing multiple handshake messages in a single datagram (if space permits). This reduces the likelihood of message reordering, hence the likelihood of retransmissions, and hence the expected time to set up a DTLS connection."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/controlling_package_size.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/controlling_package_size.md#configuring-mbed-tls-in-lossy-networks"
license: "Apache-2.0"
mode: "V"
---

### Packing multiple messages in a single datagram

In DTLS, Mbed TLS offers packing multiple handshake messages in a single datagram (if space permits). This reduces the likelihood of message reordering, hence the likelihood of retransmissions, and hence the expected time to set up a DTLS connection. This _datagram packing_ feature is enabled by default and is controlled by the API function

```
mbedtls_ssl_set_datagram_packing()
```

Datagram packing should only be disabled for testing purposes, or if the peer does not support it.

### Caching out-of-order messages

DTLS handshake messages must be sent and processed in order, but may get reordered in transit (because UDP doesn't guarantee ordered delivery). Mbed TLS offers to cache future messages until they become relevant, instead of dropping them and enforcing a flight retransmission.

Caching future messages is implemented alongside reassembly of fragmented messages, and the maximum amount of RAM used for both reassembly and caching is controlled by the compile-time option

```
MBEDTLS_SSL_DTLS_MAX_BUFFERING
```

The default value is 32KB.

The configuration of `MBEDTLS_SSL_DTLS_MAX_BUFFERING` is a trade off between memory usage, network load and handshake efficiency:

1. Higher values allow to buffer more messages, thereby reducing the number of retransmission and the time until the connection has been established. Saturation happens when the value is large enough to allow for simultaneous reassembly of all messages within any flight. In this case, retransmission is only necessary on packet loss (in which case it is unavoidable).
1. Lower values reduce the RAM usage, but can lead to future messages being dropped, thereby forcing retransmission, which increases both the network load and the handshake time. When the value is too low to allow reassembly of each handshake message individually, handshakes with peers that need to send large, fragmented messages become impossible.

Numerically, these maximal and minimal sensible values of `MBEDTLS_SSL_DTLS_MAX_BUFFERING` can be approximated as follows:

1. Define `MBEDTLS_SSL_DTLS_MAX_BUFFERING` as twice the value of `MBEDTLS_SSL_IN_CONTENT_LEN`. This should be sufficient to buffer all the messages that require buffering, based on the heuristic that there is usually only a single large message in a flight, say of maximum size `MBEDTLS_SSL_IN_CONTENT_LEN`. The default value of `MBEDTLS_SSL_DTLS_MAX_BUFFERING`, 32KB, is chosen according to this heuristic, with the default value of `MBEDTLS_SSL_IN_CONTENT_LEN` being 16KB.
1. Because `MBEDTLS_SSL_DTLS_MAX_BUFFERING` bounds the size of the reassembly buffer, it must be at least as large as the largest expected incoming handshake message (which was mentioned above as also providing a lower bound for `MBEDTLS_SSL_IN_CONTENT_LEN`), and also account for internal reassembly state overhead, which is usually 12 bytes + 1/8 of the message size. Hence, unless it is known that the peer does not use handshake fragmentation, we recommend not configuring a value lower than `9/8 MBEDTLS_SSL_IN_CONTENT_LEN + 12` for this option.

Finally, note that Mbed TLS dynamically allocates space for caching and reassembly on demand only. In particular, while `MBEDTLS_SSL_DTLS_MAX_BUFFERING` controls the peak of RAM usage, the actual amount of RAM needed for reassembly and caching in an ordinary connection is much less, depending on the reliability of the network. However, an adversary attempting a DoS attack might purposefully trigger maximum RAM usage.
