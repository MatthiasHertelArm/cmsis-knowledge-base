---
id: "mbedtls-mbed-tls-tutorial"
type: "concept"
domain: "security"
title: "Mbed TLS tutorial"
summary: "The Mbed TLS library is designed to integrate with existing (embedded) applications and to provide the building blocks for secure communication, cryptography and key management. This tutorial helps you understand the steps to undertake."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@363c297:kb/how-to/mbedtls-tutorial.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/363c297/kb/how-to/mbedtls-tutorial.md"
license: "Apache-2.0"
mode: "V"
---

The Mbed TLS library is designed to integrate with existing (embedded) applications and to provide the building blocks for secure communication, cryptography and key management. This tutorial helps you understand the steps to undertake.

Mbed TLS is designed to be as loosely coupled as possible, allowing you to only integrate the parts you need without having overhead from the rest. This also results in a very low memory footprint and build footprint for the Mbed TLS library. By eliminating parts you don't need in your system you can get build sizes from as low as 45 kB to a more typical 300 kB for more fully featured setups.

Mbed TLS is designed in the portable C language with embedded environments as a main target and runs on targets as broad as embedded platforms like ARM and AVR to PCs and iPads, iPhones and even the XBox. Please let us know your experiences on other platforms as well.
