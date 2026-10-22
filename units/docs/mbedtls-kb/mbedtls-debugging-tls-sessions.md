---
id: "mbedtls-debugging-tls-sessions"
type: "concept"
domain: "security"
title: "Debugging TLS sessions"
summary: "It is important to understand why a TLS handshake has failed with Mbed TLS and this short article will guide you through ways to debug Mbed TLS within your application."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/development/debugging-tls.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/development/debugging-tls.md"
license: "Apache-2.0"
mode: "V"
---

It is important to understand why a TLS handshake has failed with Mbed TLS and this short article will guide you through ways to debug Mbed TLS within your application. Using a debugger is an important first step, but will not always assist in understanding the cause of failure for a long complex TLS handshake. If using a debugger does not help explain the issue, then we recommend the following steps to reproduce and debug the failure.
