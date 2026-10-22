---
id: "mbedtls-mbed-tls-over-low-bandwidth-unreli"
type: "concept"
domain: "security"
title: "Mbed TLS over low-bandwidth, unreliable datagram networks"
summary: "This article reviews the following topics:"
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/controlling_package_size.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/controlling_package_size.md"
license: "Apache-2.0"
mode: "V"
---

This article reviews the following topics:

1. [Configuring Mbed TLS in networks with low MTU](#configuring-mbed-tls-in-networks-with-low-mtu): using `mbedtls_ssl_set_mtu()` to configure the _Maximum Transmission Unit_ (MTU).
1. [Negotiating a maximum message size with the peer](#negotiating-a-maximum-message-size-with-the-peer): using `mbedtls_ssl_conf_max_frag_len()` to configure the _Maximum Fragment Length_ (MFL).
1. [Comparing MTU and MFL](#comparing-mtu-and-mfl): highlighting the differences between MTU and MFL.
1. [Reducing memory footprint in Mbed TLS version 2.x](#reducing-ram-usage-for-internal-message-buffers): using `MBEDTLS_SSL_IN_CONTENT_LEN` and `MBEDTLS_SSL_OUT_CONTENT_LEN` to determine the size of internal input and output buffers.
1. [Configuring Mbed TLS in networks with high loss rates](#configuring-mbed-tls-in-lossy-networks): using `MBEDTLS_SSL_DTLS_MAX_BUFFERING` and `mbedtls_ssl_set_datagram_packing()` to control two features improving DTLS
   handshake reliability.

**Note:** This article is _not_ meant as an introduction to Mbed TLS; you can find that in the separate [Mbed TLS tutorial](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/mbedtls-tutorial.md). Also, this article is about _DTLS only_ (the MFL extension exists in TLS, too, but currently Mbed TLS does not comprehensively support it), and it assumes that you are familiar with what DTLS is, why you would want to use it, and how to configure Mbed TLS to implement it. If you are looking for answers to those questions, please see the [DTLS tutorial](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/dtls-tutorial.md).
