---
id: "mbedtls-how-to-generate-a-certificate-requ-certificate-request-for-use-with-ssl-ven"
type: "concept"
domain: "security"
title: "How to generate a Certificate Request (CSR): Certificate Request for use with SSL vendors"
summary: "Whenever you request a certificate from one of the SSL vendors, you are asked to enter a CSR. CSR is short for Certificate Signing Request and is often in the PEM format."
status: "draft"
collection: "mbedtls-kb"
source: "Mbed-TLS/mbedtls-docs@7ba0cff:kb/how-to/generate-a-certificate-request-csr.md"
doc_source: "https://github.com/Mbed-TLS/mbedtls-docs/blob/7ba0cff/kb/how-to/generate-a-certificate-request-csr.md#certificate-request-for-use-with-ssl-vendors"
license: "Apache-2.0"
mode: "V"
---

Whenever you request a certificate from one of the SSL vendors, you are asked to enter a CSR. CSR is short for Certificate Signing Request and is often in the PEM format.

To generate a certificate request, you need a private-public key pair. The public key is put in the certificate request in addition to some identifying information (such as website domain, address, and country). By submitting your request, you ask the SSL vendor to sign that request with their CA key and generate a full certificate from it.

The CA will determine the validity of the certificate they generate based on how much you paid them.
