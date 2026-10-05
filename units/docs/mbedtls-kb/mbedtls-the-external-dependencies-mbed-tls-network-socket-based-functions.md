---
id: "mbedtls-the-external-dependencies-mbed-tls-network-socket-based-functions"
type: "concept"
domain: "security"
title: "The external dependencies Mbed TLS relies on: Network/socket based functions"
summary: "The network and socket based functions are only used in the Network module (net_sockets.c). As the TLS part only uses function pointers, you can replace these dependencies with something else (such as lwIP) as long as the behavior is similar."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/what-external-dependencies-does-mbedtls-rely-on.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/what-external-dependencies-does-mbedtls-rely-on.md#network-socket-based-functions"
license: "Apache-2.0"
mode: "V"
---

The network and socket based functions are only used in the *Network* module (`net_sockets.c`). As the TLS part only uses function pointers, you can replace these dependencies with something else (such as lwIP) as long as the behavior is similar. To use different networking functions, disable `MBEDTLS_NET_C`, and implement your own socket module, as described in [the porting article](https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/../how-to/how-do-i-port-mbed-tls-to-a-new-environment-OS.md).

**Functions covered:** on Windows, functions from the Windows Sockets API, and on Unix:

- `accept()`
- `bind()`
- `close()`
- `connect()`
- `fcntl()`
- `freeaddrinfo()`
- `getaddrinfo()`
- `getsockname()`
- `getsockopt()`
- `listen()`
- `read()`
- `recvfrom()`
- `setsockopt()`
- `shutdown()`
- `socket()`
- `write()`
