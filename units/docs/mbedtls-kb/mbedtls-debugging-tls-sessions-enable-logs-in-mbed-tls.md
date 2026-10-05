---
id: "mbedtls-debugging-tls-sessions-enable-logs-in-mbed-tls"
type: "concept"
domain: "security"
title: "Debugging TLS sessions: Enable logs in Mbed TLS"
summary: "Mbed TLS has a feature to show the TLS handshake logs, filtering with certain debug level. In order to see the TLS logs in your terminal, you must verify that you have MBEDTLS_DEBUG_C defined in your configuration."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/development/debugging-tls.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/development/debugging-tls.md#enable-logs-in-mbed-tls"
license: "Apache-2.0"
mode: "V"
---

Mbed TLS has a feature to show the TLS handshake logs, filtering with certain debug level. In order to see the TLS logs in your terminal, you must verify that you have `MBEDTLS_DEBUG_C` defined in your configuration.

Set the debug threshold for the TLS handshake:
```
mbedtls_debug_set_threshold( <debug_level> )
```  
Note that `debug_level` is the level of debug logs you require. Its values can be between 0 and 5, where 5 is the most logs.  
Set your debug log function to display in your terminal:
```
mbedtls_ssl_conf_dbg()
```
These steps will enable logs and print the logs according to your debug function.
