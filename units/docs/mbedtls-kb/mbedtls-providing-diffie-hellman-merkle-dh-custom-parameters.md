---
id: "mbedtls-providing-diffie-hellman-merkle-dh-custom-parameters"
type: "concept"
domain: "security"
title: "Providing Diffie-Hellman-Merkle (DHM) parameters in versions before 4.0: Custom parameters"
summary: "Before 4.0, you could use the example program programs/pkey/dh_genprime. Run dh_genprime bits=<desired size> to generate parameters in dh_prime.txt, then use them as C arrays with mbedtls_ssl_conf_dh_param_bin()."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/cryptography/providing-diffie-hellman-or-dhm-parameters.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/cryptography/providing-diffie-hellman-or-dhm-parameters.md#custom-parameters"
license: "Apache-2.0"
mode: "V"
---

Before 4.0, you could use the example program `programs/pkey/dh_genprime`. Run `dh_genprime bits=<desired size>` to generate parameters in `dh_prime.txt`, then use them as C arrays with `mbedtls_ssl_conf_dh_param_bin()`.

Mbed TLS 4 does not include the `dh_genprime` example program and no longer supports finite-field DHE in TLS 1.2 and DTLS 1.2. For TLS 1.2 and DTLS 1.2 applications with Mbed TLS 4, use ECDHE instead.
