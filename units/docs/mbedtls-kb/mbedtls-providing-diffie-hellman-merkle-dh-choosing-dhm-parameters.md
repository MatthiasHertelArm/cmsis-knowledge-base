---
id: "mbedtls-providing-diffie-hellman-merkle-dh-choosing-dhm-parameters"
type: "concept"
domain: "security"
title: "Providing Diffie-Hellman-Merkle (DHM) parameters in versions before 4.0: Choosing DHM parameters"
summary: "Developers have the option to set the DHM parameters for SSL servers with mbedtls_ssl_conf_dh_param_bin(). This is not a requirement as the default parameters are preloaded."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/cryptography/providing-diffie-hellman-or-dhm-parameters.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/cryptography/providing-diffie-hellman-or-dhm-parameters.md#choosing-dhm-parameters"
license: "Apache-2.0"
mode: "V"
---

Developers have the option to set the DHM parameters for SSL servers with `mbedtls_ssl_conf_dh_param_bin()`. This is not a requirement as the default parameters are preloaded.
