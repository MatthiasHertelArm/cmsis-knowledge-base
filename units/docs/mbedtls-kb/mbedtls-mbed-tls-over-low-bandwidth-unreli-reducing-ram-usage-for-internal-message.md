---
id: "mbedtls-mbed-tls-over-low-bandwidth-unreli-reducing-ram-usage-for-internal-message"
type: "concept"
domain: "security"
title: "Mbed TLS over low-bandwidth, unreliable datagram networks: Reducing RAM usage for internal message buffers"
summary: "As of Mbed TLS 2.13, the library uses separate, statically-sized buffers for processing incoming and outgoing messages. They are user-configurable compile-time constants in mbedtls/config.h."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/controlling_package_size.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/controlling_package_size.md#reducing-ram-usage-for-internal-message-buffers"
license: "Apache-2.0"
mode: "V"
---

As of Mbed TLS 2.13, the library uses separate, statically-sized buffers for processing incoming and outgoing messages. They are user-configurable compile-time constants in `mbedtls/config.h`. The user sets their size so that they can hold arbitrarily protected records with payload size `MBEDTLS_SSL_IN_CONTENT_LEN` (for incoming records) or `MBEDTLS_SSL_OUT_CONTENT_LEN` (for outgoing records).

It is tempting to assume that any reduction of MTU and MFL would allow saving RAM by reducing `MBEDTLS_SSL_IN_CONTENT_LEN` and `MBEDTLS_SSL_OUT_CONTENT_LEN`, but you must consider the following points:

1. Both incoming and outgoing handshake messages are currently prepared in a contiguous buffer, regardless of whether they are being fragmented before sending, or reassembled after receiving (this might change in a future version of Mbed TLS). Hence, `MBEDTLS_SSL_IN_CONTENT_LEN` and `MBEDTLS_SSL_OUT_CONTENT_LEN` must not be smaller than the maximum expected size of handshake messages during connection setup. Judging from [RFC 6347, Section 4.2.2](https://tools.ietf.org/html/rfc6347#section-4.2.2), handshake messages may be up to 16Mb in size, but estimates of their _realistic_ size should be based on the following:

   1. Are certificates used? If so, what algorithms are supported (RSA keys are longer than ECDSA ones), and how long do we expect certificate chains to be? On a generic stack making no assumptions about the kind and length of certificate chains of the peer, it must be considered that they are a few KB in length.
   1. Are session tickets used? If so, how large are they?
1. Outgoing application data packets must fit in the outgoing data buffer. Hence, `MBEDTLS_SSL_OUT_CONTENT_LEN` must not be smaller than the maximum application packet size used by the application layer protocol.
1. As long as the first two points are obeyed, no further constraints apply to `MBEDTLS_SSL_OUT_CONTENT_LEN` to guarantee that handshake and application data messages can be sent. In particular, you may configure `MBEDTLS_SSL_OUT_CONTENT_LEN` to be smaller than the MTU and MFL settings. However, for unreliable networks, consider choosing a larger value for `MBEDTLS_SSL_OUT_CONTENT_LEN` nonetheless, to allow [datagram packing](#packing-multiple-messages-in-a-single-datagram). Still, it is not sensible to increase `MBEDTLS_SSL_OUT_CONTENT_LEN` beyond the minimum of MTU and MFL, if configured.
1. As long as the first point is obeyed and `MBEDTLS_SSL_IN_CONTENT_LEN` is large enough to hold any incoming handshake message (after reassembly), and if it is known that the server supports the MFL extension, the _client_ may reduce `MBEDTLS_SSL_IN_CONTENT_LEN` to the value of the MFL extension (if used). We don't recommend reducing `MBEDTLS_SSL_IN_CONTENT_LEN` without using the MFL extension, as no other means are currently available to inform the peer about the size limitation. The _server_ usually may not reduce `MBEDTLS_SSL_IN_CONTENT_LEN` based on the value of the MFL extension, unless it knows about the maximum size of messages sent by the client through some other means. This is, again, due to the asymmetry in the MFL extension, and will be solved with the introduction of the Record Size Limit extension mentioned above.
