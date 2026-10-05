---
id: "mbedtls-using-dtls-short-version"
type: "concept"
domain: "security"
title: "Using DTLS: Short version"
summary: "If you prefer to begin with code right away, you can skip to our dtls_client.c and dtls_server.c examples in the programs/ssl directory."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/dtls-tutorial.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/dtls-tutorial.md#short-version"
license: "Apache-2.0"
mode: "V"
---

* Register timer callbacks and context with `mbedtls_ssl_set_timer_cb()`.
  * Suitable callbacks for blocking I/O are provided in `timing.c`.
    * For event-based I/O, you need to write your own callbacks based on your event framework.
* Server-side, register cookie callbacks with `mbedtls_ssl_conf_dtls_cookie()`.
   * An implementation is provided in `ssl_cookie.c` and requires context set up with `mbedtls_ssl_cookie_setup()`.

If you prefer to begin with code right away, you can skip to our `dtls_client.c` and `dtls_server.c` examples in the `programs/ssl` directory. However, this article provides more background information, so we recommend reading it in order to make more informed choices.
