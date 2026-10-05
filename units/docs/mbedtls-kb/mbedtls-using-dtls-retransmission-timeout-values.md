---
id: "mbedtls-using-dtls-retransmission-timeout-values"
type: "concept"
domain: "security"
title: "Using DTLS: Retransmission: timeout values"
summary: "The retransmission delay starts with a minimum value, then doubles on each retransmission until its maximum value is reached, in which case a handshake timeout is reported to the application."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/dtls-tutorial.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/dtls-tutorial.md#retransmission-timeout-values"
license: "Apache-2.0"
mode: "V"
---

The retransmission delay starts with a minimum value, then doubles on each retransmission until its maximum value is reached, in which case a handshake timeout is reported to the application. The minimum and maximum can be set using `mbedtls_ssl_conf_handshake_timeout()` (default: 1 to 60 seconds).

See [the documentation of this function](https://github.com/Mbed-TLS/mbedtls/blob/edb1a483971c836e84e95d7b73ee39bd6b450675/include/mbedtls/ssl.h#L1300) for the meaning of those values if you need to tune them according to the characteristics of your network in order to achieve optimal performance/reliability. Even if your timeout values are perfectly tuned, your application should still be prepared to see failing handshakes and react appropriately.

**Note:**: There might seem to be a parallel between `mbedtls_ssl_conf_handshake_timeout()` and `set_delay()` as they both accept two durations as arguments, but this is not the case. The **final delay** will take various values from `min` to `max`, doubling every time, while the **intermediate delay** is an internal implementation detail.
