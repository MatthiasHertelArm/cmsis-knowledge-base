---
id: "mbedtls-providing-diffie-hellman-merkle-dh-default-dhm-parameters"
type: "concept"
domain: "security"
title: "Providing Diffie-Hellman-Merkle (DHM) parameters in versions before 4.0: Default DHM parameters"
summary: "The DHM parameters that the TLS handshake uses are set by default to the 2048-bit MODP parameters from RFC 3526 (MBEDTLS_DHM_RFC3526_MODP_2048_P_BIN and MBEDTLS_DHM_RFC3526_MODP_2048_G_BIN)."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/cryptography/providing-diffie-hellman-or-dhm-parameters.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/cryptography/providing-diffie-hellman-or-dhm-parameters.md#default-dhm-parameters"
license: "Apache-2.0"
mode: "V"
---

The DHM parameters that the TLS handshake uses are set by default to the 2048-bit MODP parameters from [RFC 3526](https://www.ietf.org/rfc/rfc3526.txt) (`MBEDTLS_DHM_RFC3526_MODP_2048_P_BIN` and `MBEDTLS_DHM_RFC3526_MODP_2048_G_BIN`). From a security perspective, it is desirable to use a larger value, unless you have clients for which this will cause interoperability issues. Larger values are provided in [dhm.h](https://github.com/Mbed-TLS/mbedtls/blob/development/include/mbedtls/dhm.h).
