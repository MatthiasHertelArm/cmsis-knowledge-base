---
id: "mbedtls-using-dtls-protocol-differences-and-additional-sett"
type: "concept"
domain: "security"
title: "Using DTLS: Protocol differences and additional settings"
summary: "TLS usually runs on top of TCP and provides the same guarantees as TCP, in addition to authentication, integrity, and confidentiality."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/dtls-tutorial.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/dtls-tutorial.md#protocol-differences-and-additional-settings"
license: "Apache-2.0"
mode: "V"
---

TLS usually runs on top of TCP and provides the same guarantees as TCP, in addition to authentication, integrity, and confidentiality.

Like TCP, it delivers a **stream** of bytes in order and does **not** preserve packet boundaries. DTLS usually runs on top of UDP, and once the handshake is finished, provides the same guarantees as UDP as well as authentication, integrity, and confidentiality.

Just like UDP, it delivers **datagrams** of bytes. Some datagrams may be lost or re-ordered, but unlike UDP, DTLS can detect and discard duplicated datagrams if needed. In Mbed TLS, this is controlled by the compile-time flag **MBEDTLS_SSL_DTLS_ANTI_REPLAY** and the run-time setting `mbedtls_ssl_conf_dtls_anti_replay()`, both enabled by default.

With TLS, when a record is received that does not pass the integrity check, the connection is immediately terminated. This denies attackers an opportunity to do more than one guess at the message authentication key, without introducing any new DoS vectors (injecting bad records is just as hard as injecting a TCP RST to tear down the connection).

However, with DTLS over UDP, injecting bad records is very easy (an attacker only needs to know the source and destination IP and port), so the DTLS standard, [section 4.1.2.7](https://tools.ietf.org/html/rfc6347#section-4.1.2.7) recommends not to tear down the connection.

In Mbed TLS, it is possible to set a limit to the number of bad records before the connection is torn down; this is controlled by the compile-time flag **MBEDTLS_SSL_DTLS_BADMAC_LIMIT** (enabled by default) and the run-time setting `mbedtls_ssl_conf_dtls_badmac_limit()` (unlimited by default).
