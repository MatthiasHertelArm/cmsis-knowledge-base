---
id: "mbedtls-increasing-ssl-and-tls-performance-explanation"
type: "concept"
domain: "security"
title: "Increasing SSL and TLS performance: Explanation"
summary: "The overhead of the SSL debug module should be negligible when mbedtls_debug_set_threshold( 0 ); is called. You may still want to disable MBEDTLS_DEBUG_C in mbedtls_config.h in order to reduce the footprint and get the last few percent of performance improvement."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/increasing_ssl_performance_and_tls_performance.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/increasing_ssl_performance_and_tls_performance.md#explanation"
license: "Apache-2.0"
mode: "V"
---

The overhead of the SSL debug module should be negligible when `mbedtls_debug_set_threshold( 0 );` is called. You may still want to [disable **MBEDTLS_DEBUG_C** in `mbedtls_config.h`](https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/../compiling-and-building/how-do-i-configure-mbedtls.md) in order to reduce the footprint and get the last few percent of performance improvement.

<!---increasing_ssl_performance_and_tls_performance
,"Small article on increasing the performance of your SSL connection or TLS connection with Mbed TLS",,"performance, debug, speed, optimizations",published,"2014-01-23 15:21:00",2,4163,"2015-07-24 11:52:00","Paul Bakker"--->
