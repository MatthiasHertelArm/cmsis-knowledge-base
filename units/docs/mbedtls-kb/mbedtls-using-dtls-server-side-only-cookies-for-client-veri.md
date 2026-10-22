---
id: "mbedtls-using-dtls-server-side-only-cookies-for-client-veri"
type: "concept"
domain: "security"
title: "Using DTLS: Server-side only: Cookies for client verification"
summary: "Without specific protection, this would make it easy for a malicious client to use DTLS servers as amplifiers in DDoS attacks."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/dtls-tutorial.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/dtls-tutorial.md#server-side-only-cookies-for-client-verification"
license: "Apache-2.0"
mode: "V"
---

1. The client starts by sending a `ClientHello` message.

1. The server replies with a series of messages that can be long. These typically include the server's certificate chain.

Without specific protection, this would make it easy for a malicious client to use DTLS servers as amplifiers in DDoS attacks. Since it is trivial to fake the source address of a UDP packet, malicious clients could send a few bytes of `ClientHello` to innocent DTLS servers pretending to be a third machine (the victim) and the innocent DTLS servers would then send (and retransmit) kilobytes of data to the victim, unknowingly DDoSing it.

The DTLS standard has provisions against this misuse, in the form of a cookie exchange (`ClientHello verify`) that ensures verification of the client address. Mbed TLS implements this in a stateless way, in order to avoid DoS vectors against your own server, as recommended by the standard.

This mechanism uses secret server-side keys, in order to prevent an attacker from generating valid cookies. As usual, the SSL layer only expects callbacks so that you can provide your own implementation if desired, and a default implementation is provided, in `ssl_cookie.c`.

1. The keys are stored in an `mbedtls_ssl_cookie_ctx` that you need to declare or allocate.

1. Initialize with `mbedtls_ssl_cookie_init()` and `mbedtls_ssl_cookie_setup()`.

1. Register the context and callbacks with `mbedtls_ssl_conf_dtls_cookies()`.
  * If you are in a threaded environment, this should happen in the main thread during initialization.

1. Then, for each client that attempts to connect, you need to call `mbedtls_ssl_set_client_transport_id()` with the client address that will be verified (generally an IPv4 or IPv6 address).

Optionally, if you log handshake errors, you might want to treat **MBEDTLS_ERR_SSL_HELLO_VERIFY_REQUIRED** in a special way for logging, as it is expected to happen for half of the handshakes. However, it still means you should destroy or reset `mbedtls_ssl_context` and start the next handshake with a fresh context (remember, we don't want to keep state for unverified clients).
