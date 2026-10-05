---
id: "mbedtls-increasing-ssl-and-tls-performance-situation"
type: "concept"
domain: "security"
title: "Increasing SSL and TLS performance: Situation"
summary: "If you use a specific cipher suite, like TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256 on your embedded platform, when you benchmark the individual cipher and hash speeds, the performance may be:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/increasing_ssl_performance_and_tls_performance.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/increasing_ssl_performance_and_tls_performance.md#situation"
license: "Apache-2.0"
mode: "V"
---

If you use a specific cipher suite, like **TLS-ECDHE-ECDSA-WITH-AES-128-CBC-SHA256** on your embedded platform, when you benchmark the individual cipher and hash speeds, the performance may be:

* AES-128-CBC: 321 Kb/s
* SHA256-HMAC: 441 Kb/s

You expect a reasonable performance speed for your SSL connection as well. However, when you benchmark the sent and received SSL/TLS data, the performance is only about 9 Kb/s.
