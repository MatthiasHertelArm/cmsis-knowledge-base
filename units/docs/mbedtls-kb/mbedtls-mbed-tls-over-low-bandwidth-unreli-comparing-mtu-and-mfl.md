---
id: "mbedtls-mbed-tls-over-low-bandwidth-unreli-comparing-mtu-and-mfl"
type: "concept"
domain: "security"
title: "Mbed TLS over low-bandwidth, unreliable datagram networks: Comparing MTU and MFL"
summary: "The underlying datagram link's MTU, as set through mbedtls_ssl_set_mtu(), guards only the total size of outgoing datagrams; it does not control the size of incoming datagrams."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/controlling_package_size.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/controlling_package_size.md#comparing-mtu-and-mfl"
license: "Apache-2.0"
mode: "V"
---

The **underlying datagram link's MTU**, as set through `mbedtls_ssl_set_mtu()`, guards only the _total_ size of _outgoing_ datagrams; it does _not_ control the size of incoming datagrams. Because the total datagram size includes overhead for headers and encryption, the bound `mbedtls_ssl_set_mtu()` sets on the _payload_ of outgoing datagrams is strictly smaller than the MTU value, by (at most) `mbedtls_ssl_get_record_expansion()`.

For the **client**, the MFL as configured by `mbedtls_ssl_conf_max_frag_len()` guards the _payload_ size of both _incoming and outgoing_ datagrams (provided the server supports the MFL extension and acknowledges the client's request). The MFL is strictly smaller than the maximum datagram size, because of overhead from headers and protection. In particular, an MFL of 512 bytes can still lead to exchange of datagrams or records of about ~550 bytes.

For the **server**, the MFL as configured by `mbedtls_ssl_conf_max_frag_len()` guards the _payload_ size of _outgoing datagrams only_. The client is not informed about this limitation and hence need not obey it. Therefore, `mbedtls_ssl_conf_max_frag_len()`, which applies to the payload, is roughly equivalent to `mbedtls_ssl_set_mtu()`, which applies to the _total_ datagram size.

When both MFL and MTU are configured, the guards are applied independently. For example, say a client configures an MFL of 512 bytes and an MTU of 512 bytes. The stack will not send datagrams larger than 512 bytes due to the MTU setting. But, it may receive datagrams slightly larger than 512 bytes, since the MFL only restricts the server to
512 bytes of payload.

In DTLS, the maximum datagram payload size, as determined by both the MTU and the MFL setting, can be queried by `mbedtls_ssl_get_max_out_record_payload()`, and must be obeyed by both client and server. Datagrams exceeding this size will be rejected by `mbedtls_ssl_write()`.
