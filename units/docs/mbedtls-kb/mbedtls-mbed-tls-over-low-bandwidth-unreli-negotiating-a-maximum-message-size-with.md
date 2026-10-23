---
id: "mbedtls-mbed-tls-over-low-bandwidth-unreli-negotiating-a-maximum-message-size-with"
type: "concept"
domain: "security"
title: "Mbed TLS over low-bandwidth, unreliable datagram networks: Negotiating a maximum message size with the peer"
summary: "The value of mbedtls_ssl_get_max_out_record_payload() indicates the maximum size of outgoing application datagrams, but it does not bound the size of incoming application datagrams."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/controlling_package_size.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/controlling_package_size.md#negotiating-a-maximum-message-size-with-the-peer"
license: "Apache-2.0"
mode: "V"
---

### Background

The value of `mbedtls_ssl_get_max_out_record_payload()` indicates the maximum size of outgoing application datagrams, but it does not bound the size of _incoming_ application datagrams. The latter may be larger, as MTU values set by `mbedtls_ssl_set_mtu()` may be a strict under-approximation of the underlying datagram link's capabilities. For example, we might think the MTU is 512 bytes, when it is in fact 1024 bytes, while the peer might use a larger, yet still valid, approximation to the MTU, say, 800 bytes. In this case, we might receive datagrams of up to 800 bytes, even though we estimated the MTU as 512 bytes. This is acceptable as long as both parties use valid estimates of the datagram link's MTU _and_ have enough memory to store incoming and outgoing messages.

Constrained devices, however, might not have enough available RAM to store incoming messages of a size up to the underlying datagram link's MTU. For example, if the datagram link uses its own fragmentation mechanism to allow sending of packets of size 16K, that doesn't mean the DTLS stack has enough RAM to handle them. If a DTLS stack limits the size of incoming datagrams it is willing to accept because of RAM limitations, this might lead to messages from the peer being dropped even if the peer has properly configured the underlying MTU through `mbedtls_ssl_set_mtu()` and did not send packets larger than what `mbedtls_ssl_get_max_out_record_payload()` returns.

As a remedy, the communicating parties need to negotiate the maximum size of the datagrams they exchange. One such mechanism is provided by the _maximum fragment length extension_ (MFL) of DTLS, specified in [RFC 6066, Section 4](https://tools.ietf.org/html/rfc6066#section-4). This extension lets the client suggest the maximum size of datagram payloads that can be sent during the communication. The possible values are 512, 1024, 2048 and 4096 bytes. If the server consents to it, it must only send messages of a size not exceeding the client's MFL value.

Note that the server cannot suggest a different MFL value; if it knows about the MFL extension, it can only consent to the client's suggestion or abort the handshake. The [Record Size Limit Extension, RFC 8449](https://tools.ietf.org/html/rfc8449) aims to
correct this asymmetry, but is not yet implemented in Mbed TLS.

### Using the maximum fragment length (MFL) extension in Mbed TLS

Use of the MFL extension is controlled through the API call:

```
mbedtls_ssl_conf_max_frag_len()
```

Its semantics is very different depending on the caller (client or server), due to the asymmetry of the MFL extension:

* If called by the **client**, `mbedtls_ssl_conf_max_frag_len()` prevents the exchange of datagram payloads of a size exceeding the respective MFL value, _provided_ that the server supports the MFL extension and explicitly consents to the client's request. If the server is aware of the extension but doesn't explicitly acknowledge the client's request, the connection fails; if the server doesn't know the extension or does not respond to it, the connection continues without any guarantees for the client (see the example below).
    Mbed TLS does not provide an API call to determine if the server consented to an MFL request.
* If called by the **server**, `mbedtls_ssl_conf_max_frag_len()` bounds the server's maximum outgoing payload size. If the client requests a smaller MFL value, the server will accept it and not send payloads larger than the client's MFL value. However, as mentioned in the previous section, the server has no means of requesting the use of smaller packets from the client (when the server's MFL value is lower then the client's MFL value).

Note that on the server, `mbedtls_ssl_conf_max_frag_len()` is very similar to `mbedtls_ssl_set_mtu()`, the difference being that the MFL is about payload size before encryption and adding DTLS headers, while `mbedtls_ssl_set_mtu()` is about the final datagram size.

The MFL values that `mbedtls_ssl_conf_max_frag_len()` accepts are those defined in the standard: 512, 1024, 2048 and 4096 bytes. If `mbedtls_ssl_conf_max_frag_len()` is not called, the MFL defaults to the minimum of the size of the internal incoming and outgoing datagram buffers as configured by `MBEDTLS_SSL_IN_CONTENT_LEN` and `MBEDTLS_SSL_OUT_CONTENT_LEN`, respectively, which is at most 16384 bytes (the maximum record payload size according to the TLS/DTLS standards, see for example [TLS 1.2 RFC 5246, Section 6.2.1](https://tools.ietf.org/html/rfc5246#section-6.2.1) and [DTLS 1.2 RFC 6347, Section 3.2.3](https://tools.ietf.org/html/rfc6347#section-3.2.3)). In particular, unconstrained applications not wishing to restrict the MFL should not call
`mbedtls_ssl_conf_max_frag_len()`, because the MFL extension does not support values above 4096 bytes (one of the limitations leading to development of the [Record Size Limit Extension, RFC 8449](https://tools.ietf.org/html/rfc8449).

Examples:

* The server is unconstrained and doesn't call `mbedtls_ssl_conf_max_frag_len()`, but supports the MFL extension; the client has limited RAM and calls `mbedtls_ssl_conf_max_frag_len()` with an MFL value of 2048 bytes.

    Subsequently, all messages between client and server have a payload size of 2048 bytes at most.

* The server is unconstrained and doesn't support the MFL extension; the client has limited RAM and calls `mbedtls_ssl_conf_max_frag_len()` with an MFL value of 2048 bytes. In this case, no restriction applies to the size of messages sent from the server to the client.

    Potential consequences: On the one hand, the handshake might fail, for example when the server sends a certificate larger than 2KB (which the client cannot handle). On the other hand, even if the handshake succeeds, server packets of size > 2KB are dropped, resulting in a connection that may be unreliable or even unusable (depending on the amount of such packets, as well as the tolerance and adaptation mechanisms of the application layer protocol towards packet loss).

* The server and client are constrained to MFLs of 4096 bytes and 1024 bytes, respectively. The client takes precedence, and all messages subsequently sent between client and server have a payload size of 1024 bytes at most.

* The server and client are constrained to MFLs of 1024 bytes and 4096 bytes, respectively. The server has no way to lower the client's request from 4096 bytes to 1024 bytes, and must therefore either abort the connection or accept the client's MFL of 4096 bytes. In the latter case, the same remarks as in the second example apply in regards to potential handshake failure or unreliability of the resulting connection.

You can query the currently configured or negotiated MFL value through the API call:

```
mbedtls_ssl_get_max_frag_len()
```

For the **client**, this will always return the value configured in `mbedtls_ssl_conf_max_frag_len()` (or the default value mentioned above if the function hasn't been called). For the **server**, it returns the smaller of the values configured through `mbedtls_ssl_conf_max_frag_len()` and the one requested by the client (if any).

Note that `mbedtls_ssl_get_max_frag_len()` should not be used to determine the maximum datagram payload, as it does not take the configured MTU into consideration. Instead, you should always call `mbedtls_ssl_get_max_out_record_payload()` to determine the maximum application data size the stack is able to handle, which takes both MTU and MFL settings into account.
